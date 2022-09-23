"""Contains the interface used for interacting with a database.

Classes:

    DatabaseInterface: Defines the interface for interacting with a database.
"""

from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    """Defines the interface for interacting with a database.

    These objects must be able to:

        - Act as a context manager.
        - Connect to a database.
        - Disconnect from the database.
    """

    @abstractmethod
    def __init__(self):
        """Initializes the object."""

    @abstractmethod
    def create(self):
        """Writes data into storage."""

    @abstractmethod
    def read(self) -> list:
        """Returns data from storage as a list."""

    @abstractmethod
    def update(self):
        """Updates data in storage."""

    @abstractmethod
    def delete(self):
        """Deletes data from storage."""
