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

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment


@fixture
def adjustment() -> "Adjustment":
    """returns an Adjustment DataItem for testing."""
    adj_builder = (
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
    )

    return adj_builder.build()


@fixture
def reset_database():
    """Resets test_database.db for testing methods."""
    if os.path.exists("data/test_database.db"):
        os.remove("data/test_database.db")

    if os.path.exists("data/table_creation_tests.db"):
        os.remove("data/table_creation_tests.db")

    if os.path.exists("data/data_item_storage_tests.db"):
        os.remove("data/data_item_storage_tests.db")
