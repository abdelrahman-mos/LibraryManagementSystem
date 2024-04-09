import uuid
from enum import Enum
from LibraryManagementSystem.Member import Member
from datetime import datetime


class BookCategory(Enum):
    SCIENCE = 1
    FICTION = 2
    LAW = 3


class Book:
    def __init__(self, name: str, author: str, category: BookCategory, num: int = 1):

        # Public attributes
        self.id = uuid.uuid4()
        self.name = name
        self.author = author
        self.category = category

        # Private attributes
        self._num = num
        self._numAvailable = num
        self._borrowedBy: list[Member] = []
        self._reservedBy: list[tuple[Member, datetime]] = []

    def borrowBook(self, borrowBy: Member):
        if self._numAvailable > 0:
            self._numAvailable -= 1
            self._borrowedBy.append(borrowBy)
            return True
        return False

    def reserveBook(self, reserveBy: Member):
        date = datetime.now()
        # print(date)
        self._reservedBy.append((reserveBy, date))

    def returnBook(self, returnedBy: Member):
        if returnedBy in self._borrowedBy:
            self._borrowedBy.remove(returnedBy)
            self._numAvailable += 1

    # def __str__(self):
    #     tmp = f"book name: {self.name}\nauthor: {self.author}\ncategory: {self.category}\nID: {self.id}\n"
    #     return tmp
