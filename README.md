# legacy-python-repo

> **WARNING: deliberately vulnerable test fixture — never deploy.**
> This repo exists so the Sentinel scanner can detect planted flaws and demo an
> end-to-end Python 2 -> Python 3 migration. Every "secret" in here is a
> documented placeholder (AWS documentation example key, obvious fakes).
> Do not reuse any value, and never point this code at a real system.

## What this is

A tiny Python 2 HR/payroll portal fixture (3 code files, ~114 lines) so the
hackathon demo (scan -> review -> migrate -> rescan) runs fast.

## Layout

- `secrets.py` — exposed secret keys, imported by the app (planted CWE-798)
- `db.py` — Postgres access (SQLi)
- `app.py` — auth, sessions, handlers, WSGI entry point
- `architecture/` — DB schema (`schema.mmd`) + `DIAGRAM_PROMPT.md`
- `VULNERABILITIES.md` — answer key: every planted flaw with `file:line`

## Demo flow

1. `sentinel scan https://github.com/Jamnic98/legacy-python-repo.git --lang python --out reports/legacy`
2. Cross-reference `report.json` findings against `VULNERABILITIES.md` (coverage score)
3. `sentinel migrate ... --report ... --out ...` (ingesting `architecture/schema.mmd` / the generated diagram)
4. Rescan the migrated output to show the findings drop
