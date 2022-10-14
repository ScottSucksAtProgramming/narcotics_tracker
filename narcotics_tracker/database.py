"""This module is responsible for communicating with the SQlite database.

All information about controlled substance medications and their activities 
are saved within an SQLite3 database. This module handles handles storing and 
retrieving information in the database tables and functions as the receiver 
for database commands.

Classes:

Functions:

Exceptions:
"""

import sqlite3


class DatabaseManager:
    """Sends SQL statements to the database, returns a cursor with results."""

    def __init__(self, filename: str) -> None:
        """Initialize the DatabaseManager and stores the database file.

        If the database files doe not exist, it will be created.

        Args:
            filename (str): The filename of the database file.
        """
        self.connection = None
        self.filename = filename

    def __enter__(self) -> sqlite3.Connection:
        """Sets the connection to the database file as a instance variable."""
        self.connection = sqlite3.connect("data/" + self.filename)

    def __exit__(self, type, value, traceback) -> None:
        """Closes the database connection."""
        self.connection.close()

    def _execute(self, sql_statement: str, values: tuple[str] = None) -> sqlite3.Cursor:
        """Executes the sql statement, returns a cursor with any results."""
        cursor = self.connection.cursor()
        cursor.execute(sql_statement, values or [])

        return cursor
