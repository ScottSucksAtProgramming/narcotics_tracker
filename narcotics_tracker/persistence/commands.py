"""Contains the commands which affect the SQLite3 database.

Classes:

"""

from narcotics_tracker.persistence.database import SQLiteManager
from narcotics_tracker.persistence.sqlite_command import SQLiteCommand


class SaveAdjustment(SQLiteCommand):
    """Adds an adjustment to the inventory table of the SQLite3 database."""

    def __init__(self, receiver: SQLiteManager, adjustment_data: dict[str]) -> None:
        """Initializes the SaveAdjustment Command.

        Args:
            receiver (SQLiteManager): The target to receive the command.
            adjustment_data (dict[str]): A dictionary of adjustment data
                mapping column names to values.
        """
        self.table_name = "inventory"
        self.target = receiver

    def execute(self, adjustment_data: dict[str]) -> None:
        """Executes the command."""
        self.target.add(table_name=self.table_name, data=adjustment_data)
