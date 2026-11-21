import cgi

import db
from secrets import AWS_SECRET_ACCESS_KEY


def handle(environ):
    p = cgi.parse_qs(environ.get("QUERY_STRING", ""))
    expr = p.get("expr", ["1 + 1"])[0]
    return str(eval(expr))


if __name__ == "__main__":
    print "Legacy HR portal on :8000"
