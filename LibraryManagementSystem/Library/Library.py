import uuid
from datetime import datetime
from LibraryManagementSystem.Library.Book import Book, BookCategory, catMap
from typing import List, Union, Callable
from enum import Enum
import sys


class SearchMode(Enum):
    # search mode to get rid of code redundancy.
    TITLE = 1
    AUTHOR = 2
    CATEGORY = 3
    PUBLICATION_DATE = 4


class Library:

    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, bookName: str, author: str, category: BookCategory, publicationDate: datetime, num: int = 1):
        book: Book = Book(title=bookName, author=author, category=category, publicationDate=publicationDate, num=num)
        # print(book)
        self.books.append(book)

    def list_books(self):
        i = 1
        for book in self.books:
            textOut = (f'{i}) Title: {book.title}, Author: {book.author}, Category: {catMap[book.category]}, '
                       f'Publication Date: {book.publicationDate.strftime("%d/%m/%Y")}, Copies: {book.num}, ID: {book.id}')
            print(textOut)
            i += 1
        print("press enter to continue: ")
        sys.stdin.read(1)

    def remove_book(self, bookID: uuid.UUID):
        book_to_remove = [book for book in self.books if bookID == book.id][0]
        self.books.remove(book_to_remove)
        print("Removed book successfully")
        print("press enter to continue: ")
        sys.stdin.read(1)

    def edit_book(self, bookID: uuid.UUID):
        pass

    # def search_by_name(self, bookName: str) -> List[str]:
    #     # get a list with book names
    #     bookNames = [book.name for book in self.books]
    #     startWith = [book for book in bookNames if book.startswith(bookName)]
    #     includes = [book for book in bookNames if bookName in book]
    #     # return the names starting with the string first
    #     out = startWith + [book for book in includes if book not in startWith]
    #     return out

    def search(self, searchText: Union[str, BookCategory, datetime], mode: SearchMode = SearchMode.TITLE) -> List[Book]:
        # change search key depending on search mode
        if mode == SearchMode.TITLE:
            searchKey: Callable[[Book], str] = lambda x: x.title
        elif mode == SearchMode.AUTHOR:
            searchKey: Callable[[Book], str] = lambda x: x.author
        elif mode == SearchMode.CATEGORY:
            searchKey: Callable[[Book], BookCategory] = lambda x: x.category
        elif mode == SearchMode.PUBLICATION_DATE:
            searchKey: Callable[[Book], datetime] = lambda x: x.publicationDate
        else:
            print("search mode is not possible")
            raise ValueError

        # for a text input
        if mode == SearchMode.TITLE or mode == SearchMode.AUTHOR:
            books = [book for book in self.books if searchText in searchKey(book)]

        # for a non-text input (date or category
        else:
            books = [book for book in self.books if searchText == searchKey(book)]
        # booksStartWith = [book for book in books if book.title.startswith(searchText)]
        # out = (sorted(booksStartWith, key=lambda x: x.title) +
        #        sorted([book for book in books if book not in booksStartWith],
        #               key=lambda x: x.title))

        out = sorted(books, key=lambda x: x.title)

        return out

    # This will cause redundant code, need to be refactored
    # def search_by_author(self, authorName: str) -> List[Book]:
    #     pass
    #
    # def search_by_category(self, category: BookCategory) -> List[Book]:
    #     pass
    #
    # def search_by_publication_date(self, publicationDate: datetime) -> List[Book]:
    #     pass


