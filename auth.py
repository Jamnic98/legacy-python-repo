import md5
import random

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
