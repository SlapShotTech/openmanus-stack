import os
from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from typing import Optional


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/openmanus",
)

engine = create_async_engine(DATABASE_URL, echo=False)


class RunLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int
    step: int
    message: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class TaskStatus(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int
    status: str


class RunStore:
    """Persist run logs and statuses into the database."""

    async def log(self, task_id: int, step: int, message: str) -> None:
        async with AsyncSession(engine) as session:
            run = RunLog(task_id=task_id, step=step, message=message)
            session.add(run)
            await session.commit()

    async def complete(self, task_id: int) -> None:
        async with AsyncSession(engine) as session:
            status = TaskStatus(task_id=task_id, status="completed")
            session.add(status)
            await session.commit()