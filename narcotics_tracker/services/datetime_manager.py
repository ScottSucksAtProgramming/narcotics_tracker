"""Handles datetime functions for the Narcotics Tracker.

Classes:
    DateTimeManager: Provides date and time services.
"""

from typing import Optional

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

    _datetime_package: object = pendulum

    def __init__(
        self, dt_pkg: Optional[object], time_zone: str = "America/New_York"
    ) -> None:
        """Assigns the datetime package, and timezone.

        dt_package (object, optional): Datetime package used. Defaults to
            pendulum.

        time_zone (str, optional): Timezone using the IANA Timezone Database.
            Defaults to America/New York.
        """
        if dt_pkg:
            self._datetime_package = dt_pkg

        self._timezone: str = time_zone

    def return_current(self) -> int:
        """Returns the current datetime as a timestamp."""
        return self._current_datetime().int_timestamp  # type: ignore

    def convert_to_timestamp(self, string_datetime: str) -> int:
        """Returns a formatted string (MM-DD-YYYY HH:MM:SS) as a timestamp."""
        date_format = "MM-DD-YYYY HH:mm:ss"
        datetime: object = self._datetime_package.from_format(  # type: ignore
            string_datetime, date_format, self._timezone
        )

        return datetime.int_timestamp  # type: ignore

    def convert_to_string(self, timestamp: int) -> str:
        """Returns a timestamp as a readable string."""
        dt_object: object = self._datetime_package.from_timestamp(  # type: ignore
            timestamp, self._timezone
        )

        return dt_object.format("MM-DD-YYYY HH:mm:ss")  # type: ignore

    def validate(self, date: DateTimeService._date_types) -> int:
        """Corrects invalid dates and returns them as a unix timestamp."""
        if self._date_is_invalid(date):
            return self._assign(date)

        return int(date)

    def _date_is_invalid(self, date: DateTimeService._date_types) -> bool:
        """Returns False if the date is a timestamp, otherwise returns True."""
        return True if (date is None or isinstance(date, str)) else False

    def _current_datetime(self) -> int:
        """Returns current datetime as a timestamp, accounts for the timezone."""
        return self._datetime_package.now(tz=self._timezone)  # type: ignore

    def _assign(self, date: Optional[DateTimeService._date_types] = None) -> int:
        """Returns the correct datetime depending on the date valued passed."""
        if date is None:
            return self.return_current()

        if isinstance(date, str):
            return self.convert_to_timestamp(date)

        return date
