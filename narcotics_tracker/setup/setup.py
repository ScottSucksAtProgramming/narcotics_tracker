"""This module will act as a setup script for the narcotics_tracker."""

from narcotics_tracker.database import database
from narcotics_tracker.medication import medication


def create_medication_table():
    """This function will create the medication table."""
    db = database.Database()
    db.connect("inventory.db")

    db.create_table(medication.Medication.return_table_creation_query())


if __name__ == "__main__":
    create_medication_table()
