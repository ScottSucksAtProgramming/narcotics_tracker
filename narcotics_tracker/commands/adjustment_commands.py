"""Contains the commands for Adjustments.

Please see the package documentation for more information.

Classes:

    AddAdjustment: Adds an Adjustment to the database.

    DeleteAdjustment: Deletes a Adjustment from the database by its ID or code.

    ListAdjustments: Returns a list of Adjustments.

    UpdateAdjustment: Updates a Event with the given data and criteria.
"""
from typing import TYPE_CHECKING, Optional, Union

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddAdjustment(Command):
    """Adds an Adjustment to the database.

    Methods:
        execute: Executes add row operation, returns a success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(self, adjustment: "Adjustment") -> str:
        """Executes add row operation, returns a success message.

        Args:
            adjustment (Adjustment): The Adjustment object to be added to the
                database.
        """
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
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(self, adjustment_id: int) -> str:
        """Execute the delete operation and returns a success message."""
        self._receiver.remove("inventory", {"id": adjustment_id})

        return f"Adjustment #{adjustment_id} deleted."


class ListAdjustments(Command):
    """Returns a list of Adjustments.

    Methods:
        execute: Executes the command and returns a list of Adjustment.
    """

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(
        self,
        criteria: Optional[NTTypes.sqlite_types] = None,
        order_by: Optional[str] = None,
    ) -> list[tuple["Adjustment"]]:
        """Executes the command and returns a list of Adjustments.

        Args:
            criteria (dict[str, any]): The criteria of Adjustments to be
                returned as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        if criteria is None:
            criteria = {}

        cursor = self._receiver.read("inventory", criteria, order_by)
        return cursor.fetchall()


class UpdateAdjustment(Command):
    """Updates an Adjustment with the given data and criteria.

    Method:
        execute: Executes the update operation and returns a success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(
        self, data: dict[str, str], criteria: dict[str, Union[str, float]]
    ) -> str:
        """Executes the update operation and returns a success message.

        Args:
            data (dict[str, any]): The new data to update the Adjustment
            with as a dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which
                Adjustments are to be updated as a dictionary mapping the
                column name to its value.
        """
        self._receiver.update("inventory", data, criteria)

        return "Adjustment data updated."
