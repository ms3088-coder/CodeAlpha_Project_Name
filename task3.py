from flask import Flask, request, redirect, render_template_string # type: ignore
import sqlite3
import bcrypt # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <form method="POST" action="/login">
            Username: <input name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and bcrypt.checkpw(password, result[0].encode('utf-8')):
        return 'Login successful! Redirecting to dashboard...'
    else:
        return 'Invalid credentials'

if __name__ == '__main__':
    app.run(debug=True)
