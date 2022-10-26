"""Handles date and time functions fro the Narcotics Tracker.

"""

import pendulum

from narcotics_tracker.datetime_interface import DateTimeService


class DateTimeManager(DateTimeService):
    def __init__(
        self, datetime_package=pendulum, timezone: str = "America/New_York"
    ) -> None:
        self.timezone = timezone
        self.datetime_package = datetime_package

    def return_current_datetime(self) -> int:
        """Returns the current date and time as a unix timestamp.

        Returns:
            int: The current date and time as a unix timestamp.
        """
        return self._current_datetime().int_timestamp

    def convert_to_timestamp(self, string_datetime: str) -> int:
        """Converts a string DateTime to Unix Timestamp.

        Args:
            string_datetime (str): The string DateTime. Formatted as
                'MM-DD-YYYY HH:mm:ss'.

        Returns:
            int: Unix Timestamp.
        """
        dt = self.datetime_package.from_format(
            string_datetime, "MM-DD-YYYY HH:mm:ss", self.timezone
        )
        return dt.int_timestamp

    def convert_to_string(self, timestamp: int) -> str:
        """Converts a Unix Timestamp to a string DateTime.

        Args:
            unix_timestamp (int): Unix Timestamp.

        Returns:
            str: The string DateTime. Formatted as 'MM-DD-YYYY HH:mm:ss'.
        """
        dt_object = self.datetime_package.from_timestamp(timestamp, self.timezone)

        return dt_object.format("MM-DD-YYYY HH:mm:ss")

    def _current_datetime(self):
        return self.datetime_package.now(tz=self.timezone)


if __name__ == "__main__":

    print(DateTimeManager.convert_to_timestamp("10-20-2022 11:11:11"))
