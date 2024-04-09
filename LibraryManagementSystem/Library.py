import os
from LibraryManagementSystem.Book import Book


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Library:
    def __init__(self):
        self.name = ""
        self.books = []

    def add_book(self, bookName: str):
        book = Book(bookName)
        print(book.id)
        print(book.name)
        self.books.append(book)

    @staticmethod
    def run():
        x = Library()
        x.add_book('idek')

