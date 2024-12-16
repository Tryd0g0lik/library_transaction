"""Here contain structure for 'Books' table of db """
from sqlalchemy import (Column, Integer, String, Text,
                        ForeignKey)
from sqlalchemy.orm import relationship
from project.models_some.model_init import Base

class Book(Base):
    """
    TODO:Thi is a db table the books
        :param title: str. This is a name book.
        :param descriptions: str. This a line is contain a description of book.
        :param author_id: int.
        :param quantity: int. This a remainder of books.
    """

    __tablename__ = "books"

    title = Column(String(155), nullable=False, unique=True)
    descriptions = Column(Text(255))
    author_id = Column(Integer, ForeignKey("authors.id")),
    quantity = Column(Integer, nullable=False, default=0)
    authors = relationship("Authors", backref="authors")
    
    def __str__(self):
        return f"Person ID: {self.id}, Person firstname: {self.title} \
        Person birthday: {self.quantity}"