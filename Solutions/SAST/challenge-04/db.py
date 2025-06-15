import sqlite3


def get_user(name):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE name = ?', (name,))
    return cur.fetchall()
