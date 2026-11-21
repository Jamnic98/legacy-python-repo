# VULNERABILITIES.md — answer key

Exactly 4 flaws planted in this fixture, with exact `file:line`, for
cross-referencing against Sentinel's `report.json` findings (coverage score =
found / 4). All secrets are documented placeholders (AWS documentation example
key, obvious fakes). Code lives in 3 tiny modules (~45 lines): `secrets.py`,
`db.py`, `app.py`. (The Python 2 runtime itself is also EOL — CWE-1104 — e.g.
the `print` statement at `app.py:14`; not scored.)

| # | Severity | CWE | Flaw | Location |
|---|----------|-----|------|----------|
| 1 | critical | CWE-798 | Hardcoded secrets in a dedicated file, imported by the app | `secrets.py:1-4` (imports: `db.py:7`, `app.py:4`) |
| 2 | critical | CWE-89 | SQL injection via `%` string formatting | `db.py:21`, `db.py:25` |
| 3 | critical | CWE-95 | `eval()` on request parameter | `app.py:10` |
| 4 | critical | CWE-502 | `pickle.loads()` on session data | `db.py:27` |

## Schema reference

The code targets the schema in `architecture/schema.mmd` (tables: departments,
employees, users, sessions, payroll_runs, payments, audit_log, uploads,
api_keys). `architecture/DIAGRAM_PROMPT.md` is the prompt used to generate the
diagram image for Sentinel's migration stage.
