"""Contains the commands to save DataItems into the database.

Please see Package documentation for more information.
"""

from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.items.data_items import DataItem
from narcotics_tracker.sqlite_commands_interface import SQLiteCommand
from narcotics_tracker.utils.date_and_time import DateTimeManager


class SaveItem(SQLiteCommand):
    """Saves a data item to the appropriate table in the database."""

    def __init__(
        self, receiver: SQLiteManager, item: DataItem, datetime_manager: DateTimeManager
    ) -> None:
        self.receiver = receiver
        self.dataitem = item
        self.datetime_manager = datetime_manager

    def execute(self) -> str:
        """Executes the command, returns success message."""
        if self._item_created_date_is_none:
            self._assign_created_date()

        if self._item_modified_date_is_none:
            self._assign_modified_date()

        self._extract_item_info()
        table_name = self._pop_table_name()

        self.receiver.add(table_name, self.item_info)

        return f"Item added to {table_name} table."

    def _assign_created_date(self) -> None:
        """Assigns the DataItem's created_date if it is None."""
        datetime = self.datetime_manager.return_current_datetime()
        self.dataitem.created_date = datetime

    def _assign_modified_date(self) -> None:
        """Updates the DataItem's the modified_date."""
        if self._item_modified_date_is_none:
            self.dataitem.modified_date = self.dataitem.created_date
        else:
            datetime = self.datetime_manager.return_current_datetime()
            self.dataitem.created_date = datetime

    def _extract_item_info(self) -> None:
        """Extracts item attributes and stored as a dictionary."""
        self.item_info = vars(self.dataitem)

    def _pop_table_name(self) -> str:
        """Removes and returns the table name from DataItem information.

        Returns:
            string: Name of the table.
        """
        return self.item_info.pop("table")

    def _item_created_date_is_none(self) -> bool:
        """Returns True if created_date is None. Otherwise returns False."""
        return True if self.dataitem.created_date is None else False

    def _item_modified_date_is_none(self) -> bool:
        """Returns True if created_date is None. Otherwise returns False."""
        return True if self.dataitem.modified_date is None else False
