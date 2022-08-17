"""Defines the database model for the narcotics tracker.

This module contains the Database Class and its associated methods. All 
interactions with the database are done through this module or any 
associated modules as needed.

The Narcotics Tracker makes use of the SQLite3 package which comes bundled 
with Python. It requires no additional libraries, services or configuration. 
The database is stored in the data/ directory within the root directory of the 
project.

Classes:
    Database: Interacts with the SQLite3 database.
"""

import sqlite3

from narcotics_tracker import medication
from narcotics_tracker.builders import builder


class Database:
    """Interacts directly with the database.

    Initializer:
        __init__(self) -> None:
        Initializes the database object and sets connection to None.

    Instance Methods:
        connect: Creates a connection to the database.

        create_table: Creates a table in the database.

        return_tables: Returns a list of tables as a list.

        return_columns: Returns the column names from a table as a tuple.

        delete_table: Deletes a table from the database.

        update_table: Updates a table using the ALTER TABLE statement.

        return_data: Returns queried data as a list.

        write_data: Writes data to the database.

        load_medication: Create a medication object from data in the database.

    Static Methods:

        created_date_is_none: Returns True if the created date is None.

    """

    def __init__(self) -> None:
        """Initializes the database object and sets connection to None."""
        self.database_connection = None

    def connect(self, database_file) -> sqlite3.Connection:
        """Creates a connection to the database.

        Args:
            database_file (str): The database file located in the data/
                directory.

        Returns:
            database_connection (sqlite3.Connection): The connection to the
                database.
        """
        try:
            self.database_connection = sqlite3.connect("data/" + database_file)
        except sqlite3.Error as e:
            print(e)

        return self.database_connection

    def create_table(self, sql_query) -> None:
        """Creates a table in the database.

        Args:
            sql_query (str): The SQL query to create the table. i.e.
                "CREATE TABLE table_name (column_name column_type)"
        """
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)

    def return_tables(self, sql_query, table_name: list[str]) -> list:
        """Returns a list of tables in the database.

        Args:
            sql_query (str): The SQL query to read from the database. i.e.
                SELECT * FROM table_name

            table_name (list[str]): The name of the table to read from. Must
                be provided as a list.

        Returns:
            table_list (list): The list of tables in the database.

        """
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query, table_name)
        return cursor.fetchall()

    def return_columns(self, sql_query) -> tuple:
        """Returns the column names from a table as a tuple.

        Args:
            sql_query (str): The SQL query to read from the database. i.e.
                SELECT * FROM sqlite_master WHERE type = 'table' AND
                name = (?)

        Returns:
            column_names (tuple): The column names from the table.
        """
        cursor = self.database_connection.cursor()
        columns = cursor.execute(sql_query)

        return columns.description

    def delete_table(self, sql_query) -> None:
        """Deletes a table from the database.

        Args:
            sql_query (str): The SQL query to delete the table. i.e. DROP
                TABLE IF EXISTS table_name
        """
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query)
        self.database_connection.commit()

    def update_table(self, sql_query) -> None:
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

    def return_data(self, sql_query: str, values: list = None) -> list:
        """Returns queried data as a list.

        Args:
            sql_query (str): The SQL query to read from the database. i.e.
                SELECT * FROM table_name

            values (list): The values to be passed to the query.

        Returns:
            data (list): The data returned from the query.
        """
        cursor = self.database_connection.cursor()
        if values is None:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, values)
        return cursor.fetchall()

    def write_data(self, sql_query, values) -> None:
        """Writes data to the database.

        Args:
            sql_query (str): The SQL query to write to the database. i.e.
                INSERT INTO table_name (column_name) VALUES (value)

            values (list): The values to be passed to the query.
        """
        cursor = self.database_connection.cursor()
        cursor.execute(sql_query, values)
        self.database_connection.commit()

    @staticmethod
    def created_date_is_none(object) -> bool:
        """Returns True if the created date is None.

        Args:
            object (Object): The object which is being tested.

        Returns:
            bool: Returns True if the created date is None.
        """
        if object.created_date is None:
            return True
        else:
            return False

    def load_medication(self, code):  # ? Circular import when importing medication.py
        """Create a medication object from data in the database.

        Args:
            code (str): The code of the medication to be loaded.

        Returns:
            medication (medication.Medication): The medication object.
        """
        sql_query = """SELECT * FROM medication WHERE CODE = ?"""
        values = (code,)

        result = self.return_data(sql_query, values)
        medication_data = medication.parse_medication_data(result)

        medication_builder = builder.MedicationBuilder()
        medication_builder.set_all_properties(medication_data)
        loaded_med = medication_builder.build()

        return loaded_med
