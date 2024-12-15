"""Here contain structure for 'Authors' table of db """
from datetime import datetime
from sqlalchemy import (Column, DateTime, String)
from project.models_some.model_init import Base
from project.models_some.model_person import Person


class Author(Person):
    """
    :param firstname: str. Author's name.
    :param secondname: str. Authors's secondname.
    :param birthday: datetime.
    """
    __tablename__ = "authors"
    
    secondname = Column(String(35), nullable=False)