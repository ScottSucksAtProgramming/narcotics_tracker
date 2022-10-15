"""Obtains and formats datetimes."""

import sqlite3

from database import SQLiteManager


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

    def return_datetime(self) -> sqlite3.Cursor:
        """Returns a cursor containing the current unixepoch datetime."""
        sql_query = """SELECT unixepoch();"""

        self._execute(sql_query)

    def convert_to_string(self, unix_date_time: int) -> sqlite3.Cursor:
        """Converts a unixepoch datetime to a human readable format.

        Args:
            unix_date_time (int): The unixepoch formatted datetime.

        Returns:
            sqlite3.Cursor: A cursor containing the datetime in the format
                'MM-DD-YYYY HH:MM:SS'
        """
        sql_query = """SELECT datetime(?, 'unixepoch', 'localtime');"""
        values = [unix_date_time]

        return self._execute(sql_query, values)

    def convert_to_unixepoch(self, string_date_time: str) -> sqlite3.Cursor:
        """Converts a human-readable datetime to the unixepoch format.

        Args:
            string_date_time (str): The datetime in the format
                'MM-DD-YYYY HH:MM:SS'

        Returns:
            sqlite3.Cursor: A cursor containing the unixepoch datetime.
        """
        sql_query = f"""SELECT unixepoch('{string_date_time}');"""

        return self._execute(sql_query)
