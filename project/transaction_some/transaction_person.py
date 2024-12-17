"""
Here, is a DYNAMICALLY class for work with tabular models from db.
This tabular models it means the 'Author' and 'Client' models.
To the entrypoint we receive only one model. It's  from 'Client' or 'Author'.
Then, everyone methods from the Library_Person's class has as common for
working with 'Author' and 'Client' models
"""
from typing import (Type, Union)
import logging
from datetime import datetime
from project.transaction_some.transaction_basic import Library_basis
from project.models_some.model_autors import Author
from project.models_some.model_client import Client
from project.logs import configure_logging
configure_logging(logging.INFO)
log = logging.getLogger(__name__)


class Library_Person(Library_basis):
    """
    Here, is a DYNAMICALLY class for work with tabular models from db.
    This tabular models it means the 'Author' and 'Client' models.
    """
    def __init__(self,  model_name: type[Author | Client]):
        """
        TODO: To the entrypoint we receive only one model. It's  
            from 'Client' or 'Author'.
        :param model: type[Union[Author, Client]]
        """
        super().__init__()
        self.__model_name = model_name

    def get_model_name(self) ->type[Author | Client]:
        """
        TODO: Receives a value from a private variable. This a variable 
            means the 'Author' and 'Client' models
        :return: type[Union[Author, Client]]
        """
        return self.__model_name

    def add_one(self, firstname_:str,
            secondname_:str,
            birthday_: datetime = None) -> bool:
        """
        TODO: New model's line adds to the Model db's table
        :param firstname_: str. The person's firstname.
        :param secondname_: str.  The person's secondname.
        :param birthday_:  The person's datetime.
        :return: bool. 'True' it means was created new line of db or not.
        """
        log.info(f"[{Library_Person.add_one.__name__}] START")
        text = f"[{Library_Person.add_one.__name__}] END"
        status = False
        try:
            birthday = birthday_ if birthday_ else datetime.utcnow()
            Model = self.get_model_name()
            model = Model(firstname=firstname_,
                            secondname=secondname_,
                            birthday=birthday
                            )
            self.session.add(model)
            self.session.commit()
            status = True
        except Exception as e:
            text = f"[{Library_Person.add_one.__name__}]: \
Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            # CLOSE THE SESSION
            self.close()
            log.info(text)
            return status
        
    def receive(self, index: int = None) -> type[Author | Client]:
        """
        TODO: Select tne one person from the 'Model' db's table.
        :param index: int. The person's ID from db
        :return: dict a one person from selected by 'id'.
        """
        log.info(f"[{Library_Person.get_one.__name__}] START")
        text = f"[{Library_Person.get_one.__name__}] END"
        
        try:
            Model = self.get_model_name()
            if index:
                # model = self.session(Model).query.filter_by(id=index).first()
                model = self.get_one(Model, index)
                if not model:
                    text = f"{text} Mistake => Not working index. \
Index is invalid"
                
                return model
            if not index:
                text = f"{text} Mistake => Not working index. \
Index is invalid"
        except Exception as e:
            text = f"[{Library_Person.get_one.__name__}] \
Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            
    def update(self, index:int, new_firstname_:str = None,
            new_secondname_:str = None,
            new_birthday_:str=None) -> bool:
        """
        TODO: New data, we receive for entrypoint, for update the model's data \
            from tabel db. From entrypoint we can receive one \
            or more variables.
        :param index: int. The person's ID from db.
        :param new_firstname_: str. The new person's firstname.
        Default is 'None'
        :param new_secondname_: str.  The new person's secondname.
        Default is 'None'
        :param new_birthday_:  The new person's datetime. Default is 'None'
        :return: bool. 'True' it means what everyone attributes went \
        the everyone processing the very well. Or not
        """
        log.info(f"[{Library_Person.update.__name__}] START")
        text = f"[{Library_Person.update.__name__}]"
        status = False
        try:
            # get data from db
            Model = self.get_model_name()
            authors = self.session.query(Model).filter_by(id=index).first()
            if not authors:
                text = "".join(f"{text}  Mistake => Not working index. \
Index is invalid")
                raise ValueError(text)
            attrib_list = [new_firstname_, new_secondname_, new_birthday_]
            # Here, need to find working attributes then will be change
            # data in db
            working_attrib = [view for view in attrib_list if view]
            if len(working_attrib) == 0:
                text = "".join(f"{text}  Mistake => Object not found, was.")
                log.info(text)
                raise ValueError(text)
            
            if new_firstname_:
                authors.firstname = new_firstname_
                text = "".join(f"{text}  Meaning this 'firstname' was updated.")
            if new_secondname_:
                authors.secondname = new_secondname_
                text = "".join(f"{text}  Meaning this 'secondname' \
was updated.")
            if new_birthday_:
                authors.birthday = new_birthday_
                text = "".join(f"{text}  Meaning this 'birthday' \
was updated.")
            self.session.commit()
            text = "".join(f"{text} Db was updated. END")
            status = True
        except Exception as e:
            text = f"[{Library_Person.update.__name__}] \
Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status
    def removing(self, index: int) -> bool:
        """
        TODO: Delete an one db's line from db.
        :param index: int. THis is the model's ID.
        :return: 'True' meaning what the object removed from db. Or \
        Not if 'False'
        """
        log.info(f"[{Library_Person.remove_one.__name__}] START")
        text = f"[{Library_Person.remove_one.__name__}]"
        status = False
        try:
            # get data from db
            Model = self.get_model_name()
            response: bool = self.remove_one(index, Model)
            if not response:
                text = "".join(f"{text}  Mistake => Not working index. \
Index is invalid")
                raise ValueError(text)
            status = response
        except Exception as e:
            text = "".join(f"{text} Mistake => {e.__str__()}")
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status
#         """
#         TODO: Delete an one db's line from db.
#         :param index: int. THis is the model's ID.
#         :return: 'True' meaning what the object removed from db. Or \
#         Not if 'False'
#         """
#         log.info(f"[{Library_Person.remove_one.__name__}] START")
#         status_text = f"[{Library_Person.remove_one.__name__}] \
# Mistake => Not working index."
#         status = False
#         try:
#             # get data from db
#             Model = self.get_model_name()
#             authors = self.session(Model).query.filter_by(id=index).first()
#             if authors:
#                 log.info(status_text)
#                 raise ValueError(status_text)
#             authors.delete()
#             self.session.commit()
#             status = True
#             status_text = status_text.replace(
#                 "Mistake => Not working index",
#                 "Mistake => all went very well. Meaning is the True"
#             )
#         except Exception as e:
#             status_text = f"[{Library_Person.remove_one.__name__}] \
# Mistake => {e.__str__()}"
#         finally:
#             log.info(status_text)
#             return status