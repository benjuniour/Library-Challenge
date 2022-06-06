"""
    This file contains the Book Object and its methods
"""

import typing

class Book:

    def __init__(self, dataTuple: tuple):
        self.bookID = int(dataTuple[0])
        self.owner = dataTuple[-1]

    def getBookID(self) -> int:
        return self.bookID

    def getOwner(self) -> str:
        return self.owner