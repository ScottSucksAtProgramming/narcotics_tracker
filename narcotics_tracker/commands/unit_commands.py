"""Contains the commands for Units.

Please see the package documentation for more information.

Classes:

    AddUnit: Adds an Unit to the database.

    DeleteUnit: Deletes a Unit from the database by its ID or code.

    ListUnits: Returns a list of Units.

    UpdateUnit: Updates a Unit with the given data and criteria.
"""
from typing import TYPE_CHECKING, Union

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.units import Unit
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddUnit(Command):
    """Adds an Unit to the database.

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

    def execute(self, unit: "Unit") -> str:
        """Executes add row operation, returns a success message.

        Args:
            unit (Unit): The Unit object to be added to the database.
        """
        unit_info = vars(unit)
        table_name = unit_info.pop("table")

        self._receiver.add(table_name, unit_info)

        return f"Unit added to {table_name} table."


class DeleteUnit(Command):
    """Deletes a Unit from the database by its ID or code.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """ "Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(self, unit_identifier: Union[str, int]) -> str:
        """Executes the delete operation and returns a success message.

        Args:
            unit_identifier (str, int): The unit code or id number of the unit
                to be deleted.
        """
        if type(unit_identifier) is int:
            criteria = {"id": unit_identifier}

        if type(unit_identifier) is str:
            criteria = {"unit_code": unit_identifier}

        self._receiver.remove("units", criteria)

        return f"Unit {unit_identifier} deleted."


class ListUnits(Command):
    """Returns a list of Units.

    execute: Executes the query and returns a list of Units.
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
        self, criteria: dict[str, any] = {}, order_by: str = None
    ) -> list[tuple]:
        """Executes the query and returns a list of Units.

        Args:
            criteria (dict[str, any]): The criteria of Units to be returned as
                a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        cursor = self._receiver.read("units", criteria, order_by)
        return cursor.fetchall()


class UpdateUnit(Command):
    """Updates a Unit with the given data and criteria.

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

    def execute(self, data: dict[str, any], criteria: dict[str, any]) -> str:
        """Executes the update operation and returns a success message.

        Args:
            data (dict[str, any]): The new data to update the Unit with as a
                dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which units are
                to be updated as a dictionary mapping the column name to its
                value.
        """
        self._receiver.update("units", data, criteria)

        return f"Unit data updated."
