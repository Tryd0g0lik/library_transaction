"""
Here is a logic for work with the db transactions.
This is a management for control
"""
import logging
from typing import (Dict, Any, Union)
from project.models import get_session
from project.models_some.model_autors import Author
from project.models_some.model_book import Book
from project.models_some.model_borrow import Borrow
from project.models_some.model_client import Client
from project.logs import configure_logging

log = logging.getLogger(__name__)
configure_logging(logging.INFO)

class Library_basis:
    """
    TODO:" This is basic class for a work with Library db.
    """
    
    def __init__(self):
        self.session = get_session()
        self._transaction = None

    def get_transaction(self) -> [Dict[str, Any], int]:
        """
        TODO: Receive the transaction object .
        :return: object
        """
        return self._transaction

    def close(self) -> None:
        """Close the session"""
       

        try:
            self.session.close()
        except Exception as e:
            log.info(f"[{__name__}]: Session was closed. Error => {e}")

            raise ValueError(f"[{__name__}]: Session was closed. Error => {e}")
    def remove_one(self, index: int,
                   Model: type[Union[Author, Client, Book, Borrow]]) -> bool:
        """
        TODO: Delete an one db's line from db. To the entrypoint we
            receive only one model. It's from 'Book', 'Client' or 'Author'.
        :param index: int. THis is the Model's ID.
        :param Model: int. THis is the Model's ID.
        :return: 'True' meaning what the object removed from db. Or
        Not if 'False'
        """
        log.info(f"[{Library_basis.remove_one.__name__}] START")
    
        text = f"[{Library_basis.remove_one.__name__}] END"
        status = False
        try:
            # get data from db
            authors = self.session.query(Model).filter_by(id=index).first()
            if not authors:
                text = f"[{Library_basis.remove_one.__name__}] \
    Mistake => Not working index."
                raise ValueError(text)
            
            self.session.delete(authors)
            self.session.commit()
            status = True
        except Exception as e:
            text = f"[{Library_basis.remove_one.__name__}] \
    Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status

    def get_one(self,
                Model: type[Author | Client | Book| Borrow],
                index: int = None
                ) -> type[Author | Client | Book| Borrow | bool]:
        """
        TODO: By an index, be to select tne one book from the 'Model' db's table.
        :param index: [int, None]. The model's ID from db
        :return: object a one model from selected by 'id', the all models if
        an index = None or bool data.
        """
        log.info(f"[{Library_basis.get_one.__name__}] START")
        text = f"[{Library_basis.get_one.__name__}]"
        status = False
        
        try:
            if index is not None:
                book = self.session.query(Model).filter_by(id=index).first()
                if not book:
                    text = f"{text} Mistake => Not found the model's ID. \
    Index is invalid."
                else:
                    status = [self.serialize(view) for view in [book]]
            else:
                books = self.session.query(Model).all()
                
                status = [self.serialize(view) for view in books]
        except Exception as e:
            text = f"{text} Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status

    def serialize(self, author):
        return {
            "index": author.id,
            "firstname": author.firstname,
            "secondname": author.secondname,
            "birthday": author.birthday.isoformat() if author.birthday else None,
            # Add other fields as necessary
        }
        