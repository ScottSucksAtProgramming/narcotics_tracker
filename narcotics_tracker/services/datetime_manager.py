"""Handles datetime functions for the Narcotics Tracker.

Classes:
    DateTimeManager: Provides date and time services.
"""

from typing import Union

import pendulum

from narcotics_tracker.services.interfaces.datetime import DateTimeService


class DateTimeManager(DateTimeService):
    """Provides date and time services.

    Methods:

        return_current: Returns the current datetime as a timestamp.

        convert_to_timestamp: Returns a formatted string (MM-DD-YYYY HH:MM:SS)
            as a timestamp.

        convert_to_string: Returns a timestamp as a readable string.

        validate: Corrects invalid dates and returns them as a unix timestamp.
    """

    def __init__(self, dt_pkg: object = pendulum, tz: str = "America/New_York") -> None:
        """Assigns the datetime package, and timezone.

        dt_package (object, optional): Datetime package used. Defaults to
            pendulum.

        tz (str, optional): Timezone using the IANA Timezone Database.
            Defaults to America/New York.
        """
        self._timezone = tz
        self._datetime_package = dt_pkg

    def return_current(self) -> int:
        """Returns the current datetime as a timestamp."""
        return self._current_datetime().int_timestamp

    def convert_to_timestamp(self, string_datetime: str) -> int:
        """Returns a formatted string (MM-DD-YYYY HH:MM:SS) as a timestamp."""
        format = "MM-DD-YYYY HH:mm:ss"
        dt = self._datetime_package.from_format(string_datetime, format, self._timezone)

        return dt.int_timestamp

    def convert_to_string(self, timestamp: int) -> str:
        """Returns a timestamp as a readable string."""
        dt_object = self._datetime_package.from_timestamp(timestamp, self._timezone)

        return dt_object.format("MM-DD-YYYY HH:mm:ss")

    def validate(self, date: Union[int, str]) -> int:
        """Corrects invalid dates and returns them as a unix timestamp."""
        if self._date_is_invalid(date):
            return self._assign(date)

        return date

    def _date_is_invalid(self, date: Union[int, str]) -> bool:
        """Returns False if the date is a timestamp, otherwise returns True."""
        return True if (date is None or type(date) is str) else False

    def _current_datetime(self):
        """Returns current datetime as a timestamp, accounts for the timezone."""
        return self._datetime_package.now(tz=self._timezone)

    def _assign(self, date: Union[int, str] = None) -> int:
        """Returns the correct datetime depending on the date valued passed."""
        if date is None:
            return self.return_current()

        if type(date) is str:
            return self.convert_to_timestamp(date)

        if type(date) is int:
            return date
