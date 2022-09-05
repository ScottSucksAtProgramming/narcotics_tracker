"""Contains the classes used to unit tests the utils package.

Classes:
    Test_UnitConverter: Contains all unit tests for the unit_converter module.
    Test_Utilities: Contains all unit tests for the utilities module.

"""
from narcotics_tracker.utils import unit_converter


class Test_UnitConverter:
    """Contains all unit tests for the unit_converter module.

    Behaviors Tested:
        - Can convert mg to mcg.
        - Can convert mg to G.
        - Can convert G to mcg.
        - Can convert G to mg.
        - Can convert mcg to mg.
        - Can convert mcg to G.
    """

    def test_convert_mg_to_mcg(self):
        """Check to see if mg can be converted to mcg.

        Asserts that 5 mg returns 5_000 mcg.
        """
        assert unit_converter.UnitConverter.to_mcg(5, "mg") == 5_000

    def test_convert_G_to_mcg(self):
        """Check to see if G can be converted to mcg.

        Asserts that 0.9 G returns 900_000 mcg.
        """
        assert unit_converter.UnitConverter.to_mcg(0.9, "G") == 900_000

    def test_convert_mcg_to_mg(self):
        """Check to see if mcg can be converted to mg.

        Asserts that 500 mcg returns 0.5 mg.
        """
        assert unit_converter.UnitConverter.to_mg(500, "mcg") == 0.5

    def test_convert_G_to_mg(self):
        """Check to see if G can be converted to mg.

        Asserts that 0.9 G returns 900 mg.
        """
        assert unit_converter.UnitConverter.to_mg(0.9, "G") == 900

    def test_convert_mcg_to_G(self):
        """Check to see if mcg can be converted to G.

        Asserts that 1 mcg returns 0.000001 G.
        """
        assert unit_converter.UnitConverter.to_G(1, "mcg") == 0.000001

    def test_convert_mg_to_G(self):
        """
        Test that mg is converted to G.
        """
        assert unit_converter.UnitConverter.to_G(5, "mg") == 0.005
