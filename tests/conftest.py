"""Configuration for pytest."""

from pytest import fixture

from narcotics_tracker.units import units
from narcotics_tracker.medication import containers, medication_status, medication


@fixture
def test_med():
    """Return a Medication object for testing."""

    return medication.Medication(
        name="Unobtanium",
        code="Un-69420-9001",
        container_type=containers.Container.VIAL,
        fill_amount=9_001,
        dose=69_420,
        unit=units.Unit.MCG,
        concentration=69,
        status=medication_status.MedicationStatus.DISCONTINUED,
        created_date="08-01-2022",
        modified_date="08-01-2022",
        modified_by="Michael Meyers",
    )
