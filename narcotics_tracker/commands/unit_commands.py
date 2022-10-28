"""Contains the commands for Events.

Please see the package documentation for more information.
"""
from typing import TYPE_CHECKING, Union

from narcotics_tracker.commands.interfaces.command_interface import Command
from narcotics_tracker.services.service_provider import ServiceProvider

if TYPE_CHECKING:
    from narcotics_tracker.items.units import Unit
    from narcotics_tracker.services.interfaces.persistence_interface import (
        PersistenceService,
    )


class AddUnit(Command):
    """Adds an Unit to the database.

    Methods:
        execute: Executes the command, returns success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, unit: "Unit") -> str:
        """Executes the command, returns success message."""
        unit_info = vars(unit)
        table_name = unit_info.pop("table")

        self._receiver.add(table_name, unit_info)

        return f"Unit added to {table_name} table."


class DeleteUnit(Command):
    """Deletes a Unit from the database by its ID or code."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, unit_identifier: Union[str, int]) -> str:
        """Execute the delete operation and returns a success message."""
        if type(unit_identifier) is int:
            criteria = {"id": unit_identifier}

        if type(unit_identifier) is str:
            criteria = {"unit_code": unit_identifier}

        self._receiver.remove("units", criteria)

        return f"Unit {unit_identifier} deleted."


class ListUnits(Command):
    """Returns a list of Units."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, criteria: dict[str] = {}, order_by: str = None) -> list[tuple]:
        """Executes the command and returns a list of Units."""

        cursor = self._receiver.read("units", criteria, order_by)
        return cursor.fetchall()


class UpdateUnit(Command):
    """Update a Unit with the given data and criteria."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, data: dict[str, any], criteria: dict[str, any]) -> str:
        """Executes the update operation and returns a success message."""
        self._receiver.update("units", data, criteria)

        return f"Unit data updated."
