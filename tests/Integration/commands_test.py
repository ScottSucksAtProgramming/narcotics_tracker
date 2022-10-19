"""Contains integration tests for SQLiteCommands.

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

from narcotics_tracker import commands
from narcotics_tracker.database import SQLiteManager


def return_expected_columns_from_command(command: commands.SQLiteCommand) -> list[str]:
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


class Test_TableCreationCommands:
    """Performs integration testing for commands that create tables.

    Behaviors Tested:
        - CreateEventsTable Command creates expected table.
        - CreateEventsTable Command creates expected columns.
        - CreateInventoryTable Command creates expected table.
        - CreateInventoryTable Command creates expected columns.
        - CreateMedicationsTable Command creates expected table.
        - CreateMedicationsTable Command creates expected columns.
        - CreateReportingPeriodsTable Command creates expected table.
        - CreateReportingPeriodsTable Command creates expected columns.
        - CreateStatusesTable Command creates expected table.
        - CreateStatusesTable Command creates expected columns.
        - CreateUnitesTable Command creates expected table.
        - CreateUnitesTable Command creates expected columns.
    """

    def test_CreateEventsTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        commands.CreateEventsTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "events" in table_names

    def test_CreateEventsTable_creates_expected_columns(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            commands.CreateEventsTable
        )
        missing_columns = []

        commands.CreateEventsTable(sq_manager).execute()
        column_names = return_column_names_from_db(sq_manager, "events")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []

    def test_CreateInventoryTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        commands.CreateInventoryTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "inventory" in table_names

    def test_CreateInventoryTable_creates_expected_columns(
        self, reset_database
    ) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            commands.CreateInventoryTable
        )
        missing_columns = []

        commands.CreateInventoryTable(sq_manager).execute()

        column_names = return_column_names_from_db(sq_manager, "inventory")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []

    def test_CreateMedicationsTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        commands.CreateMedicationsTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "medications" in table_names

    def test_CreateMedicationsTable_creates_expected_columns(
        self, reset_database
    ) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            commands.CreateMedicationsTable
        )
        missing_columns = []

        commands.CreateMedicationsTable(sq_manager).execute()
        column_names = return_column_names_from_db(sq_manager, "medications")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []

    def test_CreateReportingPeriodsTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        commands.CreateReportingPeriodsTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "reporting_periods" in table_names

    def test_CreateReportingPeriodsTable_creates_expected_columns(
        self, reset_database
    ) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            commands.CreateReportingPeriodsTable
        )
        missing_columns = []

        commands.CreateReportingPeriodsTable(sq_manager).execute()

        column_names = return_column_names_from_db(sq_manager, "reporting_periods")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []

    def test_CreateStatusesTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        commands.CreateStatusesTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "statuses" in table_names

    def test_CreateStatusesTable_creates_expected_columns(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            commands.CreateStatusesTable
        )
        missing_columns = []

        commands.CreateStatusesTable(sq_manager).execute()
        column_names = return_column_names_from_db(sq_manager, "statuses")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []

    def test_CreateUnitsTable_creates_table(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")

        commands.CreateUnitsTable(sq_manager).execute()

        table_names = return_table_names_from_db(sq_manager)

        assert "units" in table_names

    def test_CreateUnitsTable_creates_expected_columns(self, reset_database) -> None:
        sq_manager = SQLiteManager("table_creation_tests.db")
        expected_columns = return_expected_columns_from_command(
            commands.CreateUnitsTable
        )
        missing_columns = []

        commands.CreateUnitsTable(sq_manager).execute()

        column_names = return_column_names_from_db(sq_manager, "units")

        for column in expected_columns:
            if column not in column_names:
                missing_columns.append(column)

        if missing_columns != []:
            print(missing_columns)

        assert missing_columns == []
