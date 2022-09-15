

from flask_restful import Resource, reqparse
from models.user import UserModel




#sign up users with new username and password
class UserRegister(Resource):

    #parses through json from the request to make sure username and password have been ceated
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "This field cannot be left blank")
    parser.add_argument('password',
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )


    def post(self):
        data = UserRegister.parser.parse_args()

        #checks if username is already taken
        if UserModel.find_by_username(data['username']) is not None: 
            return {"message": "this username is taken"},400
        
        user = UserModel(data['username'], data['password'])
        #could also just say UserModel(**data) 

        user.save_to_db()

        return {"message": "User created sucessfully"}, 201   

