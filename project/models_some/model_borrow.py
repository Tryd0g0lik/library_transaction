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
    client_id = Column(String, ForeignKey("clients.firstname",
                                          ondelete="CASCADE"),
                       nullable=False)
    date_borrow = Column(DateTime, default=datetime.utcnow)
    date_return = Column(DateTime)
    books = relationship("Books", backref="books")
    clients = relationship("CLients", backref="clients")
    
    def __str__(self):
        return f"Person ID: {self.book_id}, Person firstname: {self.date_borrow} \
Person birthday: {self.date_return}"