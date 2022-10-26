"""Sets up the Narcotics Tracker.

This script is intended to be called called the first time the Narcotics 
Tracker is being used. It will created the database, tabes, and standard 
items.

Functions:

    main: Sets up the Narcotics Tracker database and populates the tables.
"""

import os
import sqlite3
from typing import TYPE_CHECKING

from narcotics_tracker import commands
from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.items.events import Event
from narcotics_tracker.items.medications import Medication
from narcotics_tracker.items.reporting_periods import ReportingPeriod
from narcotics_tracker.items.statuses import Status
from narcotics_tracker.items.units import Unit
from narcotics_tracker.persistence_interface import PersistenceManager
from narcotics_tracker.setup.standard_items import StandardItemCreator
from narcotics_tracker.utils.datetime_manager import DateTimeManager

if TYPE_CHECKING:
    from narcotics_tracker.commands.command_interface import SQLiteCommand
    from narcotics_tracker.items.data_items import DataItem


def create_tables(
    persistence_manager: SQLiteManager, commands: list["SQLiteCommand"]
) -> str:
    """Initializes the database and sets up the tables.

    Args:
        persistence_manager (SQLiteManager): The object handling persistent storage of DataItems.

        commands (list[SQLiteCommand]): A list of table creation commands.
    """
    for command in commands:
        command(persistence_manager).execute()
        print(f"- {command.table_name} table created.")


def populate_events(storage_manager: PersistenceManager, events: list["Event"]) -> None:
    counter = 0

    for event in events:
        try:
            commands.AddEvent(storage_manager, event).execute()
        except sqlite3.IntegrityError as e:  # Events likely in the database already.
            print(e)
            pass
        else:
            counter += 1

    print(f"- {counter} events added to the database.")


def populate_medications(
    storage_manager: PersistenceManager, medications: list["Medication"]
) -> None:
    counter = 0

    for medication in medications:
        try:
            commands.AddMedication(storage_manager, medication).execute()
        except sqlite3.IntegrityError as e:  # medications likely in the database already.
            pass
        else:
            counter += 1

    print(f"- {counter} medications added to the database.")


def populate_reporting_periods(
    storage_manager: PersistenceManager, reporting_periods: list["ReportingPeriod"]
) -> None:
    counter = 0

    for reporting_period in reporting_periods:
        try:
            commands.AddReportingPeriod(storage_manager, reporting_period).execute()
        except sqlite3.IntegrityError as e:  # reporting_periods likely in the database already.
            pass
        else:
            counter += 1

    print(f"- {counter} reporting_periods added to the database.")


def populate_statuses(
    storage_manager: PersistenceManager, statuses: list["Status"]
) -> None:
    counter = 0

    for status in statuses:
        try:
            commands.AddStatus(storage_manager, status).execute()
        except sqlite3.IntegrityError as e:  # Statuses likely in the database already.
            pass
        else:
            counter += 1

    print(f"- {counter} statuses added to the database.")


def populate_units(storage_manager: PersistenceManager, units: list["Unit"]) -> None:
    counter = 0

    for unit in units:
        try:
            commands.AddUnit(storage_manager, unit).execute()
        except sqlite3.IntegrityError as e:  # Units likely in the database already.
            pass
        else:
            counter += 1

    print(f"- {counter} units added to the database.")


def clear_screen():
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)


def return_tables_list() -> list["DataItem"]:
    tables_list = [
        commands.CreateEventsTable,
        commands.CreateInventoryTable,
        commands.CreateMedicationsTable,
        commands.CreateReportingPeriodsTable,
        commands.CreateStatusesTable,
        commands.CreateUnitsTable,
    ]
    return tables_list


def main() -> None:
    """Sets up the Narcotics Tracker database and populates the tables."""
    clear_screen()

    print("Welcome to the Narcotics Tracker!\n")

    sq = SQLiteManager("inventory.db")
    print("Preparing to setup Inventory Database.\n")

    print("Preparing to create tables:")
    create_tables(sq, return_tables_list())
    print("\nTable creation complete!!\n")

    print("Preparing to add standard items:\n")
    item_creator = StandardItemCreator()

    events = item_creator.create_events()
    populate_events(sq, events)

    statuses = item_creator.create_statuses()
    populate_statuses(sq, statuses)

    units = item_creator.create_units()
    populate_units(sq, units)
    print("\nStandard items added successfully.")
    print("\nNarcotics Tracker database setup complete.")
    input("Press ENTER to continue.")


if __name__ == "__main__":
    main()
