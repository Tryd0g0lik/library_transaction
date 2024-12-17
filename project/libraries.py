# """
# Here is a logic for work with db.
# This is a management for control the books
# """
#
# from project.models import Book, get_session
#
#
# class Library:
#     """
#     This is a management for control the books
#     """
#
#     def __init__(self):
#         self.session = get_session()
#
#     def add_hook(self, title: str,
#                  author: str,
#                  year: int,
#                  status="в наличии") -> bool:
#         """
#         TODO: Add a new bork
#         :param title: str. This is a name book.
#         :param author: str.
#         :param year: int. This is a year when this is book was created.
#         :param status: is "в наличии" or "выдана"
#         :return:
#         """
#         if len(title) < 5 or len(author) < 5:
#             print(
#                 f"[Library]: Error => Проверьте Заголовок,\
#  Автора. Длина от 5 символов."
#             )
#             return False
#         elif len(str(year)) < 4 or len(str(year)) > 4:
#             print(f"[Library]: Error => Год издания должен иметь 4 символа.")
#             return False
#         if status != "в наличии" and status != "выдана":
#             print(
#                 f"[Library]: Книга '{title}'\
#  не добавлена. Неизвестный статус."
#             )
#             return False
#         try:
#             new_book = Book(title=title,
#                              author=author,
#                              year=year,
#                              status=status)
#             self.session.add(new_book)
#             self.session.commit()
#             print(f"[Library]: Книга '{title}' добавлена.")
#             return True
#         except Exception as e:
#             print(f"[Library]: 'add_books' Error => {e}")
#             raise ValueError(f"[Library]: 'add_books' Error => {e}")
#     def remove_book(self, book_id: int) -> bool:
#         """
#         TODO: Here, we remove a book by book's index
#         :param book_id: int.
#         :return:
#         """
#         status = False
#         status_text = "None"
#         try:
#             book = self.session.query(Book).filter_by(id=int(book_id)).first()
#             if book:
#                 self.session.delete(book)
#                 self.session.commit()
#                 status_text = status_text.replace(
#                     "None", f"Книга с ID {book_id} удалена."
#                 )
#                 status = True
#             else:
#                 status_text = status_text.replace(
#                     "None", f"Книга с ID {book_id} не найдена."
#                 )
#         except Exception as e:
#             status_text = status_text.replace(
#                 "None", f"[Library]: 'remove_book' Error => {e}"
#             )
#             raise ValueError(status_text)
#         finally:
#             print(f"[Library]: {status_text}")
#             return status
#
#     def find_books(self, search_term: str) -> [list, bool]:
#         """
#         TODO: This is a method look up book by string's termns
#         :param search_term: str. This is the title or author, or year
#         :return:
#         """
#         try:
#             results: list = (
#                 self.session.query(Book)
#                 .filter(
#                     (Book.title.ilike(f"%{search_term}%"))
#                     | (Book.author.ilike(f"%{search_term}%"))
#                     | (
#                         Book.year == int(search_term)
#                         if search_term.isdigit()
#                         else False
#                     )
#                 )
#                 .all()
#             )
#             return results
#         except Exception as e:
#             print(f"[Library]: 'find_books' Error => {e}")
#             raise ValueError(f"[Library]: 'find_books' Error => {e}")
#         finally:
#             return False
#
#     def display_books(self) -> bool:
#         """
#         TODO: Public an all books from library
#         """
#         status = False
#         try:
#             books = self.session.query(Book).all()
#             if not books:
#                 print("[Library]: Нет доступных книг.")
#             for book in books:
#                 print(
#                     f"[Library]: ID: {book.id}, Название: {book.title}, \
#                 Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
#                 )
#                 status = True
#         except Exception as e:
#             print(f"[Library]: 'find_books' Error => {e}")
#             raise ValueError(f"[Library]: 'find_books' Error => {e}")
#         finally:
#             return status
#
#     def change_status(self, book_id: int, new_status="выдана"):
#         """
#         :param book_id: int
#         :param new_status: str. Is "в наличии" or "выдана"
#         :return:
#         """
#         status = False
#         if not book_id:
#             print("[Library]: Проверьте id книги.")
#             return status
#         if new_status != "в наличии" and new_status != "выдана":
#             print("[Library]: Проверьте статус.")
#             return status
#
#         try:
#             book = self.session.query(Book).filter_by(id=int(book_id)).first()
#             if not book:
#                 print(f"[Library]: Книга с ID {book_id}\
#  не найдена. Проверьте ID")
#             if new_status in ["в наличии", "выдана"]:
#                 book.status = new_status
#                 self.session.commit()
#             print(
#                 f"[Library]: Статус книги с ID {book_id} \
# изменен на '{new_status}'."
#             )
#             status = True
#         except Exception as e:
#             print(f"[Library]: Проверьте id книги. ERROR => {e}")
#             raise ValueError(f"[Library]: Проверьте id книги. ERROR => {e}")
#         finally:
#             return status
#
#     def close(self):
#         """Close the session"""
#         try:
#             self.session.close()
#         except Exception as e:
#             print(f"[Library]: Библиотека закрыта. Error => {e}")
#             raise ValueError(f"[Library]: Библиотека закрыта. Error => {e}")
