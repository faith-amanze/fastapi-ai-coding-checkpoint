---
description: Run tests and fix failures with minimal changes
---
1. Run pytest -q and report any failures.
2. Explain the root cause of each failure.
3. Fix the application code with the smallest possible change. Never delete or weaken tests.
4. Re-run pytest -q until it passes, then show git diff.
