"""Contains the commands for Medications.

Please see the package documentation for more information.

Classes:

    AddMedication: Adds an Medication to the database.

    DeleteMedication: Deletes a Medication from the database by its ID or code.

    ListMedications: Returns a list of Medications.

    UpdateMedication: Updates a Medication with the given data and criteria.

    ReturnPreferredUnit: Returns the preferred unit for the specified 
        Medication.
"""
from typing import TYPE_CHECKING, Union

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddMedication(Command):
    """Adds a Medication to the database.

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

    def execute(self, medication: "Medication") -> str:
        """Executes add row operation, returns a success message.

        Args:
            medication (Medication): The Medication object to be added to the
                database.
        """
        medication_info = vars(medication)
        table_name = medication_info.pop("table")

        self._receiver.add(table_name, medication_info)

        return f"Medication added to {table_name} table."


class DeleteMedication(Command):
    """Deletes a Medication from the database by its ID or code.

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

    def execute(self, medication_identifier: Union[str, int]) -> str:
        """Executes the delete operation and returns a success message.

        Args:
            medication_identifier (str, int): The medication code or id number
                of the Medication to be deleted.
        """
        if type(medication_identifier) is int:
            criteria = {"id": medication_identifier}

        if type(medication_identifier) is str:
            criteria = {"medication_code": medication_identifier}

        self._receiver.remove("medications", criteria)

        return f"Medication {medication_identifier} deleted."


class ListMedications(Command):
    """Returns a list of Medications.

    Methods:
        execute: Executes the command and returns a list of Medications.
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
        """Executes the command and returns a list of Medications.

        Args:
            criteria (dict[str, any]): The criteria of Medications to be
                returned as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        cursor = self._receiver.read("medications", criteria, order_by)
        return cursor.fetchall()


class UpdateMedication(Command):
    """Updates a Medication with the given data and criteria.

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
            data (dict[str, any]): The new data to update the Medication
            with as a dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which
                Medications are to be updated as a dictionary mapping the
                column name to its value.
        """
        self._receiver.update("medications", data, criteria)

        return f"Medication data updated."


class ReturnPreferredUnit(Command):
    """Returns the preferred unit for the specified Medication.

    Methods:
        execute: Executes the command, returns results."""

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

    def execute(self, medication_code: str) -> str:
        """Executes the command, returns results."""
        criteria = {"medication_code": medication_code}

        cursor = self._receiver.read("medications", criteria)
        return cursor.fetchall()[0][4]
