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
        - Adjustments can be removed from the inventory table.
    """

    def test_adjustments_can_be_added_to_db(self, reset_database, adjustment) -> None:
        adjustment = adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateInventoryTable(sq_man).execute()

        sqlite_commands.SaveItem(receiver=sq_man, item=adjustment).execute()

        cursor = sq_man.select(table_name="inventory")
        adjustment_ids = return_ids(cursor)
        assert -1 in adjustment_ids

    def test_adjustments_can_be_removed_from_db(self, reset_database, adjustment):
        adjustment = adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateInventoryTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=adjustment).execute()

        sqlite_commands.DeleteAdjustment(receiver=sq_man, adjustment_id=-1).execute()

        cursor = sq_man.select(table_name="inventory")
        adjustment_ids = return_ids(cursor)
        assert -1 not in adjustment_ids


class Test_EventStorage:
    """Tests Event Storage in the SQLite3 database.

    Behaviors Tested:
        - Events can be added to the events table.
        - Events can be removed from the inventory table.
    """

    def test_events_can_be_added_to_db(self, event) -> None:
        event = event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateEventsTable(sq_man).execute()

        sqlite_commands.SaveItem(receiver=sq_man, item=event).execute()

        cursor = sq_man.select(table_name="events")
        event_ids = return_ids(cursor)
        assert -77 in event_ids

    def test_events_can_be_removed_from_db_using_ID(self, reset_database, event):
        event = event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateEventsTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=event).execute()

        sqlite_commands.DeleteEvent(receiver=sq_man, event_identifier=-1).execute()

        cursor = sq_man.select(table_name="events")
        event_id = return_ids(cursor)
        assert -1 not in event_id

    def test_events_can_be_removed_from_db_using_code(self, reset_database, event):
        event = event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateEventsTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=event).execute()

        sqlite_commands.DeleteEvent(receiver=sq_man, event_identifier="TEST").execute()

        cursor = sq_man.select(table_name="events")
        event_id = return_ids(cursor)
        assert -1 not in event_id


class Test_MedicationStorage:
    """Tests Medication Storage in the SQLite3 database.

    Behaviors Tested:
        - Medications can be added to the medications table.
        - Medications can be removed from the inventory table.
    """

    def test_medications_can_be_added_to_db(self, medication) -> None:
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateMedicationsTable(sq_man).execute()

        sqlite_commands.SaveItem(receiver=sq_man, item=medication).execute()

        cursor = sq_man.select(table_name="medications")
        medication_ids = return_ids(cursor)
        assert -1 in medication_ids

    def test_medications_can_be_removed_from_db_using_ID(
        self, reset_database, medication
    ):
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateMedicationsTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=medication).execute()

        sqlite_commands.DeleteMedication(
            receiver=sq_man, medication_identifier=-1
        ).execute()

        cursor = sq_man.select(table_name="medications")
        medication_id = return_ids(cursor)
        assert -1 not in medication_id

    def test_medications_can_be_removed_from_db_using_code(
        self, reset_database, medication
    ):
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateMedicationsTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=medication).execute()

        sqlite_commands.DeleteMedication(
            receiver=sq_man, medication_identifier="apap"
        ).execute()

        cursor = sq_man.select(table_name="medications")
        medication_id = return_ids(cursor)
        assert -1 not in medication_id


class Test_ReportingPeriodStorage:
    """Tests ReportingPeriod Storage in the SQLite3 database.

    Behaviors Tested:
        - ReportingPeriods can be added to the reporting_periods table.
        - ReportingPeriods can be removed from the inventory table.
    """

    def test_ReportingPeriods_can_be_added_to_db(self, reporting_period) -> None:
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateReportingPeriodsTable(sq_man).execute()

        sqlite_commands.SaveItem(receiver=sq_man, item=reporting_period).execute()

        cursor = sq_man.select(table_name="reporting_periods")
        reporting_period_ids = return_ids(cursor)
        assert -1 in reporting_period_ids

    def test_ReportingPeriods_can_be_removed_from_db(
        self, reset_database, reporting_period
    ):
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateReportingPeriodsTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=reporting_period).execute()

        sqlite_commands.DeleteReportingPeriod(
            receiver=sq_man, reporting_period_id=-1
        ).execute()

        cursor = sq_man.select(table_name="reporting_periods")
        reporting_period_id = return_ids(cursor)
        assert -1 not in reporting_period_id


class Test_StatusStorage:
    """Tests Status Storage in the SQLite3 database.

    Behaviors Tested:
        - Statuses can be added to the status table.
        - Statuses can be removed from the inventory table.
    """

    def test_Statuses_can_be_added_to_db(self, status) -> None:
        status = status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateStatusesTable(sq_man).execute()

        sqlite_commands.SaveItem(receiver=sq_man, item=status).execute()

        cursor = sq_man.select(table_name="statuses")
        status_ids = return_ids(cursor)
        assert -1 in status_ids

    def test_Statuses_can_be_removed_from_db_using_ID(self, reset_database, status):
        status = status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateStatusesTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=status).execute()

        sqlite_commands.DeleteStatus(receiver=sq_man, status_identifier=-1).execute()

        cursor = sq_man.select(table_name="statuses")
        status_id = return_ids(cursor)
        assert -1 not in status_id

    def test_Statuses_can_be_removed_from_db_using_code(self, reset_database, status):
        status = status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateStatusesTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=status).execute()

        sqlite_commands.DeleteStatus(
            receiver=sq_man, status_identifier="BROKEN"
        ).execute()

        cursor = sq_man.select(table_name="statuses")
        status_id = return_ids(cursor)
        assert -1 not in status_id


class Test_UnitStorage:
    """Tests Unit Storage in the SQLite3 database.

    Behaviors Tested:
        - Units can be added to the units table.
        - Units can be removed from the inventory table.
    """

    def test_Units_can_be_added_to_db(self, unit) -> None:
        unit = unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateUnitsTable(sq_man).execute()

        sqlite_commands.SaveItem(receiver=sq_man, item=unit).execute()

        cursor = sq_man.select(table_name="units")
        unit_ids = return_ids(cursor)
        assert -1 in unit_ids

    def test_Units_can_be_removed_from_db_using_ID(self, reset_database, unit):
        unit = unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateUnitsTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=unit).execute()

        sqlite_commands.DeleteUnit(receiver=sq_man, unit_identifier=-1).execute()

        cursor = sq_man.select(table_name="units")
        unit_id = return_ids(cursor)
        assert -1 not in unit_id

    def test_units_can_be_removed_from_db_using_code(self, reset_database, unit):
        unit = unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        sqlite_commands.CreateUnitsTable(sq_man).execute()
        sqlite_commands.SaveItem(receiver=sq_man, item=unit).execute()

        sqlite_commands.DeleteUnit(receiver=sq_man, unit_identifier="dg").execute()

        cursor = sq_man.select(table_name="units")
        unit_id = return_ids(cursor)
        assert -1 not in unit_id
