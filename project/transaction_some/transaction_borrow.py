"""
Here is a logic for work with the db Borrow's transactions .
This is a management for control
"""
import logging
from datetime import datetime
from project.logs import configure_logging
from project.models_some.model_autors import Author
from project.transaction_some.transactin_basic import Library_basis
from project.transaction_some.transaction_person import Library_Person

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

class Library_borrow(Library_basis):
    def add_one(self, book_id_: int, client_id_: int,
                date_borrow_: datetime = datetime.utcnow,
                date_return: datetime = None,) -> bool:
        """
        TODO: New borrow's line adds to the Model db's table
        :param book_id_: int. The book's index from 'Book'.
        :param client_id_: int. The Client's index from 'Client'.
        :param date_borrow_: datetime. This is datetime when the client
         received a book.
         :param date_return: datetime. This is datetime when the client
         returned a book.
        :return: bool. 'True' it means was created new line of db or not.
        """
        log.info(f"[{Library_borrow.add_one.__name__}] START")
        text = f"[{Library_borrow.add_one.__name__}] END"
        status = False
        try:
            person = Library_Person(Author)
            author = person.get_one(client_id_)
    
            if not author:
                text = f"[{Library_borrow.add_one.__name__}] \
            Mistake => Not found the author. 'author_id' is invalid."
                raise ValueError(text)
            
        except Exception as e:
            pass
        finally:
            pass