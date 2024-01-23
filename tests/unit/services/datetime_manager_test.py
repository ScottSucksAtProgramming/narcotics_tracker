"""Contains unit tests for the datetime Manager Module.

Classes:
    Test_DateTimeManager: Unit tests the DateTimeManager class.
"""


import datetime

import pendulum

from narcotics_tracker.services.datetime_manager import DateTimeManager


class Test_DateTimeManager:
    """Unit tests the DateTimeManager class.

    Behaviors Tested:
        - Can return correct current datetime.

        - Can return current datetime as a timestamp.

        - Can convert string to timestamp.

        - Can convert timestamp to string.

        - _date_is_invalid returns True when None is passed.

        - _date_is_invalid returns True when a string is passed.

        - _date_is_invalid returns False when int is passed.
    """

    def test_DateTimeManager_can_return_current_datetime(self) -> None:
        pdt = DateTimeManager()
        assert pdt._current_datetime() != datetime.datetime.now()

    def test_DateTimeManager_can_return_current_datetime_as_timestamp(self) -> None:
        pdt = DateTimeManager()
        assert type(pdt.return_current()) == int

    def test_DateTimeManager_can_convert_string_to_timestamp(self) -> None:
        pdt = DateTimeManager()
        assert pdt.convert_to_timestamp("01-02-1986 14:10:00") == 505077000

    def test_DateTimeManager_can_convert_timestamp_to_string(self) -> None:
        pdt = DateTimeManager()

        assert pdt.convert_to_string(505077000) == "01-02-1986 14:10:00"

    def test_assign_datetime_returns_current_timestamp(self) -> None:
        pdt = DateTimeManager()
        assert pdt._assign(None) == pdt._current_datetime().int_timestamp

    def test_assign_datetime_converts_string_to_timestamp(self) -> None:
        pdt = DateTimeManager()
        assert pdt._assign("12-31-1969 19:00:01") == 1

    def test_assign_datetime_passes_integer(self) -> None:
        pdt = DateTimeManager()
        assert pdt._assign(12) == 12

    def test_date_is_invalid_returns_true_when_None_is_passed(self) -> None:
        assert DateTimeManager()._date_is_invalid(None) == True

    def test_date_is_invalid_returns_true_when_string_is_passed(self) -> None:
        assert DateTimeManager()._date_is_invalid("Hello") == True

    def test_date_is_invalid_returns_false_when_int_is_passed(self) -> None:
        assert DateTimeManager()._date_is_invalid(123) == False

    def test_assign_datetime_returns_current_datetime_when_none_passed(self) -> None:
        assert DateTimeManager()._assign(None) == pendulum.now().int_timestamp

    def test_assign_datetime_returns_correct_timestamp_when_string_passed(self) -> None:
        assert DateTimeManager()._assign("01-02-1986 14:10:00") == 505077000

    def test_assign_datetime_returns_initial_value_when_integer(self) -> None:
        assert DateTimeManager()._assign(123) == 123

    def test_validate_date_returns_initial_value_when_int_passed(self) -> None:
        assert DateTimeManager().validate(123) == 123

    def test_validate_date_returns_converted_timestamp_when_string_passed(self) -> None:
        assert DateTimeManager().validate("01-02-1986 14:10:00") == 505077000

    def test_validate_date_returns_current_datetime_when_None_passed(self) -> None:
        assert DateTimeManager().validate(None) == pendulum.now().int_timestamp
