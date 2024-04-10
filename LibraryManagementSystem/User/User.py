import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from LibraryManagementSystem.Library.Book import Book


class User:

    # _MAX_BORROW = 5

    def __init__(self, name: str, userName: str, passwd: bytes):
        self.name = name
        self.id = uuid.uuid4()
        self.userName = userName
        self._passwd = passwd

    def onLogin(self):
        pass

    def borrowBook(self, book: "Book"):
        pass

    def reserveBook(self, book: "Book"):
        pass
