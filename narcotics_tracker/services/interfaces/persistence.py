"""Defines the protocol for communication with data repositories.

Classes:
    PersistenceService: Protocol for communicating with a data repository.
    """


from typing import TYPE_CHECKING, Any, Optional, Protocol

if TYPE_CHECKING:
    from narcotics_tracker.typings import NTTypes


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

    def add(self, table_name: str, data: "NTTypes.sqlite_types"):
        """Adds new data to the repository."""

    def remove(self, table_name: str, criteria: "NTTypes.sqlite_types"):
        """Deletes data from the repository."""

    def read(
        self,
        table_name: str,
        criteria: "NTTypes.sqlite_types",
        order_by: Optional[str] = None,
    ) -> Any:
        """Returns data from the repository."""

    def update(
        self,
        table_name: str,
        data: "NTTypes.sqlite_types",
        criteria: "NTTypes.sqlite_types",
    ):
        """Updates data in the repository."""
