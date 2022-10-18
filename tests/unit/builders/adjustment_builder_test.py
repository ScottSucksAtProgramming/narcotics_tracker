"""Contains the unit tests for the AdjustmentBuilder.

Classes:
    Test_adjustmentBuilder: Unit tests the AdjustmentBuilder.
"""


from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.items.adjustments import Adjustment


class Test_AdjustmentBuilder:
    """Unit tests the AdjustmentBuilder.

    Behaviors Tested:
        - Can be accessed.
        - Returns an Adjustment Object.
        - Returned object has expected attribute values.
    """

    test_adjustment = (
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
        .build()
    )

    def test_adjustmentbuilder_can_be_accessed(self) -> None:
        assert AdjustmentBuilder.__doc__ != None

    def test_returned_object_is_an_adjustment(self) -> None:
        assert isinstance(self.test_adjustment, Adjustment)

    def test_returned_object_had_expected_attributes(self) -> None:
        assert vars(self.test_adjustment) == {
            "table": "inventory",
            "id": -77,
            "created_date": 1666117887,
            "modified_date": 1666117887,
            "modified_by": "System",
            "adjustment_date": 1666117887,
            "event_code": "TEST",
            "medication_code": "FakeMed",
            "adjustment_amount": 10,
            "reference_id": "TestReferenceID",
            "reporting_period_id": 0,
        }
