import sqlite3
from typing import List, Dict, Any

con= sqlite3.connect('users.db')
cur = con.cursor()
def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    con.commit()

rows=cur.execute('SELECT * FROM users').fetchall()
for row in rows:
    print(row)



