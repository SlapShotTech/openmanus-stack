import asyncio
import json
import os
import aioredis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
TASK_QUEUE_KEY = "openmanus:tasks"


async def enqueue_demo_task():
    redis = await aioredis.from_url(REDIS_URL)
    task = {"id": 1, "goal": "Find the top 5 programming languages. Summarize pros and cons."}
    await redis.rpush(TASK_QUEUE_KEY, json.dumps(task))
    print("Enqueued demo wide research task.")


if __name__ == "__main__":
    asyncio.run(enqueue_demo_task())