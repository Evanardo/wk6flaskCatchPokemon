from app.models import User, db
from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import current_user, login_required
from app.create_roster.forms import CreateRoster

createRoster = Blueprint('createRoster', __name__, template_folder='templates_roster')

@createRoster.route('/roster', methods = ["GET", "POST"])
@login_required
def genRoster():
    form = CreateRoster()
    print(form)
    print(request.method)
    if request.method == "POST":
        print("POST")
        if form.validate():
            print('valid')
            pokemon1 = form.pokemon1.data
            pokemon2 = form.pokemon2.data
            pokemon3 = form.pokemon3.data
            pokemon4 = form.pokemon4.data
            pokemon5 = form.pokemon5.data
            pokemon6 = form.pokemon6.data

            roster = GangGang(pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, current_user)

            db.session.add(roster)
            db.session.commit()

            flash('Saved to Roster', 'success')
        
        else:
            flash("Not saved to Roster", 'error')
    return render_template('createRoster', form=form)

