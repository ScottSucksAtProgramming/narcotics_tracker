"""Defines the protocol for communication with data repositories.

Classes:
    PersistenceServiceForDatabase: Protocol for communicating with a data repository.
    """


from typing import Any, Optional, Protocol, Union

from narcotics_tracker.typings import NTTypes


class PersistenceServiceForDatabase(Protocol):
    """Protocol for communicating with a database.

    Classes using this protocol must be able to store and retrieve data from
    the data repository using the methods declared below.

    Methods:
        add: Adds new data to the repository.

        remove: Deletes data from the repository.

        read: Returns data from the repository.

        update: Updates data in the repository.
    """

    def add(self, table_name: str, data: NTTypes.sqlite_types):
        """Adds new data to the repository."""

    def remove(self, table_name: str, criteria: NTTypes.sqlite_types):
        """Deletes data from the repository."""

    def read(
        self,
        table_name: str,
        criteria: NTTypes.sqlite_types,
        order_by: Optional[str] = None,
    ) -> Any:
        """Returns data from the repository."""

    def update(
        self,
        table_name: str,
        data: NTTypes.sqlite_types,
        criteria: NTTypes.sqlite_types,
    ):
        """Updates data in the repository."""

    def create_table(
        self,
        table_name: str,
        column_info: dict[str, str],
        foreign_key_info: Optional[list[str]] = None,
    ) -> None:
        "Adds tables to the database."
