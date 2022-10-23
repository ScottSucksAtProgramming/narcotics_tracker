"""Script which works with a personal database for testing."""

from typing import TYPE_CHECKING

from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.commands import SaveItem
from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.scripts.setup import (
    create_tables,
    populate_database,
    return_tables_list,
)
from narcotics_tracker.setup.standard_items import StandardItemCreator
from narcotics_tracker.utils.date_and_time import DateTimeManager

if TYPE_CHECKING:
    from narcotics_tracker.items.medications import Medication

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
        .build()
    )
    wlvac_medications.append(fentanyl)
    wlvac_medications.append(morphine)
    wlvac_medications.append(versed)

    return wlvac_medications


def add_standard_items():
    items = item_creator.create()
    populate_database(db, items, dt)


def main():
    create_tables(db, return_tables_list())
    add_standard_items()

    meds = build_wlvac_meds()

    for medication in meds:
        print(repr(medication))
        SaveItem(db, medication, dt).execute()


if __name__ == "__main__":
    main()
