from typing import List, TYPE_CHECKING
from LibraryManagementSystem.User.Librarian import Librarian
from LibraryManagementSystem.User.Member import Member
import bcrypt


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
        usr = self._getUser(userName)
        if usr:
            if usr[0].checkpasswd(passwd):
                return usr[0].onLogin()
        print("Username or Password is wrong")
        return False

    def _getUser(self, userName: str):
        usr = [usr for usr in self._LIBRARIANS if userName == usr.userName]
        if not usr:
            usr = [usr for usr in self._MEMBERS if userName == usr.userName]
        return usr
