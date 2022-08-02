"""Configuration for pytest."""

from pytest import fixture

from narcotics_tracker.medication.medication import (
    Medication,
    MedicationStatus,
    Container,
)
from narcotics_tracker.units.units import Unit


@fixture
def test_med():
    """Return a Medication object for testing."""

    return Medication(
        name="Fentanyl",
        code="Fe-100-2",
        container_type=Container.VIAL,
        fill_amount=2,
        dose=100,
        unit=Unit.MCG,
        concentration=50,
        status=MedicationStatus.ACTIVE,
        created_date="08-01-2022",
        modified_date="08-01-2022",
        modified_by="test",
    )
