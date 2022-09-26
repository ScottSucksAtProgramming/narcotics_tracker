"""Contains the interface used for interacting with persistent storage.

Classes:

    PersistenceInterface: Defines the interface for interacting with 
        persistent storage.
"""

from abc import ABC, abstractmethod


class PersistenceInterface(ABC):
    """Defines the interface for interacting with persistent storage.

    These objects must be able to:

        - Be initialized as objects.
        - Write data to storage using a `create()` method.
        - Return data from storage as a list using a `read()` method.
        - Update data saved in storages using a `update()` method.
        - Delete data from storage using a `delete()` method.
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
