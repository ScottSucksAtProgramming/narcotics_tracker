#
# * ----------------------------- Documentation ------------------------------ #
# Module:  medication_test.py
# Contains tests for the Medication class, as well as other related classes.
#
#
# Modification History
# 07-27-2022 | SRK | Module Created

from narcotics_tracker.database import database
from narcotics_tracker.medication import (
    containers,
    medication,
    medication_status,
    builder,
)
from narcotics_tracker.units import units


class TestMedicationMethods:
    """Unit Tests for the methods of the Medication class."""

    def test_printing_a_Medication_object_returns_correct_string(self, test_med):
        """Check to see if printing a Medication object returns a string."""

        test_med = test_med
        assert str(test_med) == (
            f"Medication Object 1 for Unobtanium with code Un-69420-9001. "
            f"Container type: Vial. "
            f"Fill amount: 9001 ml. "
            f"Dose: 69420 mcg. "
            f"Concentration: 7.712476391512054. "
            f"Status: Discontinued. Created on 08-01-2022. "
            f"Last modified on 08-09-2022 by SRK."
        )

    def test_medication_table_query_returns_correct_string(self):
        """Check to see if medication table query returns correct string."""

        assert medication.Medication.return_table_creation_query() == (
            """CREATE TABLE IF NOT EXISTS medication (
                MEDICATION_ID INTEGER,
                NAME TEXT,
                CODE TEXT,
                CONTAINER_TYPE TEXT,
                FILL_AMOUNT REAL,
                DOSE REAL,
                UNIT TEXT,
                CONCENTRATION REAL,
                STATUS TEXT,
                CREATED_DATE TEXT,
                MODIFIED_DATE TEXT,
                MODIFIED_BY TEXT,
                PRIMARY KEY (CODE)
                )"""
        )

    def test_return_properties(self, test_med):
        """Checks to see if the medication data is correctly returned."""

        test_med = test_med
        assert test_med.return_properties() == (
            1,
            "Un-69420-9001",
            "Unobtanium",
            "Vial",
            9001,
            69420,
            "mcg",
            7.712476391512054,
            "Discontinued",
            "08-01-2022",
            "08-09-2022",
            "SRK",
        )

    def test_save_to_database(self, test_med):
        """Checks to see if the medication data is correctly written to
        database."""

        test_med = test_med
        values = test_med.return_properties()
        db = database.Database()
        db.connect("test_database.db")

        sql_query = """INSERT OR IGNORE INTO medication VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        test_med.save_to_database(db, sql_query, values)
        data = db.read_table(
            """SELECT * FROM sqlite_master WHERE type='table' AND name=(?)""",
            ["medication"],
        )[0][4]

        assert (
            data
            == """CREATE TABLE medication (
                MEDICATION_ID INTEGER,
                NAME TEXT,
                CODE TEXT,
                CONTAINER_TYPE TEXT,
                FILL_AMOUNT REAL,
                DOSE REAL,
                UNIT TEXT,
                CONCENTRATION REAL,
                STATUS TEXT,
                CREATED_DATE TEXT,
                MODIFIED_DATE TEXT,
                MODIFIED_BY TEXT,
                PRIMARY KEY (CODE)
                )"""
        )
