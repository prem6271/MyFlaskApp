from model.user import UserModel
from werkzeug.security import safe_str_cmp

# given a username and password, select the correct user from the list
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):      # payload is the contents/body of JWT token
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
