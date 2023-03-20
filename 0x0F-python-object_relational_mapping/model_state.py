#!/usr/bin/python3
"""This script models a state."""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.delarative import declarative_base


Base = declarative_base()


class State(Base):
    """This class defines a state class."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(sting(128), nullable=False)
