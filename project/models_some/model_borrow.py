"""Here contain structure for 'Authors' table of db """
from datetime import datetime
from sqlalchemy import (Column, DateTime, Integer, String, Text,
                        ForeignKey)
from sqlalchemy.orm import relationship

from project.models_some.model_init import Base


class Borrows(Base):
    """Borrows books"""
    __tablename__ = "borrows"
    books_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    client_id = Column(String, ForeignKey("clients.firstname"), nullable=False)
    date_borrows = Column(DateTime, default=datetime.utcnow)
    date_return = Column(DateTime)
    books = relationship("Books", backref="books")
    clients = relationship("CLients", backref="clients")
    