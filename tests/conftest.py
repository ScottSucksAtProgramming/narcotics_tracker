"""Contains the fixtures and configuration used in the Testing Suite.

Testing for the Narcotics Tracker is done using pytest. This configuration 
file contains various fixtures and setting to help with testing.

Fixtures:
    reset_database: Resets test_database.db for testing functions.
"""

import os
from typing import TYPE_CHECKING

from pytest import fixture

from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.builders.event_builder import EventBuilder
from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.builders.reporting_period_builder import ReportingPeriodBuilder
from narcotics_tracker.builders.status_builder import StatusBuilder
from narcotics_tracker.builders.unit_builder import UnitBuilder

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment
    from narcotics_tracker.items.events import Event
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.items.reporting_periods import ReportingPeriod
    from narcotics_tracker.items.statuses import Status
    from narcotics_tracker.items.units import Unit


@fixture
def test_adjustment() -> "Adjustment":
    """Returns an Adjustment DataItem Object for testing."""
    test_adjustment = (
        AdjustmentBuilder()
        .set_table("inventory")
        .set_id(-77)
        .set_created_date(1666117887)
        .set_modified_date(1666117887)
        .set_modified_by("System")
        .set_adjustment_date(1666117887)
        .set_event_code("TEST")
        .set_medication_code("FakeMed")
        .set_adjustment_amount(10)
        .set_reference_id("TestReferenceID")
        .set_reporting_period_id(0)
        .build()
    )

    return test_adjustment


@fixture
def test_event() -> "Event":
    """Returns an Event DataItem Object for testing."""
    test_event = (
        EventBuilder()
        .set_table("events")
        .set_id(-77)
        .set_created_date(1666117887)
        .set_modified_date(1666117887)
        .set_modified_by("System")
        .set_event_code("TEST")
        .set_event_name("Test Event")
        .set_description("An event used for testing.")
        .set_modifier(999)
        .build()
    )

    return test_event


@fixture
def test_medication() -> "Medication":
    """Returns a Medication DataItem Object for testing."""
    test_medication = (
        MedicationBuilder()
        .set_table("medications")
        .set_id(-1)
        .set_created_date(1666061200)
        .set_modified_date(1666061200)
        .set_modified_by("SRK")
        .set_medication_code("apap")
        .set_medication_name("Acetaminophen")
        .set_fill_amount(10)
        .set_medication_amount(1)
        .set_preferred_unit("mcg")
        .set_concentration()
        .set_status("unknown")
        .build()
    )

    return test_medication


@fixture
def test_reporting_period() -> "ReportingPeriod":
    """Returns a ReportingPeriod DataItem Object for testing."""
    test_reporting_period = (
        ReportingPeriodBuilder()
        .set_table("reporting_periods")
        .set_id(-1)
        .set_created_date(1666061200)
        .set_modified_date(1666061200)
        .set_modified_by("SRK")
        .set_start_date(1666061200)
        .set_end_date(1666061200)
        .set_status("unfinished")
        .build()
    )

    return test_reporting_period


@fixture
def test_status() -> "Status":
    """Returns a Status DataItem Object for testing."""
    test_status = (
        StatusBuilder()
        .set_table("statuses")
        .set_id(-1)
        .set_created_date(1666061200)
        .set_modified_date(1666061200)
        .set_modified_by("Systems")
        .set_status_code("BROKEN")
        .set_status_name("Broken")
        .set_description("Used for testing purposes.")
        .build()
    )

    return test_status


@fixture
def test_unit() -> "Unit":
    """Returns a Unit DataItem Object for testing."""
    test_unit = (
        UnitBuilder()
        .set_table("units")
        .set_id(-1)
        .set_created_date(1666061200)
        .set_modified_date(1666061200)
        .set_modified_by("System")
        .set_unit_code("dg")
        .set_unit_name("Decagrams")
        .set_decimals(7)
        .build()
    )

    return test_unit


@fixture
def reset_database():
    """Resets test_database.db for testing methods."""
    if os.path.exists("data/test_database.db"):
        os.remove("data/test_database.db")

    if os.path.exists("data/table_creation_tests.db"):
        os.remove("data/table_creation_tests.db")

    if os.path.exists("data/data_item_storage_tests.db"):
        os.remove("data/data_item_storage_tests.db")
