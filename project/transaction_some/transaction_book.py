"""
Here is a logic for work with the db Book's transactions .
This is a management for control
"""
import logging
from project.models_some.model_autors import Author
from project.models_some.model_book import Book
from project.transaction_some.transaction_basic import Library_basis
from project.logs import configure_logging
from project.transaction_some.transaction_person import Library_Person

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

class Library_book(Library_basis):
    
    async def add_one(self,
                title_: str,
                descriptions_: str,
                register_number_: str,
                author_id_: int,
                quantity_: int,
                ) -> bool:
        """
        TODO: New model's line adds to the Books db's table
        :param title_: str.  This is book's name. Max quantity symbols is
         before 155.
        :param descriptions_: str. this is book's description. Max quantity
         symbols is before 255.
         :param register_number_: This is register number. Mas quantity
         symbols is before 50. It is unique book's nuber.
        :param author_id_: int. This number (index from db) author.
        :param quantity_: int.
        :return:
        """
        log.info(f"[{Library_book.add_one.__name__}] START")
        status = False
        text=f"[{Library_book.add_one.__name__}] END"
        try:
            person = Library_Person(Author)
            author = await person.receive(author_id_)
            
            if not author:
                text = f"[{Library_book.add_one.__name__}] \
Mistake => Not found the author. 'author_id' is invalid."
            else:
                
                book = Book(
                    title=title_,
                    descriptions=descriptions_,
                    register_number=register_number_,
                    author_id=author_id_,
                    quantity=quantity_
                )
                self.session.add(book)
                self.session.commit()
                status = True
        except Exception as e:
            text = f"[{Library_book.add_one.__name__}]: \
Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status

    async def receive(self, index: int = None) -> type[Book | bool]:
        """
        TODO: By an index, be to select tne one book from the 'Book' db's table.
        :param index: int. The book's ID from db
        :return: object a one book from selected by 'id' or bool data.
        """
        text = f"[{Library_book.receive.__name__}]:"
        log.info(f"{text} START")
        text = "END"
        status = False
        try:
            if index is not None:
                book = self.session.query(Book).filter_by(id=index).first()
                if not book:
                    text = f"{text} Mistake => Not found the  book's ID. \
Index is invalid."
                else:
                    status = [self.serialize(view) for view in [book]]

            else:
                books = self.session.query(Book).all()
                status = [self.serialize(view) for view in books]
        except Exception as e:
            text = f"[{Library_book.receive.__name__}] \
 Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status
    
    async def update(self,index:int, new_title_: str = None,
               new_descriptions_:str = None,
               new_author_id_:int = None,
               new_quantity_:int = None
               ) -> bool:
        """
        TODO: New data, we receive from entrypoint, for update the Book's data, \
            from tabel db. From entrypoint we can receive one \
            or more variables.
        :param index: int. The book's ID from db.
        :param new_title_: str. The new book's title. Default is 'None'.
        :param new_descriptions_: str.  The new book's descriptions.
        Default is 'None'.
        :param new_author_id_: int.  The new book's author. Default is 'None'.
        :param new_quantity_: int.  The new book's quantity. Default is 'None'.
        :return: bool. 'True' it means what everyone attributes went \
        the everyone processing the very well. Or not
        """
        log.info(f"[{Library_book.update.__name__}] START")
        text = f"[{Library_book.update.__name__}]:"
        status = False
        try:
            # get data from db
            book = self.session.query(Book).filter_by(id=index).first()
            if not book:
                text = f"[{text} \
Mistake => Not working index. Index is invalid"
                raise ValueError(text)
            attrib_list = [new_title_, new_descriptions_,
                           new_author_id_, new_quantity_]
            # Here, need to find working attributes then will be change
            # data in db
            working_attrib = [view for view in attrib_list if view]
            if len(working_attrib) == 0:
                text = f"[{Library_book.update.__name__}] \
Mistake => Object not found, was"
                raise ValueError(text)
            status_text = ""
            if new_title_:
                book.title = new_title_
                status_text = f"{status_text} Meaning this 'title' \
was updated."
            if new_descriptions_:
                book.descriptions = new_descriptions_
                status_text = "".join(f"{status_text}  Meaning this 'description' \
was updated")
            if new_author_id_:
                book.author_id = new_author_id_
                status_text = "".join(f"{status_text}  Meaning this 'authors \
was updated")
            if new_quantity_:
                book.quantity = new_quantity_
                status_text = "".join(f"{status_text}  Meaning this 'quantity' \
was updated")
            self.session.commit()
            text = f"{text} {status_text}. Db 'Book' was updated. END"
            status = True
        except Exception as e:
            text = f"{text} \
Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status

    async def removing(self, index: int) -> bool:
        """
        TODO: Delete an one db's line from db.
        :param index: int. THis is the model's ID.
        :return: 'True' meaning what the object removed from db. Or \
        Not if 'False'
        """
        log.info(f"[{Library_book.remove_one.__name__}] START")
        text = f"[{Library_book.remove_one.__name__}] END"
        status = False
        try:
            # get data from db
            response: bool = await self.remove_one(index, Book)
            if not response:
                text = text.join(
                    " Mistake => Not working index. \
Index is invalid"
                )
            else:
                status = response
        except Exception as e:
            text = f"[{Library_book.update.__name__}] \
  Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status
            
    def serialize(self, book):
        return {
            "index": book.id,
            "title": book.title,
            "descriptions": book.descriptions,
            "register_number": book.register_number,
            "author_id": book.author_id,
            "quantity": book.quantity
            
        }
