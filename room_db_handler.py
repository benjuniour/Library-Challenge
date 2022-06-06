from db_handler import DB_Handler
from room import Room
import random
from typing import List

class ROOM_DB_Handler( DB_Handler ):
    
    def __init__(self):
        self.roomDB = DB_Handler('room', 'rooms')
        self.createTable()

    def createTable(self):
        self.roomDB.createTable({
                'roomID': 'integer', 
                'numOccupants': 'integer', 
                'maxOccupants': 'integer',
                'isFull': 'integer'
            })

    def findAllEmptyRooms(self):
        """
            Finds all empty rooms and returns the result
        """
        self.roomDB.cursor.execute(" SELECT * FROM rooms WHERE numOccupants < maxOccupants ")
        return self.roomDB.cursor.fetchall()

    def getCurrentRoom(self, room_id):
        self.roomDB.cursor.execute(""" SELECT * FROM rooms WHERE roomID = ? """, (room_id,))
        return Room(self.roomDB.cursor.fetchall()[0])

    def insertRoom(self):
        self.roomDB.cursor.execute(" SELECT * FROM rooms ")
        table_size = len(self.roomDB.cursor.fetchall())

        roomType = int(random.randrange(1, 6))
        self.roomDB.cursor.execute("INSERT INTO rooms VALUES (?, ?, ?, ?)", (table_size + 1, 0, roomType, 0))
        self.roomDB.conn.commit()

    def insertRoomRepeat(self, numOfInputs):
        for i in range(numOfInputs):
            self.insertRoom()

    def toRoomObject(self, sql_result: List[tuple]) -> List[Room]:
        roomList = []
        for sql_tuple in sql_result:
            roomList.append(Room(sql_tuple))

        return roomList
