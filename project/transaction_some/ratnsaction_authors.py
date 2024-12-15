from typing import (Dict, Any, )
import logging
from datetime import datetime
from project.transaction_some.transactin_basic import Library_basis
from project.models_some.model_autors import Author
from project.logs import configure_logging
configure_logging(logging.INFO)
log = logging.getLogger(__name__)

class Lybrary_Author(Library_basis):
    
    def add_one(self, firstname_:str,
            secondname_:str,
            birthday_: datetime = datetime.utcnow) -> bool:
        """
        TODO: New author adds to the 'Author' db's table
        :param firstname_: str. Author's name.
        :param secondname_: str. Authors's secondname.
        :param birthday_: datetime.
        :return: bool. 'True' it means was created new line of db or not.
        """
        log.info(f"[{Lybrary_Author.add_one.__name__}] START")
        status = False
        try:
            author = Author(firstname=firstname_,
                            secondname=secondname_,
                            birthday=birthday_
                            )
            self.session.add(author)
            self.session.commit()
            status = True
        except Exception as e:
            log.info(f"[{Lybrary_Author.add_one.__name__}]: \
Mistake => {e.__str__()}")
        finally:
            # CLOSE THE SESSION
            self.close()
            log.info(f"[{Lybrary_Author.add_one.__name__}] END")
            return status
        
    def get_one(self, index: int) -> dict:
        """
        TODO: Select tne one person from the 'Author' db's table.
        :param index: int.
        :return: dict a one person from selected by 'id'.
        """
        log.info(f"[{Lybrary_Author.get_one.__name__}] START")
        try:
            author = self.session(Author).query.filter_by(id=index).first()
            if not author:
                text = f"[{Lybrary_Author.get_one.__name__}] \
Mistake => Not found the author's ID"
                log.info(text)
                raise ValueError(text)
            return author.__dict__
                
        except Exception as e:
            log.info(f"[{Lybrary_Author.get_one.__name__}] \
Mistake => {e.__str__()}")
        finally:
            self.close()
            log.info(f"[{Lybrary_Author.get_one.__name__}] END")
            
    def update(self, index:[int, None], new_firstname_:[str, None]=None,
            new_secondname_:[str, None] = None,
            new_birthday_:[str, None]=None) -> bool:
        """
        TODO: New data we receive to entrypoint for update  the author data \
            from 'Author' db's table.
        :param firstname_: str. Author's name.
        :param secondname_: str. Authors's secondname.
        :param birthday_: datetime. It means the author's birthday.
        :return: bool. 'True' it means what an everyone attributes went \
        the everyone processing the very well. Or not
        """
        log.info(f"[{Lybrary_Author.update.__name__}] START")
        status = False
        try:
            # get data from db
            authors = self.session(Author).query.filter_by(id=index).first()
            attrib_list = [new_firstname_, new_secondname_, new_birthday_]
            # Here, need to find working attributes then will be change
            # data in db
            working_attrib = [view for view in attrib_list if view]
            if len(working_attrib) == 0:
                text = f"[{Lybrary_Author.update.__name__}] \
Mistake => Object not found, was"
                log.info(text)
                raise ValueError(text)
            status_text = ''
            if new_firstname_:
                authors.firstname = new_firstname_
                status_text = ''.join(" Meaning this 'firstname' was updated.")
            if new_secondname_:
                authors.secondname = new_secondname_
                status_text = status_text.join(" Meaning this 'secondname' \
was updated")
            if new_birthday_:
                authors.birthday = new_birthday_
                status_text = status_text.join(" Meaning this 'birthday' \
was updated")
            self.session.commit()
            log.info(status_text.join("Db was updated"))
            status = True
        except Exception as e:
            log.info(f"[{Lybrary_Author.update.__name__}] \
Mistake => {e.__str__()}")
        finally:
            self.close()
            log.info(f"[{Lybrary_Author.update.__name__}] END. \
It all was  {status} ")
            return status
