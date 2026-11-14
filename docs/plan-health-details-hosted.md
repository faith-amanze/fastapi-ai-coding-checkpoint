# Plan: GET /health-details (OpenCode Plan mode, hosted model)

Model: MiniMax M3.1 Flash Free, Plan mode, 24.3s. The model read the repo (app/main.py, tests/test_health.py, docs/plan-health-details.md) before planning.

1. Goal: add GET /health-details returning service status, name and version.
2. Files: modify app/main.py (constants only); modify tests/test_health.py (keep /health test); create docs/endpoints.md.
3. Tests: success (200 and {"status":"ok","service":"checkpoint-api","version":"0.1.0"}); edge case (exactly the keys status, service, version); existing /health test still passes.
4. Risks: secret/environment leakage (no os.environ or .env); breaking /health; scope creep (no changes to opencode.json, .opencode/); hard-coded version drift.
5. Order: add endpoint with type hints; add two tests; create docs/endpoints.md; run pytest -q; review git diff against this plan.
Open question answered by human: service "checkpoint-api", version "0.1.0".

Approval: Approved by the project owner before any edit.
