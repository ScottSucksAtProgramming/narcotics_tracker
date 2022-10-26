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

from narcotics_tracker import commands
from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.utils.datetime_manager import DateTimeManager


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


dtm = DateTimeManager()


class Test_AdjustmentStorage:
    """Tests Adjustment Storage in the SQLite3 database.

    Behaviors Tested:
        - Adjustments can be added to the inventory table.
        - Adjustments can be removed from the inventory table.
        - Adjustments can be read from the inventory table.
        - Adjustments can be updated.
    """

    def test_adjustments_can_be_added_to_db(self, reset_database, adjustment) -> None:
        adjustment = adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateInventoryTable(sq_man).execute()

        commands.SaveItem(
            receiver=sq_man, item=adjustment, datetime_manager=dtm
        ).execute()

        cursor = sq_man.read(table_name="inventory")
        adjustment_ids = return_ids(cursor)
        assert -1 in adjustment_ids

    def test_adjustments_can_be_removed_from_db(self, reset_database, adjustment):
        adjustment = adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateInventoryTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=adjustment, datetime_manager=dtm
        ).execute()

        commands.DeleteAdjustment(receiver=sq_man, adjustment_id=-1).execute()

        cursor = sq_man.read(table_name="inventory")
        adjustment_ids = return_ids(cursor)
        assert -1 not in adjustment_ids

    def test_adjustments_can_be_read_from_db(self, reset_database, adjustment):
        adjustment = adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateInventoryTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=adjustment, datetime_manager=dtm
        ).execute()

        data = commands.ListAdjustments(sq_man).execute()

        assert data != None

    def test_adjustments_can_be_updated_in_db(self, reset_database, adjustment) -> None:
        adjustment = adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateInventoryTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=adjustment, datetime_manager=dtm
        ).execute()

        commands.UpdateAdjustment(
            receiver=sq_man, data={"amount": 9999}, criteria={"id": -1}
        ).execute()

        returned_adjustment = commands.ListAdjustments(
            receiver=sq_man, criteria={"id": -1}
        ).execute()[0]

        assert returned_adjustment[4] == 9999


class Test_EventStorage:
    """Tests Event Storage in the SQLite3 database.

    Behaviors Tested:
        - Events can be added to the events table.
        - Events can be removed from the inventory table.
        - Events can be read from the inventory table.
        - Events can be updated.
    """

    def test_events_can_be_added_to_db(self, event) -> None:
        event = event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()

        commands.SaveItem(receiver=sq_man, item=event, datetime_manager=dtm).execute()

        cursor = sq_man.read(table_name="events")
        event_ids = return_ids(cursor)
        assert -77 in event_ids

    def test_events_can_be_removed_from_db_using_ID(self, reset_database, event):
        event = event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=event, datetime_manager=dtm).execute()

        commands.DeleteEvent(receiver=sq_man, event_identifier=-1).execute()

        cursor = sq_man.read(table_name="events")
        event_id = return_ids(cursor)
        assert -1 not in event_id

    def test_events_can_be_removed_from_db_using_code(self, reset_database, event):
        event = event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=event, datetime_manager=dtm).execute()

        commands.DeleteEvent(receiver=sq_man, event_identifier="TEST").execute()

        cursor = sq_man.read(table_name="events")
        event_id = return_ids(cursor)
        assert -1 not in event_id

    def test_events_can_be_read_from_db(self, reset_database, event):
        event = event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=event, datetime_manager=dtm).execute()

        data = commands.ListEvents(sq_man).execute()

        assert data != None

    def test_events_can_be_updated_in_db(self, reset_database, event) -> None:
        event = event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=event, datetime_manager=dtm).execute()

        commands.UpdateEvent(
            receiver=sq_man,
            data={"event_code": "NEW CODE"},
            criteria={"event_code": "TEST"},
        ).execute()

        returned_event = commands.ListEvents(
            receiver=sq_man, criteria={"id": -77}
        ).execute()[0]

        assert "NEW CODE" in returned_event


