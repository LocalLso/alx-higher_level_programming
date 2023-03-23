#!/usr/bin/python3
"""
This module prints the State.id object of the name passed as arg from the db.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    create = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            state_found = True
            break
        if state_found is False:
            print("Not found")
