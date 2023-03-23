#!/usr/bin/python3
"""This module lists State objects that contain the letter a from the db."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    create = create_engine("mysql+msqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for result in session.query(State).order_by(State.id):
        if "a" in result.name:
            print("{}: {}".format(result.id, result.name))
