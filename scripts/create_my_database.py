"""This script will creates the medications which I use at my agency and 
writes them to the table."""


from narcotics_tracker import database, medication, periods
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import medication_builder

FENTANYL_PROPERTIES = [
    "fentanyl",
    "Fentanyl",
    containers.Container.VIAL,
    100,
    units.Unit.MCG,
    2,
    medication_statuses.MedicationStatus.ACTIVE,
]

MIDAZOLAM_PROPERTIES = [
    "midazolam",
    "Midazolam",
    containers.Container.VIAL,
    10,
    units.Unit.MG,
    2,
    medication_statuses.MedicationStatus.ACTIVE,
]

MORPHINE_PROPERTIES = [
    "morphine",
    "Morphine",
    containers.Container.VIAL,
    10,
    units.Unit.MG,
    1,
    medication_statuses.MedicationStatus.ACTIVE,
]

REPORTING_PERIOD_1_PROPERTIES = ["01-01-2022", "06-30-2022"]

REPORTING_PERIOD_2_PROPERTIES = ["07-01-2022", "12-31-2022"]


def build_medication(medication_properties: list):
    """Uses the MedicationBuilder to create medication objects."""
    med_builder = medication_builder.MedicationBuilder()

    med_builder.set_code(medication_properties[0])
    med_builder.set_name(medication_properties[1])
    med_builder.set_container(medication_properties[2])
    med_builder.set_dose_and_unit(medication_properties[3], medication_properties[4])
    med_builder.set_fill_amount(medication_properties[5])
    med_builder.set_status(medication_properties[6])

    return med_builder.build()


def main():

    # Build Medication Objects
    fentanyl = build_medication(FENTANYL_PROPERTIES)
    fentanyl.created_date = "08-08-2022"
    fentanyl.modified_by = "SRK"

    morphine = build_medication(MORPHINE_PROPERTIES)
    morphine.created_date = "08-08-2022"
    morphine.modified_by = "SRK"

    midazolam = build_medication(MIDAZOLAM_PROPERTIES)
    midazolam.modified_by = "SRK"

    # Build Reporting Period Objects

    db = database.Database()
    db.connect("inventory.db")

    sql_query = medication.return_table_creation_query()
    db.create_table(sql_query)

    sql_query = periods.return_table_creation_query()
    db.create_table(sql_query)

    fentanyl.save(db)
    morphine.save(db)
    midazolam.save(db)


if __name__ == "__main__":
    main()
