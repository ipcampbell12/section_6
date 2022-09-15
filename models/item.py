#no longer need sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    #should be string not text
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))


    def __init__(self,name,price):
        self.name=name
        self.price =price

    #dictionary representing item
    def json(self):
        return {'name':self.name,'price':self.price}


    #use this method to check if an item already exists in the database when posting
    #use this for both get and post requests

    #should still be a class method
    @classmethod
    def find_by_name(cls,name):

        # returns ItemModel object
        # cls refers to the class itself
        return cls.query.filter_by(name=name).first()
        #SELECT * FROM items WHERE name = name LIMIT 1

    #insert item into the database 
    
    #completes functions of both inserting and updating
    def save_to_db(self): 
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    