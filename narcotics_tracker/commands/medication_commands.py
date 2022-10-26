"""Contains the commands for Medications.

Please see the package documentation for more information.
"""

from typing import Union

from narcotics_tracker.commands.interfaces.command_interface import SQLiteCommand
from narcotics_tracker.items.medications import Medication
from narcotics_tracker.services.interfaces.persistence_interface import (
    PersistenceService,
)
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class AddMedication(SQLiteCommand):
    """Adds an Medication to the database.

    Methods:
        execute: Executes the command, returns success message.
    """

    def __init__(self, receiver: PersistenceService, medication: Medication) -> None:
        """Initializes the command. Sets the receiver and Medication.

        Args:
            receiver (PersistenceManager): Persistence manager for the data
                repository.

            Medication: The Medication to be added to the database.
        """
        self._receiver = receiver
        self._medication = medication

    def execute(self) -> str:
        """Executes the command, returns success message."""

        self._extract_medication_info()
        table_name = self._pop_table_name()

        self._receiver.add(table_name, self.medication_info)

        return f"Medication added to {table_name} table."

    def _extract_medication_info(self) -> None:
        """Extracts medication attributes and stores as a dictionary."""
        self.medication_info = vars(self._medication)

    def _pop_table_name(self) -> str:
        """Removes and returns the table name from Medication's attributes.

        Returns:
            string: Name of the table.
        """
        return self.medication_info.pop("table")


class DeleteMedication(SQLiteCommand):
    """Deletes a Medication from the database by its ID or code."""

    def __init__(
        self, receiver: SQLiteManager, medication_identifier: Union[int, str]
    ) -> None:
        """Sets the SQLiteManager and medication identifier.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            medication_identifier (int OR str): Unique ID or Medication_code
                of the Medication.
        """
        self._target = receiver
        self._dataitem_id = medication_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self._dataitem_id) is int:
            criteria = {"id": self._dataitem_id}

        if type(self._dataitem_id) is str:
            criteria = {"medication_code": self._dataitem_id}

        self._target.remove("medications", criteria)

        return f"Medication {self._dataitem_id} deleted."


class ListMedications(SQLiteCommand):
    """Returns a list of Medications."""

    def __init__(
        self,
        receiver: SQLiteManager,
        criteria: dict[str] = {},
        order_by: str = None,
    ):
        """Sets the SQLiteManager, criteria and order_by column.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            criteria (dict[str, any], optional): Criteria of medications to be
                returned as a dictionary mapping column names to values.

            order_by (str, optional): Column name by which to sort the results.
        """
        self._target = receiver
        self._criteria = criteria
        self._order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Medications."""

        cursor = self._target.read("medications", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateMedication(SQLiteCommand):
    """Update a Medication with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self._target = receiver
        self._data = data
        self._criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._target.update("medications", self._data, self._criteria)

        return f"Medication data updated."
