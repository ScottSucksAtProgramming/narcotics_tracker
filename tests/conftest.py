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
        name="Unobtanium",
        code="Un-69420-9001",
        container_type=Container.VIAL,
        fill_amount=9_001,
        dose=69_420,
        unit=Unit.MCG,
        concentration=69,
        status=MedicationStatus.DISCONTINUED,
        created_date="08-01-2022",
        modified_date="08-01-2022",
        modified_by="Michael Meyers",
    )
