import uuid
from datetime import datetime
from typing import List, Tuple, TYPE_CHECKING
from LibraryManagementSystem.User.User import User

if TYPE_CHECKING:
    from LibraryManagementSystem.Book import Book


class Librarian(User):

    def __init__(self, name: str):
        super().__init__(name)
        self.borrowedBooks: List[Tuple["Book", datetime]] = []
        self.reservedBooks: List["Book"] = []
        self._canBorrow = True

    def borrowBook(self, book: "Book"):
        pass

    def reserveBook(self, book: "Book"):
        pass

    def addMemberAccount(self):
        pass

    def removeMemberAccount(self):
        pass

    def addBook(self):
        pass

    def removeBook(self):
        pass

    def editBook(self):
        pass
