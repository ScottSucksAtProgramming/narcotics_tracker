"""Contains unit tests for the Date And Time Module.

Classes:
"""


from narcotics_tracker.utils.date_and_time import DateTimeManager


class Test_DateTimeManager:
    """Unit tests the DateTimeManager class.

    Behaviors Tested:
        - Can return current datetime.
        - Can return current datetime as a timestamp.
    """

    def test_DateTimeManager_can_return_current_datetime(self) -> None:
        pdt = DateTimeManager()
        assert pdt._current_datetime() != None

    def test_DateTimeManager_can_return_current_datetime_as_timestamp(self) -> None:
        pdt = DateTimeManager()
        assert type(pdt.return_current_datetime()) == int

    def test_DateTimeManager_can_convert_string_to_timestamp(self) -> None:
        pdt = DateTimeManager()
        assert pdt.convert_to_timestamp("01-02-1986 14:10:00") == 505077000

    def test_DateTimeManager_can_convert_timestamp_to_string(self) -> None:
        pdt = DateTimeManager()

        assert pdt.convert_to_string(505077000) == "01-02-1986 14:10:00"
