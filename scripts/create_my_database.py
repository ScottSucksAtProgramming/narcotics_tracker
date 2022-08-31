"""This script will creates the medications which I use at my agency and 
writes them to the table."""


from narcotics_tracker import database, event_types, inventory, medication, periods
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

DATABASE_FILES = ["inventory.db", "test_database_2.db"]


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
    fentanyl.created_date = database.return_datetime("2022-08-08")
    fentanyl.modified_by = "SRK"

    morphine = build_medication(MORPHINE_PROPERTIES)
    morphine.created_date = database.return_datetime("2022-08-08")
    morphine.modified_by = "SRK"

    midazolam = build_medication(MIDAZOLAM_PROPERTIES)
    midazolam.modified_by = "SRK"

    # Build Reporting Period Objects
    period_1 = periods.ReportingPeriod("2022-01-01 00:00:00", "2022-06-30 23:59:59")
    period_1.modified_by = "SRK"
    period_2 = periods.ReportingPeriod("2022-07-01 00:00:00", "2022-12-31 23:59:59")
    period_2.modified_by = "SRK"
    period_3 = periods.ReportingPeriod("2023-01-01 00:00:00", "2023-06-30 23:59:59")
    period_3.modified_by = "SRK"
    period_4 = periods.ReportingPeriod("2023-07-01 00:00:00", "2023-12-31 23:59:59")
    period_4.modified_by = "SRK"

    # Build Standard Inventory Events
    import_event = event_types.EventType(
        "IMPORT",
        "Imported Medications",
        "Used when adding pre-existing stock to the table",
        +1,
    )
    import_event.modified_by = "SRK"

    order_event = event_types.EventType(
        "ORDER",
        "Ordered Medications",
        "Used when adding new stock from a purchase order.",
        +1,
    )
    order_event.modified_by = "SRK"

    use_event = event_types.EventType(
        "USE",
        "Used Medications",
        "Used when subtracting medication that was administered to a patient.",
        -1,
    )
    use_event.modified_by = "SRK"

    waste_event = event_types.EventType(
        "WASTE",
        "Wasted Medications",
        "Used when subtracting medication which was wasted.",
        -1,
    )
    waste_event.modified_by = "SRK"

    destruction_event = event_types.EventType(
        "DESTROY",
        "Destroy Medications",
        "Used when subtracting medication which was destroyed through a reverse distributor.",
        -1,
    )
    destruction_event.modified_by = "SRK"

    loss_event = event_types.EventType(
        "LOSS",
        "Loss of Medications",
        "Used when subtracting medication which were lost or stolen.",
        -1,
    )
    loss_event.modified_by = "SRK"

    for _ in DATABASE_FILES:
        db = database.Database()
        db.connect(f"{_}")

        med_table_query = medication.return_table_creation_query()
        db.create_table(med_table_query)

        periods_table_query = periods.return_table_creation_query()
        db.create_table(periods_table_query)

        event_types_table_query = event_types.return_table_creation_query()
        db.create_table(event_types_table_query)

        inventory_table_query = inventory.return_table_creation_query()
        db.create_table(inventory_table_query)

        fentanyl.save(db)
        morphine.save(db)
        midazolam.save(db)

        period_1.save(db)
        period_2.save(db)
        period_3.save(db)
        period_4.save(db)

        import_event.save(db)
        order_event.save(db)
        use_event.save(db)
        waste_event.save(db)
        destruction_event.save(db)
        loss_event.save(db)


if __name__ == "__main__":
    main()
