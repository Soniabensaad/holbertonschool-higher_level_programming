#!/usr/bin/python3
"""Python file similar to model_state.py named model_city.py
that contains the class definition of a City"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state, city in session.query(State, City).filter(
        State.id == City.state_id).order_by(State.id).all():
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
