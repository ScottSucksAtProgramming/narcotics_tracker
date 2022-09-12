"""Contains the implementation and representation of Reporting Period Objects.

#* Background

EMS agencies need to report all changes to their controlled substance 
inventory periodically. Grouping Inventory Adjustments in to reporting periods 
keeps them organized and is helpful when generating reports. 

#* Intended Use

This module and the ReportingPeriods Class defined below allow for the 
creation of Reporting Period Objects. It is highly recommended to use the 
Reporting Period Builder Module contained within the Builders Package to 
create these objects. Instructions for using builders can be found within that 
package.

#* Reporting Periods in the Database

Reporting Periods are stored in the 'reporting_periods' table of the database 
with their numeric id, starting date, ending date, and creation / modification 
information specified. Inventory Adjustments will be assigned to a Reporting 
Period based on the date on which they occurred and are limited to the 
Reporting Periods listed in the table.

#* Classes:

    ReportingPeriod: Defines Reporting Periods and instantiates them as 
        objects.

#* Functions:

    return_table_creation_query: Returns the query needed to create the 
        'reporting_periods' table.

    return_periods: Returns the 'reporting_periods' table as lists of strings 
        and values.

    parse_reporting_period_data: Returns a Reporting Periods's attributes as a 
        dictionary.
"""

import sqlite3
from typing import Union

from narcotics_tracker import database


