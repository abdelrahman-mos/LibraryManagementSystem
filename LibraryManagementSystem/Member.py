import uuid
from LibraryManagementSystem.Book import Book
from datetime import datetime


class Member:
    def __init__(self, name: str):
        self.name = name
        self.id = uuid.uuid4()
        self.borrowedBooks: list[tuple[Book, datetime]] = []
        self.reservedBooks: list[Book] = []
        self._canBorrow = True
