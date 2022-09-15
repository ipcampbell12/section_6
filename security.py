
from models.user import UserModel




def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user is not None and user.password == password:
        return user
#generates jwt token

def identity(payload):
    user_id = payload['identity']
    # identity = userid, 
    #retrieve user object
    return UserModel.find_by_id(user_id)

4
#if user and hmac.compare_digest(user.password, password):