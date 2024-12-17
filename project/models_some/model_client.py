from project.models_some.model_person import Person
from sqlalchemy import (Column, Integer)

class Client(Person):
    """
    TODO: This guys take books from a library
    :param firstname: str. Author's name.
    :param secondname: str. Authors's secondname.
    :param birthday: datetime.
    """
    __tablename__ = "client"
    # id = Column(Integer, primary_key=True)

    def __str__(self):
        return f"Person ID: {self.id}, Person firstname: {self.firstname} \
        Person birthday: {self.birthday}"