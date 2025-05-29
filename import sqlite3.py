import sqlite3
import bcrypt # type: ignore

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

username = 'admin'
password = 'securepassword123'.encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed.decode('utf-8')))
    print("User created.")
except sqlite3.IntegrityError:
    print("User already exists.")

conn.commit()
conn.close()
