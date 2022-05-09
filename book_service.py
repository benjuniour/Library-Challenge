from typing import List
import sqlite3

BOOKS = 10

conn = sqlite3.connect('books.db')

cursor = conn.cursor()

# cursor.execute(""" CREATE TABLE books (
#             book_id integer PRIMARY KEY,
#             owner text
#         ) """)

# for x in range(1, BOOKS + 1):
#     cursor.execute("INSERT INTO books VALUES (?, ?)", (x, ''))
#     conn.commit()

class BookService:

    def __init__(self) -> None:
        pass

    def find_all(self) -> List[dict]: 
        cursor.execute(" SELECT * FROM books WHERE owner = ''")
        return cursor.fetchall()

    def checkout_book(book_id: str):
        # TODO: implementation required
        pass

if __name__ == "__main__":
    book_service = BookService()
    print(book_service.find_all())

    conn.close()
