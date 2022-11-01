"""Contains the fixtures and configuration used in the Testing Suite.

Testing for the Narcotics Tracker is done using pytest. This configuration 
file contains various fixtures and setting to help with testing.

Fixtures:
    reset_database: Resets test_database.db for testing functions.
"""

import os

from pytest import fixture

from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.items.events import Event
from narcotics_tracker.items.medications import Medication
from narcotics_tracker.items.reporting_periods import ReportingPeriod
from narcotics_tracker.items.statuses import Status
from narcotics_tracker.items.units import Unit


@fixture
def test_unit() -> "Unit":
    """Returns a Unit DataItem Object for testing."""
    test_unit = Unit(
        table="units",
        id=-1,
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="System",
        unit_code="dg",
        unit_name="decagrams",
        decimals=7,
    )

    return test_unit


@fixture
def test_adjustment() -> "Adjustment":
    """Returns an Adjustment DataItem Object for testing."""
    test_adjustment = Adjustment(
        table="inventory",
        id=-77,
        created_date=1666117887,
        modified_date=1666117887,
        modified_by="System",
        adjustment_date=1666117887,
        event_code="TEST",
        medication_code="apap",
        amount=10,
        reference_id="TestReferenceID",
        reporting_period_id=0,
    )

    return test_adjustment


@fixture
def test_event() -> "Event":
    """Returns an Event DataItem Object for testing."""
    test_event = Event(
        table="events",
        id=-77,
        created_date=1666117887,
        modified_date=1666117887,
        modified_by="System",
        event_code="TEST",
        event_name="Test Event",
        description="An event used for testing.",
        modifier=999,
    )

    return test_event


@fixture
def test_medication() -> "Medication":
    """Returns a Medication DataItem Object for testing."""
    test_medication = Medication(
        table="medications",
        id=-1,
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="System",
        medication_code="apap",
        medication_name="Acetaminophen",
        fill_amount=10,
        medication_amount=1,
        preferred_unit="mcg",
        concentration=0.1,
        status="BROKEN",
    )
    return test_medication


@fixture
def test_reporting_period() -> "ReportingPeriod":
    """Returns a ReportingPeriod DataItem Object for testing."""
    test_reporting_period = ReportingPeriod(
        table="reporting_periods",
        id=-1,
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="System",
        start_date=1666061200,
        end_date=1666061200,
        status="BROKEN",
    )

    return test_reporting_period


@fixture
def test_status() -> "Status":
    """Returns a Status DataItem Object for testing."""
    test_status = Status(
        table="statuses",
        id=-1,
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="System",
        status_code="BROKEN",
        status_name="Broken",
        description="Used for testing purposes.",
    )

    return test_status


@fixture
def reset_database():
    """Resets test_database.db for testing methods."""
    if os.path.exists("data/test_database.db"):
        os.remove("data/test_database.db")

    if os.path.exists("data/table_creation_tests.db"):
        os.remove("data/table_creation_tests.db")

    if os.path.exists("data/data_item_storage_tests.db"):
        os.remove("data/data_item_storage_tests.db")
