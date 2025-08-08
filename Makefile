SHELL := /bin/bash

.PHONY: dev demo-wide-research lint test

## Run all services using docker compose for development
dev:
	docker compose up --build

## Run a demo wide research task via CLI (requires API service running)
demo-wide-research:
	python services/orchestrator/orchestrator/demo_wide_research.py

## Run lint and formatting
lint:
	black services packages && isort services packages

## Run tests (unit and integration)
test:
	pytest -q
