"""Contains the unit tests for the builders module."""

from narcotics_tracker import medication
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import builder
from narcotics_tracker.utils import utilities


class Test_Builder:
    """Unit tests for the Builder class."""

    def test_set_medication_id(self):
        """Tests that the medication builder sets the medication id"""
        medication_builder = builder.ObjectBuilder()

        medication_builder.set_medication_id(1)

        assert medication_builder.medication_id == 1

    def test_set_name(self):
        """Tests that the medication builder sets the name"""
        medication_builder = builder.ObjectBuilder()

        medication_builder.set_name("Aspirin")

        assert medication_builder.name == "Aspirin"

    def test_set_code(self):
        """Tests that the medication builder sets the code"""

        medication_builder = builder.ObjectBuilder()

        medication_builder.set_code("ASA")

        assert medication_builder.code == "ASA"

    def test_set_container(self):
        """Tests that the medication builder sets the container type"""
        medication_builder = builder.ObjectBuilder()

        medication_builder.set_container(containers.Container.AMPULE)
        assert medication_builder.container_type.value == "Ampule"

    def test_set_fill_amount(self):
        """Tests that the medication builder sets the fill amount"""

        medication_builder = builder.ObjectBuilder()

        medication_builder.set_fill_amount(10)

        assert medication_builder.fill_amount == 10

    def test_sets_dose_correctly(self):
        """Tests that the medication builder sets the dose and unit"""
        medication_builder = builder.ObjectBuilder()

        medication_builder.set_dose_and_unit(10, units.Unit.MG)

        assert medication_builder.dose == 10_000

    def test_sets_unit_correctly(self):
        """Tests that the medication builder sets the dose and unit"""

        medication_builder = builder.ObjectBuilder()

        medication_builder.set_dose_and_unit(10, units.Unit.MG)

        assert medication_builder.unit.value == "mg"

    def test_set_concentration(self):
        """Tests that the medication builder sets the concentration"""

        medication_builder = builder.ObjectBuilder()
        medication_builder.set_concentration(10)

        assert medication_builder.concentration == 10

    def test_set_status(self):
        """Tests that the medication builder sets the status"""

        medication_builder = builder.ObjectBuilder()

        medication_builder.set_status(medication_statuses.MedicationStatus.ACTIVE)

        assert medication_builder.status.value == "Active"

    def test_set_created_date(self):
        """Tests that the medication builder sets the created date"""

        medication_builder = builder.ObjectBuilder()

        medication_builder.set_created_date("01/01/2019")

        assert medication_builder.created_date == "01/01/2019"

    def test_set_modified_date(self):
        """Tests that the medication builder sets the modified date"""

        medication_builder = builder.ObjectBuilder()

        medication_builder.set_modified_date("01/01/2019")

        assert medication_builder.modified_date == "01/01/2019"

    def test_set_modified_by(self):
        """Tests that the medication builder sets the modified by"""

        medication_builder = builder.ObjectBuilder()

        medication_builder.set_modified_by("John Doe")

        assert medication_builder.modified_by == "John Doe"

    def test_medication_builder_calculates_concentration(self):
        """Tests that the medication builder sets the concentration"""

        medication_builder = builder.ObjectBuilder()
        medication_builder.set_dose_and_unit(10, units.Unit.MCG)
        medication_builder.set_fill_amount(10)

        medication_builder.calculate_concentration()

        assert medication_builder.concentration == 1

    def test_medication_builder_creates_medication_object(self):
        """Tests that the medication builder creates a medication object"""

        medication_builder = builder.ObjectBuilder()
        medication_builder.set_name("Aspirin")
        medication_builder.set_code("ASA")
        medication_builder.set_fill_amount(10)
        medication_builder.set_container(containers.Container.AMPULE)
        medication_builder.set_dose_and_unit(10, units.Unit.MCG)
        medication_builder.set_status(medication_statuses.MedicationStatus.ACTIVE)

        aspirin = medication_builder.build()

        assert isinstance(aspirin, medication.Medication)
