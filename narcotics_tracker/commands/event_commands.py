"""Contains the commands for Events.

Please see the package documentation for more information.
"""


from typing import Union

from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.sqlite_commands_interface import SQLiteCommand


class DeleteEvent(SQLiteCommand):
    """Deletes an Event from the database by its ID or code."""

    def __init__(
        self, receiver: SQLiteManager, event_identifier: Union[int, str]
    ) -> None:
        """Sets the SQLiteManager and event identifier.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            event_identifier (int OR str): Unique ID or event_code of the
                event.
        """
        self.receiver = receiver
        self.target_identifier = event_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self.target_identifier) is int:
            criteria = {"id": self.target_identifier}

        if type(self.target_identifier) is str:
            criteria = {"event_code": self.target_identifier}

        self.receiver.delete("events", criteria)

        return f"Event {self.target_identifier} deleted."


class ListEvents(SQLiteCommand):
    """Returns a list of Events."""

    def __init__(
        self,
        receiver: SQLiteManager,
        criteria: dict[str] = {},
        order_by: str = None,
    ):
        """Sets the SQLiteManager, criteria and order_by column.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            criteria (dict[str, any], optional): Criteria of Events to be
                returned as a dictionary mapping column names to values.

            order_by (str, optional): Column name by which to sort the results.
        """
        self.receiver = receiver
        self.criteria = criteria
        self.order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Events."""

        cursor = self.receiver.select("events", self.criteria, self.order_by)
        return cursor.fetchall()


class UpdateEvent(SQLiteCommand):
    """Update an Event with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self.receiver = receiver
        self.data = data
        self.criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self.receiver.update("events", self.data, self.criteria)

        return f"Event data updated."
