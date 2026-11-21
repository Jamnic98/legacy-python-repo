import psycopg2
import psycopg2.extras

from config import DB_CONN_STRING


def get_connection():
    conn = psycopg2.connect(DB_CONN_STRING)
    conn.cursor_factory = psycopg2.extras.RealDictCursor
    return conn


def run(sql):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


def query(sql):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows


def query_one(sql):
    rows = query(sql)
    if rows:
        return rows[0]
    return None


def search_employees(name):
    return query("SELECT id, name, ssn, salary FROM employees WHERE name LIKE '%%%s%%'" % name)
