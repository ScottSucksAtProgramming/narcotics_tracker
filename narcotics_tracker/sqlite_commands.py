"""Contains the commands for the SQLite3 Database.

Classes:

"""

from typing import Union

from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.items.data_items import DataItem
from narcotics_tracker.sqlite_commands_interface import SQLiteCommand


# * Table Creation Commands
class CreateEventsTable(SQLiteCommand):

    table_name = "events"
    column_info = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "event_code": "TEXT NOT NULL",
        "event_name": "TEXT NOT NULL",
        "description": "TEXT NOT NULL",
        "modifier": "INTEGER NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(self, receiver: SQLiteManager) -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the events table in the SQLite3 database."""
        self.receiver.create_table(self.table_name, self.column_info)


class CreateInventoryTable(SQLiteCommand):
    table_name = "inventory"
    column_info = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "adjustment_date": "INTEGER NOT NULL",
        "event_code": "TEXT NOT NULL",
        "medication_code": "TEXT NOT NULL",
        "amount": "INTEGER NOT NULL",
        "reporting_period_id": "INTEGER NOT NULL",
        "reference_id": "TEXT NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    foreign_key_info = [
        "FOREIGN KEY (event_code) REFERENCES events (event_code) ON UPDATE CASCADE",
        "FOREIGN KEY (medication_code) REFERENCES medications (medication_code) ON UPDATE CASCADE",
        "FOREIGN KEY (reporting_period_id) REFERENCES reporting_periods (id) ON UPDATE CASCADE",
    ]

    def __init__(self, receiver: SQLiteManager) -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the inventory table in the SQLite3 database."""
        self.receiver.create_table(
            table_name=self.table_name,
            column_info=self.column_info,
            foreign_key_info=self.foreign_key_info,
        )


class CreateMedicationsTable(SQLiteCommand):
    table_name = "medications"
    column_info = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "medication_code": "TEXT NOT NULL UNIQUE",
        "medication_name": "TEXT NOT NULL",
        "medication_amount": "REAL NOT NULL",
        "preferred_unit": "TEXT NOT NULL",
        "fill_amount": "REAL NOT NULL",
        "concentration": "REAL NOT NULL",
        "status": "TEXT NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    foreign_key_info = [
        "FOREIGN KEY (preferred_unit) REFERENCES units (unit_code) ON UPDATE CASCADE",
        "FOREIGN KEY (status) REFERENCES statuses (status_code) ON UPDATE CASCADE",
    ]

    def __init__(self, receiver: SQLiteManager) -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the medications table in the SQLite3 database."""
        self.receiver.create_table(
            self.table_name, self.column_info, self.foreign_key_info
        )


class CreateReportingPeriodsTable(SQLiteCommand):
    table_name = "reporting_periods"
    column_info = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "start_date": "INTEGER NOT NULL",
        "end_date": "INTEGER NOT NULL",
        "status": "TEXT NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(self, receiver: SQLiteManager) -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the reporting periods table in the SQLite3 database."""
        self.receiver.create_table(self.table_name, self.column_info)


class CreateStatusesTable(SQLiteCommand):
    table_name = "statuses"
    column_info = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "status_code": "TEXT NOT NULL UNIQUE",
        "status_name": "TEXT NOT NULL",
        "description": "TEXT NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(self, receiver: SQLiteManager) -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the statuses table in the SQLite3 database."""
        self.receiver.create_table(self.table_name, self.column_info)


class CreateUnitsTable(SQLiteCommand):
    table_name = "units"
    column_info = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "unit_code": "TEXT NOT NULL UNIQUE",
        "unit_name": "TEXT NOT NULL",
        "decimals": "INTEGER NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(self, receiver: SQLiteManager) -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the units table in the SQLite3 database."""
        self.receiver.create_table(self.table_name, self.column_info)


