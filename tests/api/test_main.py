import pytest
from httpx import AsyncClient, ASGITransport
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from services.api.app.main import app
from services.api.app.database import get_session
from services.api.app.models import Task

DATABASE_URL = "sqlite+aiosqlite://"

engine = create_async_engine(DATABASE_URL, echo=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def override_get_session():
    async_session = AsyncSession(engine, expire_on_commit=False)
    async with async_session as session:
        yield session


@pytest.mark.asyncio
async def test_create_and_list_tasks(monkeypatch):
    await init_db()
    app.dependency_overrides[get_session] = override_get_session
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # create task
        resp = await ac.post("/api/tasks", json={"name": "Test", "goal": "Do something"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["name"] == "Test"
        # list tasks
        resp = await ac.get("/api/tasks")
        assert resp.status_code == 200
        tasks = resp.json()
        assert len(tasks) == 1
