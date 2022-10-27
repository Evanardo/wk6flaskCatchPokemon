from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from datetime import datetime

db = SQLAlchemy()

pokedex = db.Table('pokedex', 
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id')), 
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime,nullable=False, default=datetime.utcnow())
    # roster = db.relationship("GangGang", backref="trainer", lazy=True)
    caught = db.relationship("Pokemon",
        # primaryjoin = (pokedex.c.pokemon_id == id),
        # secondaryjoin = (pokedex.c.caughtMonster_id == id),
        secondary = pokedex,
        backref = db.backref('trainer', lazy= 'dynamic'),
        lazy = 'dynamic'
    )

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    def catch(self, pokemon):
        self.caught.append(pokemon)
        db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon = db.Column(db.String(50), nullable=False, unique=True)
    ability = db.Column(db.String(50), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    baseXP = db.Column(db.Integer, nullable=False)
    sprite = db.Column(db.String(300), nullable=False)

    def __init__(self, pokemon,ability,hp,attack,defense, baseXP, sprite):
        self.pokemon = pokemon
        self.ability = ability
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.baseXP = baseXP
        self.sprite = sprite


# class GangGang(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pokemon1 = db.Column(db.String(50))
#     pokemon2 = db.Column(db.String(50))
#     pokemon3 = db.Column(db.String(50))
#     pokemon4 = db.Column(db.String(50))
#     pokemon5 = db.Column(db.String(50))
#     pokemon6 = db.Column(db.String(50))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __init__(self, pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, user_id):
#         self.pokemon1 = pokemon1
#         self.pokemon2 = pokemon2
#         self.pokemon3 = pokemon3
#         self.pokemon4 = pokemon4
#         self.pokemon5 = pokemon5
#         self.pokemon6 = pokemon6
#         self.user_id = user_id