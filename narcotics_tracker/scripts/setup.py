"""Sets up the Narcotics Tracker.

This script is intended to be called called the first time the Narcotics 
Tracker is being used. It will created the database, tabes, and standard 
items.

Functions:

    main: Sets up the Narcotics Tracker database and populates the tables.
"""

from typing import TYPE_CHECKING

from narcotics_tracker import sqlite_commands
from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.setup.standard_items import StandardItemCreator
from narcotics_tracker.utils.date_and_time import DateTimeManager

if TYPE_CHECKING:
    from narcotics_tracker.items.data_items import DataItem
    from narcotics_tracker.sqlite_commands_interface import SQLiteCommand


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
        sqlite_commands.SaveItem(storage_manager, item, dt_manager).execute()
        counter += 1

    print(f"{counter} items added to the database.")


def main() -> None:
    """Sets up the Narcotics Tracker database and populates the tables."""
    print("Welcome to the Narcotics Tracker!\n")

    sq = SQLiteManager("inventory.db")
    print("Persistence manager initialized.\n")

    TABLES_LIST = [
        sqlite_commands.CreateEventsTable,
        sqlite_commands.CreateInventoryTable,
        sqlite_commands.CreateMedicationsTable,
        sqlite_commands.CreateReportingPeriodsTable,
        sqlite_commands.CreateStatusesTable,
        sqlite_commands.CreateUnitsTable,
    ]

    print("Preparing to create tables:")
    create_tables(sq, TABLES_LIST)
    print("\nTable creation complete!!\n")

    print("Preparing to add standard items.\n")
    item_creator = StandardItemCreator()
    items = item_creator.create()
    dtm = DateTimeManager()
    populate_database(sq, items, dtm)
    print("Standard items added successfully.\n")


if __name__ == "__main__":
    main()
