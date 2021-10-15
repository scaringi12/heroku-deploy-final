from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from datetime import timedelta


db = SQLAlchemy()   #initialize database
DB_NAME = "ProjectPopcorn.db"  #database name object name

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ravioli ravioli give me the formuoli'       #uses sha-256 just added security 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'    #old tutorial sql DB                       #sqalchemy database will be located at this location will need to change later
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=30) #for testing purposes should stop remembering session after 30 seconds so i can test more signups 
    # new MySQL.DB
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:BalledGripe01729@localhost/our_users'
    db.init_app(app)  #initializes database



    from .views import views
    from .auth import auth
    #url prefix is saying all the urls that are stored in the blueprint files / means no prefix currently will change later
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User #importing database everytime server is loaded #need to add #Movies later when database is formed 

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'     #when someone isant logged in annonymous user redirects them to login page
    login_manager.init_app(app) 

    @login_manager.user_loader       #this tells flask how we load a user gets the primary key of user in database
    def load_user(id):
        return User.query.get(int(id))

        

    return app 


def create_database(app):
    if not path.exists('website/' + DB_NAME):      #checks if database exists if not will create it and print message
        db.create_all(app=app)
        print('Created Database!')


        