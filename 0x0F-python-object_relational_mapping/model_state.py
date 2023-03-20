#!/usr/bin/python3
"""This script models a state."""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.delarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """This class represents a state class for MyiSQL db."""

    __tablename__ = 'states'
    id = Column(Integer, unique=True , nullable=False, primary_key=True)
    name = Column(string(128), nullable=False)
