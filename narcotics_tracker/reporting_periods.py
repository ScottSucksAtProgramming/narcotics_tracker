"""Contains the implementation and representation of reporting periods.

The reporting_periods table stores periods of time defined by a starting and 
ending date which are used for report generation.

In New York State the Department of Health and Bureau of EMS and Trauma 
Systems requires narcotics reporting to be completed twice a year. The two 
reporting periods are from January 1st to June 30th, and from July 1st to 
December 31st.

This module handles the creation of the reporting_periods table, returns 
reporting period data from the database and parses raw data from the database 
into a usable format. It houses the ReportingPeriod Class which defines and 
instantiates the reporting periods as objects.

The Inventory Module and Adjustment Class make use of the Reporting Periods in 
order to organize inventory adjustments.

The Reporting Periods Builder Module contains information on creating 
reporting periods and specifying their attributes.

The database module contains information on communicating with the database.

Classes:
    ReportingPeriod: Defines the representation of reporting periods for the 
        project.

Functions:

    return_table_creation_query: Returns the query needed to create the Table.

    return_periods: Returns the contents of the reporting_periods table.
"""

import sqlite3

from narcotics_tracker import database


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the Reporting Periods Table.

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


def return_periods(db_connection: sqlite3.Connection) -> str:
    """Returns the contents of the reporting_periods table.

    Args:
        db_connection (sqlite3.Connection): The database connection.

    Returns:
        table_contents (str): The contents of the table as a string.
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
    """Returns event_type data from the database as a dictionary.

    Args:
        reporting_period_data (list): The event_type data

    Returns:
        properties (dict): Dictionary objects contains the properties of
            the event_type."""

    properties = {}

    properties["period_id"] = reporting_period_data[0][0]
    properties["starting_date"] = reporting_period_data[0][1]
    properties["ending_date"] = reporting_period_data[0][2]
    properties["created_date"] = reporting_period_data[0][3]
    properties["modified_date"] = reporting_period_data[0][4]
    properties["modified_by"] = reporting_period_data[0][5]

    return properties


class ReportingPeriod:
    """Defines the representation of reporting periods for the project.

    Initializer:
        def __init__(self, starting_date: str, ending_date: str) -> None:

            Creates an instance of ReportingPeriod and assigns attributes.

            Arguments:
                starting_date (str): The date when the reporting period
                    starts.

                ending_date (str): The date when the reporting period ends.

    Attributes:
        period_id (int): Unique identifier of each reporting period.
            Assigned by the database.

        starting_date (str): The date when the reporting period starts.

        ending_date (str): The date when the reporting period ends.

        created_date (str): The date the reporting period was created in the
            table.

        modified_date (str): The date the reporting period was last modified.

        modified_by (str): Identifier of the person who last modified the
            reporting period.

    Instance Methods:
        __repr__: Returns a string expression of the reporting period object.

        save: Saves a new reporting period to the database.

        update_starting_date: Updates the starting date of the period.

        update_ending_date: Updates the ending date of the reporting period.

        delete: Deletes the reporting period from the database.

        return_attributes: Returns the period's attributes as a tuple.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of an EventType using the EventTypeBuilder.

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
        """Saves a new reporting period to the database.

        The save method will only write the period into the table if it does
        not already exist. Use the update method to update the period's
        attributes.

        Use the date module to set the created date if it is None. Sets the
        modified date.

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
        """Returns the reporting period's data from the database as a tuple.

        This function will make no changes to the data.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:
            tuple: A tuple containing the reporting period's attribute values.
        """
        sql_query = """SELECT * from reporting_periods WHERE period_id = ?"""

        values = (self.period_id,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the reporting period in the database.

        The update method will overwrite the reporting_period's data if it
        already exists within the database. Use the save method to store new
        reporting periods in the database.

        How to use:
            Use the reporting_periods.return_reporting_periods() method to
            return a list of reporting periods.

            Use the database.load_reporting_period() method, passing in the
            period_id of the reporting period you wish to update.

            Modify the attributes as necessary and call this method to update
            the attributes in the database.

            If you are changing the period_id use the save() method to create
            a new reporting period entry in the table and use the delete
            method to remove the old entry.

        Assigns a new modified_date.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

            period_id (int): The numeric identifier of the reporting_period.

        Raises:

            IndexError: An Index Error will be raised if the period_id is not
            found on the reporting_periods table.
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
        """Returns the attributes of the reporting period as a tuple.

        Returns:
            tuple: The attributes of the reporting period. Follows the order
                of the columns in the reporting_periods table.
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
        """Deletes the reporting period from the database.

        The delete method will delete the reporting period from the database
        entirely. Note: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM reporting_periods WHERE period_id = ?"""
        values = (self.period_id,)
        db_connection.write_data(sql_query, values)
