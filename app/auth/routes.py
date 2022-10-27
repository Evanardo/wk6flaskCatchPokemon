from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from .forms import LoginForm, UserCreationForm
from app.models import User
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=["GET", "POST"])
def signUp():
    form = UserCreationForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data

            #add user to database
            user = User(username, first_name, last_name, email, password)
            
            #add instance to SQL
            user.saveToDB()

            flash('Trainer registered!', 'success')

            return redirect(url_for('auth.logIn'))
        else:
            flash('You are not valid. Please try once more future Trainer.')   
    return render_template('signup.html', x=form)

@auth.route('/login', methods=["GET", "POST"])
def logIn():
    form = LoginForm()
    if request.method == "POST":
        print('post method made')
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            print(user.username, user.password, user.id)
            
            
            if user:
                if check_password_hash(user.password, password):
                    print('succesfully logged in')
                    login_user(user)
                    return redirect(url_for('homePage'))
                else:
                    flash('Incorrect username and/or password')

            else:
                flash('You have not registered with this Gym, Please register.')



    return render_template('login.html', form=form)


@auth.route('/logout')
def logOut():
    flash('Later, Trainer', 'warning')
    logout_user()
    return redirect(url_for('auth.logIn'))
