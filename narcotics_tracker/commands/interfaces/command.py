"""Defines the protocol for commands which interact with the SQLite3 database.

Classes: 
    SQLiteCommand: The interface for SQLite3 database commands.

"""
from typing import Protocol


class Command(Protocol):
    """The interface for SQLite3 database commands.

    Required method signatures:
        def __init__(self, receiver) -> None:

        def execute(self) -> None:
    """

    def __init__(self, receiver) -> None:
        """Sets the receiver of the command."""
        ...

    def execute(self) -> None:
        """Executes the command. Accepts parameters required by the receiver."""
        ...
