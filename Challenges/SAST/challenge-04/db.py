import sqlite3


def get_user(name):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cur.execute(query)
    return cur.fetchall()
