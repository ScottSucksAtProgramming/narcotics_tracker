"""Contains Adjustments which make changes to the inventory amounts.

Classes: 
"""

from dataclasses import dataclass

from narcotics_tracker.items import database_items


@dataclass
class Adjustment(database_items.DatabaseItem):
    """The Adjustments which affect the inventory amounts.

    Attributes:
        adjustment_date (int): The date the adjustment took place.
        event_code (str): The code of the event that triggered the adjustment. Must
            match an event_code from the events table.
        medication_code (str): The code of the medication which is being adjusted.
            Must match a medication_code from the medications table.
        adjustment_amount (float): The amount of medication (in the preferred unit)
            which was adjusted during the event.
        reference_id (str): The identifier of the document containing
            additional information about the adjustment. (i.e. PCR Number,
            Purchase Order Number)

    Methods:
        add: Adds the adjustment to the inventory table.
        delete: Deletes the adjustment from the inventory table.
        update: Updates the adjustment in the inventory table.

    Class Methods:
        load: Loads an adjustment object from data in the inventory table.
    """

    adjustment_date: int
    event_code: str
    medication_code: str
    adjustment_amount: float
    reference_id: str

    def add(self):
        """Adds the adjustment to the inventory table."""

    def delete(self):
        """Removes the adjustment from the inventory table."""

    def update(self):
        """Updates the adjustment in the inventory table."""

    @classmethod
    def load(self):
        """Loads an adjustment object from data in the inventory table."""
