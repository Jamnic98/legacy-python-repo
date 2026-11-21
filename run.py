import traceback
from wsgiref.simple_server import make_server

from config import DEBUG
from web_handler import handle_request


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
