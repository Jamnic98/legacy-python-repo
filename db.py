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


def search_employees(name):
    return query("SELECT id, name, ssn, salary FROM employees WHERE name LIKE '%%%s%%'" % name)
