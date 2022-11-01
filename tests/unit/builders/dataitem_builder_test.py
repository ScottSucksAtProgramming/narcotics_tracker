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
            "table": "inventory",
            "id": -77,
            "created_date": 1666117887,
            "modified_date": 1666117887,
            "modified_by": "System",
            "adjustment_date": 1666117887,
            "event_code": "TEST",
            "medication_code": "apap",
            "amount": 10,
            "reference_id": "TestReferenceID",
            "reporting_period_id": 0,
        }
