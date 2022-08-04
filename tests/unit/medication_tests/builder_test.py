"""Contains the TestMedicationBuilder class."""

from narcotics_tracker.medication import (
    builder,
    containers,
    medication_status,
    medication,
)
from narcotics_tracker.units import units, unit_converter


class TestMedicationBuilder:
    """Tests the behaviors of the Medication Builder"""


def test_medication_builder_sets_name():
    """Tests that the medication builder sets the name"""
    medication_builder = builder.MedicationBuilder()

    medication_builder.set_name("Aspirin")

    assert medication_builder.name == "Aspirin"


def test_medication_builder_sets_code():
    """Tests that the medication builder sets the codes"""
    medication_builder = builder.MedicationBuilder()

    medication_builder.set_code("ASA")

    assert medication_builder.code == "ASA"


def test_medication_builder_sets_container_type():
    """Tests that the medication builder sets the container type"""
    medication_builder = builder.MedicationBuilder()

    medication_builder.set_container_type(containers.Container.AMPULE)
    assert medication_builder.container_type.value == "Ampule"


def test_medication_builder_sets_dose():
    """Tests that the medication builder sets the dose and unit"""
    medication_builder = builder.MedicationBuilder()

    medication_builder.set_container_type(containers.Container.AMPULE)

    medication_builder.set_dose_and_unit(10, units.Unit.MG)

    assert medication_builder.dose == unit_converter.UnitConverter.to_mcg(
        10, units.Unit.MG.value
    )


def test_medication_builder_sets_unit():
    """Tests that the medication builder sets the dose and unit"""

    medication_builder = builder.MedicationBuilder()

    medication_builder.set_dose_and_unit(10, units.Unit.MG)

    assert medication_builder.unit.value == "mg"


def test_medication_builder_sets_fill_amount():
    """Tests that the medication builder sets the fill amount"""

    medication_builder = builder.MedicationBuilder()

    medication_builder.set_fill_amount(10)

    assert medication_builder.fill_amount == 10


def test_medication_builder_calculates_concentration():
    """Tests that the medication builder sets the concentration"""

    medication_builder = builder.MedicationBuilder()
    medication_builder.set_dose_and_unit(10, units.Unit.MCG)
    medication_builder.set_fill_amount(10)

    medication_builder.calculate_concentration()

    assert medication_builder.concentration == 1


def test_medication_builders_set_status():
    """Tests that the medication builder sets the status"""

    medication_builder = builder.MedicationBuilder()

    medication_builder.set_status(medication_status.MedicationStatus.ACTIVE)

    assert medication_builder.status.value == "Active"


def test_medication_builder_creates_medication_object():
    """Tests that the medication builder creates a medication object"""

    medication_builder = builder.MedicationBuilder()
    medication_builder.set_name("Aspirin")
    medication_builder.set_code("ASA")
    medication_builder.set_container_type(containers.Container.AMPULE)
    medication_builder.set_dose_and_unit(10, units.Unit.MCG)
    medication_builder.set_fill_amount(10)
    medication_builder.set_status(medication_status.MedicationStatus.ACTIVE)

    aspirin = medication_builder.build

    assert isinstance(aspirin, medication.Medication)
