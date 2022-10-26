"""Contains the commands for Adjustments.

Please see the package documentation for more information.
"""

from narcotics_tracker.commands.command_interface import SQLiteCommand
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.services.persistence_interface import PersistenceService


class AddAdjustment(SQLiteCommand):
    """Adds an Adjustment to the database.

    Methods:
        execute: Executes the command, returns success message."""

    def __init__(self, receiver: PersistenceService, adjustment: Adjustment) -> None:
        """Initializes the command. Sets the receiver and adjustment.

        Args:
            receiver (PersistenceManager): Persistence manager for the data
                repository.

            adjustment: That adjustment to be added to the database.
        """
        self._receiver = receiver
        self._adjustment = adjustment

    def execute(self) -> str:
        """Executes the command, returns success message."""

        self._extract_adjustment_info()
        table_name = self._pop_table_name()

        self._receiver.add(table_name, self.adjustment_info)

        return f"Adjustment added to {table_name} table."

    def _extract_adjustment_info(self) -> None:
        """Extracts adjustment attributes and stored as a dictionary."""
        self.adjustment_info = vars(self._adjustment)

    def _pop_table_name(self) -> str:
        """Removes and returns the table name from Adjustment's attributes.

        Returns:
            string: Name of the table.
        """
        return self.adjustment_info.pop("table")


class DeleteAdjustment(SQLiteCommand):
    """Deletes an Adjustment from the database by its ID.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    def __init__(self, receiver: PersistenceService, adjustment_id: int) -> None:
        """Initializes the command. Sets the receiver and adjustment.

        Args:
            receiver (PersistenceManager): Persistence manager for the data
                repository.

            adjustment: That adjustment to be added to the database.
        """
        self._receiver = receiver
        self._adjustment_id = adjustment_id

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        self._receiver.remove("inventory", {"id": self._adjustment_id})

        return f"Adjustment #{self._adjustment_id} deleted."


class ListAdjustments(SQLiteCommand):
    """Returns a list of Adjustments."""

    def __init__(
        self,
        receiver: PersistenceService,
        criteria: dict[str] = {},
        order_by: str = None,
    ):
        """Sets the command's target, criteria and order_by column.

        Args:
            receiver (PersistenceManager): PersistenceManager connected to the database.

            criteria (dict[str, any], optional): Criteria of adjustments to be
                returned as a dictionary mapping column names to values.

            order_by (str, optional): Column name by which to sort the results.
        """
        self._receiver = receiver
        self._criteria = criteria
        self._order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Adjustments."""

        cursor = self._receiver.read("inventory", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateAdjustment(SQLiteCommand):
    """Update an Adjustment with the given data and criteria."""

    def __init__(
        self,
        receiver: PersistenceService,
        data: dict[str, any],
        criteria: dict[str, any],
    ) -> None:
        """Sets the command's target, criteria and order_by column.

        Args:
            receiver (PersistenceManager): PersistenceManager connected to the database.

            criteria (dict[str, any], optional): Criteria of adjustments to be
                returned as a dictionary mapping column names to values.

            order_by (str, optional): Column name by which to sort the results.
        """
        self._receiver = receiver
        self._data = data
        self._criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._receiver.update("inventory", self._data, self._criteria)

        return f"Adjustment data updated."
