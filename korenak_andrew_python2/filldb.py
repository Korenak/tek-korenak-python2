# This script will create some puppies, owners, and toys!
# Note, if you run this more than once, you'll be creating dogs with the same
# name and duplicate owners. The script will still work, but you'll see some
# warnings. Watch the video for the full explanation.
from models import db,Puppy,Owner

# Create 20 puppies
brady = Puppy('Brady','2')
buddy = Puppy('Buddy','5')
hazel = Puppy('Hazel','1')
minnie = Puppy('Minnie','7')
cody = Puppy('Cody','6')
lucky = Puppy('Lucky','5')
gizmo = Puppy('Gizmo','3')
princess = Puppy('Princess','2')
gunner = Puppy('Gunner','1')
katie = Puppy('Katie','10')
layla = Puppy('Layla','8')
foxy = Puppy('Foxy','6')
winnie = Puppy('Winnie','4')
ranger = Puppy('Ranger','3')
bandit = Puppy('Bandit','1')
emma = Puppy('Emma','2')
sugar = Puppy('Sugar','2')
grace = Puppy('Grace','3')
murphy = Puppy('Murphy','3')
lily = Puppy('Lily','6')

# Add puppies to database
db.session.add_all([brady, buddy, hazel, minnie, cody, lucky, gizmo, princess, gunner, katie, layla, foxy, winnie, ranger, bandit, emma, sugar, grace, murphy, lily
])
db.session.commit()

# Check with a query, this prints out all the puppies!
print(Puppy.query.all())


#  .first() or .all()[0] can be used to limit if multi dogs share name
lily = Puppy.query.filter_by(name='lily')
print(lily)

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



db.session.add_all([nikola, harri, yousaf, howard, felicity, akbar, warwick, timur, tess, monty, crystal, reece, kieron, shanai, tyreke, reegan, darcie, hanna, duncan, kaydee
])



db.session.commit()


emma = Puppy.query.filter_by(name='Emma').first()
print(emma)


# to delete
# variable = Puppy.query.get(1) 1 is the key
# db.session.delete(variable)
# db.session.commit()
