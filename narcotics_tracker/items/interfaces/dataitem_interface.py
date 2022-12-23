"""Defines the interface for items stored in the database.

Classes:
    DatabaseItems: The interface for items which are stored in the database.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from narcotics_tracker.typings import DateType, NTTypes

# pylint: disable=[invalid-name]


@dataclass
class DataItem(ABC):
    """The interface for items which are stored in the database.

    Attributes:
        table (str): Name of the table the item belongs to.

        id (int): Numeric identifier of the item.

        created_date (int): Unix timestamp when the item was first added.

        modified_date (int): Unix timestamp when the item was last modified.

        modified_by (str): The name of the user who last modified the item.
    """

    table: Optional[str]
    id: Optional[int]
    created_date: Optional[DateType]
    modified_date: Optional[DateType]
    modified_by: Optional[str]

    @abstractmethod
    def __str__(self) -> str:
        """Returns a string representation of the item."""
