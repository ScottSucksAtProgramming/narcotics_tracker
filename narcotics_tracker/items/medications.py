"""Defines the medications which are tracked.

Classes:
    Medication: A controlled substance medication which is tracked.
"""

from dataclasses import dataclass

from narcotics_tracker.items.data_items import DataItem


@dataclass
class Medication(DataItem):
    """A controlled substance medication which is to be tracked.

    Attributes:
        medication_code (str): Unique code identifying the medication.
        medication_name (str): Name of the medication.
        fill_amount (float): Amount of liquid the medication is dissolved in.
        medication_amount (float): Amount of medication.
        preferred_unit (str): The unit of measurement for the medication.
        concentration (float): The ratio of medication to liquid.
        status (str): Status of the medication.
    """

    medication_code: str
    medication_name: str
    fill_amount: float
    medication_amount: float
    preferred_unit: str
    concentration: float
    status: str

    def __str__(self) -> str:
        return f"Medication #{self.id}: {self.medication_name} ({self.medication_code}) {self.medication_amount} {self.preferred_unit} in {self.fill_amount} ml."
