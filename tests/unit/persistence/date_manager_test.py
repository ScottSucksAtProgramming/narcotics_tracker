"""Contains classes to test the Date Manager Module.

Classes:

    Test_DateTimeFormatter: Tests the DateTimeFormatter class.

"""

from narcotics_tracker.persistence.date_manager import DateTimeFormatter


class Test_DateTimeFormatter:
    """Tests the DateTimeFormatter class.

    DateTimeFormatter Behaviors Tested:
        - Can be instantiated.
        - Returns datetime.
        - Converts unixepoch to expected string format.
        - Converts string to unixepoch.

    """

    def test_DateTimeFormatter_can_be_instantiated(self):
        with DateTimeFormatter("test_database.db") as dt:

            assert isinstance(dt, DateTimeFormatter)

    def test_DateTimeFormatter_returns_datetime(self):
        with DateTimeFormatter("test_database.db") as dt:
            cursor = dt.return_datetime()
            data = cursor.fetchone()
            datetime = data[0]

        assert type(datetime) != None

    def test_DateTimeFormatter_converts_unixepoch_to_expected_string(self):
        with DateTimeFormatter("test_database.db") as dt:
            cursor = dt.convert_to_string(1665872425)
            data = cursor.fetchone()
            formatted_datetime = data[0]

        assert formatted_datetime == "10-15-2022 18:20:25"

    def test_DateTimeFormatter_converts_string_to_unixepoch(self):
        with DateTimeFormatter("test_database.db") as dt:
            unixepoch_datetime = dt.convert_to_unixepoch("10-15-2022 18:20:25")

        assert unixepoch_datetime == 1665872425
