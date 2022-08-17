"""Contains the unit tests for the builders module."""

from narcotics_tracker import medication
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import medication_builder


class Test_Builder:
    """Unit tests for the Builder class."""

    def test_set_medication_id(self):
        """Tests that the medication builder sets the medication id"""
        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_medication_id(1)

        assert med_builder.medication_id == 1

    def test_set_name(self):
        """Tests that the medication builder sets the name"""
        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_name("Aspirin")

        assert med_builder.name == "Aspirin"

    def test_set_code(self):
        """Tests that the medication builder sets the code"""

        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_code("ASA")

        assert med_builder.code == "ASA"

    def test_set_container(self):
        """Tests that the medication builder sets the container type"""
        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_container(containers.Container.AMPULE)
        assert med_builder.container_type.value == "Ampule"

    def test_set_fill_amount(self):
        """Tests that the medication builder sets the fill amount"""

        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_fill_amount(10)

        assert med_builder.fill_amount == 10

    def test_sets_dose_correctly(self):
        """Tests that the medication builder sets the dose and unit"""
        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_dose_and_unit(10, units.Unit.MG)

        assert med_builder.dose == 10_000

    def test_sets_unit_correctly(self):
        """Tests that the medication builder sets the dose and unit"""

        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_dose_and_unit(10, units.Unit.MG)

        assert med_builder.unit.value == "mg"

    def test_set_concentration(self):
        """Tests that the medication builder sets the concentration"""

        med_builder = medication_builder.MedicationBuilder()
        med_builder.set_concentration(10)

        assert med_builder.concentration == 10

    def test_set_status(self):
        """Tests that the medication builder sets the status"""

        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_status(medication_statuses.MedicationStatus.ACTIVE)

        assert med_builder.status.value == "Active"

    def test_set_created_date(self):
        """Tests that the medication builder sets the created date"""

        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_created_date("01/01/2019")

        assert med_builder.created_date == "01/01/2019"

    def test_set_modified_date(self):
        """Tests that the medication builder sets the modified date"""

        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_modified_date("01/01/2019")

        assert med_builder.modified_date == "01/01/2019"

    def test_set_modified_by(self):
        """Tests that the medication builder sets the modified by"""

        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_modified_by("John Doe")

        assert med_builder.modified_by == "John Doe"

    def test_med_builder_calculates_concentration(self):
        """Tests that the medication builder sets the concentration"""

        med_builder = medication_builder.MedicationBuilder()
        med_builder.set_dose_and_unit(10, units.Unit.MCG)
        med_builder.set_fill_amount(10)

        med_builder.calculate_concentration()

        assert med_builder.concentration == 1

    def test_med_builder_creates_medication_object(self):
        """Tests that the medication builder creates a medication object"""

        med_builder = medication_builder.MedicationBuilder()
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

        assert isinstance(aspirin, medication.Medication)
