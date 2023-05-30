import sqlite3
from flask import Flask, jsonify,  request, url_for, flash, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    results = [dict(row) for row in posts]

    return jsonify(results)

@app.route('/contact/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if not name or not email or not message:
            flash('all fields are required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (name, email, message) VALUES (?, ?, ?)',
                         (name, email, message))
            conn.commit()
            conn.close()
            return "done"
    return "send post request"