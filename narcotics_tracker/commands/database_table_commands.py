"""Creates and modifies tables in the SQLite3 database.

Please review the package documentation for information on using commands.
"""
from typing import TYPE_CHECKING

from narcotics_tracker.commands.interfaces.command_interface import Command

if TYPE_CHECKING:
    from narcotics_tracker.services.sqlite_manager import SQLiteManager


class CreateEventsTable(Command):

    table_name = "events"
    column_info = {
        "id": "INTEGER PRIMARY KEY",
        "event_code": "TEXT NOT NULL UNIQUE",
        "event_name": "TEXT NOT NULL",
        "description": "TEXT NOT NULL",
        "modifier": "INTEGER NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(self, receiver: "SQLiteManager") -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the events table in the SQLite3 database."""
        self.receiver.create_table(self.table_name, self.column_info)


class CreateInventoryTable(Command):
    table_name = "inventory"
    column_info = {
        "id": "INTEGER PRIMARY KEY",
        "adjustment_date": "INTEGER NOT NULL",
        "event_code": "TEXT NOT NULL",
        "medication_code": "TEXT NOT NULL",
        "amount": "REAL NOT NULL",
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

    def __init__(self, receiver: "SQLiteManager") -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the inventory table in the SQLite3 database."""
        self.receiver.create_table(
            table_name=self.table_name,
            column_info=self.column_info,
            foreign_key_info=self.foreign_key_info,
        )


class CreateMedicationsTable(Command):
    table_name = "medications"
    column_info = {
        "id": "INTEGER PRIMARY KEY",
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

    def __init__(self, receiver: "SQLiteManager") -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the medications table in the SQLite3 database."""
        self.receiver.create_table(
            self.table_name, self.column_info, self.foreign_key_info
        )


class CreateReportingPeriodsTable(Command):
    table_name = "reporting_periods"
    column_info = {
        "id": "INTEGER PRIMARY KEY",
        "start_date": "INTEGER NOT NULL",
        "end_date": "INTEGER",
        "status": "TEXT NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(self, receiver: "SQLiteManager") -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the reporting periods table in the SQLite3 database."""
        self.receiver.create_table(self.table_name, self.column_info)


class CreateStatusesTable(Command):
    table_name = "statuses"
    column_info = {
        "id": "INTEGER PRIMARY KEY",
        "status_code": "TEXT NOT NULL UNIQUE",
        "status_name": "TEXT NOT NULL",
        "description": "TEXT NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(self, receiver: "SQLiteManager") -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the statuses table in the SQLite3 database."""
        self.receiver.create_table(self.table_name, self.column_info)


class CreateUnitsTable(Command):
    table_name = "units"
    column_info = {
        "id": "INTEGER PRIMARY KEY",
        "unit_code": "TEXT NOT NULL UNIQUE",
        "unit_name": "TEXT NOT NULL",
        "decimals": "INTEGER NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(self, receiver: "SQLiteManager") -> None:
        self.receiver = receiver

    def execute(self):
        """Creates the units table in the SQLite3 database."""
        self.receiver.create_table(self.table_name, self.column_info)
