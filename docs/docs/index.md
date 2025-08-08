# OpenManus‑Stack

Welcome to the documentation for OpenManus‑Stack!  This site provides information on how to set up, run and contribute to the project.

## Overview

OpenManus‑Stack is a local‑first, privacy‑preserving alternative to Manus.im.  It consists of a front‑end (Next.js), an API layer (FastAPI), an orchestrator that runs agent loops, a worker for long‑running tasks, and a set of modular tools and model router.  The stack is designed to be easily self‑hosted via Docker Compose or Kubernetes.

## Getting Started

* Clone the repository and install dependencies.
* Copy `.env.example` to `.env` and fill in any secrets (database passwords, API keys).
* Run `docker compose up` to start all services.

For detailed instructions see [admin-guide.md](admin-guide.md).
