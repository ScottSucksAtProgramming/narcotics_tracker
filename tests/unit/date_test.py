"""Contains units tests for the date module."""

import time_machine

from narcotics_tracker import date


class Test_DateClass:
    """Contains the tests for the Date module."""

    @time_machine.travel("1986-01-02")
    def test_returns_correct_date(self):
        """Tests the get_date_as_string function."""
        assert date.get_date_as_string() == "01-02-1986"

    def test_returns_string(self):
        """Tests the get_date_as_string function."""
        assert type(date.get_date_as_string()) == str
