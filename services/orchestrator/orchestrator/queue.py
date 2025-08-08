import os
import aioredis
import json
from typing import AsyncIterator, Dict, Any


REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
TASK_QUEUE_KEY = "openmanus:tasks"


async def get_task_stream() -> AsyncIterator[Dict[str, Any]]:
    """Stream tasks from Redis list and yield them one by one."""
    redis = await aioredis.from_url(REDIS_URL)
    while True:
        _, raw = await redis.blpop(TASK_QUEUE_KEY)
        task = json.loads(raw)
        yield task