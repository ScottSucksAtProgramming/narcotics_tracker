"""This module will act as a setup script for the narcotics_tracker."""

import sqlite3

from narcotics_tracker import database, medication, periods


def create_medication_table(db_connection: sqlite3.Connection) -> None:
    """This function will create the medication table."""
    db_connection.create_table(medication.return_table_creation_query())


def create_reporting_periods_table(db_connection: sqlite3.Connection) -> None:
    """Creates the reporting_periods table."""
    db_connection.create_table(periods.return_table_creation_query())


if __name__ == "__main__":
    db = database.Database()
    db.connect("inventory.db")

    create_medication_table(db)
    create_reporting_periods_table(db)
