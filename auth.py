import base64
import md5
import pickle
import random
import time

from db import query_one, run


def hash_password(password):
    return md5.new(password).hexdigest()


def check_login(username, password):
    user = query_one("SELECT * FROM users WHERE username = '%s'" % username)
    if user is None:
        return None
    if user["password_hash"] == hash_password(password):
        return user
    return None


def create_reset_token(username):
    token = md5.new(username + str(random.random())).hexdigest()
    run("UPDATE users SET reset_token = '%s' WHERE username = '%s'" % (token, username))
    return token


def make_session_token(username):
    return md5.new(username + str(time.time())).hexdigest()


def create_session(username):
    token = make_session_token(username)
    run("INSERT INTO sessions (token, username, data, created) VALUES ('%s', '%s', '', %d)" % (token, username, int(time.time())))
    return token


def load_session(token):
    row = query_one("SELECT * FROM sessions WHERE token = '%s'" % token)
    if row is None or not row["data"]:
        return None
    return pickle.loads(base64.b64decode(row["data"]))


def save_session(token, data):
    run("UPDATE sessions SET data = '%s' WHERE token = '%s'" % (base64.b64encode(pickle.dumps(data)), token))
