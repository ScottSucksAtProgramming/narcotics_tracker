"""Defines the changes which occur to the inventory.

Classes:
    Adjustment: A change which occurred to the inventory.
"""

from dataclasses import dataclass, field

from narcotics_tracker.items.interfaces.dataitem_interface import DataItem
from typing import Optional


@dataclass
class Adjustment(DataItem):
    """A change which occurred to the inventory.

    Attributes:
        adjustment_date (int): Unix timestamp when the adjustment occurred.

        event_code (str): Unique code of the event that caused the adjustment.

        medication_code (str): Unique code of the medication being adjusted.

        amount (float): Amount of medication being adjusted.

        reference_id (str): ID of the document containing more adjustment info.

        reporting_period_id (int): ID of the period adjustment occurred during.
    """

    
    adjustment_date: int
    event_code: str
    medication_code: str
    amount: float
    reference_id: str
    reporting_period_id: int
    table: str
    def __str__(self) -> str:
        return (
            f"Adjustment #{self.id}: {self.medication_code} adjusted by "
            f"{self.amount} due to {self.event_code} on {self.adjustment_date}."
        )
