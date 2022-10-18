"""Unit tests the Units Module.

Classes:

    Test_Units: Unit tests the Unit Class.
"""

from narcotics_tracker.items.units import Unit


class Test_Unit:
    """Unit tests the Unit Class.

    Behaviors Tested:
        - Units class can be accessed.
        - Units return expected id.
        - Units return expected unit_code.
        - Units return expected unit_name.
        - Units return expected decimals.
        - Units return expected string.
        - Units return expected dictionary.
    """

    test_unit = Unit(
        table="units",
        id=-1,
        unit_code="dg",
        unit_name="Decagrams",
        decimals=7,
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="System",
    )

    def test_unit_class_can_be_accessed(self) -> None:
        assert Unit.__doc__ != None

    def test_units_return_expected_id(self) -> None:
        assert self.test_unit.id == -1

    def test_units_return_expected_code(self) -> None:
        assert self.test_unit.unit_code == "dg"

    def test_units_return_expected_name(self) -> None:
        assert self.test_unit.unit_name == "Decagrams"

    def test_units_return_expected_decimals(self) -> None:
        assert self.test_unit.decimals == 7

    def test_units_return_expected_string(self) -> None:
        assert str(self.test_unit) == "Unit #-1: Decagrams (dg)."

    def test_units_return_expected_dictionary(self) -> None:
        assert vars(self.test_unit) == {
            "table": "units",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "System",
            "unit_code": "dg",
            "unit_name": "Decagrams",
            "decimals": 7,
        }
