import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import create_engine
# taking my tables from MySQL server!!!!!
engine = create_engine('mysql+pymysql://root:toor@localhost:3306/sakila', echo=False)

my_dogs = pd.read_sql_table('puppies',engine)
my_owners = pd.read_sql_table('owners', engine)

print(my_dogs)
print('--------------------')
print(my_owners)
