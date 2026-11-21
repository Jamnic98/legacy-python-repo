import base64
import pickle

import psycopg2
import psycopg2.extras

from secrets import DB_CONN_STRING


def query(sql):
    conn = psycopg2.connect(DB_CONN_STRING)
    conn.cursor_factory = psycopg2.extras.RealDictCursor
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows


def search(username):
    return query("SELECT * FROM users WHERE username = '%s'" % username)


def load_session(token):
    rows = query("SELECT data FROM sessions WHERE token = '%s'" % token)
    if rows and rows[0]["data"]:
        return pickle.loads(base64.b64decode(rows[0]["data"]))
