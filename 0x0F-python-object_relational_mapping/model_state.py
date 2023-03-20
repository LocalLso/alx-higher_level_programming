#!/usr/bin/python3
"""This module models a state."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative_base import declarative_base

Base = declarative_base()


class State(Base):
    """This class defines a state class for MySQLdb."""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
