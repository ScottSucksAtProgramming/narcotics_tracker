"""Contains the commands for the SQLite3 Database.

Classes:

"""

from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.sqlite_interface import SQLiteCommand


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
        "amount_in_mcg": "INTEGER NOT NULL",
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
            self.table_name, self.column_info, self.foreign_key_info
        )


class CreateMedicationsTable(SQLiteCommand):
    table_name = "medications"
    column_info = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "medication_code": "TEXT NOT NULL UNIQUE",
        "medication_name": "TEXT NOT NULL",
        "dose_in_mcg": "REAL NOT NULL",
        "preferred_unit": "TEXT NOT NULL",
        "fill_amount": "REAL NOT NULL",
        "concentration": "REAL NOT NULL",
        "medication_status": "TEXT NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    foreign_key_info = [
        "FOREIGN KEY (preferred_unit) REFERENCES units (unit_code) ON UPDATE CASCADE",
        "FOREIGN KEY (medication_status) REFERENCES statuses (status_code) ON UPDATE CASCADE",
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
        "starting_date": "INTEGER NOT NULL",
        "ending_date": "INTEGER NOT NULL",
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
