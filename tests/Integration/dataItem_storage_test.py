"""Integration tests for handling DataItems in the SQlite3 database.

Classes:


Methods:

"""


import sqlite3
from typing import TYPE_CHECKING

import pytest

from narcotics_tracker import sqlite_commands
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.database import SQLiteManager

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment


@pytest.fixture
def adjustment() -> "Adjustment":
    adj_builder = (
        AdjustmentBuilder()
        .set_table("inventory")
        .set_id(-77)
        .set_created_date(1666117887)
        .set_modified_date(1666117887)
        .set_modified_by("System")
        .set_adjustment_date(1666117887)
        .set_event_code("TEST")
        .set_medication_code("FakeMed")
        .set_adjustment_amount(10)
        .set_reference_id("TestReferenceID")
        .set_reporting_period_id(0)
    )

    return adj_builder.build()


# def return_expected_columns_from_command(
#     command: sqlite_commands.SQLiteCommand,
# ) -> list[str]:
#     """Returns a list of column names created from the given command."""
#     columns = []
#     for item in command.column_info.keys():
#         columns.append(item)
#     return columns


# def return_column_names_from_db(db: SQLiteManager, table_name: str) -> list[str]:
#     """Returns a list of column names from the passed SQLiteManager and table."""
#     column_names = []

#     cursor = db.select(table_name)
#     data = cursor.description

#     for _tuple in data:
#         column_names.append(_tuple[0])

#     return column_names


# def return_table_names_from_db(db: SQLiteManager) -> list[str]:
#     """Returns a list of table names from the passed SQLiteManager."""

#     cursor = db._execute("""SELECT name FROM sqlite_master WHERE type = 'table'""")
#     table_names = []
#     data = cursor.fetchall()

#     for item in data:
#         table_names.append(item[0])

#     return table_names


def return_ids(cursor: sqlite3.Cursor) -> list[int]:
    """Returns id numbers of DataItems returned from the database.

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

        cursor = sq_man.select(table_name="inventory", criteria={"id": -77})
        adjustment_ids = return_ids(cursor)
        assert -77 in adjustment_ids


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

        cursor = sq_man.select(table_name="inventory", criteria={"id": -77})
        adjustment_ids = return_ids(cursor)
        assert -77 in adjustment_ids
