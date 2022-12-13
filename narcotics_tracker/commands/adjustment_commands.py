"""Contains the commands for Adjustments.

Please see the package documentation for more information.

Classes:

    AddAdjustment: Adds an Adjustment to the database.

    DeleteAdjustment: Deletes a Adjustment from the database by its ID or code.

    ListAdjustments: Returns a list of Adjustments.

    UpdateAdjustment: Updates a Event with the given data and criteria.
"""
from typing import TYPE_CHECKING, Optional

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes

if TYPE_CHECKING:

    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddAdjustment(Command):
    """Adds an Adjustment to the database.

    Methods:
        execute: Executes add row operation, returns a success message.
    """

    _adjustment: "Adjustment"

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

    def set_adjustment(self, adjustment: "Adjustment") -> "Command":
        """Sets the adjustment which will be added to the database."""
        self._adjustment: "Adjustment" = adjustment
        return self

    def execute(self) -> str:
        """Executes add row operation, returns a success message."""
        adjustment_info = vars(self._adjustment)
        table_name = adjustment_info.pop("table")

        self._receiver.add(table_name, adjustment_info)

        return f"Adjustment added to {table_name} table."


class DeleteAdjustment(Command):
    """Deletes an Adjustment from the database by its ID.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    _adjustment_id: int

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

    def set_id(self, adjustment_id: int) -> "Command":
        """Sets the ID of the Adjustment to be deleted.

        Args:
            adjustment_id (int): Adjustment's ID number.
        """
        self._adjustment_id = adjustment_id
        return self

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        self._receiver.remove("inventory", {"id": self._adjustment_id})

        return f"Adjustment #{self._adjustment_id} deleted."


class ListAdjustments(Command):
    """Returns a list of Adjustments.

    Methods:
        execute: Executes the command and returns a list of Adjustment.
    """

    _criteria: NTTypes.sqlite_types = {}
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
        criteria: Optional[NTTypes.sqlite_types] = None,
        order_by: Optional[str] = None,
    ) -> "Command":
        """Sets the criteria and order_by column.

        Args:
            criteria (dict[str, any]): The criteria of Adjustments to be
                returned as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        if criteria:
            self._criteria = criteria

        if order_by:
            self._order_by = order_by

        return self

    def execute(
        self,
        criteria: Optional[NTTypes.sqlite_types] = None,
        order_by: Optional[str] = None,
    ) -> list["Adjustment"]:
        """Executes the command and returns a list of Adjustments.

        Args:
            criteria (dict[str, any]): The criteria of Adjustments to be
                returned as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        adjustment_list: list["Adjustment"] = []
        if criteria is None:
            criteria = {}

        cursor = self._receiver.read("inventory", criteria, order_by)
        results = cursor.fetchall()

        for adjustment_data in results:
            adjustment = (
                LoadAdjustment(self._receiver).set_data(adjustment_data).execute()
            )
            adjustment_list.append(adjustment)

        return adjustment_list


class UpdateAdjustment(Command):
    """Updates an Adjustment with the given data and criteria.

    Method:
        execute: Executes the update operation and returns a success message.
    """

    _data: NTTypes.sqlite_types
    _criteria: NTTypes.sqlite_types

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

    def set_data(
        self, data: NTTypes.sqlite_types, criteria: NTTypes.sqlite_types
    ) -> "Command":
        """Sets the data and criteria for the update.

        Args:
            data (dict[str, any]): The new data to update the Adjustment with
                as a dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which
                adjustments are to be updated as a dictionary mapping the
                column name to its value.
        """
        self._data = data
        self._criteria = criteria

        return self

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._receiver.update("inventory", self._data, self._criteria)

        return "Adjustment data updated."


class LoadAdjustment(Command):
    """Loads a Adjustment Object from data.

    Methods:
        execute: Executes the command. Returns a Adjustment object.
    """

    _data: NTTypes.adjustment_data_type

    def __init__(self, receiver: Optional["Adjustment"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (Builder, optional): Object which constructs Adjustment
                Objects. Default to AdjustmentBuilder.
        """
        if receiver:
            self._receiver = receiver

    def set_data(self, data: NTTypes.adjustment_data_type) -> "Command":
        """Sets the data which will create the Adjustment

        Args:
            data (tuple[Union[str, int, float]]): A tuple of Adjustment
                attributes retrieved from the database.
        """

        self._data = data

        return self

    def execute(self) -> "Adjustment":
        """Executes the command. Returns a Adjustment object."""
        return Adjustment(
            table="inventory",
            id=self._data[0],
            adjustment_date=self._data[1],
            event_code=self._data[2],
            medication_code=self._data[3],
            amount=self._data[4],
            reporting_period_id=self._data[5],
            reference_id=self._data[6],
            created_date=self._data[7],
            modified_date=self._data[8],
            modified_by=self._data[9],
        )
