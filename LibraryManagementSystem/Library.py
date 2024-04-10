import os
from datetime import datetime
from LibraryManagementSystem.Book import Book, BookCategory
from LibraryManagementSystem.Member import Member
from typing import List


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, bookName: str, author: str, category: BookCategory, publicationDate: datetime, num: int = 1):
        book: Book = Book(name=bookName, author=author, category=category, publicationDate=publicationDate, num=num)
        # print(book)
        self.books.append(book)

    # def search_by_name(self, bookName: str) -> List[str]:
    #     # get a list with book names
    #     bookNames = [book.name for book in self.books]
    #     startWith = [book for book in bookNames if book.startswith(bookName)]
    #     includes = [book for book in bookNames if bookName in book]
    #     # return the names starting with the string first
    #     out = startWith + [book for book in includes if book not in startWith]
    #     return out

    def search_by_name(self, bookName: str) -> List[Book]:
        books = [book for book in self.books if bookName in book.name]
        booksStartWith = [book for book in books if book.name.startswith(bookName)]
        out = (sorted(booksStartWith, key=lambda x: x.name) +
               sorted([book for book in books if book not in booksStartWith],
                      key=lambda x: x.name))

        return out

    def search_by_author(self, authorName: str) -> List[Book]:
        pass

    def search_by_category(self, category: BookCategory) -> List[Book]:
        pass

    def search_by_publication_date(self, publicationDate: datetime) -> List[Book]:
        pass

    @staticmethod
    def run():
        lib: Library = Library()
        lib.add_book('Kafara', "who?", BookCategory.SCIENCE, datetime.strptime("2018/7/25", "%Y/%m/%d"))
        lib.add_book('Yasser Kafka', "Yasser Murakami", BookCategory.FICTION, datetime.strptime("2017/7/5", "%Y"
                                                                                                            "/%m/%d"))
        lib.add_book('Mohamed Kafka', "Ahmed Murakami", BookCategory.FICTION, datetime.strptime("2017/7/5", "%Y"
                                                                                                            "/%m/%d"))
        lib.add_book('Kafka on The Shore', "Haruki Murakami", BookCategory.FICTION, datetime.strptime("2017/7/5", "%Y"
                                                                                                                  "/%m/%d"))

        mem: Member = Member('Ahmed')
        mem2: Member = Member('Mohamed')
        mem.borrowBook(lib.books[0])
        mem2.borrowBook(lib.books[0])
        lib.search_by_name('Ka')
        lib.search_by_name('Kafk')
