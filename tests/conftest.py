"""Contains the fixtures and configuration for the tests.

Fixtures:
    test_med: Return's a medication object for testing.
"""
from pytest import fixture
from typing import TYPE_CHECKING

from narcotics_tracker import database, event_types, inventory, periods
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import adjustment_builder, medication_builder

if TYPE_CHECKING:
    from narcotics_tracker import medication


@fixture
def test_med() -> "medication.Medication":
    """Return a Medication object for testing.

    The test_med fixture uses the builder to create a medication object for
    testing. All the medication attributes are set with values which would not
    be valid for a medication in a real system.

    Returns:
        test_med (medication.Medication): A medication object for testing.
    """
    med_builder = medication_builder.MedicationBuilder()
    med_builder.set_medication_id(1)
    med_builder.set_name("Unobtanium")
    med_builder.set_code("Un-69420-9001")
    med_builder.set_container(containers.Container.VIAL)
    med_builder.set_dose_and_unit(69.420, units.Unit.MG)
    med_builder.set_fill_amount(9_001)
    med_builder.set_status(medication_statuses.MedicationStatus.DISCONTINUED)
    med_builder.set_created_date("01-02-1986")
    med_builder.set_modified_date("08-09-2022")
    med_builder.set_modified_by("Kvothe")

    test_med = med_builder.build()

    return test_med


@fixture
def test_db() -> str:
    """Return the name of the testing database file.

    The test_db fixture returns the name of the testing database file.
    This is used in the tests to connect to the database.

    Returns:
        test_db (str): The path to the database file.
    """
    return "test_database.db"


@fixture
def test_period() -> periods.ReportingPeriod:
    """Creates a test object from the Period Class.

    Returns:
        test_period (period.Period): A period object for testing.
    """
    test_period = periods.ReportingPeriod("02-29-0001", "01-35-0000")

    test_period.period_id = 9001
    test_period.created_date = "08-26-2022"
    test_period.modified_date = "08-01-2022"
    test_period.modified_by = "Cinder"

    return test_period


@fixture
def test_event_type() -> event_types.EventType:
    """Creates a test object from the EventType Class.

    Returns:
        test_event_type (event_type.EventType): An EventType object for
            testing.
    """
    test_event_type = event_types.EventType(
        "TEST", "Test Event", "Used for testing the EventType Class.", -1
    )

    test_event_type.event_id = 2001
    test_event_type.created_date = "08-26-2022"
    test_event_type.modified_date = "08-01-2022"
    test_event_type.modified_by = "Bast"

    return test_event_type


@fixture
def test_adjustment() -> "inventory.Adjustment":
    """Return a Medication object for testing.

    The test_adjustment fixture uses the builder to create a medication object for
    testing. All the medication attributes are set with values which would not
    be valid for a medication in a real system.

    Returns:
        test_adjustment (medication.Medication): A medication object for testing.
    """

    adj_builder = adjustment_builder.AdjustmentBuilder()
    adj_builder.set_database_connection("test_database_2.db")
    adj_builder.set_adjustment_id(-300)
    adj_builder.set_adjustment_date("06-06-1989")
    adj_builder.set_event_code("DONATE")
    adj_builder.set_medication_code("Un-69420-9001")
    adj_builder.set_adjustment_amount(1)
    adj_builder.set_reference_id("TEST ID")
    adj_builder.set_created_date("Yesterday")
    adj_builder.set_modified_date("Tomorrow")
    adj_builder.set_modified_by("Ambrose")

    test_adjustment = adj_builder.build()

    return test_adjustment


@fixture
def reset_database():
    """Resets test_database.db"""
    db = database.Database()
    db.connect("test_database.db")
    db.delete_database("test_database.db")
