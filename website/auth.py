from flask import Blueprint, render_template, request, flash, redirect, url_for 
from.models import User
from werkzeug.security import generate_password_hash, check_password_hash #this is for user password encryption
from . import db       #import the database
from flask_login import login_user, login_required, logout_user, current_user   #we can use these imports to access information about current user etc


#redirect will allow us to make the website more dynamic can redirect them to homepage
#flash is for error handling will flash a message to user
#request can retrieve information sent in the form
#auth blueprint for login page
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()  #filter all users by their signup email
        if user:  
            if check_password_hash(user.password, password):  #if hashes are the same we will log in successfully
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) #logs in the user, and remembers that the user is logged in the session   login_user(user, remember = True) for final version
                return redirect(url_for('views.profile'))
            else:
                flash('Incorrect password buddy, try again :(', category='error') 
        else: 
            flash('Email does not exist try again.', category='error')

    return render_template("login.html", user=current_user)  #the methods are the type of the requests the root can accept

@auth.route('/logout')
@login_required #cannot access page unless user is required
def logout():
    logout_user() #logs out user 
    return redirect(url_for('auth.login')) #redirects to signin page

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        #error handling this is very simple will make more complete later
        if user:
            flash("Email already exists", category='error')
        elif len(email) < 4:
            flash('Email must be greater thatn 3 characters', category='error')
        elif len(first_name) < 3:
            flash('Firstname must be greater thatn 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match try again', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))   #define the user
            db.session.add(new_user)   #add the user 
            db.session.commit() #creates the new user in the database
            login_user(new_user, remember=True) #logged in when account created
            flash('Account created! enjoy our movie reccomendations', category='success')
            return redirect(url_for('views.profile'))  #blueprint name for less errors if homepage changes

    return render_template("sign_up.html", user=current_user)


"""
to pass values to the templates you can do something like
@auth.route('/login')
def login():
    return render_template("login.html", text ="testing")
then on the login.html if you do
{{testing}}
it will print out the value for the login page
"""