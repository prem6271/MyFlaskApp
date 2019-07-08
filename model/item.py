import mysql.connector

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name':self.name, 'price':self.price}

    @classmethod
    def get_item_by_name(cls, name):
        conn = mysql.connector.connect(host='172.31.42.184',
	     database='flaskapp',
	     user='prem',
	     password='password')
        cursor = conn.cursor()
        query = "SELECT * FROM items where name=%s"
        cursor.execute(query, (name,)) # Note that arguments should be passed as a Tuple, even if it is just 1 argument
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return cls(*row)

    def insert(self):
        connect_var =  mysql.connector.connect(host='172.31.42.184',
	     database='flaskapp',
	     user='prem',
	     password='password')
        cursor = connect_var.cursor()
        insert_query = "INSERT INTO items values (%s, %s)"

        cursor.execute(insert_query, (self.name, self.price))

        connect_var.commit()
        cursor.close()
        connect_var.close()

    def update(self):
        connect_var = mysql.connector.connect(host='172.31.42.184',
	     database='flaskapp',
	     user='prem',
	     password='password')
        cursor = connect_var.cursor()
        upd_query = "UPDATE items set price=%s where name = %s"

        cursor.execute(upd_query, (self.price, self.name))

        connect_var.commit()
        cursor.close()
        connect_var.close()
