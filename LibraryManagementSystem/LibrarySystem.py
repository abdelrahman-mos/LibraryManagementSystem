import bcrypt
from LibraryManagementSystem.Library.Library import Library, SearchMode
from LibraryManagementSystem.User.Member import Member
from LibraryManagementSystem.Library.Book import BookCategory
from datetime import datetime
from typing import List, TYPE_CHECKING
from LibraryManagementSystem.LibDB import LibdB

if TYPE_CHECKING:
    from LibraryManagementSystem.User.Librarian import Librarian


class LibrarySystem:
    # This acts as the system

    def _Login(self, dB: LibdB):
        usrName = input("Username: ")
        passwd = str.encode(input("password: "))
        dB.checkCredentials(usrName, passwd)
        # passwd = getpass("Password: ")

    def _hashPass(self, passwd: bytes):
        # used for hashing new passwords
        return bcrypt.hashpw(passwd, bcrypt.gensalt())

    def run(self):
        dB = LibdB()
        self._Login(dB)
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
