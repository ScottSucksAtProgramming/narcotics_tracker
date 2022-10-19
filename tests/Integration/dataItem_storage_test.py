"""Integration tests for handling DataItems in the SQlite3 database.

Classes:


Methods:

"""


import sqlite3

from narcotics_tracker import sqlite_commands
from narcotics_tracker.database import SQLiteManager

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
