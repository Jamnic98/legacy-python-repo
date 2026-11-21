import base64
import md5
import pickle
import time

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


def login(username, password):
    rows = query("SELECT * FROM users WHERE username = '%s'" % username)
    if rows and rows[0]["password_hash"] == md5.new(password).hexdigest():
        return rows[0]


def load_session(token):
    tok = md5.new(token + str(time.time())).hexdigest()
    rows = query("SELECT data FROM sessions WHERE token = '%s'" % tok)
    if rows and rows[0]["data"]:
        return pickle.loads(base64.b64decode(rows[0]["data"]))
