"""
Here is a logic for work with the db Borrow's transactions .
This is a management for control
"""
import logging
from datetime import datetime
from project.logs import configure_logging
from project.transaction_some.transactin_basic import Library_basis

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

class Library_borrows(Library_basis):
    def add_one(self, books_id_: int, client_id_: int,
                date_borrows_: datetime = datetime.utcnow,
                date_return: datetime = None ):
        """
        TODO: New borrow's line adds to the Model db's table
        :param firstname_: str. The person's firstname.
        :param secondname_: str.  The person's secondname.
        :param birthday_:  The person's datetime.
        :return: bool. 'True' it means was created new line of db or not.
        """
        try:
            pass
        except Exception as e:
            pass
        finally:
            pass