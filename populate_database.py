# Import create engine and session make to load the database
# and run our scripts

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# let the program know which database do we want to comnucate to 
# by using the create_engine command
engine = create_engine("sqlite:///restaurantmenu.db")

# Bind the engine to the base class using the following command
# This command makes the connection between our class definations
# and there following tables in the database
Base.metadata.bind = engine

# Setup a session to create the link to the database
DBSession = sessionmaker(bind = engine)

# A session will hold our entries to the database and 
# not add it to the db untill we add and commit it
session = DBSession()

# create the Restaurant
myFirstRestaurant = Restaurant(name = "Pizza Palace")
# Add the new restaurant to the staging zone
session.add(myFirstRestaurant)
# commit and add the new restaurant to the database
session.commit()

# Session objects can also be used to query data from the database
# using the following command you can retrive all data from a db
print session.query(Restaurant).all()
