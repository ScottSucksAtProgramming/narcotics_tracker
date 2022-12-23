"""Contains the commands for Medications.

Please see the package documentation for more information.

Classes:

    AddMedication: Adds an Medication to the database.

    DeleteMedication: Deletes a Medication from the database by its ID or code.

    ListMedications: Returns a list of Medications.

    UpdateMedication: Updates a Medication with the given data and criteria.

    ReturnPreferredUnit: Returns the preferred unit for the specified
        Medication.

    LoadMedication: Loads a Medication Object from data.
"""
from typing import TYPE_CHECKING, Optional, Union

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.items.medications import Medication
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes, SQLiteDict

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddMedication(Command):
    """Adds a Medication to the database.

    Methods:
        execute: Executes add row operation, returns a success message.
    """

    _medication: "Medication"

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

    def set_medication(self, medication: "Medication") -> "Command":
        """Sets the medication which will be added to the database.

        Args:
            Medication (Medication): The medication object to be added to the
                database.
        """
        self._medication: "Medication" = medication
        return self

    def execute(self) -> str:
        """Executes add row operation, returns a success message."""
        medication_info = vars(self._medication)
        table_name = medication_info.pop("table")

        self._receiver.add(table_name, medication_info)

        return f"Medication added to {table_name} table."


class DeleteMedication(Command):
    """Deletes a Medication from the database by its ID or code.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    _criteria: SQLiteDict
    _medication_identifier: Union[int, str]

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

    def set_id(self, medication_identifier: Union[int, str]) -> "Command":
        """Sets the ID of the Medication to be deleted.

        Args:
            medication_id (str, int): The medication code or id number of the
                Medication to be deleted.
        """
        self._medication_identifier = medication_identifier
        return self

    def execute(self) -> str:
        """Executes the delete operation and returns a success message."""
        if isinstance(self._medication_identifier, int):
            self._criteria = {"id": self._medication_identifier}

        if isinstance(self._medication_identifier, str):
            self._criteria = {"medication_code": self._medication_identifier}

        self._receiver.remove("medications", self._criteria)

        return f"Medication {self._medication_identifier} deleted."


class ListMedications(Command):
    """Returns a list of Medications.

    Methods:
        execute: Executes the command and returns a list of Medications.
    """

    _receiver = ServiceManager().persistence
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

    def set_parameters(
        self,
        criteria: Optional[SQLiteDict] = None,
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

    def execute(self) -> list["Medication"]:
        """Executes the command and returns a list of Medications."""
        medication_list: list["Medication"] = []
        cursor = self._receiver.read("medications", self._criteria, self._order_by)
        results = cursor.fetchall()

        for med_data in results:
            returned_med = LoadMedication().set_data(med_data).execute()
            medication_list.append(returned_med)

        return medication_list


class UpdateMedication(Command):
    """Updates a Medication with the given data and criteria.

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
        """Executes the update operation and returns a success message."""
        self._receiver.update("medications", self._data, self._criteria)

        return "Medication data updated."


class ReturnPreferredUnit(Command):
    """Returns the preferred unit for the specified Medication.

    Methods:
        execute: Executes the command, returns results.
    """

    _criteria: SQLiteDict
    _medication_identifier: Union[int, str]

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

    def set_id(self, medication_identifier: Union[int, str]) -> "Command":
        """Sets the ID of the Medication to be deleted.

        Args:
            medication_identifier (str, int): The Medication code or id
                number of the Medication to be deleted.
        """
        self._medication_identifier = medication_identifier
        return self

    def execute(self) -> str:
        """Executes the command, returns results."""
        self._criteria = {"medication_code": self._medication_identifier}

        cursor = self._receiver.read("medications", self._criteria)
        return cursor.fetchall()[0][4]


class LoadMedication(Command):
    """Loads a Medication Object from data.

    Methods:
        execute: Executes the command. Returns a Medication object.
    """

    _data: NTTypes.medication_data_type

    def __init__(self, receiver: Optional["Medication"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (Builder, optional): Object which constructs Medication
                Objects. Default to MedicationBuilder.
        """
        if receiver:
            self._receiver = receiver

    def set_data(self, data: NTTypes.medication_data_type) -> "Command":
        """Sets the data which will create the Medication

        Args:
            data (tuple[Union[str, int, float]]): A tuple of medication
                attributes retrieved from the database.
        """

        self._data = data

        return self

    def execute(self) -> "Medication":
        """Executes the command. Returns a Medication object."""
        return Medication(
            table="medications",
            id=self._data[0],
            medication_code=self._data[1],
            medication_name=self._data[2],
            medication_amount=self._data[3],
            preferred_unit=self._data[4],
            fill_amount=self._data[5],
            concentration=self._data[6],
            status=self._data[7],
            created_date=self._data[8],
            modified_date=self._data[9],
            modified_by=self._data[10],
        )
