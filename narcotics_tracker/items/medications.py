"""Represents controlled substance medications within the Narcotics Tracker.

Classes:
"""

from dataclasses import dataclass

from narcotics_tracker.items.data_items import DataItem
from narcotics_tracker.sqlite_command import SQLiteCommand


@dataclass
class Medication(DataItem):
    """Representation of a controlled substance medication."""

    medication_code: str
    medication_name: str
    fill_amount: float
    medication_amount: float
    preferred_unit: str
    concentration: float

    def add(self, target: SQLiteCommand) -> None:
        """Adds a new medication to the medications table."""
        medication_data = {
            "medication_code": self.medication_code,
            "medication_name": self.medication_name,
            "fill_amount": self.fill_amount,
            "medication_amount": self.medication_amount,
            "preferred_unit": self.preferred_unit,
            "concentration": self.concentration,
            "created_date": self.created_date or None,
            "modified_date": self.modified_date or None,
            "modified_by": None,
        }

    def delete(self, target: SQLiteCommand) -> None:
        """Removes a medication from the medication table."""

    def update(self, target: SQLiteCommand) -> None:
        """Updates a medication in the medication table."""

    @classmethod
    def load(cls) -> "Medication":
        """Loads a medication object from data in the medication table."""
