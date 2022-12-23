"""Defines the "builder" for generic DataItems. Only meant to be inherited from.

Classes:

    DataItemBuilder: Builds a generic DataItem. Intended to be inherited by
        other builders.

"""
from typing import TYPE_CHECKING, Optional

from narcotics_tracker.builders.interfaces.builder import Builder
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import DateTypes

if TYPE_CHECKING:
    from narcotics_tracker.items.interfaces.dataitem_interface import DataItem
    from narcotics_tracker.services.interfaces.service_provider import ServiceProvider


class DataItemBuilder(Builder):
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

    _service_provider: "ServiceProvider" = ServiceManager()
    _dataitem: "DataItem"

    def __init__(self) -> None:
        """Calls the _reset method."""
        self._reset()

    def set_table(self, table_name: str) -> "Builder":
        """Sets the table attribute."""
        self._dataitem.table = table_name

        return self

    def set_id(self, id_number: Optional[int] = None) -> "Builder":
        """Sets the id attribute to None, unless overridden."""
        self._dataitem.id = id_number
        return self

    def set_created_date(self, date: Optional[DateTypes] = None) -> "Builder":
        """Sets the attribute to the current datetime, unless overridden.

        Args:
            date (int, str, optional): Unix timestamp, or formatted date time
                string (MM-DD-YYYY HH:MM:SS). If None, will use the current
                datetime.
        """
        if date is None:
            date = ServiceManager().datetime.return_current()

        valid_date = self._validate_date(date)
        self._dataitem.created_date = valid_date
        return self

    def set_modified_date(self, date: Optional[DateTypes] = None) -> "Builder":
        """Sets the attribute to the current datetime, unless overridden.

        Args:
            date (int, str, optional): Unix timestamp, or formatted date time
                string (MM-DD-YYYY HH:MM:SS). If None, will use the current
                datetime.
        """
        if date is None:
            date = ServiceManager().datetime.return_current()

        valid_date = self._validate_date(date)
        self._dataitem.modified_date = valid_date
        return self

    def _validate_date(self, raw_date: DateTypes) -> int:
        """Runs dates through validator. Sets the instance variables correctly."""

        date = self._service_provider.datetime.validate(raw_date)
        return date

    def set_modified_by(self, modified_by: str) -> "Builder":
        """Sets the modified by attribute to the passed string."""
        self._dataitem.modified_by = modified_by
        return self

    def build(self) -> "DataItem":
        """Returns the DataItem object."""
        raise NotImplementedError

    def _reset(self) -> None:
        """Sets all attributes to default."""
        raise NotImplementedError
