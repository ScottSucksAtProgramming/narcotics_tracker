"""Contains the TestUnit class."""

import pytest

from narcotics_tracker.medication import containers, medication_status, medication
from narcotics_tracker.units import units


class TestUnit:
    """Tests the Unit class."""

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
                status=medication_status.MedicationStatus.ACTIVE,
                created_date="08-01-2022",
                modified_date="08-01-2022",
                modified_by="test",
            )
