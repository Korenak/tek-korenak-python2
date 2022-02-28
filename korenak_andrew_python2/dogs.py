import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

#######################

class Dogs(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    owner_f_name = db.Column(db.Text)
    owner_l_name = db.Column(db.Text)
    dog_name = db.Column(db.Text)
    dog_age = db.Column(db.Integer)

    def __init__(self, owner_f_name, owner_l_name, dog_name, dog_age):
        self.owner_f_name = owner_f_name
        self.owner_l_name = owner_l_name
        self.dog_name = dog_name
        self.dog_age = dog_age

    def __repr__(self):
        return f"{self.dog_name} is {self.dog_age} and their owners name is {self.owner_l_name}, {self.owner_f_name}.\n"
