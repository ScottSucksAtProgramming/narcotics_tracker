"""Contains the commands for Units.

Please see the package documentation for more information.

Classes:

    AddUnit: Adds an Unit to the database.

    DeleteUnit: Deletes a Unit from the database by its ID or code.

    ListUnits: Returns a list of Units.

    UpdateUnit: Updates a Unit with the given data and criteria.
"""
from typing import TYPE_CHECKING, Optional, Union

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import SQLiteDict

if TYPE_CHECKING:
    from narcotics_tracker.items.units import Unit
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddUnit(Command):
    """Adds an Unit to the database.

    Methods:
        execute: Executes add row operation, returns a success message.
    """

    _unit: "Unit"

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

    def set_unit(self, unit: "Unit") -> "Command":
        """Sets the unit which will be added to the database."""
        self._unit: "Unit" = unit
        return self

    def execute(self) -> str:
        """Executes add row operation, returns a success message.

        Args:
            unit (Unit): The Unit object to be added to the database.
        """
        unit_info = vars(self._unit)
        table_name = unit_info.pop("table")

        self._receiver.add(table_name, unit_info)

        return f"Unit added to {table_name} table."


class DeleteUnit(Command):
    """Deletes a Unit from the database by its ID or code.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    _criteria: SQLiteDict
    _unit_identifier: Union[str, int]

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """ "Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_identifier(self, unit_identifier: Union[str, int]) -> "Command":
        """Sets the identifier of the unit being deleted."""

        self._unit_identifier = unit_identifier

        if isinstance(unit_identifier, int):
            self._criteria = {"id": unit_identifier}

        if isinstance(unit_identifier, str):
            self._criteria = {"unit_code": unit_identifier}

        return self

    def execute(self) -> str:
        """Executes the delete operation and returns a success message.

        Args:
            unit_identifier (str, int): The unit code or id number of the unit
                to be deleted.
        """

        self._receiver.remove("units", self._criteria)

        return f"Unit {self._unit_identifier} deleted."


class ListUnits(Command):
    """Returns a list of Units.

    execute: Executes the query and returns a list of Units.
    """

    _criteria: SQLiteDict = {}
    _order_by: Optional[str] = None

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

    def set_parameters(
        self,
        criteria: Optional[SQLiteDict] = None,
        order_by: Optional[str] = None,
    ) -> "Command":
        """Sets the criteria and order_by column.

        Args:
            criteria (dict[str, any]): The criteria of Units to be returned as
                a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        if criteria:
            self._criteria = criteria

        if order_by:
            self._order_by = order_by

        return self

    def execute(self) -> list[tuple[str, SQLiteDict]]:
        """Executes the query and returns a list of Units."""
        cursor = self._receiver.read("units", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateUnit(Command):
    """Updates a Unit with the given data and criteria.

    Method:
        execute: Executes the update operation and returns a success message.
    """

    _data: SQLiteDict
    _criteria: SQLiteDict

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

    def set_data(self, data: SQLiteDict, criteria: SQLiteDict) -> "Command":
        """Sets the data and criteria for the update.

        Args:
            data (dict[str, any]): The new data to update the Unit with as a
                dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which units are
                to be updated as a dictionary mapping the column name to its
                value.
        """
        self._data = data
        self._criteria = criteria

        return self

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._receiver.update("units", self._data, self._criteria)

        return "Unit data updated."
