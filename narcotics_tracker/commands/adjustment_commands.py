"""Contains the commands for Adjustments.

Please see the package documentation for more information.
"""
from typing import TYPE_CHECKING

from narcotics_tracker.commands.command_interface import SQLiteCommand
from narcotics_tracker.database import SQLiteManager

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment


class AddAdjustment(SQLiteCommand):
    """Adds and Adjustment to the database.

    Attributes:
        receiver: Persistence manager for the data repository.

    """

    def __init__(self, receiver: SQLiteManager, item: Adjustment) -> None:
        self._target = receiver
        self._dataitem = item

    def execute(self) -> str:
        """Executes the command, returns success message."""

        self._extract_item_info()
        table_name = self._pop_table_name()

        self._target.add(table_name, self.item_info)

        return f"Item added to {table_name} table."

    def _extract_item_info(self) -> None:
        """Extracts item attributes and stored as a dictionary."""
        self.item_info = vars(self._dataitem)

    def _pop_table_name(self) -> str:
        """Removes and returns the table name from DataItem information.

        Returns:
            string: Name of the table.
        """
        return self.item_info.pop("table")


class DeleteAdjustment(SQLiteCommand):
    """Deletes an Adjustment from the database by its ID."""

    def __init__(self, receiver: SQLiteManager, adjustment_id: int) -> None:
        """Sets the SQLiteManager and adjustment_id."""
        self._target = receiver
        self._dataitem_id = adjustment_id

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        self._target.remove("inventory", {"id": self._dataitem_id})

        return f"Adjustment #{self._dataitem_id} deleted."


class ListAdjustments(SQLiteCommand):
    """Returns a list of Adjustments."""

    def __init__(
        self,
        receiver: SQLiteManager,
        criteria: dict[str] = {},
        order_by: str = None,
    ):
        """Sets the SQLiteManager, criteria and order_by column.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            criteria (dict[str, any], optional): Criteria of adjustments to be
                returned as a dictionary mapping column names to values.

            order_by (str, optional): Column name by which to sort the results.
        """
        self._target = receiver
        self._criteria = criteria
        self._order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Adjustments."""

        cursor = self._target.read("inventory", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateAdjustment(SQLiteCommand):
    """Update an Adjustment with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self._target = receiver
        self._data = data
        self._criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._target.update("inventory", self._data, self._criteria)

        return f"Adjustment data updated."