# * Item Storage Commands
class SaveItem(SQLiteCommand):
    """Saves a data item to the appropriate table in the database."""

    def __init__(self, receiver: SQLiteManager, item: DataItem) -> None:
        self.receiver = receiver
        self.dataitem = item

    def execute(self) -> str:
        """Executes the command, returns success message."""
        self._extract_item_info()
        table_name = self._extract_table_name()

        self.receiver.add(table_name, self.item_info)

        return f"Item added to {table_name} table."

    def _extract_item_info(self) -> None:
        """Extracts item attributes and stored as a dictionary."""
        self.item_info = vars(self.dataitem)

    def _extract_table_name(self) -> str:
        """Removes and returns the table name from DataItem information.

        #! Note: The 'table' key and value are removed from self.item_info.

        Returns:
            string: Name of the table.
        """
        return self.item_info.pop("table")


class DeleteAdjustment(SQLiteCommand):
    """Deletes an Adjustment from the database by its ID."""

    def __init__(self, receiver: SQLiteManager, adjustment_id: int) -> None:
        """Sets the SQLiteManager and adjustment_id."""
        self.receiver = receiver
        self.target_id = adjustment_id

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        self.receiver.delete("inventory", {"id": self.target_id})

        return f"Adjustment #{self.target_id} deleted."


class DeleteEvent(SQLiteCommand):
    """Deletes an Event from the database by its ID or code."""

    def __init__(
        self, receiver: SQLiteManager, event_identifier: Union[int, str]
    ) -> None:
        """Sets the SQLiteManager and event identifier.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            event_identifier (int OR str): Unique ID or event_code of the
                event.
        """
        self.receiver = receiver
        self.target_identifier = event_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self.target_identifier) is int:
            criteria = {"id": self.target_identifier}

        if type(self.target_identifier) is str:
            criteria = {"event_code": self.target_identifier}

        self.receiver.delete("events", criteria)

        return f"Event {self.target_identifier} deleted."


class DeleteMedication(SQLiteCommand):
    """Deletes a Medication from the database by its ID or code."""

    def __init__(
        self, receiver: SQLiteManager, medication_identifier: Union[int, str]
    ) -> None:
        """Sets the SQLiteManager and medication identifier.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            medication_identifier (int OR str): Unique ID or Medication_code
                of the Medication.
        """
        self.receiver = receiver
        self.target_identifier = medication_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self.target_identifier) is int:
            criteria = {"id": self.target_identifier}

        if type(self.target_identifier) is str:
            criteria = {"medication_code": self.target_identifier}

        self.receiver.delete("medications", criteria)

        return f"Medication {self.target_identifier} deleted."


class DeleteReportingPeriod(SQLiteCommand):
    """Deletes a ReportingPeriod from the database by its ID."""

    def __init__(self, receiver: SQLiteManager, reporting_period_id: int) -> None:
        """Sets the SQLiteManager and reporting_period_id."""
        self.receiver = receiver
        self.target_id = reporting_period_id

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        self.receiver.delete("reporting_periods", {"id": self.target_id})

        return f"Reporting Period #{self.target_id} deleted."


class DeleteStatus(SQLiteCommand):
    """Deletes a Status from the database by its ID or code."""

    def __init__(
        self, receiver: SQLiteManager, status_identifier: Union[int, str]
    ) -> None:
        """Sets the SQLiteManager and Status identifier.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            status_identifier (int OR str): Unique ID or status_code
                of the Status.
        """
        self.receiver = receiver
        self.target_identifier = status_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self.target_identifier) is int:
            criteria = {"id": self.target_identifier}

        if type(self.target_identifier) is str:
            criteria = {"status_code": self.target_identifier}

        self.receiver.delete("statuses", criteria)

        return f"Status {self.target_identifier} deleted."


class DeleteUnit(SQLiteCommand):
    """Deletes a Unit from the database by its ID or code."""

    def __init__(
        self, receiver: SQLiteManager, unit_identifier: Union[int, str]
    ) -> None:
        """Sets the SQLiteManager and unit's identifier.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            Unit_identifier (int OR str): Unique ID or unit_code
                of the Unit.
        """
        self.receiver = receiver
        self.target_identifier = unit_identifier

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        if type(self.target_identifier) is int:
            criteria = {"id": self.target_identifier}

        if type(self.target_identifier) is str:
            criteria = {"unit_code": self.target_identifier}

        self.receiver.delete("units", criteria)

        return f"Unit {self.target_identifier} deleted."
