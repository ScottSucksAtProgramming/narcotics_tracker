"""Contains type aliases used throughout the Narcotics Tracker."""

from typing import Union


class NTTypes:
    """Contains types used throughout the Narcotics Tracker."""

    sqlite_types = dict[str, Union[str, int, float]]

    date_types = Union[int, str]
