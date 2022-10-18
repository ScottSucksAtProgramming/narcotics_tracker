"""Unit tests the Adjustments Module.

Classes:

    Test_Adjustment: Unit tests the Adjustment Class.
"""

from narcotics_tracker.items.adjustments import Adjustment


class Test_Adjustment:
    """Unit tests the Adjustment Class.

    Behaviors Tested:
        - Adjustments class can be accessed.
        - Adjustments return expected id.
        - Adjustments return expected adjustment_date.
        - Adjustments return expected event_code.
        - Adjustments return expected medication_code.
        - Adjustments return expected adjustment_amount.
        - Adjustments return expected reporting_period_id.
        - Adjustments return expected reference_id.
        - Adjustments return expected created_date.
        - Adjustments return expected modified_date.
        - Adjustments return expected modified_by.
        - Adjustments return expected string.
        - Adjustments return expected dictionary.
    """

    test_adjustment = Adjustment(
        table="inventory",
        id=-1,
        adjustment_date=524990800,
        event_code="BIRTH",
        medication_code="TINA",
        adjustment_amount=1,
        reference_id="Tina's Mom",
        reporting_period_id=-36,
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="SRK",
    )

    def test_adjustment_class_can_be_accessed(self) -> None:
        assert Adjustment.__doc__ != None

    def test_adjustments_return_expected_id(self) -> None:
        assert self.test_adjustment.id == -1

    def test_adjustments_return_expected_adjustment_date(self) -> None:
        assert self.test_adjustment.adjustment_date == 524990800

    def test_adjustments_return_expected_event_code(self) -> None:
        assert self.test_adjustment.event_code == "BIRTH"

    def test_adjustments_return_expected_medication_code(self) -> None:
        assert self.test_adjustment.medication_code == "TINA"

    def test_adjustments_return_expected_adjustment_amount(self) -> None:
        assert self.test_adjustment.adjustment_amount == 1

    def test_adjustments_return_expected_reporting_period_id(self) -> None:
        assert self.test_adjustment.reporting_period_id == -36

    def test_adjustments_return_expected_reference_id(self) -> None:
        assert self.test_adjustment.reference_id == "Tina's Mom"

    def test_adjustments_return_expected_created_date(self) -> None:
        assert self.test_adjustment.created_date == 1666061200

    def test_adjustments_return_expected_modified_date(self) -> None:
        assert self.test_adjustment.modified_date == 1666061200

    def test_adjustments_return_expected_modified_by(self) -> None:
        assert self.test_adjustment.modified_by == "SRK"

    def test_adjustments_return_expected_string(self) -> None:
        assert (
            str(self.test_adjustment)
            == "Adjustment #-1: TINA adjusted by 1 due to BIRTH on 524990800."
        )

    def test_adjustments_return_expected_dictionary(self) -> None:
        assert vars(self.test_adjustment) == {
            "table": "inventory",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "SRK",
            "adjustment_date": 524990800,
            "event_code": "BIRTH",
            "medication_code": "TINA",
            "adjustment_amount": 1,
            "reference_id": "Tina's Mom",
            "reporting_period_id": -36,
        }
