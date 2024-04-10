from datetime import datetime
from typing import List, Tuple, TYPE_CHECKING
from LibraryManagementSystem.User.User import User

if TYPE_CHECKING:
    from LibraryManagementSystem.Library.Book import Book


class Member(User):

    _MAX_BORROW = 5

    def __init__(self, name: str, userName: str, passwd: bytes):
        super().__init__(name, userName, passwd)
        self.borrowedBooks: List[Tuple["Book", datetime]] = []
        self.reservedBooks: List["Book"] = []
        self._canBorrow = True

    def borrowBook(self, book: "Book"):
        if self._canBorrow:
            # if the book cannot be borrowed, the member should be able to reserve it
            if book.borrowBook(self):
                date = datetime.now()
                self.borrowedBooks.append((book, date))
                if len(self.borrowedBooks) == self._MAX_BORROW:
                    self._canBorrow = False
            else:
                # shouldn't be like this, will edit later
                reply = input("Book is not available now, want to reserve it? (y/n)\n")
                if reply.lower() == 'y':
                    return self.reserveBook(book)
        else:
            print("Sorry, you have exceeded your borrowing limit.")

    def reserveBook(self, book: "Book"):
        date = book.reserveBook(self)
        # print(f"Book reserved on date {date.strftime("%d/%m/%Y, %H:%M:%S")}")
        self.reservedBooks.append(book)
