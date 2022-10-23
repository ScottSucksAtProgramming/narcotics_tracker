"""Contains the commands for Statuses.

Please see the package documentation for more information.
"""
from typing import Union

from narcotics_tracker.commands.command_interface import SQLiteCommand
from narcotics_tracker.database import SQLiteManager


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
        self.receiver = receiver
        self.target_identifier = status_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self.target_identifier) is int:
            criteria = {"id": self.target_identifier}

        if type(self.target_identifier) is str:
            criteria = {"status_code": self.target_identifier}

        self.receiver.delete("statuses", criteria)

        return f"Status {self.target_identifier} deleted."


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
        self.receiver = receiver
        self.criteria = criteria
        self.order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Statuses."""

        cursor = self.receiver.select("statuses", self.criteria, self.order_by)
        return cursor.fetchall()


class UpdateStatus(SQLiteCommand):
    """Update a Status with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self.receiver = receiver
        self.data = data
        self.criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self.receiver.update("statuses", self.data, self.criteria)

        return f"Status data updated."
