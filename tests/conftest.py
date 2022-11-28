"""Contains the fixtures and configuration used in the Testing Suite.

Testing for the Narcotics Tracker is done using pytest. This configuration 
file contains various fixtures and setting to help with testing.

Fixtures:
    reset_database: Resets test_database.db for testing functions.
"""

import os
import sqlite3
from typing import TYPE_CHECKING

from pytest import fixture

from narcotics_tracker import commands
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.builders.reporting_period_builder import ReportingPeriodBuilder
from narcotics_tracker.configuration.standard_items import StandardItemCreator
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.items.events import Event
from narcotics_tracker.items.medications import Medication
from narcotics_tracker.items.reporting_periods import ReportingPeriod
from narcotics_tracker.items.statuses import Status
from narcotics_tracker.items.units import Unit
from narcotics_tracker.scripts import create_my_database, setup, wlvac_adjustment
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.services.sqlite_manager import SQLiteManager

if TYPE_CHECKING:
    from narcotics_tracker.items.interfaces.dataitem_interface import DataItem


@fixture
def all_test_dataItems(
    test_adjustment,
    test_event,
    test_medication,
    test_reporting_period,
    test_status,
    test_unit,
) -> dict[str, "DataItem"]:
    """Return all Tests DataItems in a dict mapped by DataItem type."""
    return {
        "adjustment": test_adjustment,
        "event": test_event,
        "medication": test_medication,
        "reporting_period": test_reporting_period,
        "status": test_status,
        "unit": test_unit,
    }


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
        reporting_period_id=-1,
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


def delete_database(filename: str) -> None:
    if os.path.exists(f"data/{filename}"):
        os.remove(f"data/{filename}")


@fixture
def setup_integration_db():
    """Creates a new integration database and populates it with data."""
    meds = []
    periods = []
    adjustment_list = []
    delete_database("integration_test.db")

    receiver = SQLiteManager("integration_test.db")
    dt_man = ServiceManager().datetime
    create_tables(receiver)
    populate_standard_items(receiver)

    meds = build_test_meds()
    for medication in meds:
        commands.AddMedication(receiver).execute(medication)

    periods = build_reporting_periods(dt_man)
    for period in periods:
        commands.AddReportingPeriod(receiver).execute(period)

    adjustment_data = return_adjustments_data()
    adjustment_list = construct_adjustments(adjustment_data)
    for adjustment in adjustment_list:
        commands.AddAdjustment(receiver).execute(adjustment)


def create_tables(receiver):
    commands_list = [
        commands.CreateEventsTable,
        commands.CreateInventoryTable,
        commands.CreateMedicationsTable,
        commands.CreateReportingPeriodsTable,
        commands.CreateStatusesTable,
        commands.CreateUnitsTable,
    ]
    for command in commands_list:
        command(receiver).execute()


def populate_standard_items(receiver):
    try:
        events = None
        events = StandardItemCreator().create_events()
        for event in events:
            event.table = "events"
            commands.AddEvent(receiver).execute(event)

        statuses = StandardItemCreator().create_statuses()
        for status in statuses:
            commands.AddStatus(receiver).execute(status)

        units = StandardItemCreator().create_units()
        for unit in units:
            commands.AddUnit(receiver).set_unit(unit).execute()
    except sqlite3.IntegrityError as e:
        pass


def build_test_meds() -> list["Medication"]:
    """Builds Medication Objects used at WLVAC and returns them as a list."""
    test_medications = []
    med_builder = MedicationBuilder()
    dt_man = ServiceManager().datetime

    fentanyl = (
        med_builder.set_medication_code("fentanyl")
        .set_medication_name("Fentanyl")
        .set_fill_amount(2)
        .set_medication_amount(100)
        .set_preferred_unit("mcg")
        .set_concentration()
        .set_status("ACTIVE")
        .set_created_date(dt_man.return_current())
        .set_modified_date(dt_man.return_current())
        .set_modified_by("SRK")
        .build()
    )
    midazolam = (
        med_builder.set_medication_code("midazolam")
        .set_medication_name("Midazolam")
        .set_fill_amount(2)
        .set_medication_amount(10)
        .set_preferred_unit("mg")
        .set_concentration(5)
        .set_status("ACTIVE")
        .set_created_date(dt_man.return_current())
        .set_modified_date(dt_man.return_current())
        .set_modified_by("SRK")
        .build()
    )
    morphine = (
        med_builder.set_medication_code("morphine")
        .set_medication_name("Morphine")
        .set_fill_amount(1)
        .set_medication_amount(10)
        .set_preferred_unit("mg")
        .set_concentration(10)
        .set_status("ACTIVE")
        .set_created_date(dt_man.return_current())
        .set_modified_date(dt_man.return_current())
        .set_modified_by("SRK")
        .build()
    )

    test_medications.append(fentanyl)
    test_medications.append(midazolam)
    test_medications.append(morphine)

    return test_medications


