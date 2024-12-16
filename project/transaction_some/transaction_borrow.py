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
            raise ValueError(text)
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
    
    def update(self, index: int, book_id_: int = None, client_id_: int = None,
               date_borrow_: datetime = None, date_return_= datetime.utcnow):
        """
         TODO: New data, we receive for entrypoint, for update the borrow's data \
            from tabel db. From entrypoint we can receive one \
            or more variables.
        :param index: int. THis is the model's ID.
        :param book_id_: int. The book's index from 'Book'. Default is 'None'
        :param client_id_: int. The Client's index from 'Client'.
         Default is 'None'
        :param date_borrow_: datetime. This is datetime when the client
         received a book.  Default is 'None'
        :param date_return_: datetime. This is datetime when the client
         returned a book. Default 'datetime.utcnow'
        :return: bool. 'True' it means what everyone attributes went \
        the everyone processing the very well. Or not
        """
        log.info(f"[{Library_Borrow.update.__name__}] START")
        text = f"[{Library_Borrow.update.__name__}]"
        status = False
        try:
            borrow = self.session(Borrow).query.filter_by(id=index).first()
            if not borrow:
                text = f"[{text} \
Mistake => Not working index. Index is invalid"
                raise ValueError(text)
            attrib_list = [book_id_, client_id_,
                date_borrow_, date_return_]
            # Here, need to find working attributes then will be change
            # data in db
            working_attrib = [view for view in attrib_list if view]
            if len(working_attrib) == 0:
                text = f"[{Library_Borrow.update.__name__}] \
Mistake => Object not found, was"
                raise ValueError(text)
            if book_id_:
                borrow.book_id = book_id_
                text = text.join(" Meaning this 'book_id' was updated.")
            if client_id_:
                borrow.client_id = client_id_
                text = text.join(" Meaning this 'client_id' was updated.")
            if date_borrow_:
                borrow.date_borrow = date_borrow_
                text = text.join(" Meaning this 'date_borrow' was updated.")
            if date_return_:
                borrow.date_return = date_return_
                text = text.join(" Meaning this 'date_return' was updated.")
            self.session.commit()
            text = text.join(" Db 'Borrow' was updated. END")
        except Exception as e:
            text = f"[{Library_Borrow.update.__name__}] \
Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status