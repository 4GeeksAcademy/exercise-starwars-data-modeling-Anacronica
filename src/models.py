import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()
class User(Base):
    __tableneme__ = 'user'
    id = Column(Integer, prima_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites = relationship("Favorite", backref="user", lazy=True)
class Character(Base):
    __tableneme__ = 'character'
    id = Column(Integer, prima_key=True)
    name = Column(String(250), nullable=False)
    gender =Column(Enum('female', 'male', 'other', 'n/a'))
    birth_year = Column(Integer)
    height = Column(Integer)
    hair_color = Column(Enum('brown', 'blond', 'red', 'black', 'n/a'))
    eye_color = Column(Enum('brown', 'green', 'blue', 'gold', 'n/a'))
    planet_id = Column(Integer, ForeignKey(planet.id))
    vehicle = relationship("Vehicle", backref='Character', lazy=True)
class Planet(Base):
     __tablename__ = 'planet'
     id = Column(Integer, prima_key=True)
     name = Column(String(250), nullable=False)
     climate = Column(Enum('arid','temperate','tropical','frozen','murky'))
     terrain = Column(Enum('desert', 'grasslands', 'mountains', 'forests', 'rainforests','jungle', 'ocean', 'tundra','ice caves','ranges','swamps','gas gigant','lakes','grassy hills','cityscape'))
     population = Column(Integer)
     orbital_period = Column(Integer)
     rotation_period = Column(Integer)
     diameter = Column(Integer)
     characters = relationship("Character", backref='planet', lazy=True)
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name= Column(String(100), nullable=False)
    model= Column(String(100), nullable=False)
    vehicle_class=Column(Enum('repulsorcraft', 'wheeled', 'starfighter'))
    manufacturer= Column(Enum('Incom Corporation', 'Corellia Mining Corporation'), nullable=False)
    length= Column(Integer)
    passengers= Column(Integer)
    max_atmosphering_speed= Column(Integer)
    consumables= Column(String(100))
    pilot_id= Column(Integer, ForeignKey('character.id'))
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key = True)
    user_id = Column(String(250), ForeignKey("user.id"))
    character_id = Column(String(250), ForeignKey("character.id"))
    planet_id = Column(String(250), ForeignKey("planet.id"))
    vehicle_id = Column(String(250), ForeignKey("vehicle.id"))
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
