"""Defines the protocol for working with datetimes.

Classes:
    DatetimeService: Protocol for working with datetimes.
"""

from typing import Protocol


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

    def return_current() -> int:
        ...

    def convert_to_timestamp() -> int:
        ...

    def convert_to_string() -> str:
        ...

    def validate() -> int:
        ...
