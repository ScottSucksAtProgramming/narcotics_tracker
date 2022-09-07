"""Contains the Test_Builder class used to test the medication_builder module.

Classes: 

    Test_Builder: Contains all unit tests for the medication_builder module.
"""
import pytest

from narcotics_tracker import database, inventory, medications, units
from narcotics_tracker.builders import (
    adjustment_builder_template,
    adjustment_builder,
    container_builder,
    container_builder_template,
    event_builder,
    event_builder_template,
    medication_builder,
    reporting_period_builder,
    reporting_period_builder_template,
    status_builder_template,
    unit_builder,
    unit_builder_template,
)


class Test_MedicationBuilder:
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

        med_builder.set_container("Ampule")
        assert med_builder.container_type == expected

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

        med_builder.set_dose_and_unit(10, "mg")

        assert med_builder.dose == expected

    def test_set_unit(self):
        """Tests that the medication builder sets the dose and unit.

        Asserts that the medication dose returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "mg"

        med_builder.set_dose_and_unit(10, "mg")

        assert med_builder.unit == expected

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

        med_builder.set_status("Active")
        expected = "Active"

        assert med_builder.status == expected

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

        med_builder.set_dose_and_unit(10, "mcg")
        med_builder.set_fill_amount(10)

        med_builder.calculate_concentration()

        assert med_builder.concentration == expected

    def test_med_builder_creates_medication_object(self):
        """Tests that the medication builder creates a medication object.

        Asserts that the medication object returns a Medication object.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = medications.Medication

        med_builder.set_medication_id(None)
        med_builder.set_name("Aspirin")
        med_builder.set_code("ASA")
        med_builder.set_fill_amount(10)
        med_builder.set_container("Ampule")
        med_builder.set_dose_and_unit(10, "mcg")
        med_builder.set_status("Active")
        med_builder.set_created_date(None)
        med_builder.set_modified_date(None)
        med_builder.set_modified_by("SRK")

        aspirin = med_builder.build()

        assert isinstance(aspirin, expected)


class Test_AdjustmentAbstractBuilder:
    """Contains the unit tests for the adjustment_builder_template module.

    Behaviors Tested:
        - Module adjustment_builder_template can be accessed.
        - Class Adjustment can be accessed.
    """

    def test_adjustment_builder_template_module_can_be_accessed(self) -> None:
        """Tests if the adjustment_builder_template exists and is accessible.

        Asserts that adjustment_builder_template.__doc__ does not return
        'None'.
        """

    assert adjustment_builder_template.__doc__ != None

    def test_adjustment_class_can_be_accessed(self) -> None:
        """Tests that Adjustment class exists and is accessible.

        Asserts that adjustment_builder_template.Adjustment.__doc__ does not
        return 'None'.
        """
        assert adjustment_builder_template.Adjustment.__doc__ != None


class Test_AdjustmentBuilderModule:
    """Contains the unit tests for the adjustment_builder module.

    Behaviors Tested:

        - Module adjustment_builders can be accessed.
    """

    def test_adjustment_builder_module_can_be_accessed(self) -> None:
        """Tests that adjustment_builder.py module exists and is accessible.

        Asserts that adjustment_builder.__doc__ does not return 'None'.
        """
        assert adjustment_builder.__doc__ != None


