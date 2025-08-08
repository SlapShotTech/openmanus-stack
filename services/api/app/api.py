from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlmodel import select
from .models import Task, RunLog
from .schemas import TaskCreate, TaskRead, RunLogRead
from .database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter()


@router.post("/tasks", response_model=TaskRead)
async def create_task(task: TaskCreate, session: AsyncSession = Depends(get_session)) -> TaskRead:
    """Create a new task and enqueue it to the orchestrator."""
    db_task = Task(name=task.name, goal=task.goal)
    session.add(db_task)
    await session.commit()
    await session.refresh(db_task)
    # TODO: enqueue to orchestrator via Redis or HTTP
    return db_task


@router.get("/tasks/{task_id}", response_model=TaskRead)
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)) -> TaskRead:
    task = await session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.get("/tasks/{task_id}/logs", response_model=List[RunLogRead])
async def get_task_logs(task_id: int, session: AsyncSession = Depends(get_session)) -> List[RunLogRead]:
    statement = select(RunLog).where(RunLog.task_id == task_id).order_by(RunLog.step)
    results = await session.exec(statement)
    return results.all()


@router.get("/tasks", response_model=List[TaskRead])
async def list_tasks(session: AsyncSession = Depends(get_session)) -> List[TaskRead]:
    """Return all tasks."""
    result = await session.exec(select(Task))
    return result.all()