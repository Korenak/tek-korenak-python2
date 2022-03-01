from dbinit import db,Puppy,Owner



all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)
print('\n')

puppy_one = Puppy.query.get(1)
print(puppy_one)
print('\n')

printowners = Owner.query.all()


'''
remove = Puppy.query.get(1)
db.session.delete(remove)
db.session.commit()
'''
