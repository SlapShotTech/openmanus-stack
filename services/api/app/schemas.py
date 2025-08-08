from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TaskCreate(BaseModel):
    name: str
    goal: str


class TaskRead(BaseModel):
    id: int
    name: str
    status: str
    goal: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class RunLogRead(BaseModel):
    step: int
    message: str
    timestamp: datetime

    class Config:
        orm_mode = True