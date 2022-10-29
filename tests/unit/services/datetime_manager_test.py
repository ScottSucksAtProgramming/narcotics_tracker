"""Contains unit tests for the datetime Manager Module.

Classes:
    Test_DateTimeManager: Unit tests the DateTimeManager class.
"""


from narcotics_tracker.services.datetime_manager import DateTimeManager


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

    def test_assign_datetime_returns_current_timestamp(self) -> None:
        pdt = DateTimeManager()
        assert pdt.assign_datetime(None) == pdt._current_datetime().int_timestamp

    def test_assign_datetime_converts_string_to_timestamp(self) -> None:
        pdt = DateTimeManager()
        assert pdt.assign_datetime("12-31-1969 19:00:01") == 1

    def test_assign_datetime_passes_integer(self) -> None:
        pdt = DateTimeManager()
        assert pdt.assign_datetime(12) == 12
