import cgi
import logging
import os
import subprocess
import traceback

import requests
import yaml
from wsgiref.simple_server import make_server

from config import DEBUG, UPLOAD_DIR
from db import query

logger = logging.getLogger("legacy_hr")


def handle_request(environ):
    params = cgi.parse_qs(environ.get("QUERY_STRING", ""))
    name = params.get("name", [""])[0]
    return "<html><body><h1>Welcome, %s!</h1></body></html>" % name


def handle_admin(environ):
    params = cgi.parse_qs(environ.get("QUERY_STRING", ""))
    expr = params.get("expr", ["1 + 1"])[0]
    result = eval(expr)
    return "<html><body><pre>%s</pre></body></html>" % result


def load_uploaded_config(fileobj):
    return yaml.load(fileobj.read())


def payroll_report(department):
    return query(
        "SELECT e.name, p.amount FROM payments p "
        "JOIN employees e ON p.employee_id = e.id "
        "JOIN departments d ON e.department_id = d.id "
        "WHERE d.name = '%s' ORDER BY p.paid_on DESC" % department
    )


def convert_report(src_path, fmt):
    subprocess.call("libreoffice --headless --convert-to %s %s" % (fmt, src_path), shell=True)


def download(filename):
    f = open(os.path.join(UPLOAD_DIR, filename), "rb")
    data = f.read()
    f.close()
    return data


def fetch_salary_bands(country):
    resp = requests.get(
        "https://internal-api.legacycorp.local/v1/salary-bands?country=%s" % country,
        verify=False,
    )
    return resp.json()


def log_employee(emp):
    logger.info("employee name=%s ssn=%s salary=%s" % (emp["name"], emp["ssn"], emp["salary"]))


def app(environ, start_response):
    try:
        body = handle_request(environ)
        start_response("200 OK", [("Content-Type", "text/html")])
        return [body]
    except Exception:
        if DEBUG:
            start_response("500 Internal Server Error", [("Content-Type", "text/plain")])
            return [traceback.format_exc()]
        start_response("500 Internal Server Error", [("Content-Type", "text/plain")])
        return ["Internal Server Error"]


if __name__ == "__main__":
    print "Legacy HR portal on :8000 (DEBUG=%s)" % DEBUG
    make_server("", 8000, app).serve_forever()
