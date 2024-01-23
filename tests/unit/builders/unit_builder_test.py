"""Contains the unit tests for the UnitBuilder.

Classes:
    Test_UnitBuilder: Unit tests the UnitBuilder.
"""


from narcotics_tracker.builders.unit_builder import UnitBuilder
from narcotics_tracker.items.units import Unit


class Test_UnitBuilder:
    """Unit tests the UnitBuilder.

    Behaviors Tested:
        - Can be accessed.
        - Returns a Unit Object.
        - Returned object has expected attribute values.
    """

    def test_UnitBuilder_can_be_accessed(self) -> None:
        assert UnitBuilder.__doc__ != None

    def test_returned_object_is_an_reporting_period(self, test_unit) -> None:
        assert isinstance(test_unit, Unit)

    def test_returned_object_had_expected_attributes(self, test_unit) -> None:
        assert vars(test_unit) == {
            "table": "units",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "System",
            "unit_code": "dg",
            "unit_name": "decagrams",
            "decimals": 7,
        }
