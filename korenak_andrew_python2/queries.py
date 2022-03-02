import os
from flask import Flask
from dbinit import db,Puppy,Owner
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'mysecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


'''
all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)
print('\n')

puppy_one = Puppy.query.get(1)
print(puppy_one)
print('\n')
'''
printowners = Owner.query.all()
print(printowners)
'''
first_puppy = Puppy.query.get(21)
print(first_puppy)
'''


'''
remove = Puppy.query.get(1)
db.session.delete(remove)
db.session.commit()
'''
