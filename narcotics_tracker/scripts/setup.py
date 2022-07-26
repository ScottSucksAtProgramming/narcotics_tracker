"""Sets up the Narcotics Tracker.

This script is intended to be called called the first time the Narcotics 
Tracker is being used. It will created the database, tabes, and standard 
items.

Functions:

    main: Creates a database file, populates with the standard tables and 
        items.

    clear_screen: Clears the screen.

    create_tables: Initializes the database and sets up the tables.

    populate_events: Adds the Standard Events to the database.

    populate_statuses: Adds the Standard Statuses to the database.

    populate_units: Adds the Standard Units to the database.
"""

import os
import sqlite3
from typing import TYPE_CHECKING

from narcotics_tracker import commands
from narcotics_tracker.configuration.standard_items import StandardItemCreator
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.commands.interfaces.command import Command


def main() -> None:
    """Creates a database file, populates with the standard tables and items."""
    clear_screen()

    print("Welcome to the Narcotics Tracker!\n")
    print("Starting database setup.\n")

    print("Preparing to create tables:")
    create_tables()
    print("\nTable creation complete!!\n")

    print("Preparing to add standard items:\n")
    populate_events()
    populate_statuses()
    populate_units()

    print("\nStandard items added successfully.")
    print("\nNarcotics Tracker database setup complete.")
    input("Press ENTER to continue.")


def clear_screen():
    """Clears the screen."""
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)


def create_tables() -> str:
    """Initializes the database and sets up the tables."""
    persistence_manager = ServiceManager().persistence
    commands = _return_table_list()

    for command in commands:
        command().execute()
        print(f"- {command._table_name} table created.")


def _return_table_list() -> list["Command"]:
    """Returns a list of table creation commands."""
    tables_list = [
        commands.CreateEventsTable,
        commands.CreateInventoryTable,
        commands.CreateMedicationsTable,
        commands.CreateReportingPeriodsTable,
        commands.CreateStatusesTable,
        commands.CreateUnitsTable,
    ]
    return tables_list


def populate_events() -> None:
    """Adds the Standard Events to the database."""
    events = StandardItemCreator().create_events()
    counter = 0

    for event in events:
        try:
            commands.AddEvent().execute(event)
        except sqlite3.IntegrityError as e:  # Events likely in the database already.
            pass
        else:
            counter += 1

    print(f"- {counter} events added to the database.")


def populate_statuses() -> None:
    """Adds the Standard Statuses to the database."""
    statuses = StandardItemCreator().create_statuses()
    counter = 0

    for status in statuses:
        try:
            commands.AddStatus().execute(status)
        except sqlite3.IntegrityError as e:  # Statuses likely in the database already.
            pass
        else:
            counter += 1

    print(f"- {counter} statuses added to the database.")


def populate_units() -> None:
    """Adds the Standard Units to the database."""
    units = StandardItemCreator().create_units()
    counter = 0

    for unit in units:
        try:
            commands.AddUnit().execute(unit)
        except sqlite3.IntegrityError as e:  # Units likely in the database already.
            print(e)
            pass
        else:
            counter += 1

    print(f"- {counter} units added to the database.")


if __name__ == "__main__":
    main()
