"""Contains the interface for concrete DataItem builders.

Classes:

"""

from abc import ABC

from narcotics_tracker.items.data_items import DataItem


class BuilderInterface(ABC):
    """Defines the interface for concrete DataItem builders."""

    def set_table(self) -> None:
        """Sets the name of the table the DataItem belongs to."""

    def set_id(self) -> None:
        """Sets the numeric ID of the DataItem."""

    def set_created_date(self) -> None:
        """Sets the unix timestamp of when the DataItem was created."""

    def set_modified_date(self) -> None:
        """Sets the unix timestamp of when the DataItem was last modified."""

    def set_modified_by(self) -> None:
        """Sets the name of the user who last modified the DataItem."""

    def build(self) -> DataItem:
        """Returns the constructed DataItem."""
