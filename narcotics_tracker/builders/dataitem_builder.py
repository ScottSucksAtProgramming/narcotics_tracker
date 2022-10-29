"""Defines the builder for generic DataItems. Only meant to be inherited from.

Classes:

    DataItemBuilder: Builds a generic DataItem. Intended to be inherited by 
        other builders.

"""
from typing import TYPE_CHECKING, Union

from narcotics_tracker.builders.interfaces.builder_interface import BuilderInterface
from narcotics_tracker.services.service_provider import ServiceProvider

if TYPE_CHECKING:
    from narcotics_tracker.items.interfaces.dataitem_interface import DataItem


class DataItemBuilder(BuilderInterface):
    """Builds a generic DataItem. Intended to be inherited by other builders.

    This class is meant to be inherited by other builders which create various
    data items.

    Methods:
        __init__: Calls the _reset method.
        set_table: Sets the table attribute.
        set_id: Sets the id attribute to None, unless overridden.
        set_created_date: Sets the attribute to the current datetime, unless
            overridden.
        set_modified_date: Sets the attribute to the current datetime, unless
            overridden.
        set_modified_by: Sets the modified by attribute to the passed string.
    """

    datetime_service = ServiceProvider().datetime

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

    def set_created_date(self, date: Union[int, str] = None) -> BuilderInterface:
        """Sets the attribute to the current datetime, unless overridden.

        Args:
            date (int, str, optional): Unix timestamp, or formatted date time
                string (MM-DD-YYYY HH:MM:SS). If None, will use the current
                datetime.
        """
        self._dataitem.created_date = self.datetime_service.assign_datetime(date)
        return self

    def set_modified_date(self, date: Union[int, str] = None) -> BuilderInterface:
        """Sets the attribute to the current datetime, unless overridden.

        Args:
            date (int, str, optional): Unix timestamp, or formatted date time
                string (MM-DD-YYYY HH:MM:SS). If None, will use the current
                datetime.
        """
        self._dataitem.modified_date = self.datetime_service.assign_datetime(date)
        return self

    def set_modified_by(self, modified_by: str) -> BuilderInterface:
        """Sets the modified by attribute to the passed string."""
        self._dataitem.modified_by = modified_by
        return self

    def build(self) -> None:
        """Returns the DataItem object."""
        raise NotImplementedError

    def _reset(self) -> None:
        """Sets all attributes to default."""