class Test_MedicationStorage:
    """Tests Medication Storage in the SQLite3 database.

    Behaviors Tested:
        - Medications can be added to the medications table.
        - Medications can be removed from the inventory table.
        - Medications can be read from the inventory table.
        - Medications can be updated.
    """

    def test_medications_can_be_added_to_db(self, medication) -> None:
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()

        commands.SaveItem(
            receiver=sq_man, item=medication, datetime_manager=dtm
        ).execute()

        cursor = sq_man.read(table_name="medications")
        medication_ids = return_ids(cursor)
        assert -1 in medication_ids

    def test_medications_can_be_removed_from_db_using_ID(
        self, reset_database, medication
    ):
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=medication, datetime_manager=dtm
        ).execute()

        commands.DeleteMedication(receiver=sq_man, medication_identifier=-1).execute()

        cursor = sq_man.read(table_name="medications")
        medication_id = return_ids(cursor)
        assert -1 not in medication_id

    def test_medications_can_be_removed_from_db_using_code(
        self, reset_database, medication
    ):
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=medication, datetime_manager=dtm
        ).execute()

        commands.DeleteMedication(
            receiver=sq_man, medication_identifier="apap"
        ).execute()

        cursor = sq_man.read(table_name="medications")
        medication_id = return_ids(cursor)
        assert -1 not in medication_id

    def test_medications_can_be_read_from_db(self, reset_database, medication):
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=medication, datetime_manager=dtm
        ).execute()

        data = commands.ListMedications(sq_man).execute()

        assert data != None

    def test_medications_can_be_updated_in_db(self, reset_database, medication) -> None:
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=medication, datetime_manager=dtm
        ).execute()

        commands.UpdateMedication(
            receiver=sq_man,
            data={"medication_code": "NEW CODE"},
            criteria={"medication_code": "apap"},
        ).execute()

        returned_medication = commands.ListMedications(
            receiver=sq_man, criteria={"id": -1}
        ).execute()[0]

        assert "NEW CODE" in returned_medication


class Test_ReportingPeriodStorage:
    """Tests ReportingPeriod Storage in the SQLite3 database.

    Behaviors Tested:
        - ReportingPeriods can be added to the reporting_periods table.
        - ReportingPeriods can be removed from the inventory table.
        - ReportingPeriods can be read from the inventory table.
        - ReportingPeriods can be updated.
    """

    def test_ReportingPeriods_can_be_added_to_db(self, reporting_period) -> None:
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()

        commands.SaveItem(
            receiver=sq_man, item=reporting_period, datetime_manager=dtm
        ).execute()

        cursor = sq_man.read(table_name="reporting_periods")
        reporting_period_ids = return_ids(cursor)
        assert -1 in reporting_period_ids

    def test_ReportingPeriods_can_be_removed_from_db(
        self, reset_database, reporting_period
    ):
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=reporting_period, datetime_manager=dtm
        ).execute()

        commands.DeleteReportingPeriod(
            receiver=sq_man, reporting_period_id=-1
        ).execute()

        cursor = sq_man.read(table_name="reporting_periods")
        reporting_period_id = return_ids(cursor)
        assert -1 not in reporting_period_id

    def test_ReportingPeriods_can_be_read_from_db(
        self, reset_database, reporting_period
    ):
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=reporting_period, datetime_manager=dtm
        ).execute()

        data = commands.ListReportingPeriods(sq_man).execute()

        assert data != None

    def test_reporting_periods_can_be_updated_in_db(
        self, reset_database, reporting_period
    ) -> None:
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()
        commands.SaveItem(
            receiver=sq_man, item=reporting_period, datetime_manager=dtm
        ).execute()

        commands.UpdateReportingPeriod(
            receiver=sq_man,
            data={"status": "NEW STATUS"},
            criteria={"id": -1},
        ).execute()

        returned_reporting_period = commands.ListReportingPeriods(
            receiver=sq_man, criteria={"id": -1}
        ).execute()[0]

        assert "NEW STATUS" in returned_reporting_period


