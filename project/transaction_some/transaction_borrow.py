"""
Here is a logic for work with the db Borrow's transactions .
This is a management for control
"""
import logging
from datetime import datetime
from project.logs import configure_logging
from project.models_some.model_book import Book
from project.models_some.model_borrow import Borrow
from project.models_some.model_client import Client
from project.transaction_some.transaction_basic import Library_basis
from project.transaction_some.transaction_book import Library_book
from project.transaction_some.transaction_person import Library_Person

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

class Library_Borrow(Library_basis):
    async def add_one(self, book_id_: int,
                      client_id_: int,
                      date_borrow_: datetime = datetime.utcnow,
                      date_return_: datetime = None,
                      quantity_: int = 1) -> bool:
                      
        """
        TODO: New borrow's is line adds to the Model db's table.
            There is checking of book quantity. If client received a book,
            we have the book quantity state to the less
          
        :param book_id_: int. The book's index from 'Book'.
        :param client_id_: int. The Client's index from 'Client'.
        :param date_borrow_: datetime. This is datetime when the client
         received a book.
         :param date_return_: datetime. This is datetime when the client
         return a book.
        :return: bool. 'True' it means was created new line in db or not.
         If we received meaning 'False', it means what we receives
         a mistake or the book quantity equal is zero.
        """
        log.info(f"[{Library_Borrow.add_one.__name__}] START")
        text = f"[{Library_Borrow.add_one.__name__}]:"
        status = False
        try:
            # The 'ID' checking in db
            book = Library_book()
            result_book = await book.receive(book_id_)
            client = Library_Person(Client)
            result_client = await client.receive(client_id_)
    
            for view in [result_client[0] if result_client else None,
                         result_book[0] if result_book else None]:
                if not view:
                    text = f"{text} \
Mistake => Not found the client or book. 'client_id_' or 'book_id_' is invalid."
                    raise ValueError(text)
            if result_book[0]["quantity"] > 0:
                # CREATE new a line
                borrow = Borrow(
                    book_id=book_id_,
                    client_id=client_id_,
                    date_borrow=date_borrow_,
                    date_return=date_return_
                )
                # One client take the one a book from library
                self.session.add(borrow)
                self.session.commit()
                # Book quantity we make less
                book = self.session.query(Book).filter_by(id=book_id_).first()
            
                if date_borrow_ and not date_return_:
                    book.quantity -= 1 if not quantity_ else quantity_
                    self.session.commit()
        
                # Book quantity we make more
                if date_borrow_ and date_return_:
                    book.quantity += 1 if not quantity_ else quantity_
                    self.session.commit()
               
                status = True
            text = f"{text} END"
        except Exception as e:
            text = f"{text} \
Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            # CLOSE THE SESSION
            self.close()
            log.info(text)
            return status
    
    async def receive(self, index: int):
        """
        TODO: Receive an one db's line from db.
        :param index: int. THis is the model's ID.
        :return: 'True' meaning what the object removed from db. Or \
        Not if 'False'
        """
        log.info(f"[{Library_Borrow.remove_one.__name__}] START")
        text = f"[{Library_Borrow.remove_one.__name__}]:"
        status = False
        # get_one
        try:
            
            response = self.session.query(Borrow).filter_by(id=index).first()
            if not index:
                response = self.session.query(Borrow).all()
                
            if not response:
                text = text.join(
                    " Mistake => Not working index. \
Index is invalid")
                raise ValueError(text)
                
            status = [self.serialize(view) for view in ([response]
                                                        if type(response) != list
                                                        else response)
                      ]
        
        except Exception as  e:
            text = f"{text} Mistake => {e.__str__()}"
        finally:
            self.close()
            log.info(text)
            return status
            
    
    async def update(self, index: int, book_id_: int = None,
                     client_id_: int = None,
                     quantity_: int = None,
                     date_borrow_: datetime = None,
                     date_return_: datetime = datetime.utcnow):
        """
         TODO: New data, we receive for entrypoint, for update the borrow's data \
            from tabel db. From entrypoint we can receive one \
            or more variables.
        :param index: int. THis is the model's ID.
        :param book_id_: int. The book's index from 'Book'. Default is 'None'
        :param client_id_: int. The Client's index from 'Client'.
         Default is 'None'
        :param quantity_: int. The books quantity take an one client.
         These books have an one/single/common name.
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
            borrow = self.session.query(Borrow).filter_by(id=index).first()
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
                text = "".join(f"{text}  Meaning this 'book_id' was updated.")
            if client_id_:
                borrow.client_id = client_id_
                text = "".join(f"{text}  Meaning this 'client_id' was updated.")
            if date_borrow_:
                borrow.date_borrow = date_borrow_
                text = "".join(f"{text}  Meaning this 'date_borrow' was updated.")
            if date_return_:
                borrow.date_return = date_return_
                text = "".join(f"{text}  Meaning this 'date_return' was updated.")
            if quantity_:
                # Book quantity we make more
    
                """
                меняем количество книг в зависимости от:
                - возврата или выдачи книг;
                
                либо тут условия раздуваем, ориентируясь на:
                1. фактическое количество из ДБ;
                2 даты
                2.1 размер дат. Это приведет к раздуванию кода/веса.
                2.2.0 Или на фронте/backend-е ставим ('выдача''возврат'):
                    2.2.1 'book_status' (тип строки строка/checktpoint/choice) в виде:
                        2.2.1.1 выбираем статус из списка;
                        2.2.1.2 ставим галочку.
                Но, пп. 2.* потребуют проверку на человеческий фактор,
                что опять раздует код.
                .
                .
                Как проще сделать?
"""
                # This is only plug/empty, below
                if borrow.date_return and (
                  borrow.date_return > borrow.date_borrow
                ):
                    borrow.books.quantity +=1
                elif borrow.date_borrow and quantity_ and \
                    not borrow.date_return:
                    borrow.books.quantity -= 1
                    

            self.session.commit()
            text = f"{text}  Db 'Borrow' was updated. END"
            status = True
            

        except Exception as e:
            text = f"[{Library_Borrow.update.__name__}] \
Mistake => {e.__str__()}"
            
            raise ValueError(text)
        finally:
            self.close()
            log.info(text)
            return status

    def serialize(self, borrow):
        # GET QUANTITY
        quantity_book = borrow.books.quantity
        return {
            "index": borrow.id if borrow.id else None,
            "book_id": borrow.book_id if borrow.book_id else None,
            "client_id": borrow.client_id if borrow.client_id else None,
            "date_borrow": borrow.date_borrow if borrow.date_borrow else None,
            "date_return": borrow.date_return if borrow.date_return else None,
            "quantity": quantity_book if quantity_book else None
        }