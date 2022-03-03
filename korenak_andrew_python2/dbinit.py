import os
import config
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm
import pymysql
#import secrets

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

'''
change values in config.py to change every instance of this across all files
'''
conn= "mysql+pymysql://{0}:{1}@{2}/{3}".format(config.username, config.password, config.host, config.schema)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
# pre config file uri connection.
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:toor@localhost/sakila"
#old sqllite option. ignore
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)


class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    # 1 to 1
    owner = db.relationship('Owner',backref='Puppy',uselist=False, cascade="all, delete-orphan")

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"{self.name} has no owner assigned yet."


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"{self.name} \n"

db.create_all()
##############VIEWS###############################################

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        # we have 2 required input fields
        name = form.name.data
        name2 = form.name2.data
        # Add puppies
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        #the aobve ensures the puppy is assigned an id
        # before the below attempts to attach an owner to new_pup.id
        puppy_id= new_pup.id
        new_owner= Owner(name2,puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_pup.html', form=form)


@app.route('/list')
def list_pup():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()

    return render_template('list_pup.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete_pup.html', form=form)

@app.route('/update_owner',methods=['GET','POST'])
def update_owner():
    form = UpdateOwnerForm()

    if form.validate_on_submit():
        name= form.name.data
        pup_id= form.pup_id.data


        updated_owner = Owner(name,pup_id)
        db.session.add(updated_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('update_owner.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
