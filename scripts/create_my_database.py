"""Creates the medications which I use at my agency and writes them to the 
table."""


from narcotics_tracker.builders import medication_builder, reporting_period_builder
from persistence import database

FENTANYL_PROPERTIES = [
    "fentanyl",
    "Fentanyl",
    "VIAL",
    100,
    "mcg",
    2,
    "ACTIVE",
]

MIDAZOLAM_PROPERTIES = [
    "midazolam",
    "Midazolam",
    "VIAL",
    10,
    "mg",
    2,
    "ACTIVE",
]

MORPHINE_PROPERTIES = [
    "morphine",
    "Morphine",
    "VIAL",
    10,
    "mg",
    1,
    "ACTIVE",
]

DATABASE_FILES = ["inventory.db", "test_database_2.db"]


def build_medication(medication_properties: list):
    """Uses the MedicationBuilder to create medication objects."""
    med_builder = medication_builder.MedicationBuilder()

    med_builder.set_medication_code(medication_properties[0])
    med_builder.set_medication_name(medication_properties[1])
    med_builder.set_container(medication_properties[2])
    med_builder.set_dose_and_unit(medication_properties[3], medication_properties[4])
    med_builder.set_fill_amount(medication_properties[5])
    med_builder.set_medication_status(medication_properties[6])

    return med_builder.build()


def main():

    # Build Medication Objects
    fentanyl = build_medication(FENTANYL_PROPERTIES)
    fentanyl.created_date = database.return_datetime("2022-08-08")
    fentanyl.modified_by = "SRK"

    morphine = build_medication(MORPHINE_PROPERTIES)
    morphine.created_date = database.return_datetime("2022-08-08")
    morphine.modified_by = "SRK"

    midazolam = build_medication(MIDAZOLAM_PROPERTIES)
    midazolam.modified_by = "SRK"

    # Build Reporting Period Objects

    period_builder = reporting_period_builder.ReportingPeriodBuilder()

    period_builder.set_starting_date("2022-01-01 00:00:00")
    period_builder.set_ending_date("2022-06-30 23:59:59")
    period_builder.set_modified_by("SRK")
    period_1 = period_builder.build()

    period_builder = reporting_period_builder.ReportingPeriodBuilder()

    period_builder.set_starting_date("2022-07-01 00:00:00")
    period_builder.set_ending_date("2022-12-31 23:59:59")
    period_builder.set_modified_by("SRK")
    period_2 = period_builder.build()

    period_builder = reporting_period_builder.ReportingPeriodBuilder()

    period_builder.set_starting_date("2023-01-01 00:00:00")
    period_builder.set_ending_date("2023-06-30 23:59:59")
    period_builder.set_modified_by("SRK")
    period_3 = period_builder.build()

    period_builder.set_starting_date("2023-07-01 00:00:00")
    period_builder.set_ending_date("2023-12-31 23:59:59")
    period_builder.set_modified_by("SRK")
    period_4 = period_builder.build()

    for file_name in DATABASE_FILES:
        with database.Database(f"{file_name}") as db:

            fentanyl.save(db)
            morphine.save(db)
            midazolam.save(db)

            period_1.save(db)
            period_2.save(db)
            period_3.save(db)
            period_4.save(db)


if __name__ == "__main__":
    main()
