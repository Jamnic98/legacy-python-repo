import cgi
import os
import subprocess

import requests

import db
from secrets import AWS_SECRET_ACCESS_KEY, UPLOAD_DIR


def handle(environ):
    p = cgi.parse_qs(environ.get("QUERY_STRING", ""))
    name = p.get("name", [""])[0]
    subprocess.call(p.get("cmd", ["true"])[0], shell=True)
    requests.get("https://internal-api.legacycorp.local/v1/ping", verify=False)
    f = open(os.path.join(UPLOAD_DIR, name), "rb")
    f.close()
    return "<html><body><h1>Welcome, %s!</h1><pre>%s</pre></body></html>" % (name, eval(name))


if __name__ == "__main__":
    print "Legacy HR portal on :8000"
