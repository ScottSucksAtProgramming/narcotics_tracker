"""This script sets up the Narcotics Tracker.

This script is intended to be called called the first time the Narcotics 
Tracker is being used. It will created the database, tabes, and standard 
items.

Functions:

    main: Sets up the Narcotics Tracker database and populates the tables.
"""

import sqlite3

from narcotics_tracker import database, sqlite_commands
from narcotics_tracker.builders import event_builder, status_builder, unit_builder
from narcotics_tracker.setup import standard_items


# Populate Tables.
def populate_database_with_standard_events(db_connection: sqlite3.Connection) -> None:
    """Builds and saves standard events to the database.

    Standard events are located in the Standard Items module of the Setup
    package.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    standard_events = standard_items.STANDARD_EVENTS

    e_builder = event_builder.EventBuilder()

    for event in standard_events:
        e_builder.assign_all_attributes(event)
        built_event = e_builder.build()
        built_event.save(db_connection)


def populate_database_with_standard_units(db_connection: sqlite3.Connection) -> None:
    """Builds and saves standard units to the database.

    Standard units are located in the Standard Items module of the Setup
    package.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    standard_units = standard_items.STANDARD_UNITS

    unt_builder = unit_builder.UnitBuilder()

    for unit in standard_units:
        unt_builder.assign_all_attributes(unit)
        built_unit = unt_builder.build()
        built_unit.save(db_connection)


def populate_database_with_standard_statuses(db_connection: sqlite3.Connection) -> None:
    """Builds and saves standard statuses to the database.

    Standard statuses are located in the Standard Items module of the Setup
    package.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    standard_statuses = standard_items.STANDARD_STATUSES

    stat_builder = status_builder.StatusBuilder()

    for status in standard_statuses:
        stat_builder.assign_all_attributes(status)
        built_status = stat_builder.build()
        built_status.save(db_connection)


def main() -> None:
    """Sets up the Narcotics Tracker database and populates the tables."""
    sq = database.SQLiteManager("inventory.db")

    create_table_commands = [
        sqlite_commands.CreateEventsTable,
        sqlite_commands.CreateInventoryTable,
        sqlite_commands.CreateMedicationsTable,
        sqlite_commands.CreateReportingPeriodsTable,
        sqlite_commands.CreateStatusesTable,
        sqlite_commands.CreateUnitsTable,
    ]

    for command in create_table_commands:
        command(sq).execute()

        # populate_database_with_standard_units(db)
        # populate_database_with_standard_events(db)
        # populate_database_with_standard_containers(db)
        # populate_database_with_standard_statuses(db)


if __name__ == "__main__":
    main()
