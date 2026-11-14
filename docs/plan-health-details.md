# Plan: GET /health-details

## Model draft (OpenCode, Plan mode, llama3.2:3b, 23m 25s) - NOT approved as-is

Files: app/main.py, tests/test_health.py
Tests: one test asserting status, service name and version
Risks and security: "None"
Steps: implement endpoint; add test; run pytest -q; "commit the changes to opencode.json"; wait for approval

## Human review of the draft
- Missing docs/endpoints.md (docs rule: update docs in the same change).
- Only one test; the test rules require a success case and an edge case.
- Risks listed as "None"; this is wrong, see below.
- Step 4 (commit opencode.json) is unrelated to this feature and Plan mode cannot commit.

## Revised plan (APPROVED by human before any edit)

Goal: Add GET /health-details returning status, service name, and version.

Expected files
- Modify app/main.py (add the endpoint; return hard-coded constants)
- Modify tests/test_health.py (add tests; keep the existing /health test)
- Create docs/endpoints.md (document /health and /health-details)

Tests
- Success: GET /health-details returns 200 and {"status": "ok", "service": "checkpoint-api", "version": "0.1.0"}
- Edge case: the response contains only the keys status, service and version (no environment data)
- Existing /health test must still pass

Risks and security
- Accidentally exposing environment variables or secrets: use constants only; do not read .env or os.environ.
- Breaking the existing /health endpoint: leave it unchanged and re-run its test.
- Scope creep: no changes to opencode.json, rules, or other files.

Implementation order
1. Add the endpoint to app/main.py.
2. Add the two tests to tests/test_health.py.
3. Create docs/endpoints.md.
4. Run pytest -q.
5. Review git diff against this plan.

Approval: Approved by the project owner.
