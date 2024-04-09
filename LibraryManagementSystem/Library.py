import os
from LibraryManagementSystem.Book import Book
from LibraryManagementSystem.Book import BookCategory


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, bookName: str, author: str, category: BookCategory):
        book: Book = Book(name=bookName, author=author, category=category)
        print(book)
        self.books.append(book)

    @staticmethod
    def run():
        lib: Library = Library()
        lib.add_book('idek', "who?", BookCategory.SCIENCE)

