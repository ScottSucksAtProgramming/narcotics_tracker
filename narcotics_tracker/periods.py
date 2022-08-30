"""Contains the representation and implementation of reporting periods.

In New York State the Department of Health and Bureau of EMS and Trauma 
Systems requires narcotics reporting to be completed twice a year. The two 
reporting periods are from January 1st to June 30th, and from July 1st to 
December 31st.

The periods module and classes assist with the creation and management of 
reporting periods and the Reporting Periods Table within the database.

Please look at the database module for more information on communicating with 
the database.

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

    def __init__(self, starting_date: str, ending_date: str) -> None:
        """Creates an instance of ReportingPeriod and assigns attributes.

        Sets the period_id to None.

        Arguments:
                starting_date (str): The date when the reporting period
                    starts.

                ending_date (str): The date when the reporting period ends.
        """
        self.period_id = None
        self.starting_date = database.return_datetime(starting_date)
        self.ending_date = database.return_datetime(ending_date)
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

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

    def update_starting_date(
        self, new_starting_date: str, db_connection: sqlite3.Connection
    ) -> None:
        """Updates the starting date of the reporting period.

        Args:
            new_starting_date (str): The new starting date in format
                YYY-MM-DD HH:MM:SS.

            db_connection (sqlite3.Connection) The database connection.
        """
        self.modified_date = database.return_datetime()

        sql_query = (
            """UPDATE reporting_periods SET starting_date =(?) WHERE period_id = (?)"""
        )
        values = (database.return_datetime(new_starting_date), self.period_id)

        db_connection.write_data(sql_query, values)

    def update_ending_date(
        self, new_ending_date: str, db_connection: sqlite3.Connection
    ) -> None:
        """Updates the ending date of the reporting period.

        Args:
            new_ending_date (str): The new ending date in format MM-DD-YYYY.

            db_connection (sqlite3.Connection) The database connection.
        """
        self.modified_date = database.return_datetime()

        sql_query = (
            """UPDATE reporting_periods SET ending_date =(?) WHERE period_id = (?)"""
        )
        values = (database.return_datetime(new_ending_date), self.period_id)

        db_connection.write_data(sql_query, values)

    def delete(self, db_connection: sqlite3.Connection):
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
