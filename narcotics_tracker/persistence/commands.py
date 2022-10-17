"""Contains the commands which affect the SQLite3 database.

Classes:

"""
import time

from narcotics_tracker.persistence.database import SQLiteManager
from narcotics_tracker.persistence.sqlite_command import SQLiteCommand


class SaveAdjustment(SQLiteCommand):
    """Adds an adjustment to the inventory table of the SQLite3 database."""

    def __init__(self, receiver: SQLiteManager) -> None:
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

    class CreateEventsTable(SQLiteCommand):
        """Creates the Events Table."""
        
        def __init__():

    class SaveEvent(SQLiteCommand):
        """Adds an Event to the Events Table of the SQLite3 database."""

        def __init__(self, receiver: SQLiteManager) -> None:
            """Initializes the command and pairs it with a receiver instance.

            Args:
                receiver (SQLiteManager): The target of the command.
            """
            self.table_name = "events"
            self.target = receiver

        def execute(self, event_data: dict[str]) -> str:
            """Executes the command, returns a message if successful.

            Args:
                event_data (dict[str]): A dictionary of event data mapping
                    column names to values.
            """
            current_timestamp = int(time.time())
            event_data["created_date"] = current_timestamp
            event_data["modified_date"] = current_timestamp
            self.target.add(self.table_name, event_data)
