"""Contains the unit tests for the utilities module."""

from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.utils import unit_converter, utilities


class Test_UnitConverterClass:
    """Unit tests for the UnitConverter class."""

    def test_convert_mg_to_mcg(self):
        """Check to see if mg to mcg conversion works."""

        assert unit_converter.UnitConverter.to_mcg(5, "mg") == 5_000

    def test_convert_G_to_mcg(self):
        """
        Test that G is converted to mcg.
        """

        assert unit_converter.UnitConverter.to_mcg(0.9, "G") == 900_000

    def test_convert_mcg_to_mg(self):
        """
        Test that mcg is converted to mg.
        """

        assert unit_converter.UnitConverter.to_mg(500, "mcg") == 0.5

    def test_convert_G_to_mg(self):
        """
        Test that G is converted to mg.
        """

        assert unit_converter.UnitConverter.to_mg(0.9, "G") == 900

    def test_convert_mcg_to_G(self):
        """
        Test that mcg is converted to G.
        """

        assert unit_converter.UnitConverter.to_G(1, "mcg") == 0.000001

    def test_convert_mg_to_D(self):
        """
        Test that mg is converted to G.
        """

        assert unit_converter.UnitConverter.to_G(5, "mg") == 0.005


class Test_UtilitiesClass:
    """Unit tests for the Utilities class."""

    def test_from_string_for_Container(self):
        """Check that from_string returns the correct enum value."""

        assert (
            utilities.enum_from_string(containers.Container, "Pre-filled Syringe")
            == containers.Container.PRE_FILLED_SYRINGE
        )

    def test_from_string_for_MedicationStatus(self):
        """Check that from_string returns the correct enum value."""

        assert (
            utilities.enum_from_string(
                medication_statuses.MedicationStatus, "disConTinueD"
            )
            == medication_statuses.MedicationStatus.DISCONTINUED
        )

    def test_from_string_for_Unit(self):
        """Check that from_string returns the correct enum value."""

        assert utilities.enum_from_string(units.Unit, "mg") == units.Unit.MG
