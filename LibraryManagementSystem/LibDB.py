from enum import Enum
from typing import List, TYPE_CHECKING
from LibraryManagementSystem.User.Librarian import Librarian
from LibraryManagementSystem.User.Member import Member
import bcrypt


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

    def checkCredentials(self, userName: str, passwd: bytes):
        tmp = self._getUser(userName)
        if tmp:
            usr, permission = tmp[0]
            if usr.checkpasswd(passwd):
                return usr.onLogin(), usr, permission
        print("Username or Password is wrong")
        return False, None, Permissions.NO_PERMISSION

    def listMembers(self):
        pass

    def _getUser(self, userName: str):
        usr = [(usr, Permissions.LIBRARIAN) for usr in self._LIBRARIANS if userName == usr.userName]
        if not usr:
            usr = [(usr, Permissions.MEMBER) for usr in self._MEMBERS if userName == usr.userName]
        return usr

    def getUserNames(self):
        usernames = [user.userName for user in self._MEMBERS]
        return usernames
