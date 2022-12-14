"""Contains the unit tests for the ReturnMedicationStock Report.

Classes:
"""
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.items.medications import Medication
from narcotics_tracker.reports import ReturnMedicationStock

# pylint: disable=missing-function-docstring, singleton-comparison, protected-access
# pyright: reportPrivateUsage=false


class TestReturnMedicationStock:
    """Unit tests the ReturnMedicationStock Report.

    Behaviors Tested:

        - Class can be accessed.
        - Receiver can be set in initializer."""

    def test_can_access_class(self):
        assert ReturnMedicationStock().__doc__ != None

    def test_can_set_receiver(self):
        return_medication_stock = ReturnMedicationStock("FakePersistenceService")  # type: ignore
        assert return_medication_stock._receiver == "FakePersistenceService"

    def test_can_set_medication_code(self, test_medication) -> None:
        med = test_medication
        report = ReturnMedicationStock()
        report.set_medication(med)
        assert report._medication == med

    def test_can_reset(self, test_medication) -> None:
        med: "Medication" = test_medication
        report = ReturnMedicationStock()
        report.set_medication(med)
        report._reset()
        assert report._medication == Medication(
            table=None,
            id=None,
            created_date=None,
            modified_by=None,
            modified_date=None,
            medication_amount=None,
            medication_code=None,
            medication_name=None,
            fill_amount=None,
            concentration=None,
            preferred_unit=None,
            status=None,
        )

    def test_can_extract_amount_from_adjustment_data(self):
        test_adjustments = [
            Adjustment(
                table="inventory",
                id=1,
                adjustment_date=1658523600,
                event_code="IMPORT",
                medication_code="fentanyl",
                amount=1,
                reporting_period_id=2200001,
                reference_id="2200001",
                created_date=1667351782,
                modified_date=1667351782,
                modified_by="SRK",
            ),
            Adjustment(
                table="inventory",
                id=4,
                adjustment_date=1659212760,
                event_code="USE",
                medication_code="fentanyl",
                amount=2,
                reporting_period_id=2200001,
                reference_id="2200001",
                created_date=1667351782,
                modified_date=1667351782,
                modified_by="SRK",
            ),
            Adjustment(
                table="inventory",
                id=7,
                adjustment_date=1661027838,
                event_code="DESTROY",
                medication_code="fentanyl",
                amount=3,
                reporting_period_id=2200001,
                reference_id="2200001",
                created_date=1667351782,
                modified_date=1667351782,
                modified_by="SRK",
            ),
            Adjustment(
                table="inventory",
                id=9,
                adjustment_date=1661701387,
                event_code="USE",
                medication_code="fentanyl",
                amount=4,
                reporting_period_id=2200001,
                reference_id="2200001",
                created_date=1667351782,
                modified_date=1667351782,
                modified_by="SRK",
            ),
            Adjustment(
                table="inventory",
                id=10,
                adjustment_date=1662580020,
                event_code="USE",
                medication_code="fentanyl",
                amount=5,
                reporting_period_id=2200001,
                reference_id="2200001",
                created_date=1667351782,
                modified_date=1667351782,
                modified_by="SRK",
            ),
        ]

        result = ReturnMedicationStock()._extract_adjustment_amounts(test_adjustments)

        assert result == [1, 2, 3, 4, 5]
