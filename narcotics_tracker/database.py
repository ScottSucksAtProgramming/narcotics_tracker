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

import os
from typing import TYPE_CHECKING
import sqlite3

from narcotics_tracker import (
    events,
    inventory,
    medications,
    reporting_periods,
    statuses,
    units,
)
from narcotics_tracker.builders import (
    adjustment_builder,
    event_builder,
    medication_builder,
    reporting_period_builder,
    status_builder,
    unit_builder,
)

if TYPE_CHECKING:
    from narcotics_tracker import medications


def return_datetime(string_date_time: str = None) -> int:
    """Returns current local date time as unixepoch formatted integer."""
    sql_query = """SELECT unixepoch();"""

    if string_date_time:
        sql_query = f"""SELECT unixepoch('{string_date_time}');"""

    db = Database()
    db.connect("inventory.db")

    return db.return_data(sql_query)[0][0]


def format_datetime_from_unixepoch(unix_date_time: int) -> str:
    """Formats a unixepoch datetime to readable format."""
    sql_query = """SELECT datetime(?, 'unixepoch', 'localtime');"""
    values = [unix_date_time]
    db = Database()
    db.connect("inventory.db")

    return db.return_data(sql_query, values)[0][0]


class Database:
    """Interacts directly with the database.

    Initializer:
        __init__(self) -> None:
        Initializes the database object and sets connection to None.

    Instance Methods:
        connect: Creates a connection to the database.

        create_table: Creates a table in the database.

        return_tables: Returns a list of tables as a list.

        return_columns: Returns the column names from a table as a list.

        delete_table: Deletes a table from the database.

        update_table: Updates a table using the ALTER TABLE statement.

        return_data: Returns queried data as a list.

        write_data: Writes data to the database.

        load_medication: Create a medication object from data in the database.

    Static Methods:

        created_date_is_none: Returns True if the created date is None.

    """

    def __init__(self, filename: str = "inventory.db") -> None:
        """Initializes the database object and sets it's connection to None.

        Sets the connection to None. Sets the filename to the passed filename.
        Args:
            filename (str): the filename of the database the object will
                connect to.
        """
        self.connection = None
        self.filename = filename

    def __enter__(self):
        """Creates a connection to the database and returns the cursor.

        Returns:
            sqlite3.cursor: The cursor object which executes sql queries.
        """
        self.connection = sqlite3.connect("data/" + self.filename)
        return self.connection.cursor()

    def __exit__(self):
        """Closes the database connection."""
        self.connection.close()

    def connect(self, database_file: str) -> sqlite3.Connection:
        """Creates a connection to the database.

        Args:
            database_file (str): The database file located in the data/
                directory.

        Returns:
            database_connection (sqlite3.Connection): The connection to the
                database.
        """
        self.connection = None
        try:
            self.connection = sqlite3.connect("data/" + database_file)
            print(sqlite3.version)

        except sqlite3.Error as e:
            print("Database connection error!")
            print(e)

        finally:
            return self.connection

    def delete_database(self, database_file: str) -> None:
        """Deletes a database from the data/ directory.

        Args:
            database_file (str): The database file located in the data/
                directory.
        """
        try:
            self.connection.close()
            os.remove("data/" + database_file)
            self.connection = None
        except sqlite3.Error as e:
            print(e)

    def create_table(self, sql_query: str) -> None:
        """Creates a table in the database.

        Args:
            sql_query (str): The SQL query to create the table. i.e.
                "CREATE TABLE table_name (column_name column_type)"
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_query)

    def return_table_names(self) -> list:
        """Returns a list of tables in the database.

        Returns:
            table_list (list): The list of tables in the database.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            """SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name"""
        )
        raw_data = cursor.fetchall()

        return [name[0] for name in raw_data]

    def return_columns(self, sql_query: str) -> list:
        """Returns the column names from a table as a list.

        Args:
            sql_query (str): The SQL query to return the column names. i.e.
                'SELECT * FROM table_name'
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_query)
        return [description[0] for description in cursor.description]

    def delete_table(self, sql_query: str) -> None:
        """Deletes a table from the database.

        Args:
            sql_query (str): The SQL query to delete the table. i.e. DROP
                TABLE IF EXISTS table_name
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_query)
        self.connection.commit()

    def update_table(self, sql_query: str) -> None:
        """Updates a table using the ALTER TABLE statement.

        Args:
            sql_query (str): The SQL query to update the table.

        Options:
            Rename Table: ALTER TABLE table_name RENAME TO new_table_name
            Add Column: ALTER TABLE table_name ADD column_name data_type
            Rename Column: ALTER TABLE table_name RENAME COLUMN column_name
                TO new_column_name
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_query)
        self.connection.commit()

    def return_data(self, sql_query: str, values: list = None) -> list:
        """Returns queried data as a list.

        Args:
            sql_query (str): The SQL query to read from the database. i.e.
                SELECT * FROM table_name

            values (list): The values to be passed to the query.

        Returns:
            data (list): The data returned from the query.
        """
        cursor = self.connection.cursor()
        if values is None:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, values)
        return cursor.fetchall()

    def write_data(self, sql_query: str, values: str) -> None:
        """Writes data to the database.

        Args:
            sql_query (str): The SQL query to write to the database. i.e.
                INSERT INTO table_name (column_name) VALUES (value)

            values (list): The values to be passed to the query.
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_query, values)
        self.connection.commit()

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

    def load_medication(self, code: str) -> "medications.Medication":
        """Create a medication object from data in the database.

        Args:
            code (str): The code of the medication to be loaded.

        Returns:
            medication (medication.Medication): The medication object.
        """
        sql_query = """SELECT * FROM medications WHERE MEDICATION_CODE = ?"""
        values = (code,)

        result = self.return_data(sql_query, values)
        medication_data = medications.parse_medication_data(result)

        med_builder = medication_builder.MedicationBuilder()
        med_builder.set_all_properties(medication_data)
        loaded_med = med_builder.build()

        return loaded_med

    def load_event(self, event_code: str) -> "events.Event":
        """Create an Event object from data in the database.

        Args:
            event_code (str): The event_code of the Event to be loaded.

        Returns:
            event (event_types.Event): The Event object.
        """
        sql_query = """SELECT * FROM events WHERE event_code = ?"""
        values = (event_code,)

        result = self.return_data(sql_query, values)
        event_data = events.parse_event_data(result)

        e_builder = event_builder.EventBuilder()
        e_builder.set_all_properties(event_data)
        loaded_med = e_builder.build()

        return loaded_med

    def load_reporting_period(
        self, period_id: int
    ) -> "reporting_periods.ReportingPeriod":
        """Create a ReportingPeriod object from data in the database.

        Args:
            period_id (int): The numeric identifier of the ReportingPeriod to
                be loaded.

        Returns:
            loaded_period (reporting_periods.ReportingPeriod): The
                ReportingPeriod object.
        """
        sql_query = """SELECT * FROM reporting_periods WHERE period_id = ?"""
        values = (period_id,)

        result = self.return_data(sql_query, values)
        period_data = reporting_periods.parse_reporting_period_data(result)

        period_builder = reporting_period_builder.ReportingPeriodBuilder()
        period_builder.set_all_properties(period_data)
        loaded_period = period_builder.build()

        return loaded_period

    def load_adjustment(
        self, adjustment_id: int, db_connection: sqlite3.Connection
    ) -> "inventory.Adjustment":
        """Create an Adjustment object from data in the database.

        Args:
            adjustment_id (int): The numeric identifier of the Adjustment to
                be loaded.

            db_connection (sqlite3.Connection): Connection to the database.

        Returns:
            loaded_adjustment (inventory.Adjustment): The
                Adjustment object.
        """
        sql_query = """SELECT * FROM inventory WHERE adjustment_id = ?"""
        values = (adjustment_id,)

        result = self.return_data(sql_query, values)
        adjustment_data = inventory.parse_adjustment_data(result)

        adj_builder = adjustment_builder.AdjustmentBuilder()
        adj_builder.set_all_properties(adjustment_data)
        loaded_adjustment = adj_builder.build(db_connection)

        return loaded_adjustment

    def load_unit(self, unit_code: str) -> "units.Unit":
        """Create an Unit object from data in the database.

        Args:
            unit_id (str): The numeric identifier of the Unit to
                be loaded.

        Returns:
            loaded_unit (units.Unit): The
                Unit object.
        """
        sql_query = """SELECT * FROM units WHERE unit_code = ?"""
        values = (unit_code,)

        result = self.return_data(sql_query, values)
        unit_data = units.parse_unit_data(result)

        unt_builder = unit_builder.UnitBuilder()
        unt_builder.set_all_properties(unit_data)
        loaded_unit = unt_builder.build()

        return loaded_unit

    def load_status(self, status_code: str) -> "statuses.status":
        """Create an status object from data in the database.

        Args:
            status_id (str): The numeric identifier of the status to
                be loaded.

        Returns:
            loaded_status (statuses.status): The
                status object.
        """
        sql_query = """SELECT * FROM statuses WHERE status_code = ?"""
        values = (status_code,)

        result = self.return_data(sql_query, values)
        status_data = statuses.parse_status_data(result)

        unt_builder = status_builder.StatusBuilder()
        unt_builder.set_all_properties(status_data)
        loaded_status = unt_builder.build()

        return loaded_status
