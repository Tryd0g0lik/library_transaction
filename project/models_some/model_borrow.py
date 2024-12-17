"""Here contain structure for 'Authors' table of db """
from datetime import datetime
from sqlalchemy import (Column, DateTime, Integer, String, Text,
                        ForeignKey)
from sqlalchemy.orm import relationship

from project.models_some.model_init import Base


class Borrow(Base):
    """Borrows books"""
    __tablename__ = "borrow"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id",
                                         ondelete="CASCADE"),
                     nullable=False)
    client_id = Column(Integer, ForeignKey("client.id",
                                          ondelete="CASCADE"),
                       nullable=False)
    date_borrow = Column(DateTime, default=datetime.utcnow)
    date_return = Column(DateTime)
    books = relationship("Book", backref="books")
    clients = relationship("Client", backref="client")
    
    def __str__(self):
        return f"Person ID: {self.book_id}, Person firstname: {self.date_borrow} \
Person birthday: {self.date_return}"