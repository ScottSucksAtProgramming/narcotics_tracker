"""Configuration for pytest."""

from pytest import fixture

from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import medication_builder


@fixture
def test_med():
    """Return a Medication object for testing."""

    med_builder = medication_builder.MedicationBuilder()
    med_builder.set_medication_id(1)
    med_builder.set_name("Unobtanium")
    med_builder.set_code("Un-69420-9001")
    med_builder.set_container(containers.Container.VIAL)
    med_builder.set_dose_and_unit(69_420, units.Unit.MCG)
    med_builder.set_fill_amount(9_001)
    med_builder.set_status(medication_statuses.MedicationStatus.DISCONTINUED)
    med_builder.set_created_date("08-01-2022")
    med_builder.set_modified_date("08-09-2022")
    med_builder.set_modified_by("SRK")

    test_med = med_builder.build()

    return test_med
