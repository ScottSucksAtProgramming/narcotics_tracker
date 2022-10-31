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

    def test_adjustmentbuilder_can_be_accessed(self) -> None:
        assert DataItemBuilder.__doc__ != None

    def test_returned_object_is_an_adjustment(self, test_adjustment) -> None:
        assert isinstance(test_adjustment, Adjustment)

    def test_returned_object_had_expected_attributes(self, test_adjustment) -> None:
        assert vars(test_adjustment) == {
            "table": "no table",
            "id": -5,
            "created_date": 505077000,
            "modified_date": 1666117887,
            "modified_by": "System",
            "adjustment_date": 3,
            "event_code": None,
            "medication_code": None,
            "amount": None,
            "reference_id": None,
            "reporting_period_id": None,
        }
