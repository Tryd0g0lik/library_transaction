"""
Here is a logic for work with the db Borrow's transactions .
This is a management for control
"""
import logging
from datetime import datetime
from project.logs import configure_logging
from project.models_some.model_autors import Author
from project.models_some.model_borrow import Borrow
from project.transaction_some.transactin_basic import Library_basis
from project.transaction_some.transaction_person import Library_Person

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

class Library_Borrow(Library_basis):
    def add_one(self, book_id_: int, client_id_: int,
                date_borrow_: datetime = datetime.utcnow,) -> bool:
        """
        TODO: New borrow's line adds to the Model db's table
        :param book_id_: int. The book's index from 'Book'.
        :param client_id_: int. The Client's index from 'Client'.
        :param date_borrow_: datetime. This is datetime when the client
         received a book.
        :return: bool. 'True' it means was created new line of db or not.
        """
        log.info(f"[{Library_Borrow.add_one.__name__}] START")
        text = f"[{Library_Borrow.add_one.__name__}] END"
        status = False
        try:
            person = Library_Person(Author)
            author = person.get_one(client_id_)
    
            if not author:
                text = f"[{Library_Borrow.add_one.__name__}] \
            Mistake => Not found the author. 'author_id' is invalid."
                raise ValueError(text)
            borrow = Borrow(
                book_id=book_id_,
                client_id=author.id,
                date_borrow=date_borrow_,
            )
            self.session.add(borrow)
            self.session.commit()
            status = True
        except Exception as e:
            text = f"[{Library_Borrow.add_one.__name__}]: \
Mistake => {e.__str__()}"
        finally:
            # CLOSE THE SESSION
            self.close()
            log.info(text)
            return status
    
    def receive(self, index: int):
        """
        TODO: Receive an one db's line from db.
        :param index: int. THis is the model's ID.
        :return: 'True' meaning what the object removed from db. Or \
        Not if 'False'
        """
        log.info(f"[{Library_Borrow.remove_one.__name__}] START")
        text = f"[{Library_Borrow.remove_one.__name__}]"
        status = False
        # get_one
        try:
            response = self.get_one(index, Borrow)
            if not response:
                text = text.join(
                    " Mistake => Not working index. \
Index is invalid")
                raise ValueError(text)
            status = True
        except Exception as  e:
            text = text.join(f" Mistake => {e.__str__()}")
        finally:
            self.close()
            log.info(text)
            return status