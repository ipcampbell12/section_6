import sqlite3

from db import db

class UserModel(db.Model):

#show which table is being used to store data
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(80),nullable=False)
    
#class will have ability to retrieve data from sqlite
#don't need id argument because it is auto incrementing
    def __init__(self,username,password):
        self.username = username
        self.password = password


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

#interace for other part of the program to interact with user object
    @classmethod #reference current class
    def find_by_username(cls,username):
        #first username is column name, second one is the argument name
        return cls.query.filter_by(username=username).first()

    #FIND BY ID - mapping on user id
    @classmethod #reference current class
    def find_by_id(cls,_id):
       return cls.query.filter_by(id=_id).first()



#UserModel is an API, but not a REST API
#only used in security file 