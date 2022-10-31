"""Contains the commands for Statuses.

Please see the package documentation for more information.

Classes:
    AddStatus: Adds a Status to the database.

    DeleteStatus: Deletes a Status from the database by its ID or code.

    ListStatuses: Returns a list of Statuses.

    UpdateStatus: Updates a Status with the given data and criteria.    
"""
from typing import TYPE_CHECKING, Union

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.statuses import Status
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddStatus(Command):
    """Adds a Status to the database.

    Methods:
        execute: Executes add row operation, returns a success message.
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
        """Executes add row operation, returns a success message.

        Args:
            status (Status): The Status object to be added to the database.
        """
        status_info = vars(status)
        table_name = status_info.pop("table")

        self._receiver.add(table_name, status_info)

        return f"Status added to {table_name} table."


class DeleteStatus(Command):
    """Deletes a Status from the database by its ID or code.

    Methods:
        execute: Executes the delete operation and returns a success message.
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

    def execute(self, status_identifier: Union[str, int]) -> str:
        """Executes the delete operation and returns a success message.

        Args:
            status_identifier (str, int): The status code or id number of the
                Status to be deleted.
        """
        if type(status_identifier) is int:
            criteria = {"id": status_identifier}

        if type(status_identifier) is str:
            criteria = {"status_code": status_identifier}

        self._receiver.remove("statuses", criteria)

        return f"Status {status_identifier} deleted."


class ListStatuses(Command):
    """Returns a list of Statuses.

    Methods:
        execute: Executes the command and returns a list of Statuses.
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

    def execute(self, criteria: dict[str] = {}, order_by: str = None) -> list[tuple]:
        """Executes the command and returns a list of Statuses.

        Args:
            criteria (dict[str, any]): The criteria of Statuses to be returned
                as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        cursor = self._receiver.read("statuses", criteria, order_by)
        return cursor.fetchall()


class UpdateStatus(Command):
    """Updates a Status with the given data and criteria.

    Methods:
        execute: Executes the update operation and returns a success message.
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

    def execute(self, data: dict[str, any], criteria: dict[str, any]) -> str:
        """Executes the update operation and returns a success message.

        Args:
            data (dict[str, any]): The new data to update the Status with as a
                dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which Statuses
                are to be updated as a dictionary mapping the column name to
                its value.
        """
        self._receiver.update("statuses", data, criteria)

        return f"Status data updated."
