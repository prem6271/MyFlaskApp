import mysql.connector

def create_table():

	connect_var = mysql.connector.connect(host = '100.24.14.5',
	database = 'flaskapp', user = 'prem', password = 'password', ssl_disabled='False')
	cursor = connect_var.cursor()

	create_table = 'CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, username text, password text)'
	cursor.execute(create_table)

	create_table = 'CREATE TABLE IF NOT EXISTS items (name text, price real)'
	cursor.execute(create_table)
	connect_var.commit()
	cursor.close()
	connect_var.close()