class Test_AdjustmentBuilder:
    """Contains the unit tests for the AdjustmentBuilder class.

    Behaviors Tested:

        - Class AdjustmentBuilder can be accessed.
        - AdjustmentBuilder sets the database connection correctly.
        - AdjustmentBuilder sets the adjustment id correctly.
        - AdjustmentBuilder sets the adjustment date correctly.
        - AdjustmentBuilder sets the event code correctly.
        - AdjustmentBuilder sets the medication code correctly.
        - AdjustmentBuilder sets amount in preferred unit correctly.
        - AdjustmentBuilder sets the reference ID correctly.
        - AdjustmentBuilder sets the created date correctly.
        - AdjustmentBuilder sets the modified date correctly.
        - AdjustmentBuilder sets the modified by attribute correctly.
        - Created adjustment object has type inventory.Adjustment.
    """

    def test_adjustment_builder_class_can_be_accessed(self) -> None:
        """Tests that the AdjustmentBuilder class exists and is accessible.

        Asserts that adjustment_builder.AdjustmentBuilder.__doc__ does not
        return 'None'.
        """
        assert adjustment_builder.AdjustmentBuilder.__doc__ != None

    def test_database_connection_is_set_correctly(self, test_adjustment) -> None:
        """Tests that the database connection is correct.

        Asserts that self.database_connection is not 'None' and all tables
        required exist.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.database_connection is not None

    def test_adjustment_id_is_set_correctly(self, test_adjustment) -> None:
        """Tests that AdjustmentBuilder sets the adjustment's id correctly.

        Loads test_adjustment.

        Asserts that test_adjustment.adjustment_id is set to '-300'.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.adjustment_id == -300

    def test_adjustment_date_is_set_correctly(self, test_adjustment) -> None:
        """Tests that AdjustmentBuilder sets the adjustment's date correctly.

        Loads test_adjustment.

        Asserts that test_adjustment.adjustment_date is set to '2022-08-01 06:00:00'.
        """
        test_adjustment = test_adjustment
        formatted_date = database.format_datetime_from_unixepoch(
            test_adjustment.adjustment_date
        )

        assert formatted_date == "2022-08-01 06:00:00"

    def test_event_code_is_set_correctly(self, test_adjustment) -> None:
        """Tests that AdjustmentBuilder sets the event_code correctly.

        Loads test_adjustment.

        Asserts that test_adjustment.event_code is set to 'WASTE'.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.event_code == "WASTE"

    def test_medication_code_is_set_correctly(self, test_adjustment) -> None:
        """Tests that AdjustmentBuilder sets the medication_code correctly.

        Loads test_adjustment.

        Asserts that test_adjustment.medication_code is set to 'morphine'.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.medication_code == "morphine"

    def test_amount_in_preferred_unit_is_set_correctly(self, test_adjustment) -> None:
        """Tests that amount of medication changed is set correctly.

        Loads test_med. Builds medications table and saves test_med.

        Asserts that test_adjustment.quantity_amount is '1'.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.amount_in_preferred_unit == 1

    def test_reference_id_is_set_correctly(self, test_adjustment) -> None:
        """Tests that the Adjustment's reference ID is set correctly.

        Loads test_adjustment

        Asserts that test_adjustment.reference_id is 'TEST ID'.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.reference_id == "TEST ID"

    def test_created_date_is_set_correctly(self, test_adjustment) -> None:
        """Tests that the adjustments created date is set correctly.

        Loads test_adjustment.

        Asserts test_adjustment.created_date is '2022-08-01 10:00:00'.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.created_date == database.return_datetime(
            "2022-08-01 10:00:00"
        )

    def test_modified_date_is_set_correctly(self, test_adjustment) -> None:
        """Tests that the adjustments created date is set correctly.

        Loads test_adjustment.

        Asserts test_adjustment.modified_date is '2022-08-01 10:00:00'.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.modified_date == database.return_datetime(
            "2022-08-01 10:00:00"
        )

    def test_modified_by_is_set_correctly(self, test_adjustment) -> None:
        """Tests that the adjustments created date is set correctly.

        Loads test_adjustment.

        Asserts test_adjustment.modified_by is 'Ambrose'.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.modified_by == "Ambrose"

    def test_amount_in_mcg_is_calculated_correctly(self, test_adjustment) -> None:
        """Tests that the amount in mcg is calculated correctly.

        Connects to test database. Loads test_adjustment.

        Asserts test_adjustment.amount_in_mcg is 1000.
        """

        test_adjustment = test_adjustment

        assert test_adjustment.amount_in_mcg == 1000

    def test_reporting_period_is_assigned_correctly(self, test_adjustment) -> None:
        """Tests that the correcting period is assigned to the adjustment.

        Loads test_adjustment.

        Asserts test_adjustment.reporting_period_id returns '2'.
        """
        test_adjustment = test_adjustment

        assert test_adjustment.reporting_period_id == 2

    def test_adjustment_objects_is_instance_of_adjustment_class(
        self, test_adjustment
    ) -> None:
        """Tests that the objects are instances of the Adjustment class.

        Loads test_adjustment.

        Asserts that test_adjustment is an instance of inventory.Adjustment
        """
        assert isinstance(test_adjustment, inventory.Adjustment)


class Test_EventTypeAbstractBuilder:
    """Contains the unit tests for the event_type_builder_template module.

    Behaviors Tested:
        - Module event_type_builder_template can be accessed.
        - Class event_type can be accessed.
    """

    def test_event_builder_template_module_can_be_accessed(self) -> None:
        """Tests if the event_type_builder_template exists and is accessible.

        Asserts that event_type_builder_template.__doc__ does not return
        'None'.
        """

    assert event_builder_template.__doc__ != None

    def test_event_class_can_be_accessed(self) -> None:
        """Tests that EventType class exists and is accessible.

        Asserts that event_type_builder_template.EventType.__doc__ does not
        return 'None'.
        """
        assert event_builder_template.Event.__doc__ != None


class Test_EventBuilderModule:
    """Contains the unit tests for the event_type_builder module.

    Behaviors Tested:

        - Module event_type_builder can be accessed.
    """

    def test_event_builder_can_be_accessed(self) -> None:
        """Tests that the module exists and can be accessed.

        Asserts that event_type_builder.__doc__ does not return 'None'.
        """
        assert event_builder.__doc__ != None


class Test_EventBuilder:
    """Contains the unit tests for the EventBuilder class.

    Behaviors Tested:

        - Class EventBuilder can be accessed.
        - EventBuilder sets the event id correctly.
        - EventBuilder sets the event code correctly.
        - EventBuilder sets the event_name correctly.
        - EventBuilder sets the description correctly.
        - EventBuilder sets the modifier correctly.
        - EventBuilder sets the created date correctly.
        - EventBuilder sets the modified date correctly.
        - EventBuilder sets the modified by attribute correctly.
        #! - Created EventType object has type event_type.EventType.
    """

    def test_event_class_can_be_accessed(self) -> None:
        """Tests that the EventBuilder class exists and is accessible.

        Asserts that event_type_builder.EventBuilder.__doc__ does not
        return 'None'.
        """
        assert event_builder.EventBuilder.__doc__ != None

    def test_event_id_is_set_correctly(self, test_event) -> None:
        """Tests that the event_id is set correctly.

        Asserts that test_event.event_id is 2001.
        """
        test_event = test_event

        assert test_event.event_id == 2001

    def test_event_code_is_set_correctly(self, test_event) -> None:
        """Tests that the event_code is set correctly.

        Asserts that test_event.event_code is TEST.
        """
        test_event = test_event

        assert test_event.event_code == "TEST"

    def test_event_name_is_set_correctly(self, test_event) -> None:
        """Tests that the event_name is set correctly.

        Asserts that test_event.event_name is Test Event.
        """
        test_event = test_event

        assert test_event.event_name == "Test Event"

    def test_description_is_set_correctly(self, test_event) -> None:
        """Tests that the description is set correctly.

        Asserts that test_event.description is ;Used for testing the EventType Class.'
        """
        test_event = test_event

        assert test_event.description == "Used for testing the Event Class."

    def test_operator_is_set_correctly(self, test_event) -> None:
        """Tests that the operator is set correctly.

        Asserts that test_event.operator is -1.
        """
        test_event = test_event

        assert test_event.operator == -1

    def test_created_date_is_set_correctly(self, test_event) -> None:
        """Tests that the created_date is set correctly.

        Asserts that test_event.created_date is "2022-08-26 00:00:00".
        """
        test_event = test_event

        assert test_event.created_date == database.return_datetime(
            "2022-08-26 00:00:00"
        )

    def test_modified_date_is_set_correctly(self, test_event) -> None:
        """Tests that the modified_date is set correctly.

        Asserts that test_event.modified_date is "2022-08-01 00:00:00".
        """
        test_event = test_event

        assert test_event.modified_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_date_is_set_correctly(self, test_event) -> None:
        """Tests that the modified_by is set correctly.

        Asserts that test_event.modified_by is "Bast".
        """
        test_event = test_event

        assert test_event.modified_by == "Bast"


class Test_ReportingPeriodAbstractBuilder:
    """Contains unit tests for the Reporting Period Builder Template module.

    Behaviors Tested:
        - Module reporting_period_builder_template can be accessed.
        - Class ReportingPeriod can be accessed.
    """

    def test_reporting_period_builder_template_module_can_be_accessed(self) -> None:
        """Tests if reporting_period_builder_template exists and is accessible.

        Asserts that reporting_period_builder_template.__doc__ does not return
        'None'.
        """

    assert reporting_period_builder_template.__doc__ != None

    def test_reporting_period_class_can_be_accessed(self) -> None:
        """Tests that ReportingPeriod class exists and is accessible.

        Asserts that reporting_period_builder_template.ReportingPeriod.__doc__ does not
        return 'None'.
        """
        assert reporting_period_builder_template.ReportingPeriod.__doc__ != None


class Test_ReportingPeriodBuilderModule:
    """Contains the unit tests for the reporting period builder module.

    Behaviors Tested:

        - Module reporting period builder can be accessed.
    """

    def test_reporting_period_builder_can_be_accessed(self) -> None:
        """Tests that the module exists and can be accessed.

        Asserts that reporting_period_builder.__doc__ does not return 'None'.
        """
        assert reporting_period_builder.__doc__ != None


class Test_ReportingPeriodBuilder:
    """Contains the unit tests for the ReportingPeriodBuilder class.

    Behaviors Tested:

        - Class ReportingPeriodBuilder can be accessed.
        - ReportingPeriodBuilder sets the event id correctly.
        - ReportingPeriodBuilder sets the event code correctly.
        - ReportingPeriodBuilder sets the event_name correctly.
        - ReportingPeriodBuilder sets the description correctly.
        - ReportingPeriodBuilder sets the modifier correctly.
        - ReportingPeriodBuilder sets the created date correctly.
        - ReportingPeriodBuilder sets the modified date correctly.
        - ReportingPeriodBuilder sets the modified by attribute correctly.
        #! - Created ReportingPeriod object has type event_type.ReportingPeriod.
    """

    def test_reporting_period_class_can_be_accessed(self) -> None:
        """Tests that the ReportingPeriodBuilder class exists and is accessible.

        Asserts that reporting_period_builder.ReportingPeriodBuilder.__doc__ does not
        return 'None'.
        """
        assert reporting_period_builder.ReportingPeriodBuilder.__doc__ != None

    def test_period_id_is_set_correctly(self, test_period) -> None:
        """Tests that the period_id is set correctly.

        Asserts that test_period.period_id is 2001.
        """
        test_period = test_period

        assert test_period.period_id == 9001

    def test_starting_date_is_set_correctly(self, test_period) -> None:
        """Tests that the starting_date is set correctly.

        Asserts that test_period.starting_date is expected.
        """
        test_period = test_period

        assert test_period.starting_date == database.return_datetime(
            "2001-01-01 00:00:00"
        )

    def test_ending_date_is_set_correctly(self, test_period) -> None:
        """Tests that the ending_date is set correctly.

        Asserts that test_period.ending_date is expected.
        """
        test_period = test_period

        assert test_period.ending_date == database.return_datetime(
            "2100-06-30 00:00:00"
        )

    def test_created_date_is_set_correctly(self, test_period) -> None:
        """Tests that the created_date is set correctly.

        Asserts that test_period.created_date is "2022-08-26 00:00:00".
        """
        test_period = test_period

        assert test_period.created_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_date_is_set_correctly(self, test_period) -> None:
        """Tests that the modified_date is set correctly.

        Asserts that test_period.modified_date is "2022-08-01 00:00:00".
        """
        test_period = test_period

        assert test_period.modified_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_by_is_set_correctly(self, test_period) -> None:
        """Tests that the modified_by is set correctly.

        Asserts that test_period.modified_by is "Cinder".
        """
        test_period = test_period

        assert test_period.modified_by == "Cinder"


class Test_UnitAbstractBuilder:
    """Contains unit tests for the Unit Builder Template module.

    Behaviors Tested:
        - Module unit_builder_template can be accessed.
        - Class Unit can be accessed.
    """

    def test_unit_builder_template_module_can_be_accessed(self) -> None:
        """Tests if unit_builder_template exists and is accessible.

        Asserts that unit_builder_template.__doc__ does not return
        'None'.
        """

    assert unit_builder_template.__doc__ != None

    def test_unit_class_can_be_accessed(self) -> None:
        """Tests that Unit class exists and is accessible.

        Asserts that unit_builder_template.Unit.__doc__ does not
        return 'None'.
        """
        assert unit_builder_template.Unit.__doc__ != None


class Test_UnitBuilderModule:
    """Contains the unit tests for the unit builder module.

    Behaviors Tested:

        - Module unit builder can be accessed.
    """

    def test_unit_builder_can_be_accessed(self) -> None:
        """Tests that the module exists and can be accessed.

        Asserts that unit_builder.__doc__ does not return 'None'.
        """
        assert unit_builder.__doc__ != None


class Test_UnitBuilder:
    """Contains the unit tests for the UnitBuilder class.

    Behaviors Tested:

        - Class UnitBuilder can be accessed.
        - UnitBuilder sets the unit_id correctly.
        - UnitBuilder sets the unit_code correctly.
        - UnitBuilder sets the unit_name correctly.
        - UnitBuilder sets the created date correctly.
        - UnitBuilder sets the modified date correctly.
        - UnitBuilder sets the modified by attribute correctly.
        - Created Unit object has type event_type.Unit.
    """

    def test_unit_class_can_be_accessed(self) -> None:
        """Tests that the UnitBuilder class exists and is accessible.

        Asserts that unit_builder.UnitBuilder.__doc__ does not
        return 'None'.
        """
        assert unit_builder.UnitBuilder.__doc__ != None

    def test_unit_id_is_set_correctly(self, test_unit) -> None:
        """Tests that the unit_id is set correctly.

        Asserts that test_unit.unit_id is 821.
        """
        test_unit = test_unit

        assert test_unit.unit_id == 821

    def test_unit_code_is_set_correctly(self, test_unit) -> None:
        """Tests that the unit_code is set correctly.

        Asserts that test_unit.unit_code is expected.
        """
        test_unit = test_unit

        assert test_unit.unit_code == "tn"

    def test_unit_name_is_set_correctly(self, test_unit) -> None:
        """Tests that the unit_name is set correctly.

        Asserts that test_unit.unit_name is expected.
        """
        test_unit = test_unit

        assert test_unit.unit_name == "Tina"

    def test_created_date_is_set_correctly(self, test_unit) -> None:
        """Tests that the created_date is set correctly.

        Asserts that test_unit.created_date is "2022-08-26 00:00:00".
        """
        test_unit = test_unit

        assert test_unit.created_date == database.return_datetime("2022-08-01 00:00:00")

    def test_modified_date_is_set_correctly(self, test_unit) -> None:
        """Tests that the modified_date is set correctly.

        Asserts that test_unit.modified_date is "2022-08-01 00:00:00".
        """
        test_unit = test_unit

        assert test_unit.modified_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_by_is_set_correctly(self, test_unit) -> None:
        """Tests that the modified_by is set correctly.

        Asserts that test_unit.modified_by is "Denna".
        """
        test_unit = test_unit

        assert test_unit.modified_by == "Denna"


class Test_ContainerAbstractBuilder:
    """Contains unit tests for the Container Builder Template module.

    Behaviors Tested:
        - Module container_builder_template can be accessed.
        - Class Container can be accessed.
    """

    def test_container_builder_template_module_can_be_accessed(self) -> None:
        """Tests if container_builder_template exists and is accessible.

        Asserts that container_builder_template.__doc__ does not return
        'None'.
        """

    assert container_builder_template.__doc__ != None

    def test_container_class_can_be_accessed(self) -> None:
        """Tests that container class exists and is accessible.

        Asserts that container_builder_template.Container.__doc__ does not
        return 'None'.
        """
        assert container_builder_template.Container.__doc__ != None


class Test_ContainerBuilderModule:
    """Contains the container tests for the container builder module.

    Behaviors Tested:

        - Module container builder can be accessed.
    """

    def test_container_builder_can_be_accessed(self) -> None:
        """Tests that the module exists and can be accessed.

        Asserts that container_builder.__doc__ does not return 'None'.
        """
        assert container_builder.__doc__ != None


class Test_ContainerBuilder:
    """Contains the unit tests for the ContainerBuilder class.

    Behaviors Tested:

        - Class ContainerBuilder can be accessed.
        - ContainerBuilder sets the container_id correctly.
        - ContainerBuilder sets the container_code correctly.
        - ContainerBuilder sets the container_name correctly.
        - ContainerBuilder sets the created date correctly.
        - ContainerBuilder sets the modified date correctly.
        - ContainerBuilder sets the modified by attribute correctly.
        - Created Container object has type containers.Container.
    """

    def test_container_class_can_be_accessed(self) -> None:
        """Tests that the ContainerBuilder class exists and is accessible.

        Asserts that container_builder.ContainerBuilder.__doc__ does not
        return 'None'.
        """
        assert container_builder.ContainerBuilder.__doc__ != None

    def test_container_id_is_set_correctly(self, test_container) -> None:
        """Tests that the container_id is set correctly.

        Asserts that test_container.container_id is -7.
        """
        test_container = test_container

        assert test_container.container_id == -7

    def test_container_code_is_set_correctly(self, test_container) -> None:
        """Tests that the container_code is set correctly.

        Asserts that test_container.container_code is expected.
        """
        test_container = test_container

        assert test_container.container_code == "supp"

    def test_container_name_is_set_correctly(self, test_container) -> None:
        """Tests that the container_name is set correctly.

        Asserts that test_container.container_name is expected.
        """
        test_container = test_container

        assert test_container.container_name == "Suppository"

    def test_created_date_is_set_correctly(self, test_container) -> None:
        """Tests that the created_date is set correctly.

        Asserts that test_container.created_date is "2022-08-26 00:00:00".
        """
        test_container = test_container

        assert test_container.created_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_date_is_set_correctly(self, test_container) -> None:
        """Tests that the modified_date is set correctly.

        Asserts that test_container.modified_date is "2022-08-01 00:00:00".
        """
        test_container = test_container

        assert test_container.modified_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_by_is_set_correctly(self, test_container) -> None:
        """Tests that the modified_by is set correctly.

        Asserts that test_container.modified_by is "Elodin".
        """
        test_container = test_container

        assert test_container.modified_by == "Elodin"


class Test_StatusAbstractBuilder:
    """Contains unit tests for the Status Builder Template module.

    Behaviors Tested:
        - Module status_builder_template can be accessed.
        - Class Status can be accessed.
    """

    def test_status_builder_template_module_can_be_accessed(self) -> None:
        """Tests if status_builder_template exists and is accessible.

        Asserts that status_builder_template.__doc__ does not return
        'None'.
        """

    assert status_builder_template.__doc__ != None

    def test_status_class_can_be_accessed(self) -> None:
        """Tests that Status class exists and is accessible.

        Asserts that status_builder_template.Status.__doc__ does not
        return 'None'.
        """
        assert status_builder_template.Status.__doc__ != None
