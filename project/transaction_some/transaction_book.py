"""
Here is a logic for work with the db Book's transactions .
This is a management for control
"""
import logging
from project.models_some.model_autors import Author
from project.models_some.model_book import Book
from project.transaction_some.transactin_basic import Library_basis
from project.logs import configure_logging
from project.transaction_some.transaction_person import Library_Person

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

class Library_book(Library_basis):
    
    def add_one(self,
                title_: str,
                descriptions_: str,
                author_id_: int,
                quantity_: int,
                ) -> bool:
        """
        TODO: New model's line adds to the Books db's table
        :param title_: str.  This is book's name. Max quantity symbols is
         before 155.
        :param descriptions_: str. this is book's description. Max quantity
         symbols is before 255.
        :param author_id_: int. This number (index from db) author.
        :param quantity_: int.
        :return:
        """
        log.info(f"[{Library_book.add_one.__name__}] START")
        status = False
        text=f"[{Library_book.add_one.__name__}] END"
        try:
            person = Library_Person(Author)
            author = person.get_one(author_id_)
            
            if not author:
                text = f"[{Library_book.add_one.__name__}] \
Mistake => Not found the author. 'author_id' is invalid."
                raise ValueError(text)
            
            book = Book(
                title=title_,
                descriptions=descriptions_,
                author_id=author.id,
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

    def get_one(self, index: int) -> type[Book | bool]:
        """
        TODO: By an index, be to select tne one book from the 'Book' db's table.
        :param index: int. The book's ID from db
        :return: object a one book from selected by 'id' or bool data.
        """
        log.info(f"[{Library_book.get_one.__name__}] START")
        text = "END"
        status = False
        try:
            book = self.session(Book).query.filter_by(id=index).first()
            if not book:
                text = f"[{Library_book.get_one.__name__}] \
 Mistake => Not found the book's ID. Index is invalid."
                raise ValueError(text)
            status = book
    
        except Exception as e:
            text = f"[{Library_book.get_one.__name__}] \
 Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status
    
    def update(self,index:int, new_title_: type[str | None ] = None,
               new_descriptions_: type[str | None] = None,
               new_author_id_: type[int | None] = None,
               new_quantity_: type[int | None] = None
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
        text = f"[{Library_book.update.__name__}]"
        status = False
        try:
            # get data from db
            book = self.session(Book).query.filter_by(id=index).first()
            if book:
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
            status_text = f"[{Library_book.update.__name__}]"
            if new_title_:
                book.title = new_title_
                status_text = "".join(f"{text}  Meaning this 'title' \
was updated.")
            if new_descriptions_:
                book.descriptions = new_descriptions_
                status_text = "".join(f"{text}  Meaning this 'description' \
was updated")
            if new_author_id_:
                book.author_id = new_author_id_
                status_text = "".join(f"{text}  Meaning this 'authors \
was updated")
            if new_quantity_:
                book.quantity = new_quantity_
                status_text = "".join(f"{text}  Meaning this 'quantity' \
was updated")
            self.session.commit()
            text = "".join(f"{text} Db 'Book' was updated. END")
            status = True
        except Exception as e:
            text = f"[{Library_book.update.__name__}] \
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
        log.info(f"[{Library_book.remove_one.__name__}] START")
        text = f"[{Library_book.remove_one.__name__}] END"
        status = False
        try:
            # get data from db
            response: bool = self.remove_one(index, Book)
            if not response:
                text = text.join(
                    " Mistake => Not working index. \
Index is invalid"
                )
                raise ValueError(text)
            status = response
        except Exception as e:
            text = f"[{Library_book.update.__name__}] \
  Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status
            
#     def remove_one(self, index: int) -> bool:
# #         """
# #         TODO: Delete an one db's line from db.
# #         :param index: int. THis is the book's ID.
# #         :return: 'True' meaning what the object removed from db. Or
# #         Not if 'False'
# #         """
# #         log.info(f"[{Library_book.remove_one.__name__}] START")
# #
# #         text = f"[{Library_book.remove_one.__name__}] END"
# #         status = False
# #         try:
# #             # get data from db
# #             authors = self.session(Book).query.filter_by(id=index).first()
# #             if authors:
# #                 text = f"[{Library_book.remove_one.__name__}] \
# # Mistake => Not working index."
# #                 raise ValueError(text)
# #             authors.delete()
# #             self.session.commit()
# #             status = True
# #         except Exception as e:
# #             f"[{Library_book.remove_one.__name__}] \
# # Mistake => {e.__str__()}"
# #         finally:
# #             self.close()
# #             log.info(text)
# #             return status
        
        