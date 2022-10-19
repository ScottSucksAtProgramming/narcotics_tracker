"""Integration tests for handling DataItems in the SQlite3 database.

Classes:
    Test_AdjustmentStorage: Tests Adjustment Storage in the SQLite3 database.

    Test_EventStorage: Tests Event Storage in the SQLite3 database.

    Test_MedicationStorage: Tests Medication Storage in the SQLite3 database.

    Test_ReportingPeriodStorage: Tests ReportingPeriod Storage in the database.

    Test_StatusStorage: Tests Status Storage in the SQLite3 database.

    Test_UnitStorage: Tests Unit Storage in the SQLite3 database.

Functions:
    return_ids: Returns id numbers of DataItems obtained from the database.

"""


import sqlite3

from narcotics_tracker import sqlite_commands
from narcotics_tracker.database import SQLiteManager


def return_ids(cursor: sqlite3.Cursor) -> list[int]:
    """Returns id numbers of DataItems obtained from the database.

    Args:
        cursor (sqlite3.Cursor): A cursor containing results of a select query.

    Returns:
        ids (list[int]): A list of DataItem id numbers.
    """
    ids = []

    raw_data = cursor.fetchall()
    for item in raw_data:
        ids.append(item[0])

    return ids


class Test_AdjustmentStorage:
    """Tests Adjustment Storage in the SQLite3 database.

    Behaviors Tested:
        - Adjustments can be added to the inventory table.
    """

    def test_adjustments_can_be_added_to_db(self, reset_database, adjustment) -> None:
        adjustment = adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateInventoryTable(sq_man).execute()

        sqlite_commands.SaveItemToDatabase(receiver=sq_man, item=adjustment).execute()

        cursor = sq_man.select(table_name="inventory")
        adjustment_ids = return_ids(cursor)
        assert -1 in adjustment_ids


class Test_EventStorage:
    """Tests Event Storage in the SQLite3 database.

    Behaviors Tested:
        - Events can be added to the events table.
    """

    def test_events_can_be_added_to_db(self, event) -> None:
        event = event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateEventsTable(sq_man).execute()

        sqlite_commands.SaveItemToDatabase(receiver=sq_man, item=event).execute()

        cursor = sq_man.select(table_name="events")
        event_ids = return_ids(cursor)
        assert -77 in event_ids


class Test_MedicationStorage:
    """Tests Medication Storage in the SQLite3 database.

    Behaviors Tested:
        - Medications can be added to the medications table.
    """

    def test_medications_can_be_added_to_db(self, medication) -> None:
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateMedicationsTable(sq_man).execute()

        sqlite_commands.SaveItemToDatabase(receiver=sq_man, item=medication).execute()

        cursor = sq_man.select(table_name="medications")
        medication_ids = return_ids(cursor)
        assert -1 in medication_ids


class Test_ReportingPeriodStorage:
    """Tests ReportingPeriod Storage in the SQLite3 database.

    Behaviors Tested:
        - ReportingPeriods can be added to the reporting_periods table.
    """

    def test_ReportingPeriods_can_be_added_to_db(self, reporting_period) -> None:
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateReportingPeriodsTable(sq_man).execute()

        sqlite_commands.SaveItemToDatabase(
            receiver=sq_man, item=reporting_period
        ).execute()

        cursor = sq_man.select(table_name="reporting_periods")
        reporting_period_ids = return_ids(cursor)
        assert -1 in reporting_period_ids


class Test_StatusStorage:
    """Tests Status Storage in the SQLite3 database.

    Behaviors Tested:
        - Statuses can be added to the status table.
    """

    def test_status_can_be_added_to_db(self, status) -> None:
        status = status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateStatusesTable(sq_man).execute()

        sqlite_commands.SaveItemToDatabase(receiver=sq_man, item=status).execute()

        cursor = sq_man.select(table_name="statuses")
        status_ids = return_ids(cursor)
        assert -1 in status_ids


class Test_UnitStorage:
    """Tests Unit Storage in the SQLite3 database.

    Behaviors Tested:
        - Units can be added to the units table.
    """

    def test_units_can_be_added_to_db(self, unit) -> None:
        unit = unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateUnitsTable(sq_man).execute()

        sqlite_commands.SaveItemToDatabase(receiver=sq_man, item=unit).execute()

        cursor = sq_man.select(table_name="units")
        unit_ids = return_ids(cursor)
        assert -1 in unit_ids
