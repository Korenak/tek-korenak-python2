from dogs import db, Dogs

# Create
'''
my_puppy = Dogs('name','name','name','age')
db.session.add(my_puppy)
dn.session.commit()
'''

# Read
all_puppies = Dogs.query.all()
print(all_puppies)

# Select by ID
puppy_one = Dogs.query.get(1)
print(puppy_one.dog_name)

# Filter
puppy_query = Dogs.query.filter_by(dog_name='Princess')
print(puppy_query.all())

# Update
'''
first_puppy
first_puppy.dog_age = 10
db.session.add(my_puppy)
dn.session.commit()
'''
# Delete
'''
delete = Dogs.query.get(1)
db.session.delete(delete)
db.session.commit()
'''
all_puppies = Dogs.query.all()
print()
