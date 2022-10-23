"""Contains the commands for Events.

Please see the package documentation for more information.
"""

from typing import Union

from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.sqlite_commands_interface import SQLiteCommand


class DeleteUnit(SQLiteCommand):
    """Deletes a Unit from the database by its ID or code."""

    def __init__(
        self, receiver: SQLiteManager, unit_identifier: Union[int, str]
    ) -> None:
        """Sets the SQLiteManager and unit's identifier.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            Unit_identifier (int OR str): Unique ID or unit_code
                of the Unit.
        """
        self.receiver = receiver
        self.target_identifier = unit_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self.target_identifier) is int:
            criteria = {"id": self.target_identifier}

        if type(self.target_identifier) is str:
            criteria = {"unit_code": self.target_identifier}

        self.receiver.delete("units", criteria)

        return f"Unit {self.target_identifier} deleted."


class ListUnits(SQLiteCommand):
    """Returns a list of Units."""

    def __init__(
        self,
        receiver: SQLiteManager,
        criteria: dict[str] = {},
        order_by: str = None,
    ):
        """Sets the SQLiteManager, criteria and order_by column.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            criteria (dict[str, any], optional): Criteria of Units to be
                returned as a dictionary mapping column names to values.

            order_by (str, optional): Column name by which to sort the results.
        """
        self.receiver = receiver
        self.criteria = criteria
        self.order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Units."""

        cursor = self.receiver.select("units", self.criteria, self.order_by)
        return cursor.fetchall()


class UpdateUnit(SQLiteCommand):
    """Update a Unit with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self.receiver = receiver
        self.data = data
        self.criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self.receiver.update("units", self.data, self.criteria)

        return f"Unit data updated."
