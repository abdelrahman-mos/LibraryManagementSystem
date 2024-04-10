import uuid
from datetime import datetime
from typing import List, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from LibraryManagementSystem.Book import Book


class User:

    # _MAX_BORROW = 5

    def __init__(self, name: str):
        self.name = name
        self.id = uuid.uuid4()

    def onLogin(self):
        pass

    def borrowBook(self, book: "Book"):
        pass

    def reserveBook(self, book: "Book"):
        pass
