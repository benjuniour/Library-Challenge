from typing import List
import sqlite3
from student import Student
from room import Room

from room_db_handler import ROOM_DB_Handler

class RoomService:

    def __init__(self) -> None:
        self.dbHandler = ROOM_DB_Handler()

    # make a get all in DB_Handler 
    def find_all(self) -> List[dict]:
        return self.dbHandler.findAllEmptyRooms()

    def reserve_room(self, room_id: str):
        """
            reserve room, by passing in room_id and student name
        """

        currRoom = self.dbHandler.getCurrentRoom(room_id)

        # if room is full (value of 1) then throw an err
        # TODO: add an error throw statement
        isRoomEmpty = currRoom.isFull()

        if isRoomEmpty:
            print("Room Full!")
            exit(-1)

        curr_room_occupants = currRoom.getNumOccupants()
        curr_room_max = currRoom.getOccupantMax()    # current room occupant limit

        # updates table if the room is full
        if curr_room_occupants == curr_room_max:
            self.dbHandler.updateTable("isFull", 1, "roomID", room_id)
            print("Room Full! Pick Another")
        else:
            # update table
            new_curr_room_occupants = currRoom.getNumOccupants() + 1  # increment the num of people in current room
            self.dbHandler.updateTable("numOccupants", new_curr_room_occupants, "roomID", room_id)

            return room_id  # gives the reserver the room_id for future reference


if __name__ == "__main__":
    room_service = RoomService()
    roomHandler = room_service.dbHandler.roomDB

    room_service.dbHandler.insertRoomRepeat(1)

    room_service.reserve_room(1)
    
    roomHandler.closeDB()