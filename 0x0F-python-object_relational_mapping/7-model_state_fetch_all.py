#!/usr/bin/python3
"""This module list all states from a db."""

import sys
from model_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+msqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3])
                           , pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for result in session.query(State).order_by(State.id):
        print("{}: {}".format(result.id, result.name))
