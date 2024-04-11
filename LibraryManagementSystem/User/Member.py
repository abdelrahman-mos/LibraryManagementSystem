from datetime import datetime
from typing import List, Tuple, TYPE_CHECKING
from LibraryManagementSystem.User.User import User
import uuid

if TYPE_CHECKING:
    from LibraryManagementSystem.Library.Book import Book
    from LibraryManagementSystem.Library.Library import Library


class Member(User):
    _MAX_BORROW = 5

    def __init__(self, name: str, userName: str, passwd: bytes):
        super().__init__(name, userName, passwd)
        self.borrowedBooks: List[Tuple["Book", datetime]] = []
        self.reservedBooks: List["Book"] = []
        self._canBorrow = True

    def onLogin(self):
        self._isLoggedIn = True
        self._checkBooksAvailability()

        return True

    def _checkBooksAvailability(self):
        # loop on books and check if they're available
        # can be implemented later
        # add a notify function to print all available books from reserved books where it's member's turn
        # available_books = [book for book in self.reservedBooks if book.]
        pass

    def _checkOverDue(self):
        # Loop on all borrowed books and check if a borrowed book is overdue
        pass

    def borrowBook(self, lib: "Library"):
        bookToBorrow = self._getBookByID(lib)
        if bookToBorrow is None:
            return
        if self._canBorrow:
            borrowed, dateBorrowed = bookToBorrow.borrowBook(self)
            if borrowed:
                print(f'Book borrowed successfully on {dateBorrowed.strftime("%d/%m/%Y, %H:%M:%S")}.')
                self.borrowedBooks.append((bookToBorrow, dateBorrowed))
                if len(self.borrowedBooks) == self._MAX_BORROW:
                    self._canBorrow = False
                else:
                    print("Book is not available now.")
            else:
                print("Sorry, you have exceeded your borrowing limit.")

    def reserveBook(self, lib: "Library"):
        bookToReserve = self._getBookByID(lib)
        if bookToReserve is None:
            return

        bookToReserve.reserveBook(self)
        self.reservedBooks.append(bookToReserve)


    # def borrowBook(self, lib: "Library"):
    #     if self._canBorrow:
    #         # if the book cannot be borrowed, the member should be able to reserve it
    #         if book.borrowBook(self):
    #             date = datetime.now()
    #             self.borrowedBooks.append((book, date))
    #             if len(self.borrowedBooks) == self._MAX_BORROW:
    #                 self._canBorrow = False
    #         else:
    #             # shouldn't be like this, will edit later
    #             reply = input("Book is not available now, want to reserve it? (y/n)\n")
    #             if reply.lower() == 'y':
    #                 return self.reserveBook(book)
    #     else:
    #         print("Sorry, you have exceeded your borrowing limit.")

    def returnBook(self, lib: "Library"):
        pass

    def renewBook(self):
        pass

    def listBorrowed(self):
        borrowedBooks = list(zip(*self.borrowedBooks))[0]
        self._listBooks(borrowedBooks)

    def listReserved(self):
        self._listBooks(self.reservedBooks)
    # def reserveBook(self, lib: "Library"):
    #     date = book.reserveBook(self)
    #     # print(f"Book reserved on date {date.strftime("%d/%m/%Y, %H:%M:%S")}")
    #     self.reservedBooks.append(book)
