"""Contains the interface for concrete DataItem builders.

Classes:

    BuilderInterface: Builds a generic DataItem. Intended to be inherited by 
        other builders.

"""
from typing import TYPE_CHECKING

from narcotics_tracker.builders.builder_interface import BuilderInterface

if TYPE_CHECKING:
    from narcotics_tracker.items.data_items import DataItem


class DataItemBuilder(BuilderInterface):
    """Builds a generic DataItem. Intended to be inherited by other builders.

    This class is meant to be inherited by other builders which create various
    data items.

    Methods:
        __init__: Calls the _reset method.
        set_table: Sets the table attribute.
        set_id: Sets the id attribute to None, unless overridden.
        set_created_date: Sets the created date to None, unless overridden.
        set_modified_date: Sets the modified date to None, unless overridden.
        set_modified_by: Sets the modified by attribute to the passed string.
    """

    def __init__(self) -> None:
        """Calls the _reset method."""
        self._reset()

    def set_table(self, table_name: str) -> BuilderInterface:
        """Sets the table attribute."""
        self._dataitem.table = table_name

        return self

    def set_id(self, id_number: int = None) -> BuilderInterface:
        """Sets the id attribute to None, unless overridden."""
        self._dataitem.id = id_number
        return self

    def set_created_date(self, created_date: int = None) -> BuilderInterface:
        """Sets the created date attribute to None, unless overridden."""
        self._dataitem.created_date = created_date
        return self

    def set_modified_date(self, modified_date: int = None) -> BuilderInterface:
        """Sets the modified date to None, unless overridden."""
        self._dataitem.modified_date = modified_date
        return self

    def set_modified_by(self, modified_by: str) -> BuilderInterface:
        """Sets the modified by attribute to the passed string."""
        self._dataitem.modified_by = modified_by
        return self

    def build(self) -> None:
        """Raises the NotImplementedError."""
        raise NotImplementedError

    def _reset(self) -> None:
        """Raises the NotImplementedError."""
        raise NotImplementedError
