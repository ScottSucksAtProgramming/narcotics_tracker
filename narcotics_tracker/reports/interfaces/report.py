"""Contains the inteface for Narcotics Tracker Reports.

Classes:

    Report: The protocol for Reports in the Narcotics Tracker.
"""
from typing import Protocol


class Report(Protocol):
    """The protocol for Reports in the Narcotics Tracker."""

    def __init__(self):
        """Initalizes the Report, sets any needed services."""
        ...

    def execute(self):
        """Runs the report. Accepts parameters required by the receiver."""
        ...
