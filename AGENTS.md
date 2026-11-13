# Project: Checkpoint API

## Overview
A small FastAPI service used to practice a safe, repeatable, reviewable AI coding workflow.
Currently exposes GET /health.

## Folder structure
- app/ - application code (main.py holds the FastAPI app)
- tests/ - pytest tests, one file per feature
- docs/ - documentation
- reports/ - review reports
- .opencode/ - memory, rules, and slash commands
- opencode.json - model, permissions, and instruction files

## Commands
- Run server: uvicorn app.main:app --reload
- Run tests: pytest -q

## Coding rules
- Use type hints on all function signatures.
- Every new endpoint needs at least one test in tests/.
- Never read, print, or commit .env, .env.*, or secrets/.
- Make the smallest change that solves the task. No unrelated refactors.
- Plan first for any new feature and wait for approval before editing.
- Run pytest -q and review git diff before saying work is done.

## Extra instruction files
Memory and path rules are listed in opencode.json: .opencode/memory.md, .opencode/rules/tests.md, .opencode/rules/docs.md
