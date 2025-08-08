## Contributing to OpenManus‑Stack

Thank you for considering contributing!  The project aims to be a community‑driven alternative to Manus.im.  We welcome pull requests, bug reports and feature requests.

### Getting Started

1. Fork the repository on GitHub and clone your fork locally.
2. Create a branch off of `main` for your feature or bug fix.
3. Ensure all tests pass and new code is fully tested.
4. Open a pull request with a clear description of your changes.

### Development Environment

Use the provided `docker compose` setup for an easy local stack.  Alternatively, you can run services individually:

* `apps/frontend` — `pnpm dev`
* `services/api` — `uvicorn app.main:app --reload`
* `services/orchestrator` — `python -m orchestrator`
* `services/worker` — `celery -A worker.tasks worker -l info`

See [docs/developer-guide.md](docs/developer-guide.md) for more details.

### Code of Conduct

We expect all participants to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).
