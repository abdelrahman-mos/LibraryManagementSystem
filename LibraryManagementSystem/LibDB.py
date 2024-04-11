import uuid
from enum import Enum
from typing import List, TYPE_CHECKING
from LibraryManagementSystem.User.Librarian import Librarian
from LibraryManagementSystem.User.Member import Member
import bcrypt, sys


class Permissions(Enum):
    LIBRARIAN = 1
    MEMBER = 2
    NO_PERMISSION = 3


class LibdB:
    # The Library Database
    # we will add a default Librarian
    _LIBRARIANS: List["Librarian"] = [Librarian(name='Abdelrahman', userName='abdelrahman_mos',
                                                passwd=bcrypt.hashpw(b'123456', bcrypt.gensalt()))]
    _MEMBERS: List["Member"] = []

    def addMember(self, member: "Member"):
        # should be triggered from a Librarian class
        self._MEMBERS.append(member)

    def removeMember(self, memberID: uuid.UUID):
        member_to_remove = [member for member in self._MEMBERS if memberID == member.id][0]
        self._MEMBERS.remove(member_to_remove)

    def checkCredentials(self, userName: str, passwd: bytes):
        tmp = self._getUser(userName)
        if tmp:
            usr, permission = tmp[0]
            if usr.checkpasswd(passwd):
                return usr.onLogin(), usr, permission
        print("Username or Password is wrong")
        return False, None, Permissions.NO_PERMISSION

    def listMembers(self):
        i = 1
        for member in self._MEMBERS:
            textOut = (f'{i}) Name: {member.name}, ID: {member.id}, Username: {member.userName}, Borrowed books: {member
                       .borrowedBooks}, Reserved books: {member.reservedBooks}')
            print(textOut)
            i += 1
        print("press enter to continue: ")
        sys.stdin.read(1)

    def _getUser(self, userName: str):
        usr = [(usr, Permissions.LIBRARIAN) for usr in self._LIBRARIANS if userName == usr.userName]
        if not usr:
            usr = [(usr, Permissions.MEMBER) for usr in self._MEMBERS if userName == usr.userName]
        return usr

    def getUserNames(self):
        usernames = [user.userName for user in self._MEMBERS]
        return usernames

    def fetchMembers(self):
        return self._MEMBERS
