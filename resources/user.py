import mysql.connector
from model.user import UserModel
from flask_restful import Resource, reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be empty!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be empty!"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists."}
        connect_var = mysql.connector.connect(host='172.31.42.184',
	     database='flaskapp',
	     user='prem',
	     password='password')
        cursor = connect_var.cursor()
        insert_query = "INSERT INTO test values (NULL, %s, %s)"

        cursor.execute(insert_query, (data['username'], data['password']))

        connect_var.commit()
        cursor.close()
        connect_var.close()
        return {"message": "User created successfully."}, 201
