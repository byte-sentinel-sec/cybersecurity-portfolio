# 7. File Permissions in Linux

**Skills:** Linux CLI · `ls -la` · `chmod` · principle of least privilege

## Overview
Audited and tightened file permissions for a research team's `projects` directory to match company policy.

## Reading a permission string
Example: `project_k.txt` was `-rw-rw-rw-`

| Position | Meaning | Value |
|---|---|---|
| 1 | File type | `-` regular file |
| 2–4 | Owner (user) | `rw-` read + write |
| 5–7 | Group | `rw-` read + write |
| 8–10 | Others | `rw-` read + write ⚠️ |

## Changes made
| Target | Problem | Command | Result |
|---|---|---|---|
| `project_k.txt` | World-writable | `chmod o-w project_k.txt` | `-rw-rw-r--` |
| `.project_x.txt` (hidden) | Needed to be read-only for owner and group | `chmod 440 .project_x.txt` | `-r--r-----` |
| `drafts/` | Sensitive, should be owner-only | `chmod 700 drafts` | `drwx------` |

Hidden files were revealed with `ls -la` (`-a` shows dotfiles).

📄 [Original report with terminal screenshots](original-report.pdf)
