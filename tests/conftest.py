"""Configuration for pytest."""

from pytest import fixture

from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import builder


@fixture
def test_med():
    """Return a Medication object for testing."""

    medication_builder = builder.MedicationBuilder()
    medication_builder.set_medication_id(1)
    medication_builder.set_name("Unobtanium")
    medication_builder.set_code("Un-69420-9001")
    medication_builder.set_container(containers.Container.VIAL)
    medication_builder.set_dose_and_unit(69_420, units.Unit.MCG)
    medication_builder.set_fill_amount(9_001)
    medication_builder.set_status(medication_statuses.MedicationStatus.DISCONTINUED)
    medication_builder.set_created_date("08-01-2022")
    medication_builder.set_modified_date("08-09-2022")
    medication_builder.set_modified_by("SRK")

    test_med = medication_builder.build()

    return test_med
