"""Defines the protocol for communication with data repositories.

Classes:
    PersistenceService: Protocol for communicating with a data repository.
    """


from typing import Any, Optional, Protocol, Union


class PersistenceService(Protocol):
    """Protocol for communicating with a data repository.

    Classes using this protocol must be able to store and retrieve data from
    the data repository using the methods declared below.

    Methods:
        add: Adds new data to the repository.

        remove: Deletes data from the repository.

        read: Returns data from the repository.

        update: Updates data in the repository.
    """

    db_types = Union[str, int, float]

    def add(self, table_name: str, data: dict[str, db_types]):
        """Adds new data to the repository."""

    def remove(self, table_name: str, criteria: dict[str, db_types]):
        """Deletes data from the repository."""

    def read(
        self,
        table_name: str,
        criteria: dict[str, db_types],
        order_by: Optional[str] = None,
    ) -> Any:
        """Returns data from the repository."""

    def update(
        self,
        table_name: str,
        data: dict[str, db_types],
        criteria: dict[str, db_types],
    ):
        """Updates data in the repository."""