def return_table_creation_query() -> str:
    """Returns the query needed to create the 'reporting_periods' table.

    Returns:
        str: The sql query needed to create the Reporting Periods Table.
    """
    return """CREATE TABLE IF NOT EXISTS reporting_periods (
            PERIOD_ID INTEGER PRIMARY KEY,
            STARTING_DATE INTEGER,                
            ENDING_DATE INTEGER,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""


def return_periods(db_connection: sqlite3.Connection) -> Union[list[str], list]:
    """Returns the 'reporting_periods' table as lists of strings and values.

    Args:

        db_connection (sqlite3.Connection): The database connection.

    Returns:

        period_string_list (list[str]): The contents of the table as a list of
            strings.

        period_values_list (list): The contents of the table as a list of
            values.
    """
    sql_query = (
        """SELECT period_id, starting_date, ending_date FROM reporting_periods"""
    )

    periods_string_list = []
    periods_values_list = []

    periods_data = db_connection.return_data(sql_query)

    for period in periods_data:
        periods_string_list.append(
            f"Reporting Period {period[0]}. Started on: {database.format_datetime_from_unixepoch(period[1])}. Ends on: {database.format_datetime_from_unixepoch(period[2])}"
        )
        periods_values_list.append((period[0], period[1], period[2]))
    return periods_string_list, periods_values_list


def parse_reporting_period_data(reporting_period_data) -> dict:
    """Returns a Reporting Periods's attributes as a dictionary.

    Args:

        reporting_period_data (list): The Reporting Period's data.

    Returns:

        attributes (dict): Dictionary object containing the attributes of the
            Reporting Period.
    """
    attributes = {}

    attributes["period_id"] = reporting_period_data[0][0]
    attributes["starting_date"] = reporting_period_data[0][1]
    attributes["ending_date"] = reporting_period_data[0][2]
    attributes["created_date"] = reporting_period_data[0][3]
    attributes["modified_date"] = reporting_period_data[0][4]
    attributes["modified_by"] = reporting_period_data[0][5]

    return attributes


class ReportingPeriod:
    """Defines Reporting Periods and instantiates them as objects.

    This class defines Reporting Periods within the Narcotics Tracker.
    Reporting Periods are to organize Inventory Adjustments base on the date
    they occurred.

    Reporting Periods can be declared, created and managed using this class.
    Adjustments are limited to using the Reporting Periods stored in the
    'reporting_periods' table.

    Attributes:

        period_id (int): Numeric identifier of each Reporting Period.
            Assigned by the database. Used to interact with the Reporting
            Period in the database.

        starting_date (str): The date when the Reporting Period starts.

        ending_date (str): The date when the Reporting Period ends.

        created_date (str): The date the Reporting Period was created in the
            table.

        modified_date (str): The date the Reporting Period was last modified.

        modified_by (str): Identifier of the person who last modified the
            Reporting Period.

    Initializer:
        def __init__(self, starting_date: str, ending_date: str) -> None:

            Initializes an instance of a Reporting Period using the
                ReportingPeriodBuilder.

    Instance Methods:
        __repr__: Returns a string expression of the Reporting Period object.

        save: Saves a new Reporting Period to the table in the database.

        read: Returns the data of the Reporting Period as a tuple.

        update: Updates the Reporting Period in the 'reporting_periods' table.

        return_attributes:Returns the attributes of the Reporting Period
            Object as a tuple.

        delete: Deletes the Reporting Period from the database.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of a Reporting Period using the builder.

        EventTypes are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of EventTypes to the
        Builder Package.

        Refer to the documentation for the EventTypeBuilder Class for more
        information.

        Args:
            builder (event_type_builder.EventTypeBuilder): The builder used to
                construct the EventType object.
        """
        self.period_id = builder.period_id
        self.starting_date = builder.starting_date
        self.ending_date = builder.ending_date
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """Returns a string expression of the reporting period object.

        Returns:
            str: The string describing the reporting period object
        """

        starting_date = database.format_datetime_from_unixepoch(self.starting_date)
        ending_date = database.format_datetime_from_unixepoch(self.ending_date)

        return (
            f"Reporting Period {self.period_id}. Started on: "
            f"{starting_date}. Ends on: {ending_date}."
        )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new Reporting Period to the table in the database.

        This method will not overwrite a Reporting Period already saved in the
        database. Use the `update()` to adjust a Reporting Period's
        attributes.

        Assigns a created_date and modified_date.

        Args:

            db_connection (sqlite3.Connection): The database connection.
        """
        sql_query = """INSERT OR IGNORE INTO reporting_periods VALUES (
            ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def read(self, db_connection: sqlite3.Connection) -> tuple:
        """Returns the data of the Reporting Period as a tuple.

        This method makes no changes to the data.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:

            tuple: A tuple containing the Reporting Period's attribute values
                in the order of the 'reporting_periods' table's columns.
        """
        sql_query = """SELECT * from reporting_periods WHERE period_id = ?"""

        values = (self.period_id,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the Reporting Period in the 'reporting_periods' table.

        This method will overwrite the Reporting Period's data if it already
        exists within the database. An error will be returned if the period_id
        does not already exist in the database. Use the save method to save
        new Reporting Periods in the database.

        Assigns a new modified_date.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

            period_id (int): The numeric identifier of the Reporting Period.

        Raises:

            IndexError: An Index Error will be raised if the period_id is not
            found on the reporting_periods table.

        How to use:

            1. Use the `reporting_periods.return_periods()` method to return a
            list of Reporting Periods. Identify the period_id of the period
            you wish to update.

            2. Use the database.load_reporting_period() method, passing in the
                period_id and assigning it to a variable to create a Reporting
                Periods Object.

            3. Modify the attributes as necessary and call this method on the
                Reporting Period Object to send the new values to the
                database.

            #! Note: If the period_id is being changed use the save() method
            #! to create a new reporting period entry in the table and use the
            #! delete() method to remove the old entry.
        """
        sql_query = """UPDATE reporting_periods 
            SET PERIOD_ID = ?, 
                STARTING_DATE = ?, 
                PERIOD_NAME = ?, 
                ENDING_DATE = ?, 
                CREATED_DATE = ?, 
                MODIFIED_DATE = ?, 
                MODIFIED_BY = ? 
            WHERE PERIOD_ID = ?"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes() + (self.period_id,)

        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the Reporting Period Object as a tuple.

        Returns:

            tuple: The attributes of the Reporting Period. Follows the order
            of the columns in the 'reporting_periods' table.
        """

        return (
            self.period_id,
            self.starting_date,
            self.ending_date,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )

    def delete(self, db_connection: sqlite3.Connection) -> None:
        """Deletes the Reporting Period from the database.

        The delete method will delete the Reporting Period from the database
        entirely.

        #! Note: Deleting an item from the database is irreversible.

        Args:

            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM reporting_periods WHERE period_id = ?"""
        values = (self.period_id,)
        db_connection.write_data(sql_query, values)
