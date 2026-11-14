# Claude Code Checkpoint

## 1. What I used (and why)
The checkpoint asks for Claude Code. I could not use it, because it needs a paid plan or paid API credits, and I did not have either. My instructor allowed these tools instead: **Ollama, Cline and OpenCode**.

I used **OpenCode** as my coding agent. I used **Ollama** to run a small model on my own laptop first. Later I used a free hosted model inside OpenCode, because the small model was too weak.

The workflow is the same as the checkpoint: rules, memory, safe permissions, three commands, a plan, approval, code, tests, diff review, and a report.

## 2. Configuration files I created

| File | What it does |
|---|---|
| `AGENTS.md` | Main project rules (overview, folders, run command, test command, coding rules). OpenCode's version of `CLAUDE.md`. |
| `.opencode/memory.md` | Stable facts only. No secrets, no guesses. |
| `.opencode/rules/tests.md` | Rules for tests. |
| `.opencode/rules/docs.md` | Rules for documentation. |
| `opencode.json` | Model setup, the list of rule files, and the permissions. |
| `.opencode/command/plan-feature.md` | Slash command `/plan-feature`. |
| `.opencode/command/review-diff.md` | Slash command `/review-diff`. |
| `.opencode/command/fix-tests.md` | Slash command `/fix-tests`. |
| `ollama/Modelfile`, `ollama/Modelfile-3b` | Settings for the local models (bigger context window). |
| `.github/workflows/review.yml` (if present) | Optional test workflow. |
| `CLAUDE.md` and `.claude/` | The Claude Code version of the same setup. I wrote it first. I kept it in the repo, but I did not run it. |

**One limit:** OpenCode cannot apply a rule to only one folder. So the test rules and docs rules are loaded for every task. Each rule file starts by saying when it applies.

## 3. Command examples

```powershell
uvicorn app.main:app --reload     # run the app
pytest -q                         # run the tests
opencode                          # start OpenCode (check the model name first!)
```

Inside OpenCode:
```text
/models                           # pick the model
/plan-feature add GET /health-details returning status, service name and version
/review-diff
```
I pressed **Tab** to switch between **Plan** mode (read only) and **Build** mode (can edit).

## 4. The models I tried (honest summary)

| Model | Where it ran | What happened |
|---|---|---|
| Llama 3.2 1B | My laptop (CPU) | Could not use tools. It printed fake tool calls. Failed. |
| Llama 3.2 3B | My laptop (CPU) | Read a file and wrote a rules summary in 14 minutes, but the Memory section was wrong. The plan was weak ("Risks: None"). The build ran 1 hour 8 minutes and changed nothing. The review failed on bad file paths. |
| GPT OSS 120B | Groq (hosted) | Hit the free limit: 8,000 tokens per minute. Not usable for this project. |
| MiniMax M3.1 Flash Free | OpenCode free tier (hosted) | Worked. Summary 24.9s, plan 24.3s, build done, review 2m 11s. |

Evidence is in the `transcripts/` folder. Because the hosted model is a free online service, my prompts and project files were sent to it. The project is a small practice app with no real secrets.

## 5. What each step produced

**Rules summary (Plan mode, no edits).** The 3B model got most of it right but the Memory section wrong. MiniMax got every section right. Files: `transcripts/01-rules-summary.md`, `transcripts/01b-rules-summary-hosted.md`.

**Plan for `GET /health-details`.** The 3B draft was poor, so I reviewed it myself and wrote a better plan (`docs/plan-health-details.md`). MiniMax then made a good plan (`docs/plan-health-details-hosted.md`): files, tests, risks, and "Approve this plan?". I approved it before any edit. MiniMax had read my earlier plan, so its plan was not fully independent.

**Implementation.** MiniMax wrote the code in Build mode, after my approval. The 3B model failed at this (see `transcripts/02-build-attempt.md`).

## 6. Test results

| When | Result |
|---|---|
| Start of project | 1 passed |
| After the feature | 3 passed |
| Run again by OpenCode during the review | 3 passed |

The old `/health` test still passes. The new tests check the exact response and the exact keys.

## 7. Diff review
The diff changed only the three planned files:
- `app/main.py`: two constants and the new endpoint
- `tests/test_health.py`: two new tests
- `docs/endpoints.md`: new file

It did not touch `opencode.json`, `.opencode/` or any `.env` file. The endpoint returns fixed values and reads no environment data.

**One change that was not in the plan:** `health()` got a return type hint (`-> dict[str, str]`). The plan said to leave `/health` alone. I accepted it because my own rule says all functions need type hints. The behavior is the same.

The AI review (`/review-diff`) said **APPROVE**. It also pointed out that `transcripts/git-diff.patch` was an extra file. I kept it on purpose as evidence. See `reports/review-report.md` and `transcripts/04-review-hosted.md`.

## 8. Security notes
- `.env`, `.env.*` and `secrets/` are blocked for reading and editing.
- Commands that print the environment are blocked (`env`, `printenv`, `Get-ChildItem Env:` and similar).
- Delete commands, `git push`, `git reset --hard`, `curl` and `wget` are blocked.
- Allowed without asking: reading project files, `pytest`, `git status`, `git diff`, `git log`.
- `.gitignore` excludes `.env*` and `secrets/`.

**I tested the rules with a fake `.env` file** (no real secrets), then deleted it. Results are in `transcripts/05-deny-rules-test.md`:
- Asking to read `.env`, and asking to run `Get-Content .env`: the model refused because of my `AGENTS.md` rules.
- Running `Get-ChildItem Env:`: blocked by the permission rule, with no prompt.
- Forcing a Read of `.env`: blocked by the permission rule, with no prompt.
- The fake value never appeared on screen.

I did not test reading `.env.example`.

Other safety points:
- OpenCode asked permission when the model tried to reach `C:\Users\faith\*` (my whole home folder). I rejected it every time.
- I never chose "Allow always".
- I allowed shell commands only when they were read-only commands inside the project.

## 9. Limits and what I would do differently
- My laptop has no strong graphics card, so local models were slow and weak. A better computer or a paid model would help.
- The free hosted model worked, but free services have limits and may keep prompts.
- Path-specific rules are not supported in OpenCode, so I used a workaround.
- This is not Claude Code. The results may differ from what Claude Code would do.
