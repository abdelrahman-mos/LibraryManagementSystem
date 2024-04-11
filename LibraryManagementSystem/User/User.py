import uuid, sys
from typing import TYPE_CHECKING, List
import bcrypt
from datetime import datetime
from LibraryManagementSystem.Library.Library import Library, SearchMode
from LibraryManagementSystem.Library.Book import BookCategory
from LibraryManagementSystem.Library.Book import catMap

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

    def _getBookByID(self, lib: "Library"):
        bookID = input('Enter book ID to checkout: ')
        try:
            bookID = uuid.UUID(bookID)
            bookToReturn = [book for book in lib.books if bookID == book.id][0]
        except ValueError:
            print("Book ID is incorrect")
            return None

        if not bookToReturn:
            print("Book ID is incorrect")
            return None
        return bookToReturn

    def onLogin(self):
        self._isLoggedIn = True
        return True

    def onLogout(self):
        self._isLoggedIn = False
        return True

    def checkpasswd(self, passwd: bytes):
        return bcrypt.checkpw(passwd, self._passwd)

    def borrowBook(self, lib: "Library"):
        pass

    def reserveBook(self, lib: "Library"):
        pass

    def _listBooks(self, books: List["Book"]):
        i = 1
        for book in books:
            textOut = (f'{i}) Title: {book.title}, Author: {book.author}, Category: {catMap[book.category]}, '
                       f'Publication Date: {book.publicationDate.strftime("%d/%m/%Y")}, Copies: {book
                       .num}, ID: {book.id}')
            print(textOut)
            i += 1
        print("press enter to continue: ")
        sys.stdin.read(1)

    def searchBook(self, lib: Library):
        textOut = """How do you want to search?
        1) Title
        2) Author
        3) Category
        4) Publication Date
        5) Cancel
        """
        print(textOut)
        prompt = input("your input: ")
        while prompt not in ['1', '2', '3', '4', '5']:
            print("Wrong input")
            prompt = input("your input: ")
        if prompt == '5':
            return

        prompt_map = {
            '1': SearchMode.TITLE,
            '2': SearchMode.AUTHOR,
            '3': SearchMode.CATEGORY,
            '4': SearchMode.PUBLICATION_DATE
        }
        searchMode = prompt_map[prompt]
        if searchMode == SearchMode.TITLE or searchMode == SearchMode.AUTHOR:
            searchText = input("Search for: ")
        elif searchMode == SearchMode.CATEGORY:
            searchText = self._getBookCat()
        else:
            pubDate = input("Publication Date (dd/mm/yyyy): ")
            searchText = datetime.strptime(pubDate, "%d/%m/%Y")
        self._listBooks(lib.search(searchText, searchMode))
