"""Contains the unit tests for the ReturnCurrentInventory Report.

Classes:
"""
from types import FunctionType
from typing import Union

from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.items.medications import Medication
from narcotics_tracker.reports.return_current_inventory import ReturnCurrentInventory
from narcotics_tracker.services.sqlite_manager import SQLiteManager

# pylint: disable=missing-function-docstring, protected-access, unused-argument
# pyright: reportPrivateUsage=false, reportUnknownParameterType=false


class TestReturnCurrentInventory:
    """Unit tests the ReturnCurrentInventory Report.

    Behaviors Tested:

        - Class can be accessed.
        - Receiver can be set in initializer.
    """

    def test_can_access_class(self):
        assert ReturnCurrentInventory().__doc__ is not None

    def test_can_set_receiver(self):
        return_current_inventory = ReturnCurrentInventory("FakePersistenceService")  # type: ignore

        assert return_current_inventory._receiver == "FakePersistenceService"

    def test_can_retrieve_active_medications_from_database(
        self, setup_integration_db: FunctionType
    ):
        sq_man = SQLiteManager("integration_test.db")
        result = ReturnCurrentInventory(sq_man)._retrieve_medications()

        expected = [
            Medication(
                table="medications",
                id=1,
                created_date=1670891345,
                modified_date=1670891345,
                modified_by="SRK",
                medication_code="fentanyl",
                medication_name="Fentanyl",
                fill_amount=2.0,
                medication_amount=10000.0,
                preferred_unit="mcg",
                concentration=50.0,
                status="ACTIVE",
            ),
            Medication(
                table="medications",
                id=2,
                created_date=1670891345,
                modified_date=1670891345,
                modified_by="SRK",
                medication_code="midazolam",
                medication_name="Midazolam",
                fill_amount=2.0,
                medication_amount=1000000.0,
                preferred_unit="mg",
                concentration=5.0,
                status="ACTIVE",
            ),
            Medication(
                table="medications",
                id=3,
                created_date=1670891345,
                modified_date=1670891345,
                modified_by="SRK",
                medication_code="morphine",
                medication_name="Morphine",
                fill_amount=1.0,
                medication_amount=1000000.0,
                preferred_unit="mg",
                concentration=10.0,
                status="ACTIVE",
            ),
        ]

        assert result == expected

    def test_can_add_medication_data_to_report(self) -> None:
        medications = [
            Medication(
                table="medications",
                id=1,
                created_date=1670891345,
                modified_date=1670891345,
                modified_by="SRK",
                medication_code="fentanyl",
                medication_name="Fentanyl",
                fill_amount=2.0,
                medication_amount=10000.0,
                preferred_unit="mcg",
                concentration=50.0,
                status="ACTIVE",
            ),
            Medication(
                table="medications",
                id=2,
                created_date=1670891345,
                modified_date=1670891345,
                modified_by="SRK",
                medication_code="midazolam",
                medication_name="Midazolam",
                fill_amount=2.0,
                medication_amount=1000000.0,
                preferred_unit="mg",
                concentration=5.0,
                status="ACTIVE",
            ),
            Medication(
                table="medications",
                id=3,
                created_date=1670891345,
                modified_date=1670891345,
                modified_by="SRK",
                medication_code="morphine",
                medication_name="Morphine",
                fill_amount=1.0,
                medication_amount=1000000.0,
                preferred_unit="mg",
                concentration=10.0,
                status="ACTIVE",
            ),
        ]

        new_report = ReturnCurrentInventory()
        new_report._active_medications = medications
        new_report._add_medication_data_to_report()

        expected = [
            {"code": "fentanyl", "name": "Fentanyl", "unit": "mcg"},
            {"code": "midazolam", "name": "Midazolam", "unit": "mg"},
            {"code": "morphine", "name": "Morphine", "unit": "mg"},
        ]

        assert new_report._report == expected

    def test_run_report(self, setup_integration_db: FunctionType) -> None:
        sq_man = SQLiteManager("integration_test.db")
        results = ReturnCurrentInventory(sq_man).run()

        print(results)
