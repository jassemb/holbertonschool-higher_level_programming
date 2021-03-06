#!/usr/bin/python3
"""
Script that lists all State objects from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name == state_name).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
