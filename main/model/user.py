from flask_sqlalchemy import SQLAlchemy
from main import db

# Schema definition -  new class which inherits from a basic database model
class User(db.Model):
    __table__name = 'user'

    id        = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName  = db.Column(db.String(100), nullable=False)  
    bio       = db.Column(db.String(200))

# Constructur of the User class 
def __init__(self, *args, **kwargs):
    # constructor of the Model class
    super().__init__(*args, **kwargs) 

def format(self):
    return {
      'id'       : self.id,
      'firstName': self.firstName,
      'lastName' : self.lastName,
      'bio'      : self.bio,
    }

'''
  The special __repr__ function allows you to give each object a string representation to recognize it for debugging purposes.
  This allows us to do things like print(user)
'''

def __repr__(self):
    return f'<User id: {self.id}, firstName: {self.firstname}, lastName: {self.lastName}>'