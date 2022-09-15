from flask import Flask 
from flask_restful import Api
from flask_jwt import JWT
from resources.item import Item, ItemList
from db import db


#security.py
from security import authenticate, identity

from resources.user import UserRegister

app = Flask(__name__)
#tell sqlalchemy where to find data.db file
#database will live at root folder of project
#can choose any databse type - postgres, mysql etc.
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///mycooldb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'Ian'
api = Api(app)

jwt = JWT(app,authenticate,identity)


#add resources to api
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')


#only run the app if you are running the app4.py file
#dont run the app when importing this file to another file
if __name__ == '__main__':
    db.init_app(app) #initialize db
    app.run(port=5004,debug=True)
