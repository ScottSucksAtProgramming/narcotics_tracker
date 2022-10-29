"""Manages Communication with the SQLite3 Database.

All information about controlled substance medications and their activities 
are stored within an SQLite3 database. This module contains the objects 
responsible for communicating with the database.

Classes:
    SQLiteManager: Sends and receives information from the SQlite database.
"""

import os
import sqlite3

from narcotics_tracker.services.datetime_manager import DateTimeManager


class SQLiteManager:
    """Sends and receives information from the SQlite database.

    Attributes:
        connection (sqlite3.Connection): The connection to the SQlite database.

        filename (str): The name of the database file.

    Methods:
        add: Adds a new row to the database.

        read: Returns a cursor containing data from the database.

        update: Updates a row in the database.

        remove: Removes a row from the database.

        create_table: Adds a table to the database.

        delete_database: Deletes the database file.
    """

    datetime = DateTimeManager()

    def __init__(self, filename: str) -> None:
        """Initialize the SQLiteManager and stores the database filename.

        If the database files doe not exist, it will be created.

        Args:
            filename (str): The filename of the database file.
        """
        self.connection = sqlite3.connect("data/" + filename)
        self.filename = filename

    def __del__(self) -> None:
        """Closes the database connection upon exiting the context manager."""
        self.connection.close()

    def add(self, table_name: str, data: dict[str]):
        """Adds a new row to the database.

        Args:
            table_name (str): Name of the table receiving the new row.

            data (dict[str]): A dictionary mapping column names to the values.
        """
        placeholders = ", ".join("?" for key in data.keys())
        column_names = ", ".join(data.keys())

        sql_statement = (
            f"""INSERT INTO {table_name} ({column_names}) VALUES ({placeholders});"""
        )

        column_values = tuple(data.values())

        self._execute(sql_statement, column_values)

    def _check_created_date(self, data: dict[str, any]) -> dict[str, any]:
        if data["created_date"] is None:
            timestamp = self.datetime.return_current_datetime()
            data["created_date"] = timestamp
            data["modified_date"] = timestamp
        return data

    def read(
        self, table_name: str, criteria: dict[str] = {}, order_by: str = None
    ) -> sqlite3.Cursor:
        """Returns a cursor containing data from the database.

        Args:
            table_name (str): The name of the table.

            criteria (dict[str], optional): A dictionary mapping column names
                to values used to select rows from which to pull the data.

            order_by (str, optional): The name of the column by which to order
                the data.

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

    def update(self, table_name: str, data: dict[str], criteria: dict[str]) -> None:
        """Updates a row in the database.

        Args:
            table_name (str): The name of the table.

            data (dict[str]): New data as a dictionary mapping column names to
                updated values.

            criteria (dict[str]): A dictionary mapping column names to values
                used to select which row to update.
        """
        sql_statement = f"""UPDATE {table_name} SET """

        data_placeholders = ", ".join([f"{column} = ?" for column in data.keys()])
        criteria_placeholders = [f"{column} = ?" for column in criteria.keys()]
        criteria_columns = " AND ".join(criteria_placeholders)

        sql_statement += f"{data_placeholders} WHERE {criteria_columns};"

        values = [item for item in data.values()]
        for item in criteria.values():
            values.append(item)

        values = tuple(values)

        self._execute(sql_statement, values)

    def _update_modified_date(self, data: dict[str, any]) -> dict[str, any]:
        timestamp = self.datetime.return_current_datetime()
        data["modified_date"] = timestamp

        return data

    def remove(self, table_name: str, criteria: dict[str]):
        """Removes a row from the database.

        Args:
            table_name (str): Name of the table where the row is to be removed.

            criteria (dict[str]): A dictionary mapping column names to values
                used to select rows for deletion.
        """
        placeholders = [f"{column} = ?" for column in criteria.keys()]
        criteria_columns = " AND ".join(placeholders)

        sql_statement = f"""DELETE FROM {table_name} WHERE {criteria_columns};"""

        criteria_values = tuple(criteria.values())

        self._execute(sql_statement, criteria_values)

    def create_table(
        self,
        table_name: str,
        column_info: dict[str],
        foreign_key_info: list[str] = None,
    ) -> None:
        """Adds a table to the database.

        Does nothing if the table already exists.

        Args:
            table_name (str): The name of the table.
            column_info (dict[str]): A dictionary mapping column names to its
                datatype and restraints.
            foreign_key_info (list[str], optional): A list of strings
                containing foreign key constraints.
        """
        columns_with_details = [
            f" {column_name} {details}" for column_name, details in column_info.items()
        ]

        columns_with_details = ", ".join(columns_with_details)

        if foreign_key_info:
            foreign_key_constraints = ", ".join(foreign_key_info)
            columns_with_details += f", {foreign_key_constraints}"

        sql_statement = (
            f"""CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_details});"""
        )

        self._execute(sql_statement)

    def _execute(self, sql_statement: str, values: tuple[str] = None) -> sqlite3.Cursor:
        """Executes the sql statement, returns a cursor with any results.

        Args:
            sql_statement (str): The SQL statement to be executed.
            values (tuple[str], optional): Any value required to execute the
                sql statement.
        """
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(sql_statement, values or [])

            return cursor

    def delete_database(self) -> None:
        """Deletes the database file."""
        os.remove(f"data/{self.filename}")
        self.connection.close()

    def _connect(self) -> None:
        """Connects to the database file."""
        self.connection = sqlite3.connect("data/" + self.filename)
