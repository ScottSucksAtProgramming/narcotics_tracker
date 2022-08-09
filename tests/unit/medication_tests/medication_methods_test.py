#
# * ----------------------------- Documentation ------------------------------ #
# Module:  medication_test.py
# Contains tests for the Medication class, as well as other related classes.
#
#
# Modification History
# 07-27-2022 | SRK | Module Created


import pytest

from narcotics_tracker.medication import medication_status, medication, containers
from narcotics_tracker.units import units


class TestMedicationMethods:
    """Unit Tests for the methods of the Medication class."""

    def test_printing_a_Medication_object_returns_correct_string(self, test_med):
        """Check to see if printing a Medication object returns a string."""

        test_med = test_med
        print(str(test_med))
        assert str(test_med) == (
            f"Medication Object for Unobtanium with code Un-69420-9001."
            f"Container type: Vial"
            f"Fill amount: 9001 ml"
            f"Dose: 69420 mcg"
            f"Concentration: 7.712476391512054"
            f"Status: Discontinued"
        )

    def test_medication_table_query_returns_correct_string(self):
        """Check to see if medication table query returns correct string."""

        assert medication.Medication.return_table_creation_query() == (
            """CREATE TABLE IF NOT EXISTS medication (
                NAME TEXT,
                CODE TEXT,
                CONTAINER_TYPE TEXT,
                FILL_AMOUNT REAL,
                DOSE REAL,
                UNIT TEXT,
                CONCENTRATION REAL,
                STATUS TEXT,
                PRIMARY KEY (CODE)
                )"""
        )
