"""Integration tests for handling ReportingPeriods in the SQlite3 database.

Classes:
    Test_ReportingPeriodStorage: Tests ReportingPeriod Storage in the SQLite3 database.

Functions:
    return_ids: Returns id numbers of DataItems obtained from the database.

"""

import sqlite3

from narcotics_tracker import commands
from narcotics_tracker.services.sqlite_manager import SQLiteManager


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


class Test_ReportingPeriodStorage:
    """Tests ReportingPeriod Storage in the SQLite3 database.

    Behaviors Tested:
        - ReportingPeriods can be added to the reporting_periods table.
        - ReportingPeriods can be removed from the inventory table.
        - ReportingPeriods can be read from the inventory table.
        - ReportingPeriods can be updated.
        - ReportingPeriods can be loaded from data.
    """

    def test_ReportingPeriods_can_be_added_to_db(self, test_reporting_period) -> None:
        test_reporting_period = test_reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()

        commands.AddReportingPeriod(sq_man).execute(test_reporting_period)

        cursor = sq_man.read(table_name="reporting_periods")
        reporting_period_ids = return_ids(cursor)
        assert -1 in reporting_period_ids

    def test_ReportingPeriods_can_be_removed_from_db(
        self, reset_database, test_reporting_period
    ):
        test_reporting_period = test_reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()
        commands.AddReportingPeriod(sq_man).execute(test_reporting_period)

        commands.DeleteReportingPeriod(sq_man).execute(-1)

        cursor = sq_man.read(table_name="reporting_periods")
        reporting_period_id = return_ids(cursor)
        assert -1 not in reporting_period_id

    def test_ReportingPeriods_can_be_read_from_db(
        self, reset_database, test_reporting_period
    ):
        test_reporting_period = test_reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()
        commands.AddReportingPeriod(sq_man).execute(test_reporting_period)

        data = commands.ListReportingPeriods(sq_man).execute()

        assert data != None

    def test_reporting_periods_can_be_updated_in_db(
        self, reset_database, test_reporting_period
    ) -> None:
        test_reporting_period = test_reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()
        commands.AddReportingPeriod(sq_man).execute(test_reporting_period)

        commands.UpdateReportingPeriod(sq_man).execute(
            data={"status": "NEW STATUS"}, criteria={"id": -1}
        )

        returned_reporting_period = commands.ListReportingPeriods(sq_man).execute(
            criteria={"id": -1}
        )[0]

        assert "NEW STATUS" in returned_reporting_period

    def test_reporting_periods_can_be_loaded_from_data(
        self, setup_integration_db
    ) -> None:
        sq_man = SQLiteManager("integration_test.db")
        criteria = {"id": 2200001}
        period_data = commands.ListReportingPeriods(sq_man).execute(criteria)[-1]

        period = commands.LoadReportingPeriod().execute(period_data)
        expected = "Reporting Period #2200001: Start Date: 07-23-2022 00:00:00, End Date: None, Current Status: OPEN."
        assert str(period) == expected
