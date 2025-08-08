# Developer Guide

This guide explains how to work on the OpenManus‑Stack codebase.

## Monorepo Layout

The repository uses a PNPM workspace layout:

* `apps/frontend` — Next.js TypeScript front‑end.
* `services/api` — FastAPI application.
* `services/orchestrator` — Agentic brain built with LangGraph/AutoGen.
* `services/worker` — RQ worker for long‑running tasks.
* `packages/tools` — Modular tool adapters.
* `packages/model-router` — Model routing logic.
* `infra` — Supporting infrastructure configuration (OpenTelemetry, Prometheus, etc.). The Docker Compose file lives at the repository root.
* `docs` — MkDocs documentation.
* `tests` — Pytest/Jest test suites and GAIA evaluation harness.

## Setting up Development

Install dependencies:

```bash
cd openmanus-stack
python -m venv .venv && source .venv/bin/activate
pip install -r services/api/requirements.txt -r services/orchestrator/requirements.txt
pnpm install --filter apps/frontend
```

Then run each service in separate terminals (or use `make dev`):

```bash
uvicorn services/api/app/main:app --reload
python -m services/orchestrator/orchestrator.server
python -m services/worker/worker.main
pnpm --filter apps/frontend dev
```

## Writing Tools

To add a new tool, create a module in `packages/tools`.  Each tool should provide an async API that can be called by the executor.  Write unit tests in `tests/tools`.
