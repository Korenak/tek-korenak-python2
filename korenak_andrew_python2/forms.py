from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NoneOf

class AddForm(FlaskForm):
    name = StringField('Puppy Name:',validators=[DataRequired()])
    name2= StringField('Owner Name',validators=[DataRequired()])
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):
    id = IntegerField('Puppy ID:')
    submit = SubmitField('Remove Puppy')
