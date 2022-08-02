#
# * ----------------------------- Documentation ------------------------------ #
# Module:  medication_test.py
# Contains tests for the Medication class, as well as other related classes.
#
#
# Modification History
# 07-27-2022 | SRK | Module Created


import pytest

from narcotics_tracker.medication import medication_status, medication, containers
from narcotics_tracker.units import units


class TestMedication:
    """Unit Tests for the Medication Class."""

    # TODO: Test repr.

    def test_can_see_Medication_class(self):
        """Checks to see if Medication class is defined."""

    def test_can_instantiate_Medication_object(self, test_med):
        """Check to see if Medication object can be instantiated."""

        test_med = test_med

        assert isinstance(test_med, medication.Medication)

    def test_can_get_name(self, test_med):
        """Check to see if name can be retrieved."""

        test_med = test_med

        assert test_med.name == "Unobtanium"

    def test_can_get_code(self, test_med):
        """Check to see if code can be retrieved."""

        test_med = test_med

        assert test_med.code == "Un-69420-9001"

    def test_can_get_container_type(self, test_med):
        """Check to see if container_type can be retrieved."""

        test_med = test_med

        assert test_med.container_type == containers.Container.VIAL

    def test_can_get_fill_amount(self, test_med):
        """Check to see if fill_amount can be retrieved."""

        test_med = test_med

        assert test_med.fill_amount == 9_001

    def test_can_get_dose(self, test_med):
        """Check to see if dose can be retrieved."""

        test_med = test_med

        assert test_med.dose == 69_420

    def test_can_get_unit(self, test_med):
        """Check to see if unit can be retrieved."""

        test_med = test_med

        assert test_med.unit == units.Unit.MCG

    def test_can_get_concentration(self, test_med):
        """Check to see if concentration can be retrieved."""

        test_med = test_med

        assert test_med.concentration == 69

    def test_can_restrict_container_type_to_Containers_enum(self):
        """Check that incorrect container types raise an exception."""

        with pytest.raises(AttributeError):
            fentanyl = medication.Medication(
                name="Fentanyl",
                code="Fe-100-2",
                container_type=containers.Container.BOTTLE,
                fill_amount=2,
                dose=100,
                unit=units.Unit.MCG,
                concentration=50,
                status=medication_status.MedicationStatus.ACTIVE,
                created_date="08-01-2022",
                modified_date="08-01-2022",
                modified_by="test",
            )

    def test_can_restrict_unit_to_Unit_enum(self):
        """Check that incorrect units raise an exception."""

        with pytest.raises(AttributeError):
            fentanyl = medication.Medication(
                name="Fentanyl",
                code="Fe-100-2",
                container_type=containers.Container.VIAL,
                fill_amount=2,
                dose=100,
                unit=units.Unit.KG,
                concentration=50,
                status=medication_status.MedicationStatus.ACTIVE,
                created_date="08-01-2022",
                modified_date="08-01-2022",
                modified_by="test",
            )

    def test_printing_a_Medication_object_returns_correct_string(self, test_med):
        """Check to see if printing a Medication object returns a string."""

        test_med = test_med

        assert (
            str(test_med)
            == "Medication Object for Un-69420-9001: Unobtanium - 69420mcg in a 9001ml Vial (69mcg/ml) - Status: Discontinued - Created on: 08-01-2022 - Last Modified on: 08-01-2022 by Michael Meyers."
        )

    def test_mediation_can_be_edited(self, test_med):
        """Check to see if Medication object can be edited."""

        test_med = test_med

        test_med.unit = units.Unit.G

        assert (
            str(test_med)
            == "Medication Object for Un-69420-9001: Unobtanium - 69420G in a 9001ml Vial (69G/ml) - Status: Discontinued - Created on: 08-01-2022 - Last Modified on: 08-01-2022 by Michael Meyers."
        )
