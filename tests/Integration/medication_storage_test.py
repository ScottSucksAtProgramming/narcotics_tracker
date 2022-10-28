"""Integration tests for handling Medications in the SQlite3 database.

Classes:
    Test_MedicationStorage: Tests Medication Storage in the SQLite3 database.

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


class Test_MedicationStorage:
    """Tests Medication Storage in the SQLite3 database.

    Behaviors Tested:
        - Medications can be added to the medications table.
        - Medications can be removed from the inventory table.
        - Medications can be read from the inventory table.
        - Medications can be updated.
        - Medication's preferred unit can be returned.
    """

    def test_medications_can_be_added_to_db(self, medication) -> None:
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()

        commands.AddMedication(sq_man).execute(medication)

        cursor = sq_man.read("medications")
        medication_ids = return_ids(cursor)
        assert -1 in medication_ids

    def test_medications_can_be_removed_from_db_using_ID(
        self, reset_database, medication
    ):
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()
        commands.AddMedication(sq_man).execute(medication)

        commands.DeleteMedication(sq_man).execute(-1)

        cursor = sq_man.read("medications")
        medication_id = return_ids(cursor)
        assert -1 not in medication_id

    def test_medications_can_be_removed_from_db_using_code(
        self, reset_database, medication
    ):
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()
        commands.AddMedication(sq_man).execute(medication)

        commands.DeleteMedication(sq_man).execute("apap")

        cursor = sq_man.read("medications")
        medication_id = return_ids(cursor)
        assert -1 not in medication_id

    def test_medications_can_be_read_from_db(self, reset_database, medication):
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()
        commands.AddMedication(sq_man).execute(medication)

        data = commands.ListMedications(sq_man).execute()

        assert data != None

    def test_medications_can_be_updated_in_db(self, reset_database, medication) -> None:
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()
        commands.AddMedication(sq_man).execute(medication)

        commands.UpdateMedication(sq_man).execute(
            data={"medication_code": "NEW CODE"}, criteria={"medication_code": "apap"}
        )

        returned_medication = commands.ListMedications(sq_man).execute({"id": -1})[0]

        assert "NEW CODE" in returned_medication

    def test_preferred_unit_can_be_returned(self, reset_database, medication) -> None:
        medication = medication
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateMedicationsTable(sq_man).execute()
        commands.AddMedication(sq_man).execute(medication)

        results = commands.medication_commands.ReturnPreferredUnit(sq_man).execute(
            "apap"
        )

        assert results == "dg"
