import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), unique=True, nullable=False)
    favorites = relationship("Favorites", back_populates="user")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), ForeignKey('user.username'))
    planets = Column(String(250), ForeignKey('planets.planet_name'))
    characters = Column(String(250), ForeignKey('characters.character_name'))
    user = relationship("User", back_populates="favorites")
    planet = relationship("Planets", back_populates="favorites")
    character = relationship("Characters", back_populates="favorites")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    terrain = Column(String(250))
    favorites = relationship("Favorites", back_populates="planet")

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    height = Column(Integer)
    weight = Column(Integer)
    birth_year = Column(String(5))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    hail_color = Column(String(250))
    favorites = relationship("Favorites", back_populates="character")
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
