"""Contains the protocol for any commands which affect the SQLite3 database.

Classes: 
    SQLiteCommand: The interface for SQLite3 database commands.

"""

from typing import Protocol


class SQLiteCommand(Protocol):
    """The interface for SQLite3 database commands."""

    def execute(self) -> None:
        ...
