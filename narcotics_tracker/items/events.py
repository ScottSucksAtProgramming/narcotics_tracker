"""Defines the type of events which can affect the inventory.

Classes: 
    Event: A type of event which can affect the inventory.
"""

from dataclasses import dataclass

from narcotics_tracker.items.data_items import DataItem


@dataclass
class Event(DataItem):
    """A type of event which can affect the inventory.

    Attributes:
        event_code (str): Unique code identifying the event.
        event_name (str): Name of the event.
        description (str): Description of the event.
        modifier (int): (+1 or -1) Specifies if the event adds or removes from the inventory.
    """

    event_code: str
    event_name: str
    description: str
    modifier: int

    def __str__(self):
        return f"Event #{self.id}: {self.event_name} - {self.description}"
