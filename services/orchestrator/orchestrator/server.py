"""Simple entry point for the orchestrator service.

This server listens for task events (e.g. via Redis) and orchestrates
planner/executor/verifier loops.  It provides a basic HTTP interface for health checks.
"""
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .planning import Planner
from .execution import Executor
from .verification import Verifier
from .memory import RunStore
from .queue import get_task_stream

app = FastAPI(title="OpenManus Orchestrator", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

planner = Planner()
executor = Executor()
verifier = Verifier()
store = RunStore()


async def worker_loop():
    """Listen for tasks and process them."""
    async for task in get_task_stream():
        task_id = task["id"]
        goal = task["goal"]
        # Plan steps
        plan = await planner.plan(goal)
        step_num = 0
        for step in plan:
            result = await executor.execute(step)
            await store.log(task_id, step_num, result)
            step_num += 1
            if not await verifier.verify(result):
                # Replan if verification fails
                plan = await planner.plan(goal)
                step_num = 0
        await store.complete(task_id)


@app.on_event("startup")
async def start_worker():
    loop = asyncio.get_event_loop()
    loop.create_task(worker_loop())


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8500)