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
            # if the book cannot be borrowed, the member should be able to reserve it
            if book.borrowBook(self):
                date = datetime.now()
                self.borrowedBooks.append((book, date))
                if len(self.borrowedBooks) == 5:
                    self._canBorrow = False
            else:
                # shouldn't be like this, will edit later
                reply = input("Book is not available now, want to reserve it? (y/n)\n")
                if reply.lower() == 'y':
                    return self.reserveBook(book)

    def reserveBook(self, book: "Book"):
        date = book.reserveBook(self)
        print(f"Book reserved on date {date.strftime("%d/%m/%Y, %H:%M:%S")}")