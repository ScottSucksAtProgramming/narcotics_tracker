"""Contains all unit tests for the enums used in the narcotics_tracker."""

import pytest

from narcotics_tracker import medication
from narcotics_tracker.enums import containers, medication_statuses, units


class Test_ContainerClass:
    """Unit tests for the Container class."""

    def test_VIAL_returns_correct_string(self):
        """Check that VIAL returns the correct string."""

        assert containers.Container.VIAL.value == "Vial"

    def test_AMPULE_returns_correct_string(self):
        """Check that AMPULE returns the correct string."""

        assert containers.Container.AMPULE.value == "Ampule"

    def test_PRE_FILLED_SYRINGE_returns_correct_string(self):
        """Check that PRE_FILLED_SYRINGE returns the correct string."""

        assert containers.Container.PRE_FILLED_SYRINGE.value == "Pre-filled Syringe"

    def test_PRE_MIXED_BAG_returns_correct_string(self):
        """Check that PRE_MIXED_BAG returns the correct string."""

        assert containers.Container.PRE_MIXED_BAG.value == "Pre-mixed Bag"


class Test_MedicationStatusClass:
    """Unit tests for the MedicationStatus class."""

    def test_ACTIVE_returns_correct_string(self):
        """Check that ACTIVE returns the correct string."""

        assert medication_statuses.MedicationStatus.ACTIVE.value == "Active"

    def test_INACTIVE_returns_correct_string(self):
        """Check that INACTIVE returns the correct string."""

        assert medication_statuses.MedicationStatus.INACTIVE.value == "Inactive"

    def test_DISCONTINUED_returns_correct_string(self):
        """Check that DISCONTINUED returns the correct string."""

        assert medication_statuses.MedicationStatus.DISCONTINUED.value == "Discontinued"


class Test_UnitClass:
    """Unit tests for the Unit class."""

    def test_MCG_returns_correct_string(self):
        """Check that MCG returns the correct string."""

        assert units.Unit.MCG.value == "mcg"

    def test_MG_returns_correct_string(self):
        """Check that MG returns the correct string."""

        assert units.Unit.MG.value == "mg"

    def test_G_returns_correct_string(self):
        """Check that G returns the correct string."""

        assert units.Unit.G.value == "G"

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
                status=medication_statuses.MedicationStatus.ACTIVE,
                created_date="08-01-2022",
                modified_date="08-01-2022",
                modified_by="test",
            )
