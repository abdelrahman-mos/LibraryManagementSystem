import bcrypt
import os
from LibraryManagementSystem.Library.Library import Library, SearchMode
from LibraryManagementSystem.User.Member import Member
from LibraryManagementSystem.Library.Book import BookCategory
from datetime import datetime
from typing import List, TYPE_CHECKING
from LibraryManagementSystem.LibDB import LibdB, Permissions

if TYPE_CHECKING:
    from LibraryManagementSystem.User.Librarian import Librarian


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class LibrarySystem:
    # This acts as the system

    def __init__(self):
        self.dB = None
        self.lib = None

    def _Login(self):
        usrName = input("Username: ")
        passwd = str.encode(input("password: "))
        return self.dB.checkCredentials(usrName, passwd)
        # passwd = getpass("Password: ")

    def _hashPass(self, passwd: bytes):
        # used for hashing new passwords
        return bcrypt.hashpw(passwd, bcrypt.gensalt())

    def _librarian_interface(self, user: "Librarian"):
        outText = f"""
        Hello, {user.name}.
        1) add book.
        2) remove book.
        3) edit book.
        4) search book.
        5) list all books.
        6) add member.
        7) remove member.
        8) list all members.
        q) quit.
        """
        while True:
            cls()
            print(outText)
            prompt = input("your input: ").strip().lower()
            while prompt not in ['1', '2', '3', '4', '5', '6', '7', '8', 'q']:
                print("Wrong input")
                prompt = input("your input: ").strip().lower()

            if prompt == 'q':
                quit(0)

            # prompt_map = {
            #     '1': user.addBook,
            #     '2': user.removeBook,
            #     '3': user.editBook,
            #     '4': user.searchBook,
            #     '5': self.lib.list_books,
            #     '6': user.addMemberAccount,
            #     '7': user.removeMemberAccount,
            #     '8': self.dB.listMembers,
            # }

            # prompt_map[prompt]()
            if prompt == '1':
                user.addBook(self.lib)
            elif prompt == '2':
                user.removeBook(self.lib)
            elif prompt == '3':
                user.editBook(self.lib)
            elif prompt == '4':
                user.searchBook(self.lib)
            elif prompt == '5':
                self.lib.list_books()
            elif prompt == '6':
                user.addMemberAccount(self.dB)
            elif prompt == '7':
                user.removeMemberAccount(self.dB)
            elif prompt == '8':
                self.dB.listMembers()
            elif prompt == 'q':
                quit(0)

    def run(self):
        self.dB = LibdB()
        self.lib = Library()
        while True:
            loggedIn, user, permission = self._Login()
            while not loggedIn:
                loggedIn, user, permission = self._Login()
            if permission == Permissions.LIBRARIAN:
                self._librarian_interface(user)
            if input("x to exit: ") == 'x':
                break
        # lib: Library = Library()
        # lib.add_book('Kafara', "who?", BookCategory.SCIENCE, datetime.strptime("2018/7/25", "%Y/%m/%d"))
        # lib.add_book('Yasser Kafka', "Yasser Murakami", BookCategory.FICTION, datetime.strptime("2017/7/5", "%Y"
        #                                                                                                     "/%m/%d"))
        # lib.add_book('Mohamed Kafka', "Ahmed Murakami", BookCategory.FICTION, datetime.strptime("2017/7/5", "%Y"
        #                                                                                                     "/%m/%d"))
        # lib.add_book('Kafka on The Shore', "Haruki Murakami", BookCategory.FICTION, datetime.strptime("2017/7/5", "%Y"
        #                                                                                                           "/%m/%d"))
        #
        # mem: Member = Member('Ahmed', 'mrAhmed', b'123456')
        # mem2: Member = Member('Mohamed', 'mrAhmed', b'123456')
        # mem.borrowBook(lib.books[0])
        # mem2.borrowBook(lib.books[0])
        # x = lib.search('Ka')
        # xnames = [book.title for book in x]
        # print(xnames)
        # # date1 = datetime.strptime("2018/7/25", "%Y/%m/%d")
        # # date2 = datetime.strptime("2018/7/25", "%Y/%m/%d")
        # # print(date1 == date2)
        # x = lib.search(BookCategory.FICTION, mode=SearchMode.CATEGORY)
        # xnames = [book.title for book in x]
        # print(xnames)
