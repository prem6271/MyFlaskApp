import mysql.connector

class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    # cls means current Class
    def find_by_username(cls, username):
        conn = mysql.connector.connect(host='172.31.42.184',
	     database='flaskapp',
	     user='prem',
	     password='password')
        cursor = conn.cursor()
        query = "SELECT * FROM test where username=%s"
        cursor.execute(query, (username,)) # Note that arguments should be passed as a Tuple, even if it is just 1 argument
        row = cursor.fetchone()

        if row:
            user = cls(*row) # set of positional arguments
        else:
            user = None
        cursor.close()
        conn.close()
        return user

    @classmethod
    # cls means current Class
    def find_by_id(cls, _id):
        conn =  mysql.connector.connect(host='172.31.42.184',
	     database='flaskapp',
	     user='prem',
	     password='password')
        cursor = conn.cursor()
        query = "SELECT * FROM test where id=%s"
        cursor.execute(query, (_id,)) # Note that arguments should be passed as a Tuple, even if it is just 1 argument
        row = cursor.fetchone()

        if row:
            user = cls(*row) # set of positional arguments
        else:
            user = None
        cursor.close()
        conn.close()
        return user
