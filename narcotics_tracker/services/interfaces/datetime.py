"""Defines the protocol for working with datetimes.

Classes:
    DatetimeService: Protocol for working with datetimes.
"""

from typing import Protocol, Union


class DateTimeService(Protocol):
    """Protocol for working with datetimes.

    Classes using this protocol must be able provide the current datetime as a
    unix timestamp, convert between a formatted string (MM-DD-YYYY HH:ss:mm)
    and the unix timestamp. DateTimeService providers are also used to
    evaluate user entered dates and format them correctly.

    Datetimes are stored in the database as a unix timestamp. They are input
    by and presented to the user as a formatted string: 'MM-DD-YYYY HH:MM:SS'.

    Methods:
        return_current: Returns the current datetime as a unix timestamp.

        convert_to_timestamp: Converts a formatted string to a timestamp.

        convert_to_string: Converts a timestamp to the formatted string.

        validate: Checks a date and converts it as necessary.
    """

    _date_types = Union[int, str]

    def return_current(self) -> int:
        """Returns the current datetime as a unix timestamp."""
        return 0

    def convert_to_timestamp(self, string_datetime: str) -> int:
        """Converts a formatted string to a timestamp."""
        return 0

    def convert_to_string(self, timestamp: int) -> str:
        """Converts a timestamp to the formatted string."""
        return ""

    def validate(self, date: _date_types) -> int:
        """Checks a date and converts it as necessary."""
        return 0
