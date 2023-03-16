#!/usr/bin/python3
"""adds the State object “Louisiana” to the database """
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    print(new.id)
    session.close()
