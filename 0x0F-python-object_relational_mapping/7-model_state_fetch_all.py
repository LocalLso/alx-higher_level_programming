#!/usr/bin/python3
"""This module list all states from a db."""

import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for result in session.query(State)order_by(State.id):
        print("{}: {}".format(result.id, result.name))
