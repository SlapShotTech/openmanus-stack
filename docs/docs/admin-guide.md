# Admin Guide

## Configuration

All services are configured via environment variables; see `.env.example` for defaults.  The following variables are most important:

* `DATABASE_URL` — SQLAlchemy connection string for Postgres.
* `REDIS_URL` — Redis connection string used by orchestrator and workers.
* `MINIO_ENDPOINT`, `MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY` — configuration for artifact store.
* `MODEL_PROVIDER` — which LLM provider to use (`openai`, `ollama`, `vllm`, `lmstudio`).
* `OPENAI_API_KEY` — API key for OpenAI (if using `openai` provider).
* `OLLAMA_HOST`, `VLLM_HOST`, `LM_STUDIO_HOST` — hostnames for local LLM servers.
* `ALLOW_EGRESS_DOMAINS` — comma‑separated list of domains tools are allowed to reach.

You can set these variables in a `.env` file at the repository root; Docker Compose will automatically load them.

## Running Wide Research

The orchestrator includes a special mode for “wide research.”  When a goal requires broad information gathering, the orchestrator shards the task into many sub‑tasks, runs them concurrently via the worker pool, and then merges the results.  The fan‑out/fan‑in controller ensures retries on failure and deduplicates results.

To experiment with wide research locally, run:

```bash
make demo-wide-research
```

This will enqueue a sample task that asks the agent to research programming languages.  You can observe the fan‑out and logs in the UI.

## Auth

The recommended authentication provider is Keycloak.  The provided Docker Compose file starts a Keycloak container with a default admin user.  You should log in to the Keycloak admin console (`http://localhost:8080`) and create realms, clients and users as needed.  The front‑end uses OIDC implicit flow via `@keycloak/keycloak-js`.

## Security Considerations

OpenManus‑Stack emphasizes privacy and safety.  All code executed by the agent runs inside a rootless Docker container with seccomp/cgroups, and only specific domains are allowed for network egress.  Tools must be explicitly enabled by the admin.  Sensitive user data should be redacted before logging.  See the [security model](security-model.md) for more details.
