"""Defines the protocol for commands which interact with the SQLite3 database.

Classes:
    SQLiteCommand: The interface for SQLite3 database commands.

"""
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class Command(Protocol):
    """The interface for SQLite3 database commands.

    Required method signatures:
        def __init__(self, receiver) -> None:

        def execute(self) -> None:
    """

    def __init__(self, receiver: "PersistenceService") -> None:
        """Sets the receiver of the command."""

    def execute(self) -> str:
        """Executes the command. Accepts parameters required by the receiver."""
        return ""
