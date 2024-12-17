"""Here contain structure for 'Authors' table of db """
from sqlalchemy import (Column, DateTime, String)
from project.models_some.model_person import Person

class Author(Person):
    """
    :param firstname: str. Author's name.
    :param secondname: str. Authors's secondname.
    :param birthday: datetime.
    """
    __tablename__ = "author"
    
    secondname = Column(String(35), nullable=False)
    
    def __str__(self):
        return f"Person ID: {self.id}, Person firstname: {self.firstname} \
        Person birthday: {self.birthday}"