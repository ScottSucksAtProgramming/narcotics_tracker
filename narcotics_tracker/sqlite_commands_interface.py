"""Defines the protocol for commands which interact with the SQLite3 database.

Classes: 
    SQLiteCommand: The interface for SQLite3 database commands.

"""

from typing import Protocol

from narcotics_tracker.database import SQLiteManager


class SQLiteCommand(Protocol):
    """The interface for SQLite3 database commands.

    Required method signatures:
        def __init__(self, receiver: SQLiteManager) -> None:

        def execute(self) -> None:
    """

    def __init__(self, receiver: SQLiteManager) -> None:
        ...

    def execute(self) -> None:
        ...
