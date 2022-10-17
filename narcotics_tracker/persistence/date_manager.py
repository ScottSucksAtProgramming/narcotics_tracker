"""Obtains and formats datetimes for the SQLite3 database.

The SQLite3 database provides and stores datetimes in the unixepoch format. 
This module contains the DateTimeFormatter which can obtain the current 
datetime as well as convert between the unixepoch format and the string 
format 'MM-DD-YYYY HH:MM:SS'
"""
import datetime
import sqlite3

from narcotics_tracker.persistence.database import SQLiteManager


class DateTimeFormatter(SQLiteManager):
    """Obtains and converts datetimes between various formats.

    This class is designed to be used as a context manager.

    Note:
        This class inherits functionality from the SQLiteManager class. Review
        that documentation for more info on how to use.

    Attributes:
        connection (sqlite3.Connection): The connection to the SQlite database.
        filename (str): The name of the database file.

    Methods:
        return_datetime: Returns a cursor containing the current unixepoch
            datetime.
        convert_to_string: Converts a unixepoch datetime to a human readable
            format.
        convert_to_unixepoch: Converts a human-readable datetime to the
            unixepoch format.
    """

    @property
    def _format(self):
        """Returns the format for human-readable datetime."""
        return "%m-%d-%Y %H:%M:%S"

    @classmethod
    def return_datetime(self) -> sqlite3.Cursor:
        """Returns a cursor containing the current unixepoch datetime."""
        if self.connection is None:
            self._connect()
        sql_query = """SELECT unixepoch();"""

        return self._execute(sql_query)

    def convert_to_string(self, unix_date_time: int) -> sqlite3.Cursor:
        """Converts a unixepoch datetime to a human readable format.

        Args:
            unix_date_time (int): The unixepoch formatted datetime.

        Returns:
            sqlite3.Cursor: A cursor containing the datetime in the format
                'MM-DD-YYYY HH:MM:SS'
        """
        sql_query = (
            f"""SELECT strftime('{self._format}',?, 'unixepoch', 'localtime');"""
        )
        values = [unix_date_time]

        return self._execute(sql_query, values)

    def convert_to_unixepoch(self, string_date_time: str) -> int:
        """Returns the unixepoch timestamp from a formatted string datetime.

        Args:
            string_date_time (str): The datetime in the format
                'MM-DD-YYYY HH:MM:SS'

        Returns:
            int: The unixepoch timestamp.
        """
        datetime_object = datetime.datetime.strptime(string_date_time, self._format)
        unix_epoch_time = datetime.datetime.strftime(datetime_object, "%s")

        return int(unix_epoch_time)
