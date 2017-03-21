# sys module provides functions and variables that
# can be used to manupulate
# python runtime enviroment
import os
import sys

# below imports will help writing our mapper code

from sqlalchemy import Column, ForeignKey, Integer, String

# we will use declarative_base while writing our class code
# and configuration

from sqlalchemy.ext.declarative import declarative_base

# We will use relationship module while 
# creating forign key relationships
from sqlalchemy.orm import relationship

# import functions that will connect to the pthon db
from sqlalchemy import create_engine

# create a instance of the declarative base
# will make db classes instances of this class so that 
# sqlalchemy will know that the classes relates to tables in database
Base = declarative_base()

class Restaurant(Base):
	__tablename__ = "restaurant"
	# Mapper Code
	name = Column( String, nullable = False)

	id = Column( Integer, primary_key = True)

class MenuItem(Base):
	__tablename__ = "menu_item"

	# Mapper code
	name = Column( String(80), nullable = False)
	id = Column( Integer, primary_key = True)

	course = Column(String(250))

	description = Column(String(250))

	price = Column(String(8))

	restaurant_id = Column(Integer, ForeignKey("restaurant.id"))

	restaurant = relationship(Restaurant)





# will create a new file to connect to the db
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.create_all(engine)