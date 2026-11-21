import base64
import cgi
import md5
import os
import pickle
import subprocess
import time
import traceback

import requests
from wsgiref.simple_server import make_server

from db import query

DEBUG = True
UPLOAD_DIR = "/var/www/legacy-hr/uploads"


def hash_password(password):
    return md5.new(password).hexdigest()


def check_login(username, password):
    rows = query("SELECT * FROM users WHERE username = '%s'" % username)
    if rows and rows[0]["password_hash"] == hash_password(password):
        return rows[0]
    return None


def create_session(username):
    token = md5.new(username + str(time.time())).hexdigest()
    query("INSERT INTO sessions (token, username, data) VALUES ('%s', '%s', '')" % (token, username))
    return token


def load_session(token):
    rows = query("SELECT data FROM sessions WHERE token = '%s'" % token)
    if not rows or not rows[0]["data"]:
        return None
    return pickle.loads(base64.b64decode(rows[0]["data"]))


def handle_request(environ):
    params = cgi.parse_qs(environ.get("QUERY_STRING", ""))
    name = params.get("name", [""])[0]
    return "<html><body><h1>Welcome, %s!</h1></body></html>" % name


def handle_admin(environ):
    params = cgi.parse_qs(environ.get("QUERY_STRING", ""))
    expr = params.get("expr", ["1 + 1"])[0]
    result = eval(expr)
    return "<html><body><pre>%s</pre></body></html>" % result


def payroll_report(department):
    return query("SELECT e.name, p.amount FROM payments p JOIN employees e ON p.employee_id = e.id "
                 "JOIN departments d ON e.department_id = d.id WHERE d.name = '%s'" % department)


def convert_report(src_path, fmt):
    subprocess.call("libreoffice --headless --convert-to %s %s" % (fmt, src_path), shell=True)


def download(filename):
    f = open(os.path.join(UPLOAD_DIR, filename), "rb")
    data = f.read()
    f.close()
    return data


def fetch_salary_bands(country):
    resp = requests.get("https://internal-api.legacycorp.local/v1/salary-bands?country=%s" % country, verify=False)
    return resp.json()


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