def build_reporting_periods(
    dt_manager: ServiceManager().datetime,
) -> list["ReportingPeriod"]:
    """Builds Reporting Period Objects for 2022 and returns them as a list."""
    periods = []

    period_builder = ReportingPeriodBuilder()

    jan_to_june_2021 = (
        period_builder.set_start_date("01-01-2021 00:00:00")
        .set_end_date("06-30-2021 23:59:59")
        .set_status("CLOSED")
        .set_id(2100000)
        .set_created_date("01-01-2022 00:00:00")
        .set_modified_date("01-01-2022 00:00:00")
        .set_modified_by("SRK")
        .build()
    )

    july_to_december_2021 = (
        period_builder.set_start_date("07-01-2021 00:00:00")
        .set_end_date("12-31-2021 23:59:59")
        .set_status("CLOSED")
        .set_id()
        .set_created_date("01-01-2022 00:00:00")
        .set_modified_date("01-01-2022 00:00:00")
        .set_modified_by("SRK")
        .build()
    )

    jan_to_june_2022 = (
        period_builder.set_start_date("01-20-2022 00:00:00")
        .set_end_date("07-22-2022 23:59:59")
        .set_status("CLOSED")
        .set_id(2200000)
        .set_created_date("01-01-2022 00:00:00")
        .set_modified_date("01-01-2022 00:00:00")
        .set_modified_by("SRK")
        .build()
    )

    july_to_december_2022 = (
        period_builder.set_start_date("07-23-2022 00:00:00")
        .set_end_date(None)
        .set_status("OPEN")
        .set_id()
        .set_created_date("01-01-2022 00:00:00")
        .set_modified_date("01-01-2022 00:00:00")
        .set_modified_by("SRK")
        .build()
    )

    periods.append(jan_to_june_2021)
    periods.append(july_to_december_2021)
    periods.append(jan_to_june_2022)
    periods.append(july_to_december_2022)

    return periods


def construct_adjustments(data: list[any]) -> list["Adjustment"]:
    adjustment_list = []
    for data_set in data:
        adjustment = (
            AdjustmentBuilder()
            .set_table("inventory")
            .set_id(data_set[0])
            .set_created_date()
            .set_modified_date()
            .set_modified_by("SRK")
            .set_adjustment_date(data_set[1])
            .set_event_code(data_set[2])
            .set_medication_code(data_set[3])
            .set_adjustment_amount(data_set[4])
            .set_reporting_period_id(data_set[5])
            .set_reference_id(data_set[5])
            .build()
        )
        adjustment_list.append(adjustment)

    return adjustment_list


def return_adjustments_data() -> list[list]:
    adjustment_data = []

    adjustment_data.append(
        [
            None,
            "07-22-2022 17:00:00",
            "IMPORT",
            "fentanyl",
            7450,
            2200001,
            "ref_id",
        ]
    )
    adjustment_data.append(
        [
            None,
            "07-22-2022 17:00:00",
            "IMPORT",
            "midazolam",
            663.4,
            2200001,
            "ref_id",
        ]
    )

    adjustment_data.append(
        [
            None,
            "07-22-2022 17:00:00",
            "IMPORT",
            "morphine",
            690,
            2200001,
            "ref_id",
        ]
    )
    adjustment_data.append([None, 1659212760, "USE", "fentanyl", 50, 2200001, "ref_id"])
    adjustment_data.append(
        [None, 1661027838, "DESTROY", "morphine", 440, 2200001, "ref_id"]
    )
    adjustment_data.append(
        [None, 1661027838, "DESTROY", "midazolam", 363.4, 2200001, "ref_id"]
    )
    adjustment_data.append(
        [None, 1661027838, "DESTROY", "fentanyl", 3450, 2200001, "ref_id"]
    )
    adjustment_data.append([None, 1661166388, "USE", "midazolam", 5, 2200001, "ref_id"])
    adjustment_data.append([None, 1661701387, "USE", "fentanyl", 60, 2200001, "ref_id"])
    adjustment_data.append(
        [None, 1662580020, "USE", "fentanyl", 100, 2200001, "ref_id"]
    )
    adjustment_data.append([None, 1665258240, "USE", "midazolam", 5, 2200001, "ref_id"])
    adjustment_data.append(
        [None, 1666487700, "USE", "midazolam", 1.6, 2200001, "ref_id"]
    )

    return adjustment_data
