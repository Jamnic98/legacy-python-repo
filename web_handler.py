import cgi


def handle_request(environ):
    params = cgi.parse_qs(environ.get("QUERY_STRING", ""))
    name = params.get("name", [""])[0]
    return "<html><body><h1>Welcome, %s!</h1></body></html>" % name
