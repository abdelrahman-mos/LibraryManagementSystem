import os
from LibraryManagementSystem.Book import Book, BookCategory
from LibraryManagementSystem.Member import Member


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, bookName: str, author: str, category: BookCategory, num: int = 1):
        book: Book = Book(name=bookName, author=author, category=category, num=num)
        # print(book)
        self.books.append(book)

    @staticmethod
    def run():
        lib: Library = Library()
        lib.add_book('idek', "who?", BookCategory.SCIENCE)
        mem: Member = Member('Ahmed')
        mem2: Member = Member('Mohamed')
        mem.borrowBook(lib.books[0])
        mem2.borrowBook(lib.books[0])
