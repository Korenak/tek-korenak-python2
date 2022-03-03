import config
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import create_engine


'''
!!!! taking my tables back from MySQL server!!!!!
You will need to update the below string to reflect your own database
if you want this page to work.
'''
conn= "mysql+pymysql://{0}:{1}@{2}/{3}".format(config.username, config.password, config.host, config.schema)
engine = create_engine(conn, echo=False)

# get the tables
my_dogs = pd.read_sql_table('puppies',engine)
my_owners = pd.read_sql_table('owners', engine)

# some basic data cleansing could be performed here by df['name'] = df['name'].str.capitalize()
# to capitalize entires in the name column or even .lower() first to ensure everthing
# was lowercase before making the first letter uppercase.

#shapes of data
dogs_count= my_dogs.shape[0]
dogs_columns= my_dogs.shape[1]
owners_count= my_owners.shape[0]
owners_columns= my_owners.shape[1]
#innermerge puppies and owner tables
innermerge = pd.merge(my_dogs,my_owners, how='inner', on=['id'])
# re-name all our columns for fun and clarity
innermerge.rename({'id': 'ID', 'name_x': 'Dog', 'name_y': 'Owner', 'puppy_id': 'PupID'},axis=1,inplace=True)
'''
Dog color is not a feature of our data, so instead of altering our classes back
in dbinit.py and filling in dog colors with some CRUD I will instead get creative
with pandas. Below is a huge List of semi random colors. We 'could' add reasonable
colors to all dogs manually but that would be too much work. We will just pretend
these colors are accurate.
'''
dog_colors = ['Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream','Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream','Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream','Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream','Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red']
# since dataset is so huge it will be longer than the db we are trying to merge it to, thus it will not work
#so identify the variable shape of our dataframe
count=innermerge.shape[0]
#feed shape into list to cut off at the right number of color entries
color_slice = dog_colors[:count]
# now add that new colors column to our db
# it should now work with a table from mysql that is shorter or longer than the
# 22 long one I am testing with "within reason."
innermerge['Color']=color_slice
# value count on Color and add a new column named color_count
dog_color_count= innermerge.value_counts(['Color']).reset_index(name='Color_Count')
'''
see below print statements for more important stuff!
'''
# print('--------Print Dogs Table------------')
# print(my_dogs)
print('---------Print Dogs Shape(rows) -----------')
print(dogs_count)
print('---------Print Dogs Col -----------')
print(dogs_columns)
# print('---------Print Owners Table-----------')
# print(my_owners)
print('---------Print Owners Shape(rows) -----------')
print(owners_count)
print('---------Print Owners Col -----------')
print(owners_columns)
print('---------Inner Merge and Added Colors -----------')
print(innermerge)
print('---------Filter by Colors -----------')
print(dog_color_count)

#pandas can output as a csv!!! index false saves it without the added pd index!
# this avoids duplicate indexes when we load it back in a little later
dog_color_count.to_csv('color_count.csv', index=False)

# You could read that csv back into cirulation by
data = pd.read_csv('color_count.csv')
# then assign the conents of the csv to a data frame
dog_color_count = pd.DataFrame(data)

# It can also send a dataframe back up to MySQL server!!! Check for the new
# table dog_color_count in MySQL
dbConn = engine.connect()
tableN= "dog_color_count"
dog_colors = pd.DataFrame(data=dog_color_count)
try:
    frame = dog_colors.to_sql(tableN, dbConn, if_exists='replace');
except ValueError as vx:
    print(vx)
except Exception as ex:
    print(ex)
else:
    print("Table %s created successfully."%tableN);
finally:
    dbConn.close()
