
from flask import Blueprint, render_template, redirect, url_for, request
from app.monsters.form import pokeForm, Pokeball
from app.models import Pokemon, User, db
from flask_login import login_required, current_user

import requests as r

monsters = Blueprint('monsters', __name__, template_folder='templates_monsters')

@monsters.route('/finder', methods=["GET", "POST"])
def pokeFinder():
    form = pokeForm()
    dict = {}
    # pokemon = form.pokemon.data
    # try:
        
    if request.method == "POST":
        # if request.form.get('catch-btn') == 'catch':
        #         pokemon = request.form.get('name-catch')
    
        if form.validate():
            pokemon = form.pokemon.data
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
            response = r.get(url)
            if response.ok:
                data = response.json()
                dict= {
                    'name': data['name'],
                    'ability': data['abilities'][0]['ability']['name'],
                    'baseXP': data['base_experience'],
                    'base_hp': data['stats'][0]['base_stat'],
                    'base_att': data['stats'][1]['base_stat'],
                    'base_def': data['stats'][2]['base_stat'],
                    'sprite': data['sprites']['other']['official-artwork']['front_default']
                }
                pokemon = Pokemon.query.filter_by(pokemon=dict['name']).first()
                if pokemon:
                    pass
                else:
                    pokemon = Pokemon(dict['name'], dict['ability'], dict['base_hp'], dict['base_att'], dict['base_def'], dict['baseXP'], dict['sprite'])

                    db.session.add(pokemon)
                    db.session.commit()
                dict['id'] = pokemon.id
                return render_template('finder.html', form=form, pokemon=dict)
    # except:
    #     return render_template('finder.html', form=form, pokemon=dict)
    return render_template('finder.html', form=form, pokemon=dict)

@monsters.route('/finder/catch/<id>', methods=["POST"])
@login_required
def catchPoke(id):
    # form = Pokeball()
    pokemon = Pokemon.query.get(id) #is this getting from /finder page?
    current_user.catch(pokemon)
    return redirect(url_for('monsters.cRoster'))

@monsters.route('/roster', methods=["GET"])
@login_required
def cRoster():
    # form = Pokeball()
    pokemons = current_user.caught.all()
    # print(pokemons)
    # current_user.c(pokemon)
    return render_template('roster.html', pokemons=pokemons)

    