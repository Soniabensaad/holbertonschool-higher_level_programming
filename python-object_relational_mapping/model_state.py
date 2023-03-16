#!/usr/bin/python3
"""Write a python file that contains
the class definition of a State """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
