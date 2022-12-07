"""Contains the commands for Statuses.

Please see the package documentation for more information.

Classes:
    AddStatus: Adds a Status to the database.

    DeleteStatus: Deletes a Status from the database by its ID or code.

    ListStatuses: Returns a list of Statuses.

    UpdateStatus: Updates a Status with the given data and criteria.    
"""
from typing import TYPE_CHECKING, Optional, Union

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes

if TYPE_CHECKING:
    from narcotics_tracker.items.statuses import Status
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddStatus(Command):
    """Adds a Status to the database.

    Methods:
        execute: Executes add row operation, returns a success message.
    """

    _status: "Status"

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_status(self, status: "Status") -> "Command":
        """Sets the status which will be added to the database.

        Args:
            status (Status): The status object to be added to the
                database.
        """
        self._status = status
        return self

    def execute(self) -> str:
        """Executes add row operation, returns a success message.

        Args:
            status (Status): The Status object to be added to the database.
        """
        status_info = vars(self._status)
        table_name = status_info.pop("table")

        self._receiver.add(table_name, status_info)

        return f"Status added to {table_name} table."


class DeleteStatus(Command):
    """Deletes a Status from the database by its ID or code.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    _criteria: NTTypes.sqlite_types
    _status_identifier: Union[int, str]

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_id(self, status_identifier: Union[int, str]) -> "Command":
        """Sets the ID of the Status to be deleted.

        Args:
            status_identifier (str, int): The Status code or id number of the
                Status to be deleted.
        """
        self._status_identifier = status_identifier
        return self

    def execute(self) -> str:
        """Executes the delete operation and returns a success message.

        Args:
            status_identifier (str, int): The status code or id number of the
                Status to be deleted.
        """
        if isinstance(self._status_identifier, int):
            self._criteria = {"id": self._status_identifier}

        if isinstance(self._status_identifier, str):
            self._criteria = {"status_code": self._status_identifier}

        self._receiver.remove("statuses", self._criteria)

        return f"Status {self._status_identifier} deleted."


class ListStatuses(Command):
    """Returns a list of Statuses.

    Methods:
        execute: Executes the command and returns a list of Statuses.
    """

    _criteria: NTTypes.sqlite_types = {}
    _order_by: Optional[str] = None

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_parameters(
        self,
        criteria: Optional[NTTypes.sqlite_types] = None,
        order_by: Optional[str] = None,
    ) -> "Command":
        """Sets the criteria and order_by column.

        Args:
            criteria (dict[str, any]): The criteria of Medication to be
                returned as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        if criteria:
            self._criteria = criteria

        if order_by:
            self._order_by = order_by

        return self

    def execute(self) -> list[tuple["Status"]]:
        """Executes the command and returns a list of Statuses.

        Args:
            criteria (dict[str, any]): The criteria of Statuses to be returned
                as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        cursor = self._receiver.read("statuses", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateStatus(Command):
    """Updates a Status with the given data and criteria.

    Methods:
        execute: Executes the update operation and returns a success message.
    """

    _data: NTTypes.sqlite_types
    _criteria: NTTypes.sqlite_types

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_data(
        self, data: NTTypes.sqlite_types, criteria: NTTypes.sqlite_types
    ) -> "Command":
        """Sets the data and criteria for the update.

        Args:
            data (dict[str, any]): The new data to update the Medication with
                as a dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which
                medications are to be updated as a dictionary mapping the
                column name to its value.
        """
        self._data = data
        self._criteria = criteria

        return self

    def execute(self) -> str:
        """Executes the update operation and returns a success message.

        Args:
            data (dict[str, any]): The new data to update the Status with as a
                dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which Statuses
                are to be updated as a dictionary mapping the column name to
                its value.
        """
        self._receiver.update("statuses", self._data, self._criteria)

        return "Status data updated."
