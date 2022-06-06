"""
    This file contains all the SQL query code functions
"""

import sqlite3, typing

class DB_Handler:
    def __init__(self, dbName: str, tableName: str) -> None:
        self.dbName = dbName + '.db'
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()
        self.tableName = tableName

    def createTable(self, columns: dict):
        """
            Creates a table using the columns dict
        """

        thisCols = columns.keys()   # holds the column names
        thisColsTypes = columns.values()    # holds the column types

        # works but the exact types need to typed in
        dictToList = [str(str(cols) + " " + str(types))
             for cols, types in zip(thisCols, thisColsTypes)]

        colsAndTypes = ",".join(dictToList)

        self.cursor.execute(" CREATE TABLE IF NOT EXISTS " + self.tableName + " ( " + colsAndTypes + ")")

    def updateTable(self, searchCol, searchVal, updatedCol, newValue):
        """
            Updates the a given table entry
        """
        self.cursor.execute(""" UPDATE rooms 
            SET ? = ? 
            WHERE ? = ?
            """, (updatedCol, newValue, searchCol, searchVal))
        
        self.conn.commit()

    def showTable(self):
        """
            Displays the table's contents
        """
        self.cursor.execute(" SELECT * FROM ?", (self.tableName,))
        print( self.cursor.fetchall() )

    def setPrimKey(self, colName):
        """
            Is supposed to set a column to a primary key
        """
        pass

    def getTable(self):
        """
            Gets the table entries
        """
        self.cursor.execute(" SELECT * FROM ?", (self.tableName,))
        return self.cursor.fetchall()

    def closeDB(self):
        """
            Closes off the DB connection
        """
        self.conn.close()
