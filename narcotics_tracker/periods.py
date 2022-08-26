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
"""

import sqlite3

from narcotics_tracker import database
from narcotics_tracker.utils import date


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the Reporting Periods Table.

    Returns:
        str: The sql query needed to create the Reporting Periods Table.
    """
    return """CREATE TABLE IF NOT EXISTS reporting_periods (
            PERIOD_ID INTEGER PRIMARY KEY,
            STARTING_DATE TEXT,                
            ENDING_DATE TEXT,
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT
            )"""


class ReportingPeriod:
    """Defines the representation of reporting periods for the project.

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

    Initializer:
        def __init__(self, starting_date: str, ending_date: str) -> None:

            Creates an instance of ReportingPeriod and assigns attributes.

            Arguments:
                starting_date (str): The date when the reporting period
                    starts.

                ending_date (str): The date when the reporting period ends.
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
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def __repr__(self) -> str:
        """Returns a string expression of the reporting period object.

        Returns:
            str: The string describing the reporting period object
        """

        return (
            f"Reporting Period {self.period_id}. Started on: "
            f"{self.starting_date}. Ends on: {self.ending_date}."
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
            self.created_date = date.return_date_as_string()
        self.modified_date = date.return_date_as_string()

        values = self.return_attributes()

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
