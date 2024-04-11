import uuid
from enum import Enum
from typing import List, Tuple, TYPE_CHECKING, Union
from datetime import datetime

if TYPE_CHECKING:
    from LibraryManagementSystem.User.Member import Member
    from LibraryManagementSystem.User.User import User


class BookCategory(Enum):
    SCIENCE = 1
    FICTION = 2
    LAW = 3
    UNCATEGORIZED = 4


catMap = {
    BookCategory.SCIENCE: "Science",
    BookCategory.FICTION: "Fiction",
    BookCategory.LAW: "Law",
    BookCategory.UNCATEGORIZED: "Uncategorized"
}


class Book:
    def __init__(self, title: str, author: str, category: BookCategory, publicationDate: datetime, num: int = 1):

        # Public attributes
        self.id = uuid.uuid4()
        self.title = title
        self.author = author
        self.category = category
        self.publicationDate = publicationDate
        self.num = num

        # Private attributes
        self._numAvailable = num
        self._borrowedBy: List[Tuple["Member", datetime]] = []
        self._reservedBy: List[Tuple["Member", datetime]] = []

    def borrowBook(self, borrowBy: Union["Member", "User"]):
        if self._numAvailable > 0:
            self._numAvailable -= 1
            date = datetime.now()
            self._borrowedBy.append((borrowBy, datetime.now()))
            return True, date
        return False, None

    def reserveBook(self, reserveBy: "Member"):
        date = datetime.now()
        # print(date)
        self._reservedBy.append((reserveBy, date))
        # print(f"Book \"{self.title}\" reserved by {reserveBy.name} at {date.strftime("%H:%M, %d/%m/%Y")}")
        return date

    def returnBook(self, returnedBy: "Member"):
        if returnedBy in self._borrowedBy:
            self._borrowedBy.remove(returnedBy)
            self._numAvailable += 1

    # def __lt__(self, other):
    #     return self.name < other.name

    # def __str__(self):
    #     tmp = f"book name: {self.name}\nauthor: {self.author}\ncategory: {self.category}\nID: {self.id}\n"
    #     return tmp
