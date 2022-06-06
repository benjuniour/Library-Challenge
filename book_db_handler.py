from db_handler import DB_Handler
import random
from book import Book
from typing import List

class BOOK_DB_Handler( DB_Handler ):
    
    def __init__(self):
        self.bookDB = DB_Handler('book', 'books')
        self.createTable()

    def createTable(self):

        self.bookDB.createTable({
            'book_id': 'integer',
            'owner': 'text'
        })

    def findAllUnRentedBooks(self):
        """
            Finds all books not checked out and returns sql result
        """
        self.bookDB.cursor.execute(" SELECT * FROM books WHERE owner = ''")
        return self.bookDB.cursor.fetchall()

    def getCurrentBook(self, book_id):
        self.bookDB.cursor.execute(""" SELECT * FROM books WHERE bookID = ? """, (book_id,))
        return Book(self.bookDB.cursor.fetchall()[0])

    def insertBook(self):
        self.bookDB.cursor.execute(" SELECT * FROM books ")
        table_size = len(self.bookDB.cursor.fetchall())

        self.bookDB.cursor.execute("INSERT INTO books VALUES (?, ?)", (table_size + 1, ''))

        self.bookDB.conn.commit()

    def insertBookRepeat(self, numOfInputs):
        for i in range(numOfInputs):
            self.insertBook()

    def toBookObject(self, sql_result: List[tuple]) -> List[Book]:
        roomList = []
        for sql_tuple in sql_result:
            roomList.append(Book(sql_tuple))

        return roomList