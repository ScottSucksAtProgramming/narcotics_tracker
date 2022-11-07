"""Contains the interface for Narcotics Tracker Reports.

Classes:

    Report: The protocol for Reports in the Narcotics Tracker.
"""
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class Report(Protocol):
    """The protocol for Reports in the Narcotics Tracker."""

    _receiver: "PersistenceService"

    def __init__(self):
        """Initializes the Report, sets any needed services."""
        ...

    def run(self):
        """Runs the report. Accepts parameters required by the receiver."""
        ...
