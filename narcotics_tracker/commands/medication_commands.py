"""Contains the commands for Medications.

Please see the package documentation for more information.
"""

from typing import Union

from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.sqlite_commands_interface import SQLiteCommand


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
        self.receiver = receiver
        self.target_identifier = medication_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self.target_identifier) is int:
            criteria = {"id": self.target_identifier}

        if type(self.target_identifier) is str:
            criteria = {"medication_code": self.target_identifier}

        self.receiver.delete("medications", criteria)

        return f"Medication {self.target_identifier} deleted."


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
        self.receiver = receiver
        self.criteria = criteria
        self.order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Medications."""

        cursor = self.receiver.select("medications", self.criteria, self.order_by)
        return cursor.fetchall()


class UpdateMedication(SQLiteCommand):
    """Update a Medication with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self.receiver = receiver
        self.data = data
        self.criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self.receiver.update("medications", self.data, self.criteria)

        return f"Medication data updated."
