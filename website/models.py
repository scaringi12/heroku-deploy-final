from . import db             #imports sqlalchemy
from flask_login import UserMixin  #custom class that gives user object some specific things 

#this is first database schema
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)  #this means email max length is 50 and has to be unique
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(25))
    movies = db.relationship('Movies') #user movies 




class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    director = db.Column(db.String(100))
    main_actor = db.Column(db.String(100))
    ratings = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   #relates movies they've seen to their user id one to many relationship

