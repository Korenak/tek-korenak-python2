import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# If the mysql line isn't working for you comment it out and use the sqlite one.
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/python2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)


class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Text)
    # 1 to 1
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name,age="Unkown"):
        self.name = name
        self.age = age


    def __repr__(self):
        if self.owner:
            return f"{self.name} is {self.age} and owner is {self.owner.name}"
        else:
            return f"{self.name} is {self.age} and has no owner assigned yet."


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
