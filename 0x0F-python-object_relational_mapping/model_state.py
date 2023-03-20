#!/usr/bin/python3
"""

This script defines a State class and
a Base class to work with MySQLAlchemy ORM.

"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.delarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True , nullable=False, primary_key=True)
    name = Column(string(128), nullable=False)
