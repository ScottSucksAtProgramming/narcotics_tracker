"""Contains functions for working with dates.

SQLite3 does not support dates as a native type. This module contains 
functions for obtaining and formatting dates as a string.

Functions:
    get_date_as_string: Returns the date in the format DD-MM-YYYY.
"""
import datetime


def get_date_as_string() -> str:
    """Returns the date in the format DD-MM-YYYY

    The date is obtained from the datetime library and then formatted.

    Returns:
        str: The date in the format DD-MM-YYYY.
    """
    return datetime.date.today().strftime("%m-%d-%Y")
