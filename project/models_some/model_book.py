"""Here contain structure for 'Books' table of db """
from sqlalchemy import (Column, Integer, String, Text,
                        ForeignKey)
from sqlalchemy.orm import relationship
from project.models_some.model_init import Base

class Book(Base):
    """
    TODO:Thi is a db table the books
        :param title: str. This is a name book.
        :param descriptions: str. This a line contain is a description of book.
        :param author_id: int.
        :param quantity: int. This a remainder of books.
    """

    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    register_number = Column(String(50), nullable=False, unique=True)
    title = Column(String(155), nullable=False, unique=True)
    descriptions = Column(Text)
    author_id = Column(Integer, ForeignKey("author.id"),
                       nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    authors = relationship("Author", backref="authors")
    
    def __str__(self):
        return f"Person ID: {self.id}, Person firstname: {self.title} \
        Person birthday: {self.quantity}"