"""Contains the commands for Events.

Please see the package documentation for more information.
"""


from typing import Union

from narcotics_tracker.commands.interfaces.command_interface import SQLiteCommand
from narcotics_tracker.items.events import Event
from narcotics_tracker.services.interfaces.persistence_interface import (
    PersistenceService,
)
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class AddEvent(SQLiteCommand):
    """Adds an Event to the database.

    Methods:
        execute: Executes the command, returns success message.
    """

    def __init__(self, receiver: PersistenceService, event: Event) -> None:
        """Initializes the command. Sets the receiver and Event.

        Args:
            receiver (PersistenceManager): Persistence manager for the data
                repository.

            Event: The event to be added to the database.
        """
        self._receiver = receiver
        self._event = event

    def execute(self) -> str:
        """Executes the command, returns success message."""

        self._extract_event_info()
        table_name = self._pop_table_name()

        self._receiver.add(table_name, self.event_info)

        return f"Event added to {table_name} table."

    def _extract_event_info(self) -> None:
        """Extracts event attributes and stores as a dictionary."""
        self.event_info = vars(self._event)

    def _pop_table_name(self) -> str:
        """Removes and returns the table name from Events's attributes.

        Returns:
            string: Name of the table.
        """
        return self.event_info.pop("table")


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
        self._target = receiver
        self._dataitem_id = event_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self._dataitem_id) is int:
            criteria = {"id": self._dataitem_id}

        if type(self._dataitem_id) is str:
            criteria = {"event_code": self._dataitem_id}

        self._target.remove("events", criteria)

        return f"Event {self._dataitem_id} deleted."


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
        self._target = receiver
        self._criteria = criteria
        self._order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Events."""

        cursor = self._target.read("events", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateEvent(SQLiteCommand):
    """Update an Event with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self._target = receiver
        self._data = data
        self._criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._target.update("events", self._data, self._criteria)

        return f"Event data updated."
