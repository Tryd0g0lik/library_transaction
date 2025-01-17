"""
Here is an abstract table. This table is inherit
from the flask's 'DeclarativeBase. Abstract form
'"""

from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Basic class
    Here is an abstract table. This table is inherit
    from the flask's 'DeclarativeBase.
    """

    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
