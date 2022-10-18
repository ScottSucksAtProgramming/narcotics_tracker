"""Contains the interface for concrete DataItem builders.

Classes:

"""

from abc import ABC, abstractmethod

from narcotics_tracker.items.data_items import DataItem


class BuilderInterface(ABC):
    """Defines the interface for concrete DataItem builders.

    Methods:
        __init__: Initializes the builder with an empty DataItem object.
        set_table: Sets the table attribute.
        set_id: Sets the id attribute to None, unless overridden.
        set_created_date: Sets the created date to None, unless overridden.
        set_modified_date: Sets the modified date to None, unless overridden.
        set_modified_by: Sets the modified by attribute to the passed string.

    """

    def __init__(self) -> None:
        """Initializes the builder with an empty DataItem object."""
        self._reset()

    def set_table(self, table_name: str = None) -> "BuilderInterface":
        """Sets the table attribute.

        Args:
            table_name (str, optional): Name of the table. Defaults to None.
        """
        if self._table_name:
            self._dataitem.table = self._table_name
        else:
            self._dataitem.table = table_name

        return self

    def set_id(self, id_number: int = None) -> "BuilderInterface":
        """Sets the id attribute to None, unless overridden.

        Args:
            id_number (int, optional): Numeric identifier of the DataItem.
                Defaults to None.
        """
        self._dataitem.id = id_number
        return self

    def set_created_date(self, created_date: int = None) -> "BuilderInterface":
        """Sets the created date attribute to None, unless overridden.

        Args:
            created_date (int, optional): Unix timestamp of when the DataItem
                was created. Defaults to None.
        """
        self._dataitem.created_date = created_date
        return self

    def set_modified_date(self, modified_date: int = None) -> "BuilderInterface":
        """Sets the modified date to None, unless overridden.

        Args:
            modified_date (int, optional): Unix timestamp of when the DataItem
                was last modified. Defaults to None.
        """
        self._dataitem.modified_date = modified_date
        return self

    def set_modified_by(self, modified_by: str) -> "BuilderInterface":
        """Sets the modified by attribute to the passed string.

        Args:
            modified_by (str): Identifier of the user who last modified the
                DataItem.
        """
        self._dataitem.modified_by = modified_by
        return self

    @abstractmethod
    def build(self) -> DataItem:
        """Returns the constructed DataItem."""

    @abstractmethod
    def _reset(self) -> None:
        """Resets the builder to build a new DataItem."""
