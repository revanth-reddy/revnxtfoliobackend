import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (name, email, message) VALUES (?, ?, ?)",
            ('Rev', 'revanth@reddy.com', 'Howdy! I\'m Revanth Reddy')
            )


connection.commit()
connection.close()
