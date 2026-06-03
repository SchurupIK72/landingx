# AGENTS.md

## Windows / UTF-8 rules

- Always use the `apply_patch` tool for file edits when possible.
- Never invoke `apply_patch` through PowerShell pipes, heredocs, or shell redirection.
- Do not use `Set-Content`, `Add-Content`, or raw PowerShell output to rewrite UTF-8 files unless absolutely necessary.
- If shell-based file editing is required, use Python with explicit `encoding="utf-8"`.
- Treat mojibake in PowerShell output as a console-display issue first; verify file contents with Python, not with plain terminal output.
- For Unicode verification, print `unicode_escape` or inspect the file in the editor.
- If a write fails with access errors, treat it as a sandbox/permissions issue, not an encoding issue.
- After changing files used by Docker, rebuild with `docker compose up -d --build`.
- Be especially careful with translation dictionaries and non-ASCII text; avoid bulk regex rewrites unless necessary.
- Never edit multilingual text through PowerShell string replacement.
- Never trust PowerShell console rendering as proof of file corruption.
- Prefer minimal targeted patches over full-file rewrites.
