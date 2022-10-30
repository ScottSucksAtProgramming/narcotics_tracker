"""Contains the commands for Statuses.

Please see the package documentation for more information.
"""
from typing import TYPE_CHECKING, Union

from narcotics_tracker.commands.interfaces.command_interface import Command
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.statuses import Status
    from narcotics_tracker.services.interfaces.persistence_interface import (
        PersistenceService,
    )


class AddStatus(Command):
    """Adds a Status to the database.

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
            self._receiver = ServiceManager().persistence

    def execute(self, status: "Status") -> str:
        """Executes the command, returns success message."""

        status_info = vars(status)
        table_name = status_info.pop("table")

        self._receiver.add(table_name, status_info)

        return f"Status added to {table_name} table."


class DeleteStatus(Command):
    """Deletes a Status from the database by its ID or code."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().start_services()[0]

    def execute(self, status_identifier: Union[str, int]) -> str:
        """Execute the delete operation and returns a success message."""
        if type(status_identifier) is int:
            criteria = {"id": status_identifier}

        if type(status_identifier) is str:
            criteria = {"status_code": status_identifier}

        self._receiver.remove("statuses", criteria)

        return f"Status {status_identifier} deleted."


class ListStatuses(Command):
    """Returns a list of Statuses."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().start_services()[0]

    def execute(self, criteria: dict[str] = {}, order_by: str = None) -> list[tuple]:
        """Executes the command and returns a list of Statuses."""

        cursor = self._receiver.read("statuses", criteria, order_by)
        return cursor.fetchall()


class UpdateStatus(Command):
    """Update a Status with the given data and criteria."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().start_services()[0]

    def execute(self, data: dict[str, any], criteria: dict[str, any]) -> str:
        """Executes the update operation and returns a success message."""
        self._receiver.update("statuses", data, criteria)

        return f"Status data updated."
