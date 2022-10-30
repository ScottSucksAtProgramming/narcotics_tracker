"""Contains the commands for Adjustments.

Please see the package documentation for more information.
"""
from typing import TYPE_CHECKING

from narcotics_tracker.commands.interfaces.command_interface import Command
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment
    from narcotics_tracker.services.interfaces.persistence_interface import (
        PersistenceService,
    )


class AddAdjustment(Command):
    """Adds an Adjustment to the database.

    Methods:
        execute: Executes the command, returns success message."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which
                communicates with the data repository. Defaults to
                SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().start_services()[0]

    def execute(self, adjustment: "Adjustment") -> str:
        """Executes the command, returns success message."""
        adjustment_info = vars(adjustment)
        table_name = adjustment_info.pop("table")

        self._receiver.add(table_name, adjustment_info)

        return f"Adjustment added to {table_name} table."


class DeleteAdjustment(Command):
    """Deletes an Adjustment from the database by its ID.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which
                communicates with the data repository. Defaults to
                SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().start_services()[0]

    def execute(self, adjustment_id: int) -> str:
        """Execute the delete operation and returns a success message."""
        self._receiver.remove("inventory", {"id": adjustment_id})

        return f"Adjustment #{adjustment_id} deleted."


class ListAdjustments(Command):
    """Returns a list of Adjustments."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which
                communicates with the data repository. Defaults to
                SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().start_services()[0]

    def execute(self, criteria: dict[str] = {}, order_by: str = None) -> list[tuple]:
        """Executes the command and returns a list of Adjustments."""

        cursor = self._receiver.read("inventory", criteria, order_by)
        return cursor.fetchall()


class UpdateAdjustment(Command):
    """Update an Adjustment with the given data and criteria."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which
                communicates with the data repository. Defaults to
                SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().start_services()[0]

    def execute(self, data: dict[str, any], criteria: dict[str, any]) -> str:
        """Executes the update operation and returns a success message."""
        self._receiver.update("inventory", data, criteria)

        return f"Adjustment data updated."
