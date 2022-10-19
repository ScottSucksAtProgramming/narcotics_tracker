"""Integration tests for creating tables within the SQLite3 database.

Classes:
    Test_TableCreationCommands: Performs integration testing for commands 
        that create tables.

Methods:
    return_expected_columns_from_command: Returns a list of column names 
        created from the given command.
    return_column_names_from_db: Returns a list of column names from the 
        passed SQLiteManager and table.
    return_table_names_from_db: Returns a list of table names from the passed 
        SQLiteManager.
"""

from narcotics_tracker import sqlite_commands
from narcotics_tracker.database import SQLiteManager


def return_expected_columns_from_command(
    command: sqlite_commands.SQLiteCommand,
) -> list[str]:
    """Returns a list of column names created from the given command."""
    columns = []
    for item in command.column_info.keys():
        columns.append(item)
    return columns


def return_column_names_from_db(db: SQLiteManager, table_name: str) -> list[str]:
    """Returns a list of column names from the passed SQLiteManager and table."""
    column_names = []

    cursor = db.select(table_name)
    data = cursor.description

    for _tuple in data:
        column_names.append(_tuple[0])

    return column_names


def return_table_names_from_db(db: SQLiteManager) -> list[str]:
    """Returns a list of table names from the passed SQLiteManager."""

    cursor = db._execute("""SELECT name FROM sqlite_master WHERE type = 'table'""")
    table_names = []
    data = cursor.fetchall()

    for item in data:
        table_names.append(item[0])

    return table_names


class Test_EventsTableCreation:
    """Tests that 'events' table is created by CreateEventsTable command.

    Behaviors Tested:
        - The 'events' table is created in the database.
        - All expected columns are created in the table.
    """

    def test_CreateEventsTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        sqlite_commands.CreateEventsTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "events" in table_names

    def test_CreateEventsTable_creates_expected_columns(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            sqlite_commands.CreateEventsTable
        )
        missing_columns = []

        sqlite_commands.CreateEventsTable(sq_manager).execute()
        column_names = return_column_names_from_db(sq_manager, "events")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []


class Test_InventoryTableCreation:
    """Tests that 'inventory' table is created by CreateInventoryTable command.

    Behaviors Tested:
        - The 'inventory' table is created in the database.
        - All expected columns are created in the table.
    """

    def test_CreateInventoryTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        sqlite_commands.CreateInventoryTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "inventory" in table_names

    def test_CreateInventoryTable_creates_expected_columns(
        self, reset_database
    ) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            sqlite_commands.CreateInventoryTable
        )
        missing_columns = []

        sqlite_commands.CreateInventoryTable(sq_manager).execute()

        column_names = return_column_names_from_db(sq_manager, "inventory")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []


class Test_MedicationsTableCreation:
    """Tests that 'medications' table is created by CreateMedicationsTable command.

    Behaviors Tested:
        - The 'medications' table is created in the database.
        - All expected columns are created in the table.
    """

    def test_CreateMedicationsTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        sqlite_commands.CreateMedicationsTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "medications" in table_names

    def test_CreateMedicationsTable_creates_expected_columns(
        self, reset_database
    ) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            sqlite_commands.CreateMedicationsTable
        )
        missing_columns = []

        sqlite_commands.CreateMedicationsTable(sq_manager).execute()
        column_names = return_column_names_from_db(sq_manager, "medications")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []


class Test_ReportingPeriodsTableCreation:
    """Tests that the table is created by CreateReportingPeriodsTable command.

    Behaviors Tested:
        - The 'reporting_periods' table is created in the database.
        - All expected columns are created in the table.
    """

    def test_CreateReportingPeriodsTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        sqlite_commands.CreateReportingPeriodsTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "reporting_periods" in table_names

    def test_CreateReportingPeriodsTable_creates_expected_columns(
        self, reset_database
    ) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            sqlite_commands.CreateReportingPeriodsTable
        )
        missing_columns = []

        sqlite_commands.CreateReportingPeriodsTable(sq_manager).execute()

        column_names = return_column_names_from_db(sq_manager, "reporting_periods")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []


class Test_StatusesTableCreation:
    """Tests that the 'statues' table is created by CreateStatusesTable command.

    Behaviors Tested:
        - The 'statuses' table is created in the database.
        - All expected columns are created in the table.
    """

    def test_CreateStatusesTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        sqlite_commands.CreateStatusesTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "statuses" in table_names

    def test_CreateStatusesTable_creates_expected_columns(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            sqlite_commands.CreateStatusesTable
        )
        missing_columns = []

        sqlite_commands.CreateStatusesTable(sq_manager).execute()
        column_names = return_column_names_from_db(sq_manager, "statuses")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []


class Test_UnitsTableCreation:
    """Tests that the 'units' table is created by CreateUnitsTable command.

    Behaviors Tested:
        - The 'units' table is created in the database.
        - All expected columns are created in the table.
    """

    def test_CreateUnitsTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        sqlite_commands.CreateUnitsTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "units" in table_names

    def test_CreateUnitsTable_creates_expected_columns(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            sqlite_commands.CreateUnitsTable
        )
        missing_columns = []

        sqlite_commands.CreateUnitsTable(sq_manager).execute()

        column_names = return_column_names_from_db(sq_manager, "units")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []
