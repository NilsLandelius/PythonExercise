import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
#With "INTEGER PRIMARY KEY" you get an auto incrementing key so we don't need to assign id value when creating users.
cursor.execute(create_table)

connection.commit()
connection.close()

