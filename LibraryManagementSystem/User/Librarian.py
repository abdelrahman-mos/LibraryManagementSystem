from datetime import datetime
from typing import List, Tuple, TYPE_CHECKING
from LibraryManagementSystem.User.User import User
from LibraryManagementSystem.Library.Library import Library
from LibraryManagementSystem.Library.Book import BookCategory
if TYPE_CHECKING:
    from LibraryManagementSystem.Library.Book import Book


class Librarian(User):

    def __init__(self, name: str, userName: str, passwd: bytes):
        super().__init__(name, userName, passwd)
        # self.borrowedBooks: List[Tuple["Book", datetime]] = []
        # self.reservedBooks: List["Book"] = []
        # self._canBorrow = True

    def addBook(self, lib: Library):
        bookName = input("Book Title: ")
        author = input("Author: ")
        textOut = """Book Category
        1) Science.
        2) Fiction.
        3) Law
        4) Uncategorized
        """
        print(textOut)
        cat = input("Book Category: ").strip().lower()
        while cat not in ['1', '2', '3']:
            print("Wrong Category")
            cat = input("Book Category: ").strip().lower()

        if cat == '1':
            bookCat = BookCategory.SCIENCE
        elif cat == '2':
            bookCat = BookCategory.FICTION
        elif cat == '3':
            bookCat = BookCategory.LAW
        else:
            bookCat = BookCategory.UNCATEGORIZED

        pubDate = input("Publication Date (dd/mm/yyyy): ")
        publicationDate = datetime.strptime(pubDate, "%d/%m/%Y")

        numCopies = int(input("number of copies added: "))

        lib.add_book(bookName=bookName, author=author, category=bookCat, publicationDate=publicationDate, num=numCopies)

    def removeBook(self):
        pass

    def editBook(self):
        pass

    def borrowBook(self, book: "Book"):
        pass

    def reserveBook(self, book: "Book"):
        pass

    def addMemberAccount(self):
        pass

    def removeMemberAccount(self):
        pass
