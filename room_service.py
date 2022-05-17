from typing import List
import sqlite3
from student import Student
import random

ROOMS = 10      # the number of rooms in the apartment

conn = sqlite3.connect('room.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS rooms (
            roomID integer PRIMARY KEY,
            numOccupants integer,
            maxOccupants integer,
            isFull integer
        ) """)

cursor.execute(" SELECT * FROM rooms ")
table_size = len(cursor.fetchall())


# checks if the table is empty, if so generate some empty objects

# print(table_size)
if table_size == 0:
    for x in range(1, ROOMS + 1):
        roomType = int(random.randrange(1, 6))
        cursor.execute("INSERT INTO rooms VALUES (?, ?, ?, ?)", (x, 0, roomType, 0))
        conn.commit()


class RoomService:

    def __init__(self) -> None:
        pass

    def find_all(self) -> List[dict]:
        cursor.execute(" SELECT * FROM rooms WHERE numOccupants < maxOccupants ")
        return cursor.fetchall()

    def reserve_room(self, room_id: str):
        """
            reserve room, by passing in room_id and student name
        """

        # check if the room is available
        cursor.execute(""" SELECT * FROM rooms WHERE roomID = ? """, (room_id,))
        curr_room = cursor.fetchall()[0]

        # if room is full (value of 1) then throw an err
        # TODO: add an error throw statement
        if curr_room[-1] == 1:
            print("Room Full!")
            exit(-1)

        curr_room_occupants = curr_room[1]
        curr_room_max = curr_room[2]    # current room occupant limit

        # updates table if the room is full
        if curr_room_occupants == curr_room_max:
            cursor.execute(""" UPDATE rooms 
                SET isFull = ? 
                WHERE roomID = ?
                """, (1, room_id))
            conn.commit()
        else:
            # update table
            new_curr_room_occupants = curr_room[1] + 1  # increment the num of people in current room
            cursor.execute(""" UPDATE rooms 
                            SET numOccupants = ? 
                            WHERE roomID = ?
                            """, (new_curr_room_occupants, room_id))
            conn.commit()   

            return room_id  # gives the reserver the room_id for future reference

if __name__ == "__main__":
    room_service = RoomService()
    # print(room_service.find_all())

    # stu = Student("Jon", "Doe")
    room_service.reserve_room(1)
    
    conn.close()