"""Defines the statuses for other data items.

Classes:
    Status: A status for other data items.
"""
from dataclasses import dataclass
from typing import Optional

from narcotics_tracker.items.interfaces.dataitem_interface import DataItem


@dataclass
class Status(DataItem):
    """A status for other data items.

    Attributes:
        status_code (str): Unique identifier for the status.

        status_name (str): Name of the status.

        description (str): Description of the status.

    """

    status_code: Optional[str]
    status_name: Optional[str]
    description: Optional[str]

    def __str__(self) -> str:
        return f"Status #{self.id}: {self.status_name} ({self.status_code}) {self.description}"
