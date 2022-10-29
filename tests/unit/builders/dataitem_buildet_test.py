"""Contains the unit tests for the DataItemBuilder.

Classes:
    Test_DataItemBuilder: Unit tests the DataItemBuilder.
"""


from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.builders.dataitem_builder import DataItemBuilder
from narcotics_tracker.items.adjustments import Adjustment


class Test_AdjustmentBuilder:
    """Unit tests the DataItemBuilder.

    Behaviors Tested:
        - Can be accessed.
        - Returns an Adjustment Object.
        - Returned object has expected attribute values.
    """

    test_adjustment = (
        AdjustmentBuilder()
        .set_table("no table")
        .set_id(-5)
        .set_created_date("01-02-1986 14:10:00")
        .set_modified_date(1666117887)
        .set_modified_by("System")
        .set_adjustment_date(None)
        .set_event_code(None)
        .set_medication_code(None)
        .set_adjustment_amount(None)
        .set_reference_id(None)
        .set_reporting_period_id(None)
        .build()
    )

    def test_adjustmentbuilder_can_be_accessed(self) -> None:
        assert DataItemBuilder.__doc__ != None

    def test_returned_object_is_an_adjustment(self) -> None:
        assert isinstance(self.test_adjustment, Adjustment)

    def test_returned_object_had_expected_attributes(self) -> None:
        assert vars(self.test_adjustment) == {
            "table": "no table",
            "id": -5,
            "created_date": 505077000,
            "modified_date": 1666117887,
            "modified_by": "System",
            "adjustment_date": None,
            "event_code": None,
            "medication_code": None,
            "amount": None,
            "reference_id": None,
            "reporting_period_id": None,
        }
