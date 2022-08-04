"""Configuration for pytest."""

from pytest import fixture

from narcotics_tracker.units import units
from narcotics_tracker.medication import (
    builder,
    containers,
    medication_status,
    medication,
)


@fixture
def test_med():
    """Return a Medication object for testing."""

    medication_builder = builder.MedicationBuilder()
    medication_builder.set_name("Unobtanium")
    medication_builder.set_code("Un-69420-9001")
    medication_builder.set_container_type(containers.Container.VIAL)
    medication_builder.set_dose_and_unit(69_420, units.Unit.MCG)
    medication_builder.set_fill_amount(9_001)
    medication_builder.set_status(medication_status.MedicationStatus.DISCONTINUED)

    test_med = medication_builder.build

    return test_med
