"""Integration tests for handling Statuses in the SQlite3 database.

Classes:
    Test_StatusStorage: Tests Status Storage in the SQLite3 database.

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


class Test_StatusStorage:
    """Tests Status Storage in the SQLite3 database.

    Behaviors Tested:
        - Statuses can be added to the status table.
        - Statuses can be removed from the inventory table.
        - Statuses can be read from the inventory table.
        - Statuses can be updated.
    """

    def test_Statuses_can_be_added_to_db(self, test_status) -> None:
        test_status = test_status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()

        commands.AddStatus(sq_man).execute(test_status)

        cursor = sq_man.read(table_name="statuses")
        status_ids = return_ids(cursor)
        assert -1 in status_ids

    def test_Statuses_can_be_removed_from_db_using_ID(
        self, reset_database, test_status
    ):
        test_status = test_status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()
        commands.AddStatus(sq_man).execute(test_status)

        commands.DeleteStatus(sq_man).execute(-1)

        cursor = sq_man.read(table_name="statuses")
        status_id = return_ids(cursor)
        assert -1 not in status_id

    def test_Statuses_can_be_removed_from_db_using_code(
        self, reset_database, test_status
    ):
        test_status = test_status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()
        commands.AddStatus(sq_man).execute(test_status)

        commands.DeleteStatus(sq_man).execute("BROKEN")

        cursor = sq_man.read(table_name="statuses")
        status_id = return_ids(cursor)
        assert -1 not in status_id

    def test_statuses_can_be_read_from_db(self, reset_database, test_status):
        test_status = test_status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()
        commands.AddStatus(sq_man).execute(test_status)

        data = commands.ListStatuses(sq_man).execute()

        assert data != None

    def test_statuses_can_be_updated_in_db(self, reset_database, test_status) -> None:
        test_status = test_status
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateStatusesTable(sq_man).execute()
        commands.AddStatus(sq_man).execute(test_status)

        commands.UpdateStatus(sq_man).execute(
            {"status_code": "NEW CODE"}, {"status_code": "BROKEN"}
        )

        returned_status = commands.ListStatuses(sq_man).execute({"id": -1})[0]

        assert "NEW CODE" in returned_status
