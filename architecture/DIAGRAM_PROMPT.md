# Diagram generation prompt

Give the prompt below to a diagram-capable model (e.g. mistral-large-4) to
produce the schema image that Sentinel ingests during the migration stage.
The checked-in `schema.mmd` (Mermaid `erDiagram`) is the textual source of the
same schema, so the generated image can be verified or regenerated.

---

Create a clean entity-relationship (ER) database schema diagram for a legacy
"HR/Payroll intranet portal" written in Python 2. Render it as a single image
(PNG or SVG), landscape orientation, white background. Draw one box per table:
table name as a bold header, columns listed underneath, with `PK` / `FK`
markers. Connect every foreign key with a straight line, crow's-foot on the
"many" side. Include no text other than table names, column names, and PK/FK
markers.

Tables and columns (use exactly these):

- departments(id PK, name, budget)
- employees(id PK, department_id FK -> departments.id, name, email, ssn, salary, hire_date)
- users(id PK, employee_id FK -> employees.id, username UNIQUE, password_hash, role, reset_token)
- sessions(token PK, username, data, created)
- payroll_runs(id PK, period, created_by FK -> users.id, status)
- payments(id PK, payroll_run_id FK -> payroll_runs.id, employee_id FK -> employees.id, amount, paid_on)
- audit_log(id PK, username, action, detail, created_at)
- uploads(id PK, filename, path, owner, uploaded_at)
- api_keys(id PK, service, key_value, created_at)

Suggested layout: departments top-left, employees center-left, users center,
sessions top-right, payroll_runs bottom-center, payments bottom-right,
audit_log / uploads / api_keys along the right edge.

The diagram must match the SQL statements in db.py and app.py so a
migration model can rebuild the database schema from the image alone.

---
