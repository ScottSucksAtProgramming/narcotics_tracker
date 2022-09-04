"""Contains the Test_Container, Test_MedicationStatus and Test_Unit classes.

Classes:
    Test_Container: Contains all unit tests for the containers module.
    
    Test_MedicationStatus: Contains all unit tests for the medication_status module."
    
    Test_Unit: Contains all unit tests for the units module.
    """
import pytest

from narcotics_tracker import medication
from narcotics_tracker.enums import medication_statuses


class Test_MedicationStatus:
    """Contains all unit tests for the medication_status module.

    Behaviors Tested:
        - Tests that the Enum values return the correct string.
        - Tests that an invalid value raises an 'AttributeError'.
    """

    def test_ACTIVE_returns_correct_string(self):
        """Tests that ACTIVE returns the correct string.

        Asserts that value equals 'Active'.
        """
        assert medication_statuses.MedicationStatus.ACTIVE.value == "Active"

    def test_INACTIVE_returns_correct_string(self):
        """Tests that INACTIVE returns the correct string.

        Asserts that value equals 'Inactive'.
        """
        assert medication_statuses.MedicationStatus.INACTIVE.value == "Inactive"

    def test_DISCONTINUED_returns_correct_string(self):
        """Tests that DISCONTINUED returns the correct string.

        Asserts that value equals 'Discontinued'.
        """
        assert medication_statuses.MedicationStatus.DISCONTINUED.value == "Discontinued"

    def test_can_restrict_status_to_MedicationStatus_enum(self):
        """Tests that incorrect statuses raise an exception.

        Test passes if an 'AttributeError' is raised.
        """
        with pytest.raises(AttributeError):
            fentanyl = medication.Medication(
                name="Fentanyl",
                code="Fe-100-2",
                container_type="Vial",
                fill_amount=2,
                dose=100,
                unit="mcg",
                concentration=50,
                status=medication_statuses.MedicationStatus.ON_VACATION,
                created_date="08-01-2022",
                modified_date="08-01-2022",
                modified_by="test",
            )
