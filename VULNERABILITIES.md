# VULNERABILITIES.md — answer key

Every flaw planted in this fixture, with exact `file:line`, for cross-referencing
against Sentinel's `report.json` findings (coverage score = found / total).
All secrets are documented placeholders (AWS documentation example key, obvious
fakes). Code lives in 3 tiny modules (~59 lines): `secrets.py`, `db.py`, `app.py`.

| # | Severity | CWE | Flaw | Location |
|---|----------|-----|------|----------|
| 1 | critical | CWE-798 | Exposed secret-key file, imported by the app | `secrets.py:2-4` (imported at `db.py:9`, `app.py:8`) |
| 2 | medium | CWE-798 | Hardcoded DB credentials in connection string | `secrets.py:1` |
| 3 | critical | CWE-89 | SQL injection via `%` string formatting | `db.py:23`, `db.py:30` |
| 4 | critical | CWE-95 | `eval()` on request parameter | `app.py:18` |
| 5 | critical | CWE-78 | `shell=True` with user-controlled input | `app.py:14` |
| 6 | critical | CWE-502 | `pickle.loads()` on session data | `db.py:32` |
| 7 | critical | CWE-327 | MD5 password hashing / token | `db.py:24`, `db.py:29` |
| 8 | high | CWE-22 | Path traversal in download (`../`) | `app.py:16` |
| 9 | high | CWE-79 | Reflected XSS, unescaped request param in HTML | `app.py:18` |
| 10 | high | CWE-330 | Predictable session token (`md5(token + time)`) | `db.py:29` |
| 11 | high | CWE-295 | TLS verification disabled (`verify=False`) | `app.py:15` |
| 12 | high | CWE-862 | No authentication/authorization check on handler | `app.py:11` |
| 13 | low | CWE-1104 | Python 2 EOL runtime (`import md5`, `print` stmt) | e.g. `db.py:2`, `app.py:22` |

## Schema reference

The code targets the schema in `architecture/schema.mmd` (tables: departments,
employees, users, sessions, payroll_runs, payments, audit_log, uploads,
api_keys). `architecture/DIAGRAM_PROMPT.md` is the prompt used to generate the
diagram image for Sentinel's migration stage.
