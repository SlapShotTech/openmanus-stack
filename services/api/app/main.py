from fastapi import FastAPI, Depends, BackgroundTasks, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from .api import router as api_router
from . import models
from .database import init_db

app = FastAPI(title="OpenManus API", version="0.1.0")

# CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include api routes
app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def on_startup() -> None:
    # Initialize database on startup
    await init_db()