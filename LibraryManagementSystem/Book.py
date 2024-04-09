import uuid
from enum import Enum


class BookCategory(Enum):
    SCIENCE = 1
    FICTION = 2
    LAW = 3


class Book:
    def __init__(self, name: str, author: str, category: BookCategory):
        self.id = uuid.uuid4()
        self.name = name
        self.author = author
        self.category = category

    def __str__(self):
        tmp = f"book name: {self.name}\nauthor: {self.author}\ncategory: {self.category}\nID: {self.id}\n"
        return tmp

