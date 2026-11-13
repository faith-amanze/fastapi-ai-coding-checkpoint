# OpenCode rules-summary attempts (llama3.2:1b, CPU only)

Attempt 1 (8k context): asked for a rules summary. The model printed a fake bash "tool call" as plain text and read no files (4m 36s).
Attempt 2 (32k context): asked it to list AGENTS.md coding rules. The model printed a fake JSON tool call with an invented URL and read no files (52s).

Conclusion: llama3.2:1b cannot call OpenCode's tools. No files were modified (git status clean).
