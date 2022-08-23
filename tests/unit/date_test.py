"""Contains the Test_Date class used to test the utils/date.py module.

Classes:
    
    Test_Date: Contains all unit tests for the utils/date.py module.
"""

import time_machine

from narcotics_tracker.utils import date


class Test_Date:
    """Contains all unit tests for the utils/date.py module.

    Behaviors Tested:
        - Method get_date_as_string returns the correct date.
        - Method get_date_as_string returns a the date as a string.
    """

    @time_machine.travel("1986-01-02")
    def test_return_date_as_string_returns_correct_date(self):
        """Tests the get_date_as_string function.

        Uses time_machine library to mock the date of January 2nd, 1986.

        Asserts that the date returned is 'O1-02-1986'.
        """
        assert date.return_date_as_string() == "01-02-1986"

    def test_return_date_as_string_returns_a_string(self):
        """Tests the get_date_as_string function.

        Returns the current date.

        Asserts that returned item is of type string.
        """
        assert type(date.return_date_as_string()) == str
