"""Integration tests for handling Units in the SQlite3 database.

Classes:
    Test_UnitStorage: Tests Unit Storage in the SQLite3 database.

Functions:
    return_ids: Returns id numbers of DataItems obtained from the database.

"""
# pylint: skip-file
# pylance: ignore

import sqlite3
from typing import TYPE_CHECKING, Callable

from narcotics_tracker import commands
from narcotics_tracker.services.sqlite_manager import SQLiteManager

if TYPE_CHECKING:
    from narcotics_tracker.items.units import Unit


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


class Test_UnitStorage:
    """Tests Unit Storage in the SQLite3 database.

    Behaviors Tested:
        - Units can be added to the units table.
        - Units can be removed from the inventory table.
        - Units can be read from the inventory table.
        - Units can be updated.
    """

    def test_units_can_be_added_to_db(self, test_unit: "Unit") -> None:
        unit = test_unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()

        commands.AddUnit(sq_man).set_unit(unit).execute()

        cursor = sq_man.read(table_name="units")
        unit_ids = return_ids(cursor)
        assert -1 in unit_ids

    def test_units_can_be_removed_from_db_using_ID(
        self, reset_database, test_unit: "Unit"
    ):
        test_unit = test_unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()
        commands.AddUnit(sq_man).set_unit(test_unit).execute()

        commands.DeleteUnit(sq_man).set_identifier(unit_identifier=-1).execute()

        cursor = sq_man.read(table_name="units")
        unit_id = return_ids(cursor)
        assert -1 not in unit_id

    def test_units_can_be_removed_from_db_using_code(
        self, reset_database, test_unit: "Unit"
    ):
        test_unit = test_unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()
        commands.AddUnit(sq_man).set_unit(test_unit).execute()

        commands.DeleteUnit(sq_man).set_identifier(unit_identifier="dg").execute()

        cursor = sq_man.read(table_name="units")
        unit_id = return_ids(cursor)
        assert -1 not in unit_id

    def test_units_can_be_read_from_db(
        self, reset_database: Callable, test_unit: "Unit"
    ):
        test_unit = test_unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()
        commands.AddUnit(sq_man).set_unit(test_unit).execute()

        data = commands.ListUnits(sq_man).execute()

        assert data != None

    def test_units_can_be_updated_in_db(
        self, reset_database, test_unit: "Unit"
    ) -> None:
        test_unit = test_unit
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateUnitsTable(sq_man).execute()
        commands.AddUnit(sq_man).set_unit(test_unit).execute()

        commands.UpdateUnit(sq_man).set_data(
            data={"unit_code": "NEW CODE"}, criteria={"unit_code": "dg"}
        ).execute()

        returned_unit = (
            commands.ListUnits(sq_man).set_parameters(criteria={"id": -1}).execute()[0]
        )

        assert "NEW CODE" in returned_unit
