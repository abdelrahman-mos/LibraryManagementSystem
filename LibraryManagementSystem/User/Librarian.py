import sys
import uuid
from datetime import datetime
from typing import List, Tuple, TYPE_CHECKING
from LibraryManagementSystem.User.User import User
from LibraryManagementSystem.Library.Library import Library
from LibraryManagementSystem.Library.Book import BookCategory
from LibraryManagementSystem.Library.Book import Book


class Librarian(User):

    def __init__(self, name: str, userName: str, passwd: bytes):
        super().__init__(name, userName, passwd)
        # self.borrowedBooks: List[Tuple["Book", datetime]] = []
        # self.reservedBooks: List["Book"] = []
        # self._canBorrow = True

    def _getBookCat(self):
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

        return bookCat

    def addBook(self, lib: Library):
        bookName = input("Book Title: ")
        author = input("Author: ")

        bookCat = self._getBookCat()

        pubDate = input("Publication Date (dd/mm/yyyy): ")
        publicationDate = datetime.strptime(pubDate, "%d/%m/%Y")

        numCopies = int(input("number of copies added: "))

        lib.add_book(bookName=bookName, author=author, category=bookCat, publicationDate=publicationDate, num=numCopies)

    def removeBook(self, lib: Library):
        bookID = input('Enter book ID to remove: ')
        bookID = uuid.UUID(bookID)
        lib.remove_book(bookID)

    def editBook(self, lib: Library):
        bookID = input('Enter book ID to edit: ')
        bookID = uuid.UUID(bookID)
        bookToEdit = [book for book in lib.books if bookID == book.id][0]
        if not bookToEdit:
            print("Book ID is incorrect")
            return
        textOut = """What do you want to edit?
        1) Title.
        2) Author.
        3) Book category.
        4) Publication date.
        5) Number of copies.
        6) Cancel.
        """
        print(textOut)
        prompt = input("your input: ")
        while prompt not in ['1', '2', '3', '4', '5', '6']:
            print("Wrong input")
            prompt = input("your input: ")
        if prompt == '1':
            self._editBookTitle(bookToEdit)
        elif prompt == '2':
            self._editBookAuthor(bookToEdit)
        elif prompt == '3':
            self._editBookCategory(bookToEdit)
        elif prompt == '4':
            self._editBookPublicationDate(bookToEdit)
        elif prompt == '5':
            self._editBookNumberOfCopies(bookToEdit)
        elif prompt == '6':
            return

    def _editBookTitle(self, bookToEdit: Book):
        newTitle = input("Enter new Title: ")
        bookToEdit.title = newTitle
        print("Book title edited successfully, press enter to continue: ")
        sys.stdin.read(1)

    def _editBookAuthor(self, bookToEdit: Book):
        newAuthor = input("Enter new Author: ")
        bookToEdit.author = newAuthor
        print("Book author edited successfully, press enter to continue: ")
        sys.stdin.read(1)

    def _editBookCategory(self, bookToEdit: Book):
        bookCat = self._getBookCat()
        bookToEdit.category = bookCat
        print("Book category edited successfully, press enter to continue: ")
        sys.stdin.read(1)

    def _editBookPublicationDate(self, bookToEdit: Book):
        newPubDate = input("New publication Date (dd/mm/yyyy): ")
        publicationDate = datetime.strptime(newPubDate, "%d/%m/%Y")
        bookToEdit.publicationDate = publicationDate
        print("Book publication date edited successfully, press enter to continue: ")
        sys.stdin.read(1)

    def _editBookNumberOfCopies(self, bookToEdit: Book):
        newNumCopies = int(input("New number of copies: "))
        bookToEdit.num = newNumCopies
        print("Book number of copies edited successfully, press enter to continue: ")
        sys.stdin.read(1)

    def borrowBook(self, book: "Book"):
        pass

    def reserveBook(self, book: "Book"):
        pass

    def addMemberAccount(self):
        pass

    def removeMemberAccount(self):
        pass
