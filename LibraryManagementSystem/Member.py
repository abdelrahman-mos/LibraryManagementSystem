import uuid
from datetime import datetime
from typing import List, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from LibraryManagementSystem.Book import Book


class Member:

    def __init__(self, name: str):
        self.name = name
        self.id = uuid.uuid4()
        self.borrowedBooks: List[Tuple["Book", datetime]] = []
        self.reservedBooks: List = []
        self._canBorrow = True

    def borrowBook(self, book: "Book"):
        if self._canBorrow:
            date = datetime.now()
            book.borrowBook(self)
            self.borrowedBooks.append((book, date))
