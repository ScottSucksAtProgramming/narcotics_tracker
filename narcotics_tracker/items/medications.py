"""Defines the medications which are tracked.

Classes:
    Medication: A controlled substance medication which is tracked.
"""
from dataclasses import dataclass
from typing import Optional

from narcotics_tracker.items.interfaces.dataitem_interface import DataItem
from narcotics_tracker.services.service_manager import ServiceManager


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

    medication_code: Optional[str]
    medication_name: Optional[str]
    fill_amount: Optional[float]
    medication_amount: Optional[float]
    preferred_unit: Optional[str]
    concentration: Optional[float]
    status: Optional[str]

    def __str__(self) -> str:
        converter = ServiceManager().conversion
        if self.medication_amount is None:
            raise ValueError
        medication_amount = converter.to_preferred(
            self.medication_amount, self.preferred_unit
        )
        return (
            f"Medication #{self.id}: {self.medication_name} "
            f"({self.medication_code}) {medication_amount} "
            f"{self.preferred_unit} in {self.fill_amount} ml."
        )
