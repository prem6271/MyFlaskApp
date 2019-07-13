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

        i = UserModel(**data)
        try:
            i.save_to_db()
        except:
            return {"message": "An error occurred."}, 500 # code for internal error
        return {"message": "User created successfully."}, 201
