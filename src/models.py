import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable = False)
    password = Column(String(20), nullable = False, unique = True)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(200))
    photo_url = Column(String())
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False )
    
    def to_dict(self):
        return {}

class Comentary(Base):
    __tablename__ = 'comentary'
    id = Column(Integer, primary_key=True)
    description = Column(String(200))
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False )
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False )

class Favourite(Base):
    __tablename__ = 'favourite'
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False, primary_key=True )
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False, primary_key=True )


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e