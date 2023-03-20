#!/usr/bin/python3
"""This script models a state."""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.delarative import declarative_base

Base = declarative_base()


class State(Base):
    """This class represents a state class for MyiSQL db."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(string(128), nullable=False)
