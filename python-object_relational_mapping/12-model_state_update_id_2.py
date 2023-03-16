#!/usr/bin/python3
"""changes the name of a State object from the database """
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    update = session.query(State).filter(State.id == 2).first()
    update.name = "New Mexico"
    session.commit()
    session.close()
