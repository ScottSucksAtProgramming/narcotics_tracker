"""Contains the Database class."""

import sqlite3


class Database:
    """Reads and writes to the inventory database."""

    def __init__(self):
        """Initializes the database object and sets connection to None."""
        self.database_connection = None

    def connect(self, database_file):
        """Connects to the database file.

        Args:
            database_file (str): The name of the database file. (File must be
                in the data/ directory.)"""
        self.database_connection = sqlite3.connect(
            "narcotics_tracker/data/" + database_file
        )

    def create_table(self, sql_query):
        """Creates a table in the database.

        Args:
            sql_query (str): The SQL query to create the table. i.e.
                "CREATE TABLE table_name (column_name column_type)"
        """
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)

    # Todo: Add Method to update a table.

    def read_database(self, sql_query):
        """Reads from the database.

        Args:
            sql_query (str): The SQL query to read from the database. i.e.
                SELECT * FROM table_name
        """
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()

    def delete_table(self, sql_query):
        """Deletes a table from the database."""
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)

    def write_data(self, sql_query, values):
        """Writes to the database.

        Args:
            sql_query (str): The SQL query to write to the database. i.e.
                INSERT INTO table_name (column_name) VALUES (value)"""
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query, values)
        self.database_connection.commit()
