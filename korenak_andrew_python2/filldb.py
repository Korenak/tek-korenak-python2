# Only run ONCE. will create duplicates.
from dbinit import db,Puppy,Owner
import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Create 20 puppies
brady = Puppy('Brady')
buddy = Puppy('Buddy')
hazel = Puppy('Hazel')
minnie = Puppy('Minnie')
cody = Puppy('Cody')
lucky = Puppy('Lucky')
gizmo = Puppy('Gizmo')
princess = Puppy('Princess')
gunner = Puppy('Gunner')
katie = Puppy('Katie')
layla = Puppy('Layla')
foxy = Puppy('Foxy')
winnie = Puppy('Winnie')
ranger = Puppy('Ranger')
bandit = Puppy('Bandit')
emma = Puppy('Emma')
sugar = Puppy('Sugar')
grace = Puppy('Grace')
murphy = Puppy('Murphy')
lily = Puppy('Lily')

# Add puppies to database
db.session.add(brady)
db.session.add(buddy)
db.session.add(hazel)
db.session.add(minnie)
db.session.add(cody)
db.session.add(lucky)
db.session.add(gizmo)
db.session.add(princess)
db.session.add(gunner)
db.session.add(katie)
db.session.add(layla)
db.session.add(foxy)
db.session.add(winnie)
db.session.add(ranger)
db.session.add(bandit)
db.session.add(emma)
db.session.add(sugar)
db.session.add(grace)
db.session.add(murphy)
db.session.add(lily)

db.session.commit()
# Check with a query, this prints out all the puppies!
'''
print(Puppy.query.all())
'''

# Owners
nikola = Owner('Nikola',brady.id)
harri = Owner('Harri',buddy.id)
yousaf = Owner('Yousaf',hazel.id)
howard = Owner('Howard',minnie.id)
felicity = Owner('Felicity',cody.id)
akbar = Owner('Akbar',lucky.id)
warwick = Owner('Warwick',gizmo.id)
timur = Owner('Timur',princess.id)
tess = Owner('Tess',gunner.id)
monty = Owner('Monty',katie.id)
crystal = Owner('Crystal',layla.id)
reece = Owner('Reece',foxy.id)
kieron = Owner('Kieron',winnie.id)
shanai = Owner('Shanai',ranger.id)
tyreke = Owner('Tyreke',bandit.id)
reegan = Owner('Reegan',emma.id)
darcie = Owner('Darcie',sugar.id)
hanna = Owner('Hanna',grace.id)
duncan = Owner('Duncan',murphy.id)
kaydee = Owner('Kaydee',lily.id)

db.session.add(nikola)
db.session.add(harri)
db.session.add(yousaf)
db.session.add(howard)
db.session.add(felicity)
db.session.add(akbar)
db.session.add(warwick)
db.session.add(timur)
db.session.add(tess)
db.session.add(monty)
db.session.add(crystal)
db.session.add(reece)
db.session.add(kieron)
db.session.add(shanai)
db.session.add(tyreke)
db.session.add(reegan)
db.session.add(darcie)
db.session.add(hanna)
db.session.add(duncan)
db.session.add(kaydee)


db.session.commit()



# to delete
# variable = Puppy.query.get(1) 1 is the key
# db.session.delete(variable)
# db.session.commit()
