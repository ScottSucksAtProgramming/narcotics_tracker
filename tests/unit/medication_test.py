#
# * ----------------------------- Documentation ------------------------------ #
# Module:  medication_test.py
# Contains tests for the Medication class, as well as other related classes.
#
#
# Modification History
# 07-27-2022 | SRK | Module Created


import pytest

from narcotics_tracker import Medication, Container, DoseUnit


class TestMedication:
    def test_can_see_Medication_class(self):
        """Checks to see if Medication class is defined."""
        assert type(Medication) == type(object)

    def test_can_instantiate_Medication_object(self):
        """Check to see if Medication object can be instantiated."""

        fentanyl = Medication(
            name="Fentanyl",
            manufacturer="Umbrella Corp",
            box_quantity=25,
            container_type=Container.VIAL,
            fill_amount_in_milliliters=2,
            strength_in_mg=0.1,
            dose_unit=DoseUnit.MCG,
            concentration=0.05,
        )
        assert isinstance(fentanyl, Medication)

    def test_can_get_name(self):
        """Check to see if name can be retrieved."""

        fentanyl = Medication(
            name="Fentanyl",
            manufacturer="Umbrella Corp",
            box_quantity=25,
            container_type=Container.VIAL,
            fill_amount_in_milliliters=2,
            strength_in_mg=0.1,
            dose_unit=DoseUnit.MCG,
            concentration=0.05,
        )
        assert fentanyl.name == "Fentanyl"

    def test_can_get_manufacturer(self):
        """Check to see if manufacturer can be retrieved."""

        fentanyl = Medication(
            name="Fentanyl",
            manufacturer="Umbrella Corp",
            box_quantity=25,
            container_type=Container.VIAL,
            fill_amount_in_milliliters=2,
            strength_in_mg=0.1,
            dose_unit=DoseUnit.MCG,
            concentration=0.05,
        )
        assert fentanyl.manufacturer == "Umbrella Corp"

    def test_can_get_box_quantity(self):
        """Check to see if box_quantity can be retrieved."""

        fentanyl = Medication(
            name="Fentanyl",
            manufacturer="Umbrella Corp",
            box_quantity=25,
            container_type=Container.VIAL,
            fill_amount_in_milliliters=2,
            strength_in_mg=0.1,
            dose_unit=DoseUnit.MCG,
            concentration=0.05,
        )
        assert fentanyl.box_quantity == 25

    def test_can_get_container_type(self):
        """Check to see if container_type can be retrieved."""

        fentanyl = Medication(
            name="Fentanyl",
            manufacturer="Umbrella Corp",
            box_quantity=25,
            container_type=Container.VIAL,
            fill_amount_in_milliliters=2,
            strength_in_mg=0.1,
            dose_unit=DoseUnit.MCG,
            concentration=0.05,
        )
        assert fentanyl.container_type == Container.VIAL

    def test_can_get_fill_amount_in_milliliters(self):
        """Check to see if fill_amount_in_milliliters can be retrieved."""

        fentanyl = Medication(
            name="Fentanyl",
            manufacturer="Umbrella Corp",
            box_quantity=25,
            container_type=Container.VIAL,
            fill_amount_in_milliliters=2,
            strength_in_mg=0.1,
            dose_unit=DoseUnit.MCG,
            concentration=0.05,
        )
        assert fentanyl.fill_amount_in_milliliters == 2

    def test_can_get_strength_in_mg(self):
        """Check to see if strength_in_mg can be retrieved."""

        fentanyl = Medication(
            name="Fentanyl",
            manufacturer="Umbrella Corp",
            box_quantity=25,
            container_type=Container.VIAL,
            fill_amount_in_milliliters=2,
            strength_in_mg=0.1,
            dose_unit=DoseUnit.MCG,
            concentration=0.05,
        )
        assert fentanyl.strength_in_mg == 0.1

    def test_can_get_dose_unit(self):
        """Check to see if dose_unit can be retrieved."""

        fentanyl = Medication(
            name="Fentanyl",
            manufacturer="Umbrella Corp",
            box_quantity=25,
            container_type=Container.VIAL,
            fill_amount_in_milliliters=2,
            strength_in_mg=0.1,
            dose_unit=DoseUnit.MCG,
            concentration=0.05,
        )
        assert fentanyl.dose_unit == DoseUnit.MCG

    def test_can_get_concentration(self):
        """Check to see if concentration can be retrieved."""

        fentanyl = Medication(
            name="Fentanyl",
            manufacturer="Umbrella Corp",
            box_quantity=25,
            container_type=Container.VIAL,
            fill_amount_in_milliliters=2,
            strength_in_mg=0.1,
            dose_unit=DoseUnit.MCG,
            concentration=0.05,
        )
        assert fentanyl.concentration == 0.05

    def test_can_restrict_container_type_to_Containers_enum(self):
        """Check that incorrect container types raise an exception."""

        with pytest.raises(TypeError):
            fentanyl = Medication(
                name="Fentanyl",
                manufacturer="Umbrella Corp",
                box_quantity=25,
                container_type="Vial",
                fill_amount_in_milliliters=2,
                strength_in_mg=0.1,
                dose_unit=DoseUnit.MCG,
                concentration=0.05,
            )

    def test_can_restrict_dose_unit_to_DoseUnit_enum(self):
        """Check that incorrect dose units raise an exception."""

        with pytest.raises(TypeError):
            fentanyl = Medication(
                name="Fentanyl",
                manufacturer="Umbrella Corp",
                box_quantity=25,
                container_type=Container.VIAL,
                fill_amount_in_milliliters=2,
                strength_in_mg=0.1,
                dose_unit="grain",
                concentration=0.05,
            )


class TestContainer:
    """Test the Container class."""

    def test_VIAL_returns_correct_string(self):
        """Check that VIAL returns the correct string."""

        assert Container.VIAL.value == "Vial"

    def test_AMPULE_returns_correct_string(self):
        """Check that AMPULE returns the correct string."""

        assert Container.AMPULE.value == "Ampule"

    def test_PRE_FILLED_SYRINGE_returns_correct_string(self):
        """Check that PRE_FILLED_SYRINGE returns the correct string."""

        assert Container.PRE_FILLED_SYRINGE.value == "Pre-filled Syringe"

    def test_PRE_MIXED_BAG_returns_correct_string(self):
        """Check that PRE_MIXED_BAG returns the correct string."""

        assert Container.PRE_MIXED_BAG.value == "Pre-mixed Bag"
