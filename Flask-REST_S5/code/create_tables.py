import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

sql_file = open('create.sql').read()
cursor.executescript(sql_file)

connection.commit()
connection.close()

