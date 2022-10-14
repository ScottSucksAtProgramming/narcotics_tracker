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

    Required Attributes:

        - _filename:
    """

    def __init__(self, filename: str = "inventory.db") -> "DatabaseInterface":
        """Initializes the database object and sets it's connection to None.

        Validates the file name. Sets the connection to None. Sets the path to
        the database files to the data directory.

        Args:
            filename (str): the filename of the database the object will
                connect to.
        """
        _, extension = filename.split(".")
        if extension != "db":
            raise ValueError("The filename must have the extension '.db'")

        self.connection = None
        self.path = "data/"
        self._filename = filename

    @abstractmethod
    def __enter__(self):
        """Connects to the database as a context manager."""

    @abstractmethod
    def __exit__(self, type, value, traceback):
        """Closes the connection when exiting the context manager."""

    @abstractmethod
    def connect(self):
        """Makes a connection with the database."""

    @abstractmethod
    def disconnect(self):
        """Disconnect from the database."""

    @property
    def filename(self) -> str:
        """Returns the filename of the database the object will connect to.

        Returns:
            str: The filename of the database file.
        """
        return self._filename

    @filename.setter
    def filename(self, filename: str) -> None:
        """Sets the filename of the database the object will connect to.

        Args:
            filename (str): The name of the database file.
        """
        _, extension = filename.split(".")
        if extension != "db":
            raise ValueError("The filename must have the extension '.db'")

        self._filename = filename
