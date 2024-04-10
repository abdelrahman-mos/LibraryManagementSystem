import uuid
from typing import TYPE_CHECKING
import bcrypt

if TYPE_CHECKING:
    from LibraryManagementSystem.Library.Book import Book


class User:

    # _MAX_BORROW = 5

    def __init__(self, name: str, userName: str, passwd: bytes):
        self.name = name
        self.id = uuid.uuid4()
        self.userName = userName
        self._passwd = passwd
        self._isLoggedIn = False

    def onLogin(self):
        self._isLoggedIn = True
        print(f"Hello, {self.name}")
        pass

    def checkpasswd(self, passwd: bytes):
        return bcrypt.checkpw(passwd, self._passwd)

    def borrowBook(self, book: "Book"):
        pass

    def reserveBook(self, book: "Book"):
        pass
