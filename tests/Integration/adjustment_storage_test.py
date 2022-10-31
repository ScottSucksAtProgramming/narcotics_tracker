"""Integration tests for handling Adjustments in the SQlite3 database.

Classes:
    Test_AdjustmentStorage: Tests Adjustment Storage in the SQLite3 database.

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


class Test_AdjustmentStorage:
    """Tests Adjustment Storage in the SQLite3 database.

    Behaviors Tested:
        - Adjustments can be added to the inventory table.
        - Adjustments can be removed from the inventory table.
        - Adjustments can be read from the inventory table.
        - Adjustments can be updated.
    """

    def test_adjustments_can_be_added(self, reset_database, test_adjustment) -> None:
        test_adjustment = test_adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateInventoryTable(sq_man).execute()

        commands.AddAdjustment(sq_man).execute(test_adjustment)

        cursor = sq_man.read(table_name="inventory")
        adjustment_ids = return_ids(cursor)
        assert -1 in adjustment_ids

    def test_adjustments_can_be_removed(self, reset_database, test_adjustment) -> None:
        test_adjustment = test_adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateInventoryTable(sq_man).execute()
        commands.AddAdjustment(sq_man).execute(test_adjustment)

        commands.DeleteAdjustment(sq_man).execute(-1)

        cursor = sq_man.read(table_name="inventory")
        adjustment_ids = return_ids(cursor)
        assert -1 not in adjustment_ids

    def test_adjustments_can_be_read(self, reset_database, test_adjustment) -> None:
        test_adjustment = test_adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateInventoryTable(sq_man).execute()
        commands.AddAdjustment(sq_man).execute(test_adjustment)

        data = commands.ListAdjustments(sq_man).execute()

        assert data != None

    def test_adjustments_can_be_updated(self, reset_database, test_adjustment) -> None:
        test_adjustment = test_adjustment
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateInventoryTable(sq_man).execute()
        commands.AddAdjustment(sq_man).execute(test_adjustment)

        commands.UpdateAdjustment(sq_man).execute({"amount": 9999}, {"id": -1})

        returned_adjustment = commands.ListAdjustments(sq_man).execute({"id": -1})[0]

        assert returned_adjustment[4] == 9999
