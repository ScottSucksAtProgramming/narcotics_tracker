"""Contains the Database class."""

import sqlite3

# from narcotics_tracker import medication
from narcotics_tracker.builders import builder


class Database:
    """Interacts directly with the database."""

    def __init__(self) -> None:
        """Initializes the database object and sets connection to None."""
        self.database_connection = None

    def connect(self, database_file):
        """Creates a connection to the database.

        Args:
            database_file (str): The database file located in the data/
                directory."""

        try:
            self.database_connection = sqlite3.connect("data/" + database_file)
        except sqlite3.Error as e:
            print(e)

        return self.database_connection

    def create_table(self, sql_query):
        """Creates a table in the database.

        Args:
            sql_query (str): The SQL query to create the table. i.e.
                "CREATE TABLE table_name (column_name column_type)"
        """

        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)

    def get_tables(self, sql_query, table_name: list[str]):
        """Returns a list of tables in the database.

        Args:
            sql_query (str): The SQL query to read from the database. i.e.
                SELECT * FROM table_name

            table_name (list[str]): The name of the table to read from. Must
                be provided as a list.

        """

        cursor = self.database_connection.cursor()
        cursor.execute(sql_query, table_name)
        return cursor.fetchall()

    def get_columns(self, sql_query):
        """Returns the column names from a table.

        Args:
            sql_query (str): The SQL query to read from the database. i.e.
                SELECT * FROM sqlite_master WHERE type = 'table' AND name = (?)
        """
        cursor = self.database_connection.cursor()
        columns = cursor.execute(sql_query)

        return columns.description

    def delete_table(self, sql_query):
        """Deletes a table from the database.

        Args:
            sql_query (str): The SQL query to delete the table. i.e. DROP
                TABLE IF EXISTS table_name"""

        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)
        self.database_connection.commit()

    def update_table(self, sql_query):
        """Updates a table using the ALTER TABLE statement.

        Args:
            sql_query (str): The SQL query to update the table.

        Options:
            Rename Table: ALTER TABLE table_name RENAME TO new_table_name
            Add Column: ALTER TABLE table_name ADD column_name data_type
            Rename Column: ALTER TABLE table_name RENAME COLUMN column_name
                TO new_column_name
        """

        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)
        self.database_connection.commit()

    def read_data(self, sql_query: str, values=None) -> list:
        """Reads from the database.

        Args:
            sql_query (str): The SQL query to read from the database. i.e.
                SELECT * FROM table_name
        """

        cursor = self.database_connection.cursor()
        if values is None:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, values)
        return cursor.fetchall()

    def write_data(self, sql_query, values):
        """Writes to the database.

        Args:
            sql_query (str): The SQL query to write to the database. i.e.
                INSERT INTO table_name (column_name) VALUES (value)"""

        cursor = self.database_connection.cursor()
        cursor.execute(sql_query, values)
        self.database_connection.commit()

    @staticmethod
    def created_date_is_none(object) -> bool:
        """Utility functions which returns true if the created date is none.

        Args:
            object (Object): The object which is being tested.

        Returns:
            bool: Returns True if the created date is None.
        """

        if object.created_date is None:
            return True
        else:
            return False
