"""Contains functions to get the date."""

import datetime


def get_date_as_string():
    """Returns the date in the format DD-MM-YYYY"""
    return datetime.date.today().strftime("%m-%d-%Y")
