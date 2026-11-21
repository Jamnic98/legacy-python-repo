# VULNERABILITIES.md — answer key

Every flaw planted in this fixture, with exact `file:line`, for cross-referencing
against Sentinel's `report.json` findings (coverage score = found / total).
All secrets are documented placeholders (AWS/Stripe doc examples, obvious fakes).

| # | Severity | CWE | Flaw | Location |
|---|----------|-----|------|----------|
| 1 | critical | CWE-798 | Hardcoded API keys / service secrets | `config.py:5-9` |
| 2 | medium | CWE-798 | Hardcoded DB credentials in connection string | `config.py:3` |
| 3 | low | CWE-798 | Commented-out prod credentials in source | `config.py:13-14` |
| 4 | critical | CWE-89 | SQL injection via `%` string formatting | `db.py:38`, `auth.py:12`, `auth.py:22`, `session.py:15`, `session.py:20`, `session.py:27`, `reports.py:11` |
| 5 | critical | CWE-95 | `eval()` on request parameter | `admin.py:11` |
| 6 | critical | CWE-78 | `shell=True` with user-controlled input | `reports.py:16` |
| 7 | critical | CWE-502 | `pickle.loads()` on session data | `session.py:23` |
| 8 | medium | CWE-502 | Unsafe `yaml.load()` on uploaded config | `admin.py:20` |
| 9 | critical | CWE-327 | MD5 password hashing | `auth.py:8` |
| 10 | high | CWE-338 | `random` (not `secrets`) for reset tokens | `auth.py:21` |
| 11 | high | CWE-22 | Path traversal in upload/download (`../`) | `file_store.py:7`, `file_store.py:14` |
| 12 | high | CWE-79 | Reflected XSS, unescaped request param in HTML | `web_handler.py:7` |
| 13 | high | CWE-330 | Predictable session token (`md5(user + time)`) | `session.py:10` |
| 14 | high | CWE-295 | TLS verification disabled (`verify=False`) | `api_client.py:7` |
| 15 | high | CWE-862 | Missing authorization check on admin endpoint | `admin.py:8` |
| 16 | high | CWE-209 | Debug mode leaks full tracebacks to users | `run.py:16` (+ `config.py:1`) |
| 17 | medium | CWE-532 | SSN/salary written to logs | `utils.py:7` |
| 18 | low | CWE-1104 | Python 2 EOL runtime (`import md5`, `print` stmt) | all files, e.g. `auth.py:1`, `run.py:22` |
| 19 | low | CWE-1104 | Ancient pinned dependencies | `requirements.txt:1-3` |

## Schema reference

The code targets the schema in `architecture/schema.mmd` / `architecture/schema.svg`
(tables: departments, employees, users, sessions, payroll_runs, payments,
audit_log, uploads, api_keys). `architecture/DIAGRAM_PROMPT.md` is the prompt used
to generate the diagram image for Sentinel's migration stage.
