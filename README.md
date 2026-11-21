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

- `config.py` — configuration (planted hardcoded secrets, debug flag)
- `db.py` — Postgres access (SQLi)
- `auth.py` — login + sessions (MD5, pickle, predictable/random tokens)
- `app.py` — handlers and WSGI entry point (XSS, eval, shell, traversal, TLS, authz, debug)
- `requirements.txt` — ancient pinned deps
- `architecture/` — DB schema (`schema.mmd`, `schema.svg`) + `DIAGRAM_PROMPT.md`
- `VULNERABILITIES.md` — answer key: every planted flaw with `file:line`

## Demo flow

1. `sentinel scan https://github.com/Jamnic98/legacy-python-repo.git --lang python --out reports/legacy`
2. Cross-reference `report.json` findings against `VULNERABILITIES.md` (coverage score)
3. `sentinel migrate ... --report ... --out ...` (ingesting `architecture/schema`)
4. Rescan the migrated output to show the findings drop
