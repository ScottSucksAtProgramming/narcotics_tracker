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
    """

    def test_ReportingPeriods_can_be_added_to_db(self, reporting_period) -> None:
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()

        commands.AddReportingPeriod(sq_man).execute(reporting_period)

        cursor = sq_man.read(table_name="reporting_periods")
        reporting_period_ids = return_ids(cursor)
        assert -1 in reporting_period_ids

    def test_ReportingPeriods_can_be_removed_from_db(
        self, reset_database, reporting_period
    ):
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()
        commands.AddReportingPeriod(sq_man).execute(reporting_period)

        commands.DeleteReportingPeriod(sq_man).execute(-1)

        cursor = sq_man.read(table_name="reporting_periods")
        reporting_period_id = return_ids(cursor)
        assert -1 not in reporting_period_id

    def test_ReportingPeriods_can_be_read_from_db(
        self, reset_database, reporting_period
    ):
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()
        commands.AddReportingPeriod(sq_man).execute(reporting_period)

        data = commands.ListReportingPeriods(sq_man).execute()

        assert data != None

    def test_reporting_periods_can_be_updated_in_db(
        self, reset_database, reporting_period
    ) -> None:
        reporting_period = reporting_period
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateReportingPeriodsTable(sq_man).execute()
        commands.AddReportingPeriod(sq_man).execute(reporting_period)

        commands.UpdateReportingPeriod(sq_man).execute(
            data={"status": "NEW STATUS"}, criteria={"id": -1}
        )

        returned_reporting_period = commands.ListReportingPeriods(sq_man).execute(
            criteria={"id": -1}
        )[0]

        assert "NEW STATUS" in returned_reporting_period
