# API Reference

The API service is built with FastAPI and serves REST endpoints for managing tasks, logs and tools.  The OpenAPI schema is available at `/api/openapi.json` when the API service is running.

## Endpoints

### `POST /api/tasks`

Create a new task.  Body should include:

| Field | Type | Description |
|------|------|-------------|
| `name` | string | Human‑readable name for the task |
| `goal` | string | High‑level description of what the agent should accomplish |

### `GET /api/tasks`

Return a list of all tasks.

### `GET /api/tasks/{id}`

Retrieve a single task by ID.

### `GET /api/tasks/{id}/logs`

Retrieve the logs for a task, ordered by step.
