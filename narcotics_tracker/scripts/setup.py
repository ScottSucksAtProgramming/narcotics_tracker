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
from narcotics_tracker.setup.standard_items import StandardItemCreator
from narcotics_tracker.utils.date_and_time import DateTimeManager

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


def populate_database(
    storage_manager: SQLiteManager, items: list["DataItem"], dt_manager: DateTimeManager
) -> None:
    counter = 0

    for item in items:
        try:
            commands.SaveItem(storage_manager, item, dt_manager).execute()
        except sqlite3.IntegrityError as e:  # Items likely in the database already.
            pass
        else:
            counter += 1

    print(f"- {counter} items added to the database.")


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
    items = item_creator.create()
    dtm = DateTimeManager()
    populate_database(sq, items, dtm)
    print("\nStandard items added successfully.")
    print("\nNarcotics Tracker database setup complete.")
    input("Press ENTER to continue.")


if __name__ == "__main__":
    main()
