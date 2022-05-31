from typing import List
import sqlite3
from student import Student
from room import Room
import random

from db_handler import DB_Handler

ROOMS = 10      # the number of rooms in the apartment

roomDB = DB_Handler('room', 'rooms')
roomDB.createTable({
                'roomID': 'integer', 
                'numOccupants': 'integer', 
                'maxOccupants': 'integer',
                'isFull': 'integer'
            })

class RoomService:

    def __init__(self) -> None:
        pass

    # make a get all in DB_Handler 
    def find_all(self) -> List[dict]:
        roomDB.cursor.execute(" SELECT * FROM rooms WHERE numOccupants < maxOccupants ")
        return roomDB.cursor.fetchall()

    def reserve_room(self, room_id: str):
        """
            reserve room, by passing in room_id and student name
        """

        # check if the room is available

        # TODO: make a function to map to SQL statements
        # e.g UPDATE_ROOMS(column name: str); then change the specified
        roomDB.cursor.execute(""" SELECT * FROM rooms WHERE roomID = ? """, (room_id,))
        currRoom = Room(roomDB.cursor.fetchall()[0])

        # TODO: create an object to handle future operation
        isTableEmpty = currRoom.isFull()

        # if room is full (value of 1) then throw an err
        # TODO: add an error throw statement

        # isFull = 
        if currRoom.isFull():
            print("Room Full!")
            exit(-1)

        curr_room_occupants = currRoom.getNumOccupants()
        curr_room_max = currRoom.getOccupantMax()    # current room occupant limit

        # updates table if the room is full
        if curr_room_occupants == curr_room_max:
            roomDB.cursor.execute(""" UPDATE rooms 
                SET isFull = ? 
                WHERE roomID = ?
                """, (1, room_id))
            roomDB.conn.commit()
        else:
            # update table
            new_curr_room_occupants = currRoom.getNumOccupants() + 1  # increment the num of people in current room
            roomDB.cursor.execute(""" UPDATE rooms 
                            SET numOccupants = ? 
                            WHERE roomID = ?
                            """, (new_curr_room_occupants, room_id))
            roomDB.conn.commit()   

            return room_id  # gives the reserver the room_id for future reference

    def toRoomObject(self, sql_result: List[tuple]) -> List[Room]:
        roomList = []
        for sql_tuple in sql_result:
            roomList.append(Room(sql_tuple))

        return roomList

    def insertRoom(self):
        roomDB.cursor.execute(" SELECT * FROM rooms ")
        table_size = len(roomDB.cursor.fetchall())

        roomType = int(random.randrange(1, 6))
        roomDB.cursor.execute("INSERT INTO rooms VALUES (?, ?, ?, ?)", (table_size + 1, 0, roomType, 0))
        roomDB.conn.commit()

if __name__ == "__main__":
    room_service = RoomService()
    # print(room_service.find_all())

    # stu = Student("Jon", "Doe")
    room_service.insertRoom()
    room_service.insertRoom()
    room_service.insertRoom()

    room_service.reserve_room(1)
    
    roomDB.conn.close()