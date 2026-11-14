# FastAPI AI Coding Checkpoint

A small FastAPI project used to practice a safe, repeatable, reviewable AI coding workflow.

The checkpoint asks for Claude Code. I could not use it (it needs a paid plan or API credits), so my instructor approved Ollama, Cline and OpenCode instead. I used **OpenCode**, first with a small local model (Ollama), then with a free hosted model.

**Start here:** [`docs/claude-code-checkpoint.md`](docs/claude-code-checkpoint.md) is the full write-up.

## What the app does
- `GET /health` returns `{"status": "ok"}`
- `GET /health-details` returns status, service name and version

## Run it
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest -q
```
If `requirements.txt` is missing, run `pip install fastapi uvicorn httpx pytest`.

## Where to look

| What | Where |
|---|---|
| Final write-up (config, commands, tests, diff review, security) | `docs/claude-code-checkpoint.md` |
| Review report (tests, then AI review, then my decision) | `reports/review-report.md` |
| Approved plan for the feature | `docs/plan-health-details-hosted.md` |
| My earlier plan and review of the weak model draft | `docs/plan-health-details.md` |
| Endpoint docs | `docs/endpoints.md` |
| Proof of what each model did (including failures) | `transcripts/` |
| Project rules | `AGENTS.md` |
| Memory and path rules | `.opencode/memory.md`, `.opencode/rules/` |
| Slash commands | `.opencode/command/` |
| Model setup and permissions | `opencode.json` |
| Claude Code version of the same setup (written first, not run) | `CLAUDE.md`, `.claude/` |

## Branches
- `master`: final version with everything merged
- `feature/health-details`: the feature work and history
- `manual-implementation`: my own hand-written version of the feature. A backup that I did not use.

## Safety setup
- Blocked: reading or editing `.env`, `.env.*` and `secrets/`
- Blocked: commands that print the environment, delete files, push to Git, or download from the web
- Allowed without asking: reading project files, `pytest`, `git status`, `git diff`, `git log`
- I tested the rules with a fake `.env` file. Results are in `transcripts/05-deny-rules-test.md`.

## Honest limits
- My laptop has no strong graphics card, so the local models were slow and weak. The 1B and 3B models failed at the plan, build and review steps (see `transcripts/`).
- The steps that worked used a free hosted model (MiniMax M3.1 Flash Free). Free services have limits and may keep prompts. This project has no real secrets.
- OpenCode cannot apply a rule to one folder only, so the test and docs rules load for every task.
- This is not Claude Code, so results may differ.
