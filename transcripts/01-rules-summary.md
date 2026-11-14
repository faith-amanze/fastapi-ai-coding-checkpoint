# OpenCode rules summary (Plan mode, no edits)

Tool: OpenCode 1.19.5 with Ollama, model llama3.2:3b (16k context), CPU only.
Time: 14m 39s.

Notes on accuracy:
- The model made one tool call (Read AGENTS.md). The test, docs, and memory files reached it through the "instructions" list in opencode.json.
- Overview, Commands, Coding rules, Test rules, and Docs rules match the source files.
- The "Memory facts" section is WRONG: it repeated a pointer line from AGENTS.md instead of the facts in memory.md.
- The output also contains OpenCode's built-in Plan mode reminder text, echoed by the model.
- Earlier attempts with llama3.2:1b failed (see 00-failed-attempts.md).

## Raw output

Overview
A small FastAPI service used to practice a safe, repeatable, reviewable AI coding workflow.

Commands
- Run server: uvicorn app.main:app --reload
- Run tests: pytest -q

Coding rules
- Use type hints on all function signatures.
- Every new endpoint needs at least one test in tests/.
- Never read, print, or commit .env, .env.*, or secrets/.
- Make the smallest change that solves the task. No unrelated refactors.
- Plan first for any new feature and wait for approval before editing.
- Run pytest -q and review git diff before saying work is done.

Test rules
- Use pytest and fastapi.testclient.TestClient.
- One test file per feature: tests/test_<feature>.py
- Assert both the status code and the response body.
- Cover at least one success case and one edge case for new endpoints.
- Never delete or weaken a test just to make it pass.
- Tests must not read .env files or use real secrets.

Docs rules
- Write short, clear Markdown with one H1 title.
- Include runnable command examples in code blocks.
- Document each endpoint: method, path, example response.
- Never include secrets or real environment values.
- Update docs in the same change as the code.

Memory facts
Memory and path rules are listed in opencode.json: .opencode/memory.md, .opencode/rules/tests.md, .opencode/rules/docs.md
