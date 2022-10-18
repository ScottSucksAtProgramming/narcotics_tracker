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

    test_Unit = (
        UnitBuilder()
        .set_table("units")
        .set_id(-1)
        .set_created_date(1666061200)
        .set_modified_date(1666061200)
        .set_modified_by("System")
        .set_unit_code("dg")
        .set_unit_name("Decagrams")
        .set_decimals(7)
        .build()
    )

    def test_UnitBuilder_can_be_accessed(self) -> None:
        assert UnitBuilder.__doc__ != None

    def test_returned_object_is_an_reporting_period(self) -> None:
        assert isinstance(self.test_Unit, Unit)

    def test_returned_object_had_expected_attributes(self) -> None:
        assert vars(self.test_Unit) == {
            "table": "units",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "System",
            "unit_code": "dg",
            "unit_name": "Decagrams",
            "decimals": 7,
        }
