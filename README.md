# legacy-python-repo

> **WARNING: deliberately vulnerable test fixture — never deploy.**
> This repo exists so the Sentinel scanner can detect planted flaws and demo an
> end-to-end Python 2 -> Python 3 migration. Every "secret" in here is a
> documented placeholder (AWS/Stripe documentation example keys, obvious fakes).
> Do not reuse any value, and never point this code at a real system.

## What this is

A barebones Python 2 (WSGI/CGI-era) HR/payroll intranet portal. Small on
purpose so the hackathon demo (scan -> review -> migrate -> rescan) runs fast.

## Layout

- `run.py` — WSGI entry point
- `web_handler.py`, `admin.py` — request handlers
- `auth.py`, `session.py` — login and sessions
- `db.py` — Postgres access
- `reports.py`, `file_store.py`, `api_client.py`, `utils.py` — features
- `config.py` — configuration (planted hardcoded secrets)
- `architecture/` — DB schema (`schema.mmd`, `schema.svg`) + `DIAGRAM_PROMPT.md`
- `VULNERABILITIES.md` — answer key: every planted flaw with `file:line`

## Demo flow

1. `sentinel scan https://github.com/Jamnic98/legacy-python-repo.git --lang python --out reports/legacy`
2. Cross-reference `report.json` findings against `VULNERABILITIES.md` (coverage score)
3. `sentinel migrate ... --report ... --out ...` (ingesting `architecture/schema`)
4. Rescan the migrated output to show the findings drop
