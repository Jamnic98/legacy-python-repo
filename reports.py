import subprocess

from db import query


def payroll_report(department):
    return query(
        "SELECT e.name, p.amount FROM payments p "
        "JOIN employees e ON p.employee_id = e.id "
        "JOIN departments d ON e.department_id = d.id "
        "WHERE d.name = '%s' ORDER BY p.paid_on DESC" % department
    )


def convert_report(src_path, fmt):
    subprocess.call("libreoffice --headless --convert-to %s %s" % (fmt, src_path), shell=True)
