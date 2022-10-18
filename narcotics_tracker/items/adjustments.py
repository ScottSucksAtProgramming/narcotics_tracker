"""Defines the changes where occur to the inventory.

Classes: 
    Adjustment: A change which occurred to the inventory.
"""

from dataclasses import dataclass

from narcotics_tracker.items.data_items import DataItem


@dataclass
class Adjustment(DataItem):
    """A change which occurred to the inventory.

    Attributes:
        adjustment_date (int): Unix timestamp when the adjustment occurred.
        event_code (str): Unique code of the event that caused the adjustment.
        medication_code (str): Unique code of the medication being adjusted.
        adjustment_amount (float): Amount of medication being adjusted.
        reference_id (str): ID of the document containing more adjustment info.
    """

    adjustment_date: int
    event_code: str
    medication_code: str
    adjustment_amount: float
    reference_id: str

    def __str__(self):
        return f"Adjustment #{self.id}: {self.medication_code} adjusted by {self.adjustment_amount} due to {self.event_code} on {self.adjustment_date}."
