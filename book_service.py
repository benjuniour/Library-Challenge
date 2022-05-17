from typing import List
import sqlite3
from student import Student

# def makeDB():
BOOKS = 10

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS books (
            book_id integer PRIMARY KEY,
            owner text
        ) """)

cursor.execute(" SELECT * FROM books ")
table_size = len(cursor.fetchall())

# checks if the table is empty, if so generate some empty objects

# print(table_size)
if table_size == 0:
    for x in range(1, BOOKS + 1):
        cursor.execute("INSERT INTO books VALUES (?, ?)", (x, ''))
        conn.commit()

class BookService:

    def __init__(self) -> None:
        pass

    def find_all(self) -> List[dict]: 
        cursor.execute(" SELECT * FROM books WHERE owner = ''")
        return cursor.fetchall()

    def checkout_book(book_id: str, student_name: str):
        cursor.execute(" UPDATE books SET owner = :name WHERE book_id = :bookID", {'name': student_name, 'bookID': book_id})
        conn.commit()

if __name__ == "__main__":
    book_service = BookService()
    print(book_service.find_all())

    conn.close()
