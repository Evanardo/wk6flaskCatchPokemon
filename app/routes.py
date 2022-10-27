
from app import app
from flask import render_template, url_for, redirect
from app.monsters import pokeSearch
from app.monsters.form import pokeForm
from app.monsters.pokeSearch import *
from .models import User
from flask_login import current_user


@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/finder')
def pokemon():
    users = User.query.all()
    caught = []
    caught_set = set()
    if current_user.is_authenticated:
        caught = current_user.caughtMonster.all()
        caught_set = {c.id for c in caught}
    for u in users:
        if u.id in caught_set:
            u.flag=True
    
    
    return render_template('finder.html', names=users)