"""Contains the DatabaseWriter class."""

import sqlite3


class DatabaseWriter:
    """Reads and writes to the inventory database."""

    def __init__(self):
        """Initializes the database connection."""
        self.database_connection = None

    def connect(self, database_file_path):
        """Connects to the database."""
        self.database_connection = sqlite3.connect(database_file_path)

    def create_table(self, sql_query):
        """Writes to the database."""
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)

    def update_table(self, sql_query):
        """Writes to the database."""
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)

    def read_database(self, sql_query):
        """Reads from the database."""
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()

    def delete_table(self, sql_query):
        """Deletes a table from the database."""
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)
