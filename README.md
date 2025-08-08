# OpenManus‑Stack

OpenManus‑Stack is an open‑source, self‑hostable alternative to [Manus.im](https://manus.im).  It provides an agentic platform for executing multi‑step tasks autonomously, with a modern web UI, a pluggable model router, and a robust back‑end orchestrator.  The goal of the project is to deliver feature parity (or better) with Manus while remaining privacy‑preserving and local‑first.

## Features

* **Autonomous tasks** — A planner/executor/verifier loop built with LangGraph and AutoGen executes complex workflows from a single high‑level goal.
* **Wide Research mode** — Fan‑out a task into 100+ sub‑agents for large‑scale information gathering and merge the results with deduplication and citations.
* **Pluggable tools** — Modular adapters for browser automation (Playwright), HTTP/GraphQL APIs, code execution, RAG/embeddings, email, calendar and more.
* **Model router** — Route prompts to any OpenAI‑compatible model or local LLM (LM Studio, Ollama, vLLM) with cost and latency tracking.
* **Rich UI** — Next.js front‑end (TypeScript + Tailwind + shadcn/ui) with dark mode, workspaces/projects, live run timeline, wide research dashboard, and deterministic replay.
* **Audit & replay** — Append‑only audit log in Postgres, with run replay export to JSON and deterministic re‑runs using pinned seeds.
* **Observability** — Built‑in OpenTelemetry, Prometheus and Grafana dashboards for tracing, metrics and cost accounting.
* **Privacy and security** — All services are self‑hosted, credentials are stored locally, each task runs in its own unprivileged sandbox (rootless Docker) with network egress allow‑lists.

## Quick Start

Ensure you have Docker and Docker Compose installed.  Clone this repository and run the stack:

```bash
git clone https://github.com/your-user/openmanus-stack.git
cd openmanus-stack
cp .env.example .env  # populate secrets as needed
docker compose up --build
```

Open your browser to `http://localhost:3000` to access the UI.  The API is served at `http://localhost:8000/api`.

For development, there is a `Makefile` with shortcuts:

```bash
make dev            # run services locally without Docker
make demo-wide-research  # run a sample Wide Research task via CLI
```

For more details, see the [documentation](docs/index.md).
