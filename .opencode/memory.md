# Stable Project Facts
- Framework: FastAPI. Server: uvicorn. Tests: pytest with FastAPI TestClient.
- App entry point: app.main:app
- Existing endpoint: GET /health returns {"status": "ok"}
- Test command: pytest -q
- Workflow: plan, approval, implement, pytest, git diff review.
