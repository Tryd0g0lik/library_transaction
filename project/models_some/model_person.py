"""Here contain structure of 'Persons'. It is abstract a table of db """
from datetime import datetime
from sqlalchemy import (Column, DateTime, String)
from project.models_some.model_init import Base


class Persons(Base):
    """
    :param firstname: str. Author's name.
    :param birthday: datetime.
    """
    __abstract__ = True
    
    firstname = Column(String(35), nullable=False, )
    birthday = Column(DateTime, default=datetime.utcnow)
    
    def __str__(self):
        return f"Person ID: {self.id}, Person firstname: {self.firstname} \
        Person birthday: {self.birthday}"