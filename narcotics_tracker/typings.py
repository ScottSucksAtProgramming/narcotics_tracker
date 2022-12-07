"""Contains type aliases used throughout the Narcotics Tracker."""

from typing import Union


class NTTypes:
    """Contains types used throughout the Narcotics Tracker."""

    sqlite_types = dict[str, Union[str, int, float]]

    date_types = Union[int, str]

    medication_data_type = tuple[
        int, str, str, float, str, float, float, str, int, int, str
    ]

    reporting_period_data_type = tuple[int, int, int, str, int, int, str]
