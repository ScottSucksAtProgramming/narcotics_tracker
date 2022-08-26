"""Contains the Test_Builder class used to test the medication_builder module.

Classes: 

    Test_Builder: Contains all unit tests for the medication_builder module.
"""
import pytest

from narcotics_tracker import medication
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import medication_builder


class Test_Builder:
    """Contains all unit tests for the medication_builder module.

    Behaviors Tested:
        - MedicationBuilder sets the medication id correctly.
        - MedicationBuilder sets the medication name correctly.
        - MedicationBuilder sets the medication code correctly.
        - MedicationBuilder sets the medication container correctly.
        - An exception is raised if the medication container is not valid.
        - MedicationBuilder sets the medication fill amount correctly.
        - MedicationBuilder sets the medication dose correctly.
        - MedicationBuilder sets the medication unit correctly.
        - An exception is raised if the medication unit is not valid.
        - MedicationBuilder sets the medication concentration correctly.
        - MedicationBuilder sets the medication status correctly.
        - An exception is raised if the medication status is not valid.
        - MedicationBuilder sets the medication created date correctly.
        - MedicationBuilder sets the medication modified date correctly.
        - MedicationBuilder sets the medication modified by correctly.
        - MedicationBuilder calculates the medication concentration correctly.
        - Created medication object has type medication.Medication.
    """

    def test_set_medication_id(self):
        """Tests that MedicationBuilder sets the medication id correctly.

        Asserts that the medication id returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 69420

        med_builder.set_medication_id(expected)

        assert med_builder.medication_id == expected

    def test_set_name(self):
        """Tests that the medication builder sets the name.

        Asserts the medication name returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "Aspirin"

        med_builder.set_name("Aspirin")

        assert med_builder.name == expected

    def test_set_code(self):
        """Tests that the medication builder sets the code.

        Asserts that the medication code returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "ASA"

        med_builder.set_code("ASA")

        assert med_builder.medication_code == expected

    def test_set_container(self):
        """Tests that the medication builder sets the container type.

        Asserts that the medication container returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "Ampule"

        med_builder.set_container(containers.Container.AMPULE)
        assert med_builder.container_type.value == expected

    def test_set_container_raises_exception_if_invalid(self):
        """Tests that the medication builder raises an exception if invalid.

        Passes if an AttributeError exception is raised."""

        med_builder = medication_builder.MedicationBuilder()

        with pytest.raises(AttributeError):
            med_builder.set_container(containers.Container.INVALID)

    def test_set_fill_amount(self):
        """Tests that the medication builder sets the fill amount.

        Asserts that the medication fill amount returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 10_000

        med_builder.set_fill_amount(expected)

        assert med_builder.fill_amount == expected

    def test_set_dose(self):
        """Tests that the medication builder sets the dose and unit.

        Asserts that the medication dose returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 10_000

        med_builder.set_dose_and_unit(10, units.Unit.MG)

        assert med_builder.dose == expected

    def test_set_unit(self):
        """Tests that the medication builder sets the dose and unit.

        Asserts that the medication dose returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "mg"

        med_builder.set_dose_and_unit(10, units.Unit.MG)

        assert med_builder.unit.value == expected

    def test_set_unit_raises_exception_if_invalid(self):
        """Tests that the medication builder raises an exception if invalid.

        Passes if an AttributeError exception is raised.
        """
        med_builder = medication_builder.MedicationBuilder()

        with pytest.raises(AttributeError):
            med_builder.set_unit(units.Unit.INVALID)

    def test_set_concentration(self):
        """Tests that the medication builder sets the concentration.

        Asserts that the medication concentration returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 45

        med_builder.set_concentration(expected)

        assert med_builder.concentration == expected

    def test_set_status(self):
        """Tests that the medication builder sets the status.

        Asserts that the medication status returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_status(medication_statuses.MedicationStatus.ACTIVE)
        expected = "Active"

        assert med_builder.status.value == expected

    def test_set_status_raises_exception_if_invalid(self):
        """Tests that the medication builder raises an exception if invalid.

        Passes if an AttributeError exception is raised.
        """
        med_builder = medication_builder.MedicationBuilder()

        with pytest.raises(AttributeError):
            med_builder.set_status(medication_statuses.MedicationStatus.INVALID)

    def test_set_created_date(self):
        """Tests that the medication builder sets the created date.

        Asserts that the medication created date returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "01/01/2019"

        med_builder.set_created_date(expected)

        assert med_builder.created_date == expected

    def test_set_modified_date(self):
        """Tests that the medication builder sets the modified date.

        Asserts that the medication modified date returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "08/21/1986"

        med_builder.set_modified_date(expected)

        assert med_builder.modified_date == expected

    def test_set_modified_by(self):
        """Tests that the medication builder sets the modified by.

        Asserts that the medication modified by returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "John Doe"

        med_builder.set_modified_by(expected)

        assert med_builder.modified_by == expected

    def test_calculate_concentration(self):
        """Tests that the medication builder sets the concentration.

        Asserts that the medication concentration returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 1

        med_builder.set_dose_and_unit(10, units.Unit.MCG)
        med_builder.set_fill_amount(10)

        med_builder.calculate_concentration()

        assert med_builder.concentration == expected

    def test_med_builder_creates_medication_object(self):
        """Tests that the medication builder creates a medication object.

        Asserts that the medication object returns a Medication object.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = medication.Medication

        med_builder.set_medication_id(None)
        med_builder.set_name("Aspirin")
        med_builder.set_code("ASA")
        med_builder.set_fill_amount(10)
        med_builder.set_container(containers.Container.AMPULE)
        med_builder.set_dose_and_unit(10, units.Unit.MCG)
        med_builder.set_status(medication_statuses.MedicationStatus.ACTIVE)
        med_builder.set_created_date(None)
        med_builder.set_modified_date(None)
        med_builder.set_modified_by("SRK")

        aspirin = med_builder.build()

        assert isinstance(aspirin, expected)
