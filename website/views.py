from flask import Blueprint, render_template, session, request
from flask_login import login_required, current_user

# Blueprint will have a bunch of routes inside of it has a bunch of URLs defined in it 
# such as home page movies etc
views = Blueprint('views', __name__)

#the first view @ the name of the blueprint.route inside the parameters put the url 
#this function will run whenever we go to the /route
#whatever is inside of home will run
#view.route is considered a decorator
#need to register blueprints in init.pi
@views.route('/')
@login_required #to view homepage user needs to be logged in
def home():
    return render_template("home.html", user=current_user) #references user thats logged in

@views.route('/about-us')
def about_us():
    return render_template("about_us.html", user=current_user)

@views.route('/profile')
@login_required #to view profile need to be logged in
def profile():
    return render_template("profile.html", user=current_user)




