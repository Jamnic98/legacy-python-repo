# VULNERABILITIES.md — answer key

Every flaw planted in this fixture, with exact `file:line`, for cross-referencing
against Sentinel's `report.json` findings (coverage score = found / total).
All secrets are documented placeholders (AWS documentation example key, obvious
fakes). Code lives in 3 tiny modules: `secrets.py`, `db.py`, `app.py`.

| # | Severity | CWE | Flaw | Location |
|---|----------|-----|------|----------|
| 1 | critical | CWE-798 | Exposed secret-key file, imported by the app | `secrets.py:2-4` (imported at `db.py:4`) |
| 2 | medium | CWE-798 | Hardcoded DB credentials in connection string | `secrets.py:1` |
| 3 | critical | CWE-89 | SQL injection via `%` string formatting | `db.py:18`, `app.py:24`, `app.py:32`, `app.py:37`, `app.py:58` |
| 4 | critical | CWE-95 | `eval()` on request parameter | `app.py:52` |
| 5 | critical | CWE-78 | `shell=True` with user-controlled input | `app.py:62` |
| 6 | critical | CWE-502 | `pickle.loads()` on session data | `app.py:40` |
| 7 | critical | CWE-327 | MD5 password hashing | `app.py:20` |
| 8 | high | CWE-22 | Path traversal in download (`../`) | `app.py:66` |
| 9 | high | CWE-79 | Reflected XSS, unescaped request param in HTML | `app.py:46` |
| 10 | high | CWE-330 | Predictable session token (`md5(user + time)`) | `app.py:31` |
| 11 | high | CWE-295 | TLS verification disabled (`verify=False`) | `app.py:73` |
| 12 | high | CWE-862 | Missing authorization check on admin endpoint | `app.py:49` |
| 13 | high | CWE-209 | Debug mode leaks full tracebacks to users | `app.py:85` (+ `app.py:15`) |
| 14 | low | CWE-1104 | Python 2 EOL runtime (`import md5`, `print` stmt) | all files, e.g. `app.py:3`, `app.py:91` |

## Schema reference

The code targets the schema in `architecture/schema.mmd` (tables: departments,
employees, users, sessions, payroll_runs, payments, audit_log, uploads,
api_keys). `architecture/DIAGRAM_PROMPT.md` is the prompt used to generate the
diagram image for Sentinel's migration stage.
