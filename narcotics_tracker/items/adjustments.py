"""Contains Adjustments which make changes to the inventory amounts.

Classes: 
"""

from dataclasses import dataclass

from narcotics_tracker.items.data_items import DataItem
from narcotics_tracker.persistence.sqlite_command import SQLiteCommand


@dataclass
class Adjustment(DataItem):
    """The Adjustments which affect the inventory amounts.

    Attributes:
        adjustment_date (int): The date the adjustment took place.
        event_code (str): The code of the event that triggered the adjustment.
            Must match an event_code from the events table.
        medication_code (str): The code of the medication which is being
            adjusted. Must match a medication_code from the medications table.
        adjustment_amount (float): The amount of medication (in the preferred
            unit) which was adjusted during the event.
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

    def add(self, target: SQLiteCommand) -> None:
        """Adds the adjustment to the inventory table."""
        adjustment_data = {
            "adjustment_date": str(self.adjustment_date),
            "event_code": str(self.event_code),
            "medication_code": str(self.medication_code),
            "amount_in_mcg": converted_amount,  # use a converter class to obtain the information required to convert between the units and to return the converted amounts.
            "reference_id": str(self.reference_id),
            "created_date": self.created_date or None,
            "modified_date": None,
            "modified_by": None,
        }
        target.execute()

        # TODO: Next Steps
        """I need to be able to convert between the preferred units and the 
        standard units when exchanging information with the database. 
        Conversions should be compeleted in their own object, these item 
        classes are only responsible for storing the data required to build 
        the object. Manipulating that data should not happen within the class, 
        which would be mutation. Instead maniuplate the data just before it's 
        saved in the persistence layer, or just before it's return to the 
        user.
        
        The user interface should always use the preferred unit, as that's how 
        the users are going to be able to understand the medication.
        """

        """The DatabaseItem symbol should be changed to DataItems incase a new 
        persistence mechanism is implemented.
        """

    def delete(self, target: SQLiteCommand) -> None:
        """Removes the adjustment from the inventory table."""
        target.execute()

    def update(self, target: SQLiteCommand) -> None:
        """Updates the adjustment in the inventory table."""
        target.execute()

    @classmethod
    def load(cls) -> "Adjustment":
        """Loads an adjustment object from data in the inventory table."""

    # Todo: Implement.
