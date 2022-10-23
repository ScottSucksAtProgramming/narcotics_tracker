"""Script which works with a personal database for testing."""

from typing import TYPE_CHECKING

from narcotics_tracker import commands
from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.builders.reporting_period_builder import ReportingPeriodBuilder
from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.scripts import setup
from narcotics_tracker.setup.standard_items import StandardItemCreator
from narcotics_tracker.utils.datetime_manager import DateTimeManager

if TYPE_CHECKING:
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.items.reporting_periods import ReportingPeriod


def main():
    """Sets up the narcotics database for WLVAC."""
    # * Initialize objects and Create Database File.
    sq_man = SQLiteManager("inventory_wlvac.db")
    dt_man = DateTimeManager()
    std_creator = StandardItemCreator()

    # * Add Tables.
    setup.create_tables(sq_man, setup.return_tables_list())

    # * Populate Database with Standard Items.
    items = std_creator.create()
    setup.populate_database(sq_man, items, dt_man)

    # * Populate Database with WLVAC Medications.
    meds = build_wlvac_meds()

    for medication in meds:
        commands.SaveItem(sq_man, medication, dt_man).execute()

    # * Populate Database with Reporting Periods for 2022.
    periods = build_2022_reporting_periods(dt_man)

    for period in periods:
        commands.SaveItem(sq_man, period, dt_man).execute()


def build_wlvac_meds() -> list["Medication"]:
    """Builds Medication Objects used at WLVAC and returns them as a list."""
    wlvac_medications = []
    med_builder = MedicationBuilder()

    fentanyl = (
        med_builder.set_medication_code("fentanyl")
        .set_medication_name("Fentanyl")
        .set_fill_amount(2)
        .set_medication_amount(100)
        .set_preferred_unit("mcg")
        .set_concentration()
        .set_status("ACTIVE")
        .set_modified_by("SRK")
        .build()
    )
    midazolam = (
        med_builder.set_medication_code("midazolam")
        .set_medication_name("Midazolam")
        .set_fill_amount(2)
        .set_medication_amount(1000)
        .set_preferred_unit("mg")
        .set_concentration(5)
        .set_status("ACTIVE")
        .set_modified_by("SRK")
        .build()
    )
    morphine = (
        med_builder.set_medication_code("morphine")
        .set_medication_name("Morphine")
        .set_fill_amount(1)
        .set_medication_amount(1000)
        .set_preferred_unit("mg")
        .set_concentration(10)
        .set_status("ACTIVE")
        .set_modified_by("SRK")
        .build()
    )

    wlvac_medications.append(fentanyl)
    wlvac_medications.append(morphine)
    wlvac_medications.append(midazolam)

    return wlvac_medications


def build_2022_reporting_periods(
    dt_manager: DateTimeManager,
) -> list["ReportingPeriod"]:
    """Builds Reporting Period Objects for 2022 and returns them as a list."""
    periods = []

    period_builder = ReportingPeriodBuilder()

    jan_to_june = (
        period_builder.set_start_date(
            dt_manager.convert_to_timestamp("01-20-2022 00:00:00")
        )
        .set_end_date(dt_manager.convert_to_timestamp("07-22-2022 23:59:59"))
        .set_status("CLOSED")
        .set_id(2200000)
        .set_modified_by("SRK")
        .build()
    )

    july_to_december = (
        period_builder.set_start_date(
            dt_manager.convert_to_timestamp("07-23-2022 00:00:00")
        )
        .set_status("OPEN")
        .set_id()
        .set_modified_by("SRK")
        .build()
    )

    periods.append(jan_to_june)
    periods.append(july_to_december)

    return periods


if __name__ == "__main__":
    main()
