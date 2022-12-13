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

    def test_can_retrieve_adjustments_by_medication(
        self, setup_integration_db: FunctionType
    ) -> None:
        sq_man = SQLiteManager("integration_test.db")
        fent = Medication(
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
        )
        results = ReturnCurrentInventory(sq_man)._retrieve_adjustments_for_medication(
            fent
        )

        expected: list["Adjustment"] = [
            Adjustment(
                table="inventory",
                id=1,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1658523600,
                event_code="IMPORT",
                medication_code="fentanyl",
                amount=745000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=2,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1658523600,
                event_code="IMPORT",
                medication_code="midazolam",
                amount=66340000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=3,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1658523600,
                event_code="IMPORT",
                medication_code="morphine",
                amount=69000000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=4,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1659212760,
                event_code="USE",
                medication_code="fentanyl",
                amount=-5000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=5,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1661027838,
                event_code="DESTROY",
                medication_code="morphine",
                amount=-44000000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=6,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1661027838,
                event_code="DESTROY",
                medication_code="midazolam",
                amount=-36340000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=7,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1661027838,
                event_code="DESTROY",
                medication_code="fentanyl",
                amount=-345000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=8,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1661166388,
                event_code="USE",
                medication_code="midazolam",
                amount=-500000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=9,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1661701387,
                event_code="USE",
                medication_code="fentanyl",
                amount=-6000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=10,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1662580020,
                event_code="USE",
                medication_code="fentanyl",
                amount=-10000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=11,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1665258240,
                event_code="USE",
                medication_code="midazolam",
                amount=-500000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
            Adjustment(
                table="inventory",
                id=12,
                created_date=1670896818,
                modified_date=1670896818,
                modified_by="SRK",
                adjustment_date=1666487700,
                event_code="USE",
                medication_code="midazolam",
                amount=-160000.0,
                reference_id="2200001",
                reporting_period_id=2200001,
            ),
        ]

        assert results == expected

    def test_can_retrieve_current_stock_by_medication(
        self, setup_integration_db: FunctionType
    ) -> None:
        sq_man = SQLiteManager("integration_test.db")
        fent = Medication(
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
        )

        result = ReturnCurrentInventory(sq_man)._calculate_stock(fent)

        expected = 54219000.0

        assert result == expected

    def test_run_report(self, setup_integration_db: FunctionType) -> None:
        sq_man = SQLiteManager("integration_test.db")
        results = ReturnCurrentInventory(sq_man).run()

        print(results)

    def test_can_retrieve_active_medication_info(
        self, setup_integration_db: FunctionType
    ):
        sq_man = SQLiteManager("integration_test.db")

        result = ReturnCurrentInventory(sq_man)._retrieve_medications()

        expected = [
            {"code": "fentanyl", "name": "Fentanyl", "unit": "mcg"},
            {"code": "midazolam", "name": "Midazolam", "unit": "mg"},
            {"code": "morphine", "name": "Morphine", "unit": "mg"},
        ]

        assert result == expected

    def test_can_add_amount_to_medication_dict(self, setup_integration_db):
        sq_man = SQLiteManager("integration_test.db")

        medication_info = [
            {"code": "fentanyl", "name": "Fentanyl", "unit": "mcg"},
            {"code": "midazolam", "name": "Midazolam", "unit": "mg"},
            {"code": "morphine", "name": "Morphine", "unit": "mg"},
        ]

        result = ReturnCurrentInventory(sq_man)._add_amounts(medication_info)
        amounts: list[Union[int, float, str]] = []

        for item in result:
            amounts.append(item["amount"])

        assert amounts == [379000.0, 28840000.0, 25000000.0]

    def test_can_convert_amount_to_preferred(self) -> None:
        medication_info = [
            {
                "code": "fentanyl",
                "name": "Fentanyl",
                "unit": "mcg",
                "amount": 19000,
            },
            {
                "code": "midazolam",
                "name": "Midazolam",
                "unit": "mg",
                "amount": 28840000,
            },
            {"code": "morphine", "name": "Morphine", "unit": "mg", "amount": 25000000},
        ]

        result = ReturnCurrentInventory()._convert_amounts_to_preferred(medication_info)
        converted_amounts = []
        for item in result:
            converted_amounts.append(item["amount"])

        assert converted_amounts == [190, 288.4, 250]
