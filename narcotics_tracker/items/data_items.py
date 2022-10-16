"""Contains the interface for items to be stored in the database.

Classes: 
    DatabaseItems: Defines the interface for items which are stored in the 
        database.
"""


from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class DataItem(ABC):
    """Defines the interface for items which are stored in the database.
    
    Attributes:
        table (str): The name of the table the item belongs to.
        column_info (dict[str]): Dictionary of column information for the 
            table, mapping column names to their datatypes and constraints.
        id (int): Numeric identifier of the item. Assigned by the database.
        created_date (int): Unix timestamp when the item was first created.
        modified_date (int): Unix timestamp when the item was last modified.
        modified_by (str): The name of the user who last modified the item.

    Methods:
        save: Saves the item in the database.
        delete: Deletes the item from the database.
        update: Updates the item in the database.
    """
    table: str 
    column_info: dict[str]
    id: int
    created_date: int
    modified_date: int
    modified-_by: str 


    @abstractmethod
    def save(self):
        """Saves the item in the database."""

    @abstractmethod
    def delete(self):
        """Delete the item from the database."""

    @abstractmethod
    def load(self):
        """Loads data from the database as an object."""

    @abstractmethod
    def update(self):
        """Updates the item in the database"""
