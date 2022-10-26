"""Contains the commands for Events.

Please see the package documentation for more information.
"""

from typing import Union

from narcotics_tracker.commands.interfaces.command_interface import SQLiteCommand
from narcotics_tracker.items.units import Unit
from narcotics_tracker.services.interfaces.persistence_interface import (
    PersistenceService,
)
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class AddUnit(SQLiteCommand):
    """Adds an Unit to the database.

    Methods:
        execute: Executes the command, returns success message.
    """

    def __init__(self, receiver: PersistenceService, unit: Unit) -> None:
        """Initializes the command. Sets the receiver and Unit.

        Args:
            receiver (PersistenceManager): Persistence manager for the data
                repository.

            Unit: The Unit to be added to the database.
        """
        self._receiver = receiver
        self._unit = unit

    def execute(self) -> str:
        """Executes the command, returns success message."""

        self._extract_unit_info()
        table_name = self._pop_table_name()

        self._receiver.add(table_name, self.unit_info)

        return f"Unit added to {table_name} table."

    def _extract_unit_info(self) -> None:
        """Extracts Unit attributes and stores as a dictionary."""
        self.unit_info = vars(self._unit)

    def _pop_table_name(self) -> str:
        """Removes and returns the table name from Unit's attributes.

        Returns:
            string: Name of the table.
        """
        return self.unit_info.pop("table")


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
        self._target = receiver
        self._dataitem_id = unit_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self._dataitem_id) is int:
            criteria = {"id": self._dataitem_id}

        if type(self._dataitem_id) is str:
            criteria = {"unit_code": self._dataitem_id}

        self._target.remove("units", criteria)

        return f"Unit {self._dataitem_id} deleted."


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
        self._target = receiver
        self._criteria = criteria
        self._order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Units."""

        cursor = self._target.read("units", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateUnit(SQLiteCommand):
    """Update a Unit with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self._target = receiver
        self._data = data
        self._criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._target.update("units", self._data, self._criteria)

        return f"Unit data updated."
