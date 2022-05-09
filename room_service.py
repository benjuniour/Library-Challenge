from typing import List
import sqlite3
from student import Student

ROOMS = 10      # the number of rooms in the apartment

conn = sqlite3.connect('room.db')

cursor = conn.cursor()

# cursor.execute(""" CREATE TABLE rooms (
#             roomNum integer PRIMARY KEY,
#             type text,
#             occupant text
#         ) """)

# for x in range(1, ROOMS + 1):
#     cursor.execute("INSERT INTO rooms VALUES (?, ?)", (x, ''))
#     conn.commit()


class RoomService:

    def __init__(self) -> None:
        pass

    def find_all(self) -> List[dict]:
        cursor.execute(" SELECT * FROM rooms WHERE occupant = ''")
        return cursor.fetchall()

    def reserve_room(self, room_id: str, stu):
        """
            reserve room, by passing in room_id and student name

            How do I pass the Student's details into this or do I just say
            it's taken
        """
        student_name = repr(stu)
        cursor.execute(" UPDATE rooms SET occupant = :name WHERE roomNum = :room_id", {'name': student_name, 'room_id': room_id})
        conn.commit()

if __name__ == "__main__":
    room_service = RoomService()
    print(room_service.find_all())

    # stu = Student("Jon", "Doe")
    # room_service.reserve_room(1, stu)
    
    conn.close()