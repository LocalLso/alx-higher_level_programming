#!/usr/bin/python3
"""This module list all states from a db."""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(
                            'mysql+msqldb://{}:{}@localhost:3306/{}'
                            .format(usr, passwd, db_name), echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
