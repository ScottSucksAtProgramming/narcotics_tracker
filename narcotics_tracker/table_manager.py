"""Handles writing tables and columns into the SQLite3 Database."""

import sqlite3

from narcotics_tracker.database_interface import DatabaseInterface
from narcotics_tracker.persistence_interface import PersistenceInterface


class TableManager(PersistenceInterface, DatabaseInterface):
    """Writes tables and columns to the database."""

    def __init__(self, filename: str = "inventory.db") -> "TableManager":
        """Initializes the database object and sets it's connection to None.

        Validates the file name. Sets the connection to None. Sets the path to
        the database files to the data directory.

        Args:
            filename (str): the filename of the database the object will
                connect to.
        """
        _, extension = filename.split(".")
        if extension != "db":
            raise ValueError("The filename must have the extension '.db'")

        self.connection = None
        self.path = "data/"
        self._filename = filename

    def __enter__(self) -> sqlite3.Cursor:
        """Creates a connection to the database and sets self.cursor.

        Returns:
            sqlite3.cursor: The cursor object which executes sql queries.
        """
        self.connection = sqlite3.connect(self.path + self._filename)
        self.cursor = self.connection.cursor()

        return self

    def __exit__(self, type, value, traceback) -> None:
        """Closes the database connection."""
        self.connection = self.connection.close()

    def connect(self) -> sqlite3.Cursor:
        """Creates a connection to the database, returns the cursor."""
        self.connection = sqlite3.connect(self.path + self._filename)
        self.cursor = self.connection.cursor()

    def disconnect(self) -> None:
        """Closes the database connection."""
        self.connection.close()
        self.connection = None

    @property
    def filename(self) -> str:
        """Returns the filename of the database the object will connect to.

        Returns:
            str: The filename of the database file.
        """
        return self._filename

    @filename.setter
    def filename(self, filename: str) -> None:
        """Sets the filename of the database.

        If the TableManager was perviously connected to a file, the connection
        is closed and a new connection is made to the new filename.

        Args:
            filename (str): The name of the database file.
        """
        _, extension = filename.split(".")
        if extension != "db":
            raise ValueError("The filename must have the extension '.db'")

        self._filename = filename

        if self.connection != None:
            self.connect()

    def create(self, sql_query: str) -> None:
        """Writes a table to the database.

        Args:

            sql_query (str): The SQL query to write to the database. i.e.
                INSERT INTO table_name (column_name) VALUES (value)

        Example:
            CREATE TABLE IF NOT EXISTS table_name (column_one INTEGER, column_2 TEXT)
        """

        self.cursor.execute(sql_query)
        self.connection.commit()

    def read(self) -> list[str]:
        """Returns a list of all table names from the SQLite3 database.

        Returns:
            tables (list): The data returned from the query.
        """
        tables = []
        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

        self.cursor.execute(sql_query)
        data = self.cursor.fetchall()

        for table in data:
            tables.append(table[0])

        return tables

    def read_columns(self, table_name: str) -> list[str]:
        """Returns a list of all columns from the specified table.

        Args:
            table_name: The name of the table.

        Returns:
            columns (list): The data returned from the query.
        """
        if self._verify_table_exists(table_name) == False:
            raise ValueError(
                f"The specified table '{table_name}' does not exist."
            )  # Prevents sql injection.

        sql_query = """SELECT * FROM {}""".format(table_name)

        self.cursor.execute(sql_query)

        return [description[0] for description in self.cursor.description]

    def _verify_table_exists(self, table_name: str) -> bool:
        """Checks if the given table exists and returns a boolean result.

        Args:
            table_name (str): The name of the table.

        Returns:
            bool: True if the given table exists. Otherwise, False.
        """
        tables = self.read()

        if table_name in tables:
            return True

        return False

    def update(self, sql_query: str) -> None:
        """Updates a table using the ALTER TABLE statement.

        Args:
            sql_query (str): The SQL query to update the table.

        Options:
            Rename Table: ALTER TABLE table_name RENAME TO new_table_name
            Add Column: ALTER TABLE table_name ADD column_name data_type
            Rename Column: ALTER TABLE table_name RENAME COLUMN column_name
                TO new_column_name
        """
        self.cursor.execute(sql_query)
        self.connection.commit()

    def delete(self, table_name: str) -> None:
        """Deletes data from the database.

        Args:

            sql_query (str): The SQL query to delete the data. i.e.
                DELETE FROM table_name where column_name = value

            values (list): The values to be passed to the query. Optional.
        """
        if self._verify_table_exists(table_name) == False:
            raise ValueError(
                f"The specified table '{table_name}' does not exist."
            )  # Prevents sql injection.

        sql_query = """DROP TABLE IF EXISTS {}""".format(table_name)
        self.cursor.execute(sql_query)
