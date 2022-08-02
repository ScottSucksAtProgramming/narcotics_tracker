"""Contains the TestUnitConverter class."""

from narcotics_tracker.units.converter import UnitConverter


class TestUnitConverter:
    """Tests the UnitConverter class."""

    def test_convert_mg_to_mcg(self):
        """Check to see if mg to mcg conversion works."""

        assert UnitConverter.to_mcg(5, "mg") == 5_000

    def test_convert_G_to_mcg(self):
        """
        Test that G is converted to mcg.
        """

        assert UnitConverter.to_mcg(0.9, "G") == 900_000

    def test_convert_mcg_to_mg(self):
        """
        Test that mcg is converted to mg.
        """

        assert UnitConverter.to_mg(500, "mcg") == 0.5

    def test_convert_G_to_mg(self):
        """
        Test that G is converted to mg.
        """

        assert UnitConverter.to_mg(0.9, "G") == 900

    def test_convert_mcg_to_G(self):
        """
        Test that mcg is converted to G.
        """

        assert UnitConverter.to_G(1, "mcg") == 0.000001

    def test_convert_mg_to_D(self):
        """
        Test that mg is converted to G.
        """

        assert UnitConverter.to_G(5, "mg") == 0.005
