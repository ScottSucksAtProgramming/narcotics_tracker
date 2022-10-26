"""Contains the commands for Statuses.

Please see the package documentation for more information.
"""
from typing import Union

from narcotics_tracker.commands.command_interface import SQLiteCommand
from narcotics_tracker.items.statuses import Status
from narcotics_tracker.services.persistence_interface import PersistenceService
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class AddStatus(SQLiteCommand):
    """Adds a Status to the database.

    Methods:
        execute: Executes the command, returns success message.
    """

    def __init__(self, receiver: PersistenceService, status: Status) -> None:
        """Initializes the command. Sets the receiver and Status.

        Args:
            receiver (PersistenceManager): Persistence manager for the data
                repository.

            status: The Status to be added to the database.
        """
        self._receiver = receiver
        self._status = status

    def execute(self) -> str:
        """Executes the command, returns success message."""

        self._extract_status_info()
        table_name = self._pop_table_name()

        self._receiver.add(table_name, self.status_info)

        return f"Status added to {table_name} table."

    def _extract_status_info(self) -> None:
        """Extracts status attributes and stores as a dictionary."""
        self.status_info = vars(self._status)

    def _pop_table_name(self) -> str:
        """Removes and returns the table name from Status's attributes.

        Returns:
            string: Name of the table.
        """
        return self.status_info.pop("table")


class DeleteStatus(SQLiteCommand):
    """Deletes a Status from the database by its ID or code."""

    def __init__(
        self, receiver: SQLiteManager, status_identifier: Union[int, str]
    ) -> None:
        """Sets the SQLiteManager and Status identifier.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            status_identifier (int OR str): Unique ID or status_code
                of the Status.
        """
        self._target = receiver
        self._dataitem_id = status_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self._dataitem_id) is int:
            criteria = {"id": self._dataitem_id}

        if type(self._dataitem_id) is str:
            criteria = {"status_code": self._dataitem_id}

        self._target.remove("statuses", criteria)

        return f"Status {self._dataitem_id} deleted."


class ListStatuses(SQLiteCommand):
    """Returns a list of Statuses."""

    def __init__(
        self,
        receiver: SQLiteManager,
        criteria: dict[str] = {},
        order_by: str = None,
    ):
        """Sets the SQLiteManager, criteria and order_by column.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            criteria (dict[str, any], optional): Criteria of Statuses to be
                returned as a dictionary mapping column names to values.

            order_by (str, optional): Column name by which to sort the results.
        """
        self._target = receiver
        self._criteria = criteria
        self._order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Statuses."""

        cursor = self._target.read("statuses", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateStatus(SQLiteCommand):
    """Update a Status with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self._target = receiver
        self._data = data
        self._criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._target.update("statuses", self._data, self._criteria)

        return f"Status data updated."