class Test_StatusStorage:
    """Tests Status Storage in the SQLite3 database.

    Behaviors Tested:
        - Statuses can be added to the status table.
        - Statuses can be removed from the inventory table.
        - Statuses can be read from the inventory table.
        - Statuses can be updated.
    """

    def test_Statuses_can_be_added_to_db(self, status) -> None:
        status = status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()

        commands.SaveItem(receiver=sq_man, item=status, datetime_manager=dtm).execute()

        cursor = sq_man.read(table_name="statuses")
        status_ids = return_ids(cursor)
        assert -1 in status_ids

    def test_Statuses_can_be_removed_from_db_using_ID(self, reset_database, status):
        status = status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=status, datetime_manager=dtm).execute()

        commands.DeleteStatus(receiver=sq_man, status_identifier=-1).execute()

        cursor = sq_man.read(table_name="statuses")
        status_id = return_ids(cursor)
        assert -1 not in status_id

    def test_Statuses_can_be_removed_from_db_using_code(self, reset_database, status):
        status = status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=status, datetime_manager=dtm).execute()

        commands.DeleteStatus(receiver=sq_man, status_identifier="BROKEN").execute()

        cursor = sq_man.read(table_name="statuses")
        status_id = return_ids(cursor)
        assert -1 not in status_id

    def test_statuses_can_be_read_from_db(self, reset_database, status):
        status = status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=status, datetime_manager=dtm).execute()

        data = commands.ListStatuses(sq_man).execute()

        assert data != None

    def test_statuses_can_be_updated_in_db(self, reset_database, status) -> None:
        status = status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=status, datetime_manager=dtm).execute()

        commands.UpdateStatus(
            receiver=sq_man,
            data={"status_code": "NEW CODE"},
            criteria={"status_code": "BROKEN"},
        ).execute()

        returned_status = commands.ListStatuses(
            receiver=sq_man, criteria={"id": -1}
        ).execute()[0]

        assert "NEW CODE" in returned_status


class Test_UnitStorage:
    """Tests Unit Storage in the SQLite3 database.

    Behaviors Tested:
        - Units can be added to the units table.
        - Units can be removed from the inventory table.
        - Units can be read from the inventory table.
        - Units can be updated.
    """

    def test_Units_can_be_added_to_db(self, unit) -> None:
        unit = unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()

        commands.SaveItem(receiver=sq_man, item=unit, datetime_manager=dtm).execute()

        cursor = sq_man.read(table_name="units")
        unit_ids = return_ids(cursor)
        assert -1 in unit_ids

    def test_Units_can_be_removed_from_db_using_ID(self, reset_database, unit):
        unit = unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=unit, datetime_manager=dtm).execute()

        commands.DeleteUnit(receiver=sq_man, unit_identifier=-1).execute()

        cursor = sq_man.read(table_name="units")
        unit_id = return_ids(cursor)
        assert -1 not in unit_id

    def test_units_can_be_removed_from_db_using_code(self, reset_database, unit):
        unit = unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=unit, datetime_manager=dtm).execute()

        commands.DeleteUnit(receiver=sq_man, unit_identifier="dg").execute()

        cursor = sq_man.read(table_name="units")
        unit_id = return_ids(cursor)
        assert -1 not in unit_id

    def test_units_can_be_read_from_db(self, reset_database, unit):
        unit = unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=unit, datetime_manager=dtm).execute()

        data = commands.ListUnits(sq_man).execute()

        assert data != None

    def test_units_can_be_updated_in_db(self, reset_database, unit) -> None:
        unit = unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()
        commands.SaveItem(receiver=sq_man, item=unit, datetime_manager=dtm).execute()

        commands.UpdateUnit(
            receiver=sq_man,
            data={"unit_code": "NEW CODE"},
            criteria={"unit_code": "dg"},
        ).execute()

        returned_unit = commands.ListUnits(
            receiver=sq_man, criteria={"id": -1}
        ).execute()[0]

        assert "NEW CODE" in returned_unit
