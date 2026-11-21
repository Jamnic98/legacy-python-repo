# VULNERABILITIES.md — answer key

Every flaw planted in this fixture, with exact `file:line`, for cross-referencing
against Sentinel's `report.json` findings (coverage score = found / total).
All secrets are documented placeholders (AWS documentation example key, obvious
fakes). Code lives in 4 modules: `config.py`, `db.py`, `auth.py`, `app.py`.

| # | Severity | CWE | Flaw | Location |
|---|----------|-----|------|----------|
| 1 | critical | CWE-798 | Hardcoded API keys / service secrets | `config.py:5-9` |
| 2 | medium | CWE-798 | Hardcoded DB credentials in connection string | `config.py:3` |
| 3 | low | CWE-798 | Commented-out prod credentials in source | `config.py:13-14` |
| 4 | critical | CWE-89 | SQL injection via `%` string formatting | `db.py:38`, `auth.py:15`, `auth.py:25`, `auth.py:35`, `auth.py:40`, `auth.py:47`, `app.py:39` |
| 5 | critical | CWE-95 | `eval()` on request parameter | `app.py:26` |
| 6 | critical | CWE-78 | `shell=True` with user-controlled input | `app.py:44` |
| 7 | critical | CWE-502 | `pickle.loads()` on session data | `auth.py:43` |
| 8 | medium | CWE-502 | Unsafe `yaml.load()` on uploaded config | `app.py:31` |
| 9 | critical | CWE-327 | MD5 password hashing | `auth.py:11` |
| 10 | high | CWE-338 | `random` (not `secrets`) for reset tokens | `auth.py:24` |
| 11 | high | CWE-22 | Path traversal in download (`../`) | `app.py:48` |
| 12 | high | CWE-79 | Reflected XSS, unescaped request param in HTML | `app.py:20` |
| 13 | high | CWE-330 | Predictable session token (`md5(user + time)`) | `auth.py:30` |
| 14 | high | CWE-295 | TLS verification disabled (`verify=False`) | `app.py:57` |
| 15 | high | CWE-862 | Missing authorization check on admin endpoint | `app.py:23` |
| 16 | high | CWE-209 | Debug mode leaks full tracebacks to users | `app.py:74` (+ `config.py:1`) |
| 17 | medium | CWE-532 | SSN/salary written to logs | `app.py:63` |
| 18 | low | CWE-1104 | Python 2 EOL runtime (`import md5`, `print` stmt) | all files, e.g. `auth.py:2`, `app.py:80` |
| 19 | low | CWE-1104 | Ancient pinned dependencies | `requirements.txt:1-3` |

## Schema reference

The code targets the schema in `architecture/schema.mmd` / `architecture/schema.svg`
(tables: departments, employees, users, sessions, payroll_runs, payments,
audit_log, uploads, api_keys). `architecture/DIAGRAM_PROMPT.md` is the prompt used
to generate the diagram image for Sentinel's migration stage.
