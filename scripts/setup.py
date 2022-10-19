"""This script sets up the Narcotics Tracker.

This script is intended to be called called the first time the Narcotics 
Tracker is being used. It will created the database, tabes, and standard 
items.

Functions:

    create_database: Creates the database file and returns a connection to it.

    create_event_types_table: Creates the event_types table.

    create_inventory_table: Creates the inventory table.

    create_medications_table: Creates the medications table.

    create_reporting_periods_table: Creates the reporting_periods table.

    create_units_table: Creates the units table.

    main: Sets up the Narcotics Tracker database and populates the tables.
"""

import sqlite3

from narcotics_tracker import commands, database
from narcotics_tracker.builders import event_builder, status_builder, unit_builder
from narcotics_tracker.setup import standard_items


def create_database(database_file_name: str = None) -> sqlite3.Connection:
    """Creates the database file and returns a connection to it.

    If the file name is not specified the user is prompted to enter it through
    the console.

    Args:

        database_file_name (str): Name of the database file.

    Returns:

        db (sqlite3.Connection): Connection to the created database file.
    """
    if database_file_name == None:
        database_file_name = input("What would you like to name the database file? ")

    return database_file_name


def create_containers_table(db_connection: sqlite3.Connection) -> None:
    """Creates the containers table.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    db_connection.create_table(containers.return_table_creation_query())


def create_events_table(db_connection: sqlite3.Connection) -> None:
    """Creates the events table.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    db_connection.create_table(events.return_table_creation_query())


def create_inventory_table(db_connection: sqlite3.Connection) -> None:
    """Creates the inventory table.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    db_connection.create_table(inventory.return_table_creation_query())


def create_medications_table(db_connection: sqlite3.Connection) -> None:
    """Creates the medications table.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    db_connection.create_table(medications.return_table_creation_query())


def create_reporting_periods_table(db_connection: sqlite3.Connection) -> None:
    """Creates the reporting_periods table.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    db_connection.create_table(reporting_periods.return_table_creation_query())


def create_statuses_table(db_connection: sqlite3.Connection) -> None:
    """Creates the statuses table.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    db_connection.create_table(statuses.return_table_creation_query())


def create_units_table(db_connection: sqlite3.Connection) -> None:
    """Creates the units table.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    db_connection.create_table(units.return_table_creation_query())


# Populate Tables.
def populate_database_with_standard_containers(
    db_connection: sqlite3.Connection,
) -> None:
    """Builds and saves standard containers to the database.

    Standard containers are located in the Standard Items module of the Setup
    package.

    Args:

        db_connection (sqlite3.Connection): The connection to the database.
    """
    standard_containers = standard_items.STANDARD_CONTAINERS

    cont_builder = container_builder.ContainerBuilder()

    for container in standard_containers:
        cont_builder.assign_all_attributes(container)
        built_container = cont_builder.build()
        built_container.save(db_connection)


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
        commands.CreateEventsTable,
        commands.CreateInventoryTable,
        commands.CreateMedicationsTable,
        commands.CreateReportingPeriodsTable,
        commands.CreateStatusesTable,
        commands.CreateUnitsTable,
    ]

    for command in create_table_commands:
        command(sq).execute()

        # populate_database_with_standard_units(db)
        # populate_database_with_standard_events(db)
        # populate_database_with_standard_containers(db)
        # populate_database_with_standard_statuses(db)


if __name__ == "__main__":
    main()
