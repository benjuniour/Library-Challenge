"""
    This file contains the Room Object and its methods
"""

import typing

class Room:
    """
        Room Object -> takes in a tuple of data
    """

    # TODO: make room have setters instead of feeding a tuple
    # let the constructor take in values if a list isn't passed in, 
    def __init__(self, dataTuple: tuple) -> None:
        self.roomID = int(dataTuple[0])
        self.numOccupants = int(dataTuple[1])
        self.maxOccupants = int(dataTuple[2])
        self.isRoomFull = int(dataTuple[-1])

    def getRoomID(self) -> int:
        return self.roomID

    def getNumOccupants(self) -> int:
        return self.numOccupants

    def getOccupantMax(self) -> int:
        return self.maxOccupants

    def isFull(self) -> bool:
        return True if self.isRoomFull == 1 else False