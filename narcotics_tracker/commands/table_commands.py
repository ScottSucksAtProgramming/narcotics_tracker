"""Contains commands which created and modify tables in the SQLite3 database.

Please review the package documentation for information on using commands.

Classes:

    CreateEventsTable: Creates the 'events' table in the SQLite3 database.

    CreateInventoryTable: Creates the 'inventory' table in the SQLite3
        database.

    CreateMedicationsTable: Creates the 'medications' table in the SQLite3
        database.

    CreateReportingPeriodsTable: Creates the 'reporting_periods' table in the
        SQLite3 database.

    CreateStatusesTable: Creates the 'statuses' table in the SQLite3 database.

    CreateUnitsTable: Creates the 'units' table in the SQLite3 database.
"""
from typing import Optional

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.interfaces.persistence_db import (
    PersistenceServiceForDatabase,
)
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class CreateEventsTable(Command):
    """Creates the 'events' table in the SQLite3 database.

    Methods:
        execute: Executes the command.
    """

    _receiver: "PersistenceServiceForDatabase" = SQLiteManager("inventory.db")
    _table_name: str = "events"
    _column_info: dict[str, str] = {
        "id": "INTEGER PRIMARY KEY",
        "event_code": "TEXT NOT NULL UNIQUE",
        "event_name": "TEXT NOT NULL",
        "description": "TEXT NOT NULL",
        "modifier": "INTEGER NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(
        self, receiver: Optional["PersistenceServiceForDatabase"] = None
    ) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceServiceForDatabase, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self) -> None:
        """Executes the command."""
        self._receiver.create_table(self._table_name, self._column_info)


class CreateInventoryTable(Command):
    """Creates the 'inventory' table in the SQLite3 database.

    Methods:
        execute: Executes the command.
    """

    _receiver: "PersistenceServiceForDatabase" = SQLiteManager("inventory.db")
    _table_name: str = "inventory"
    _column_info: dict[str, str] = {
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

    _foreign_key_info = [
        "FOREIGN KEY (event_code) REFERENCES events (event_code) ON UPDATE CASCADE",
        "FOREIGN KEY (medication_code) REFERENCES medications (medication_code) ON UPDATE CASCADE",
        "FOREIGN KEY (reporting_period_id) REFERENCES reporting_periods (id) ON UPDATE CASCADE",
    ]

    def __init__(
        self, receiver: Optional["PersistenceServiceForDatabase"] = None
    ) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceServiceForDatabase, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self) -> None:
        """Executes the command."""
        self._receiver.create_table(
            table_name=self._table_name,
            column_info=self._column_info,
            foreign_key_info=self._foreign_key_info,
        )


class CreateMedicationsTable(Command):
    """Creates the 'medications' table in the SQLite3 database.

    Methods:
        execute: Executes the command.
    """

    _receiver: "PersistenceServiceForDatabase" = SQLiteManager("inventory.db")
    _table_name: str = "medications"
    _column_info: dict[str, str] = {
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

    _foreign_key_info = [
        "FOREIGN KEY (preferred_unit) REFERENCES units (unit_code) ON UPDATE CASCADE",
        "FOREIGN KEY (status) REFERENCES statuses (status_code) ON UPDATE CASCADE",
    ]

    def __init__(
        self, receiver: Optional["PersistenceServiceForDatabase"] = None
    ) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceServiceForDatabase, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self) -> None:
        """Executes the command."""
        self._receiver.create_table(
            self._table_name, self._column_info, self._foreign_key_info
        )


class CreateReportingPeriodsTable(Command):
    """Creates the 'reporting_periods' table in the SQLite3 database.

    Methods:
        execute: Executes the command.
    """

    _receiver: "PersistenceServiceForDatabase" = SQLiteManager("inventory.db")
    _table_name: str = "reporting_periods"
    _column_info: dict[str, str] = {
        "id": "INTEGER PRIMARY KEY",
        "start_date": "INTEGER NOT NULL",
        "end_date": "INTEGER",
        "status": "TEXT NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(
        self, receiver: Optional["PersistenceServiceForDatabase"] = None
    ) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceServiceForDatabase, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self) -> None:
        """Executes the command."""
        self._receiver.create_table(self._table_name, self._column_info)


class CreateStatusesTable(Command):
    """Creates the 'statuses' table in the SQLite3 database.

    Methods:
        execute: Executes the command.
    """

    _receiver: "PersistenceServiceForDatabase" = SQLiteManager("inventory.db")
    _table_name: str = "statuses"
    _column_info: dict[str, str] = {
        "id": "INTEGER PRIMARY KEY",
        "status_code": "TEXT NOT NULL UNIQUE",
        "status_name": "TEXT NOT NULL",
        "description": "TEXT NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(
        self, receiver: Optional["PersistenceServiceForDatabase"] = None
    ) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceServiceForDatabase, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self) -> None:
        """Executes the command."""
        self._receiver.create_table(self._table_name, self._column_info)


class CreateUnitsTable(Command):
    """Creates the 'units' table in the SQLite3 database.

    Methods:
        execute: Executes the command.
    """

    _receiver: "PersistenceServiceForDatabase" = SQLiteManager("inventory.db")
    _table_name: str = "units"
    _column_info: dict[str, str] = {
        "id": "INTEGER PRIMARY KEY",
        "unit_code": "TEXT NOT NULL UNIQUE",
        "unit_name": "TEXT NOT NULL",
        "decimals": "INTEGER NOT NULL",
        "created_date": "INTEGER NOT NULL",
        "modified_date": "INTEGER NOT NULL",
        "modified_by": "TEXT NOT NULL",
    }

    def __init__(
        self, receiver: Optional["PersistenceServiceForDatabase"] = None
    ) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self) -> None:
        """Executes the command."""
        self._receiver.create_table(self._table_name, self._column_info)
