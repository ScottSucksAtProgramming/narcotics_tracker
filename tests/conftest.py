"""Contains the fixtures and configuration for the tests.

Fixtures:
    test_med: Return's a medication object for testing.
"""
from pytest import fixture
from typing import TYPE_CHECKING

from narcotics_tracker import database, event_types, inventory, reporting_periods
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import (
    adjustment_builder,
    event_type_builder,
    medication_builder,
    reporting_period_builder,
)

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
def test_period() -> reporting_periods.ReportingPeriod:
    """Creates a test object from the Period Class.

    Returns:
        test_period (period.Period): A period object for testing.
    """

    period_builder = reporting_period_builder.ReportingPeriodBuilder()

    period_builder.set_period_id(9001)
    period_builder.set_starting_date("2001-01-01 00:00:00")
    period_builder.set_ending_date("2100-06-30 00:00:00")
    period_builder.set_created_date("2022-08-01 00:00:00")
    period_builder.set_modified_date("2022-08-01 00:00:00")
    period_builder.set_modified_by("Cinder")

    test_period = period_builder.build()

    return test_period


@fixture
def test_event_type() -> event_types.EventType:
    """Creates a test object from the EventType Class.

    Returns:
        test_event_type (event_type.EventType): An EventType object for
            testing.
    """
    event_builder = event_type_builder.EventTypeBuilder()
    event_builder.set_event_id(2001)
    event_builder.set_event_code("TEST")
    event_builder.set_event_name("Test Event")
    event_builder.set_description("Used for testing the EventType Class.")
    event_builder.set_operator(-1)
    event_builder.set_created_date("2022-08-26 00:00:00")
    event_builder.set_modified_date("2022-08-01 00:00:00")
    event_builder.set_modified_by("Bast")

    test_event_type = event_builder.build()
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
    adj_builder.set_adjustment_date("2022-08-01 10:00:00")
    adj_builder.set_event_code("WASTE")
    adj_builder.set_medication_code("morphine")
    adj_builder.set_adjustment_amount(1)
    adj_builder.calculate_amount_in_mcg()
    adj_builder.set_reference_id("TEST ID")
    adj_builder.set_created_date("2022-08-01 10:00:00")
    adj_builder.set_modified_date("2022-08-01 10:00:00")
    adj_builder.set_modified_by("Ambrose")

    test_adjustment = adj_builder.build()

    return test_adjustment


@fixture
def reset_database():
    """Resets test_database.db"""
    db = database.Database()
    db.connect("test_database.db")
    db.delete_database("test_database.db")
