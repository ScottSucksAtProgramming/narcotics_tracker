"""Contains the TestMedicationStatus class."""

from narcotics_tracker.medication.medication_status import MedicationStatus


class TestMedicationStatus:
    """Unit tests for the MedicationStatus class."""

    def test_ACTIVE_returns_correct_string(self):
        """Check that ACTIVE returns the correct string."""

        assert MedicationStatus.ACTIVE.value == "Active"

    def test_INACTIVE_returns_correct_string(self):
        """Check that INACTIVE returns the correct string."""

        assert MedicationStatus.INACTIVE.value == "Inactive"

    def test_DISCONTINUED_returns_correct_string(self):
        """Check that DISCONTINUED returns the correct string."""

        assert MedicationStatus.DISCONTINUED.value == "Discontinued"
