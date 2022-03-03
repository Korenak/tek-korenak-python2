import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import create_engine
# taking my tables from MySQL server!!!!!
engine = create_engine('mysql+pymysql://root:toor@localhost:3306/sakila', echo=False)

my_dogs = pd.read_sql_table('puppies',engine)
my_owners = pd.read_sql_table('owners', engine)

#shapes of data
dogs_count= my_dogs.shape[0]
dogs_columns= my_dogs.shape[1]
owners_count= my_owners.shape[0]
owners_columns= my_owners.shape[1]
#innermerge puppies and owner tables
innermerge = pd.merge(my_dogs,my_owners, how='inner', on=['id'])
# huge List of semi random colors
dog_colors = ['Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream','Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream','Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream','Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red','Brown', "Brown", "White", 'Grey','Cream','Brown', 'White', 'Yellow', 'Black', 'White', 'Gold', 'Cream', 'Grey', 'Cream', 'Gold', 'White', 'Black', 'Yellow', 'White', 'Red']
# since list is so huge it will be longer than the db we are trying to merge it to, thus it will not work
#so identify the shape of the list
count=innermerge.shape[0]
#feed shape into list to cut off at the right number of colors
color_slice = dog_colors[:count]
# now add that new colors column to our db
# it should now work with a table from mysql that is shorter or longer than the 22 long one I currently have within reason.
innermerge['Color']=color_slice
# value count on Color and add a new column named color_count
x= innermerge.value_counts(['Color']).reset_index(name='Color_Count')
# Merge color count to table with inner merge
final_db= pd.merge(innermerge,x, how='inner', on=['Color'])
#group by
final_db.groupby(['id','name_x','name_y','puppy_id','Color', 'Color_Count'])


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
print(x)
print('---------Inner Merge on color (a bit of a mess...) -----------')
print(final_db)
#pandas can output as a csv!!!
x.to_csv('color_count.csv')
