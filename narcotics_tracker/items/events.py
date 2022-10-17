"""Contains the events which affect controlled substance medications.

Classes:
"""

from dataclasses import dataclass

from narcotics_tracker.items.data_items import DataItem
from narcotics_tracker.persistence.sqlite_command import SQLiteCommand


@dataclass
class Event(DataItem):
    """Events which add or remove medications from the inventory.

    Attributes:

    Methods:

    Class Methods:
    """

    event_code: str
    event_name: str
    description: str
    modifier: int

    def __str__(self):
        """Returns a string representation of the event."""
        return f"ID: {self.id} | {self.event_name}: {self.description}"

    def add(self, target: SQLiteCommand) -> None:
        """Adds a new event to the Events Table."""
        event_data = {
            "event_code": self.event_code,
            "event_name": self.event_name,
            "description": self.description,
            "modifier": self.modifier,
            "created_date": self.created_date or None,
            "modified_date": self.modified_date or None,
            "modified_by": self.modified_by or None,
        }

        target.execute()

    def delete(self, target: SQLiteCommand) -> None:
        """Removes an event from the Events Table."""

    def update(self, target: SQLiteCommand) -> None:
        """Updates an event in the Events Table."""

    @classmethod
    def load(cls) -> "Event":
        """Loads an event object from data in the Events Table."""
