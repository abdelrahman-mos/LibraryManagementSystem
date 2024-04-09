import uuid
from enum import Enum
from LibraryManagementSystem.Member import Member


class BookCategory(Enum):
    SCIENCE = 1
    FICTION = 2
    LAW = 3


class Book:
    def __init__(self, name: str, author: str, category: BookCategory, num: int):
        self.id = uuid.uuid4()
        self.name = name
        self.author = author
        self.category = category
        self._num = num
        self._numAvailable = num
        self._borrowedBy: list[Member] = []

    def borrowBook(self, borrowBy: Member):
        if self._numAvailable > 0:
            self._numAvailable -= 1
            self._borrowedBy.append(borrowBy)
            return True
        return False

    def __str__(self):
        tmp = f"book name: {self.name}\nauthor: {self.author}\ncategory: {self.category}\nID: {self.id}\n"
        return tmp

