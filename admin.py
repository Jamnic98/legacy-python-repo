import cgi

import yaml

from db import query


def handle_admin(environ):
    params = cgi.parse_qs(environ.get("QUERY_STRING", ""))
    expr = params.get("expr", ["1 + 1"])[0]
    result = eval(expr)
    return "<html><body><pre>%s</pre></body></html>" % result


def list_users():
    return query("SELECT username, role FROM users")


def load_uploaded_config(fileobj):
    return yaml.load(fileobj.read())
