"""Script which works with a personal database for testing."""

from typing import TYPE_CHECKING

from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.builders.reporting_period_builder import ReportingPeriodBuilder
from narcotics_tracker.commands import SaveItem
from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.scripts.setup import (
    create_tables,
    populate_database,
    return_tables_list,
)
from narcotics_tracker.setup.standard_items import StandardItemCreator
from narcotics_tracker.utils.datetime_manager import DateTimeManager

if TYPE_CHECKING:
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.items.reporting_periods import ReportingPeriod

db = SQLiteManager("wlvac_inventory.db")
dt = DateTimeManager()

item_creator = StandardItemCreator()


def build_wlvac_meds() -> list["Medication"]:
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
    morphine = (
        med_builder.set_medication_code("morphine")
        .set_medication_name("Morphine")
        .set_fill_amount(1)
        .set_medication_amount(1000)
        .set_preferred_unit("mg")
        .set_concentration()
        .set_status("ACTIVE")
        .set_modified_by("SRK")
        .build()
    )
    versed = (
        med_builder.set_medication_code("versed")
        .set_medication_name("Versed")
        .set_fill_amount(2)
        .set_medication_amount(1000)
        .set_preferred_unit("mg")
        .set_concentration()
        .set_status("ACTIVE")
        .set_modified_by("SRK")
        .build()
    )
    wlvac_medications.append(fentanyl)
    wlvac_medications.append(morphine)
    wlvac_medications.append(versed)

    return wlvac_medications


def add_standard_items():
    items = item_creator.create()
    populate_database(db, items, dt)


def build_2022_reporting_periods() -> list["ReportingPeriod"]:
    periods = []

    period_builder = ReportingPeriodBuilder()

    jan_to_june = (
        period_builder.set_start_date(dt.convert_to_timestamp("01-20-2022 00:00:00"))
        .set_end_date(dt.convert_to_timestamp("07-22-2022 23:59:59"))
        .set_status("CLOSED")
        .set_id(2200000)
        .set_modified_by("SRK")
        .build()
    )

    july_to_december = (
        period_builder.set_start_date(dt.convert_to_timestamp("07-23-2022 00:00:00"))
        .set_status("OPEN")
        .set_id(2200000)
        .set_modified_by("SRK")
        .build()
    )

    periods.append(jan_to_june)
    periods.append(july_to_december)

    return periods


def main():
    """Main"""
    # create_tables(db, return_tables_list())
    # add_standard_items()

    # meds = build_wlvac_meds()

    # for medication in meds:
    #     SaveItem(db, medication, dt).execute()

    periods = build_2022_reporting_periods()

    for period in periods:
        SaveItem(db, period, dt).execute()


if __name__ == "__main__":
    main()
