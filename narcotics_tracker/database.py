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
    """Sends SQL statements to the database, returns a cursor with results.

    Methods:
        create_table: Adds a table to the database using the given name and
            column info.
        add: Adds a row to the given table using the given data.
        delete: Deletes a row from the given table using the given criteria.
        select: Returns a cursor containing data for the given table and
            criteria.


    """

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

    def create_table(self, table_name: str, column_info: dict[str]):
        """Adds a table to the database using the given name and column info.

        Does nothing if the table already exists.

        Args:
            table_name (str): The name of the table.
            columns (dict[str]): A dictionary mapping column names to its
                datatype and restraints.
        """
        columns_with_details = [
            f" {column_name} {details}" for column_name, details in columns.items()
        ]

        columns_with_details = ", ".join(columns_with_details)

        sql_statement = (
            f"""CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_details});"""
        )

        self._execute(sql_statement)

    def add(self, table_name: str, data: dict[str]):
        """Adds a row to the given table using the given data.

        Args:
            table_name (str): The name of the table.
            data (dict[str]): A dictionary mapping column names to the values.
        """
        placeholders = ", ".join("?" for key in data.keys())
        column_names = ", ".join(data.keys())
        sql_statement = (
            f"""INSERT INTO {table_name} ({column_names}) VALUES ({placeholders});"""
        )

        column_values = tuple(data.values())

        self._execute(sql_statement, column_values)

    def delete(self, table_name: str, criteria: dict[str]):
        """Deletes a row from the given table using the given criteria.

        Args:
            table_name (str): The name of the table.
            criteria (dict[str]): A dictionary mapping column names to values
                used to select rows for deletion.
        """
        placeholders = [f"{column} = ?" for column in criteria.keys()]
        criteria_columns = " AND ".join(placeholders)

        sql_statement = f"""DELETE FROM {table_name} WHERE {criteria_columns};"""

        criteria_values = tuple(criteria.values())

        self._execute(sql_statement, criteria_values)

    def select(
        self, table_name: str, criteria: dict[str] = {}, order_by: str = None
    ) -> sqlite3.Cursor:
        """Returns a cursor containing data for the given table and criteria.

        Args:
            table_name (str): The name of the table.
            criteria (dict[str]): A dictionary mapping column names to values
                used to select rows from which to pull the data. Optional.
            order_by (str): The name of the column by which to order the data.
                Optional.

        Returns:
            sqlite3.Cursor: A cursor contains the returned data.
        """
        sql_query = f"""SELECT * FROM {table_name}"""

        if criteria:
            placeholders = [f"{column} = ?" for column in criteria.keys()]
            criteria_columns = " AND ".join(placeholders)
            sql_query += f" WHERE {criteria_columns}"

        if order_by:
            sql_query += f" ORDER BY {order_by}"

        return self._execute(sql_query, tuple(criteria.values()))
