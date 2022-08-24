"""Contains the classes used to unit tests the utils package.

Classes:
    Test_UnitConverter: Contains all unit tests for the unit_converter module.
    Test_Utilities: Contains all unit tests for the utilities module.

"""

from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.utils import unit_converter, utilities


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


class Test_Utilities:
    """Contains all unit tests for the utilities module.

    Behaviors Tested:
        - Can create Container enum from string.
        - Can create Unit enum from string.
        - Can create MedicationsStatus enum from string.
    """

    def test_from_string_for_Container(self):
        """Tests enum_from_string creates a Container from its string value.

        Asserts that 'Pre-filled Syringe' equals
        'containers.Container.PRE_FILLED_SYRINGE'.
        """
        assert (
            utilities.enum_from_string(containers.Container, "Pre-filled Syringe")
            == containers.Container.PRE_FILLED_SYRINGE
        )

    def test_from_string_for_MedicationStatus(self):
        """Tests enum_from_string creates a MedicationStatus from its value.

        Asserts that 'disConTinueD' equals
        'medication_statuses.MedicationStatus.Discontinued'.
        """
        assert (
            utilities.enum_from_string(
                medication_statuses.MedicationStatus, "disConTinueD"
            )
            == medication_statuses.MedicationStatus.DISCONTINUED
        )

    def test_from_string_for_Unit(self):
        """Tests enum_from_string creates a Unit from its string value.

        Asserts that 'mg' equals 'units.Unit.MG'.
        """
        assert utilities.enum_from_string(units.Unit, "mg") == units.Unit.MG
