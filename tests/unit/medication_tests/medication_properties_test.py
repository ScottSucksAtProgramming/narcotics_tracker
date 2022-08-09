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


class TestMedicationProperties:
    """Unit Tests for the properties of the Medication class."""

    def test_can_instantiate_Medication_object(self, test_med):
        """Check to see if Medication object can be instantiated."""

        test_med = test_med

        assert isinstance(test_med, medication.Medication)

    def test_medication_id(self, test_med):
        """Check to see if the medication's id can be retrieved."""

        test_med = test_med

        assert medication.Medication.medication_id == None

    def test_code(self, test_med):
        """Check to see if medication's unique code can be retrieved."""

        test_med = test_med

        assert test_med.code == "Un-69420-9001"

    def test_name(self, test_med):
        """Check to see if the medication's name can be retrieved."""

        test_med = test_med

        assert test_med.name == "Unobtanium"

    def test_container_type(self, test_med):
        """Check to see if the medications container_type can be retrieved."""

        test_med = test_med

        assert test_med.container_type == containers.Container.VIAL

    def test_fill_amount(self, test_med):
        """Check to see if the medication's fill_amount can be retrieved."""

        test_med = test_med

        assert test_med.fill_amount == 9_001

    def test_dose(self, test_med):
        """Check to see if the medication's dose can be retrieved."""

        test_med = test_med

        assert test_med.dose == 69_420

    def test__unit(self, test_med):
        """Check to see if the medication's unit can be retrieved."""

        test_med = test_med

        assert test_med.unit == units.Unit.MCG

    def test_unit_restriction(self):
        """Checks that a medication with an incorrect unit type raises an
        exception."""

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

    def test_concentration(self, test_med):
        """Check to see if the medication's concentration can be retrieved."""

        test_med = test_med

        assert test_med.concentration == 7.712476391512054

    def test_container_type_restriction(self):
        """Checks that a medication with an incorrect container types raises
        an exception."""

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

    def test_created_date(self, test_med):
        """Checks to see if the medication's created_date can be retrieved."""

        test_med = test_med
        test_med.created_date = "08-01-2022"

        assert test_med.created_date == "08-01-2022"

    def test_modified_date(self, test_med):
        """Checks to see if the medication's modified_date can be retrieved."""

        test_med = test_med
        test_med.modified_date = "08-09-2022"

        assert test_med.modified_date == "08-09-2022"

    def test_modified_by(self, test_med):
        """Checks to see if the medication's modified_by property can be retrieved."""

        test_med = test_med
        test_med.modified_by = "SRK"

        assert test_med.modified_by == "SRK"

    def test_mediation_can_be_edited(self, test_med):
        """Checks to see if a medication's properties return the new value
        after being edited."""

        test_med = test_med

        test_med.unit = units.Unit.G

        assert str(test_med) == (
            f"Medication Object 1 for Unobtanium with code Un-69420-9001. "
            f"Container type: Vial. Fill amount: 9001 ml. Dose: 69420 G. "
            f"Concentration: 7.712476391512054. Status: Discontinued. "
            f"Created on 08-01-2022. Last modified on 08-09-2022 by SRK."
        )
