"""This script will creates the medications which I use at my agency and 
writes them to the table."""

import datetime
from subprocess import DEVNULL
from narcotics_tracker.enums import containers, medication_statuses

from narcotics_tracker.medication import (
    builder,
    medication,
)
from narcotics_tracker.enums import units
from narcotics_tracker.database import database
from narcotics_tracker.setup import setup

FENTANYL_PROPERTIES = [
    "Fent1",
    "Fentanyl",
    containers.Container.VIAL,
    100,
    units.Unit.MCG,
    2,
    medication_statuses.MedicationStatus.ACTIVE,
]

MIDAZOLAM_PROPERTIES = [
    "Midaz1",
    "Midazolam",
    containers.Container.VIAL,
    10,
    units.Unit.MG,
    2,
    medication_statuses.MedicationStatus.ACTIVE,
]

MORPHINE_PROPERTIES = [
    "Morph1",
    "Morphine",
    containers.Container.VIAL,
    10,
    units.Unit.MG,
    1,
    medication_statuses.MedicationStatus.ACTIVE,
]


def build_medication(medication_properties: list) -> medication.Medication:
    """Uses the MedicationBuilder to create medication objects."""
    medication_builder = builder.ObjectBuilder()

    medication_builder.set_name(medication_properties[0])
    medication_builder.set_code(medication_properties[1])
    medication_builder.set_container_type(medication_properties[2])
    medication_builder.set_dose_and_unit(
        medication_properties[3], medication_properties[4]
    )
    medication_builder.set_fill_amount(medication_properties[5])
    medication_builder.set_status(medication_properties[6])

    return medication_builder.build()


def main():

    fentanyl = build_medication(FENTANYL_PROPERTIES)
    fentanyl.created_date = "08-08-2022"
    fentanyl.modified_by = "SRK"

    morphine = build_medication(MORPHINE_PROPERTIES)
    morphine.created_date = "08-08-2022"
    morphine.modified_by = "SRK"

    midazolam = build_medication(MIDAZOLAM_PROPERTIES)
    midazolam.created_date = "08-08-2022"
    midazolam.modified_by = "SRK"

    db = database.Database()
    db.connect("inventory.db")

    setup.create_medication_table(db)

    fentanyl.save(db)
    morphine.save(db)
    midazolam.save(db)


if __name__ == "__main__":
    main()
