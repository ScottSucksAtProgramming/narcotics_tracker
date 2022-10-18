"""Creates the medications which I use at my agency and writes them to the 
table."""

from narcotics_tracker import commands
from narcotics_tracker.sqlite_command_interface import SQLiteCommand


def create_tables(tables=list[SQLiteCommand]):
    for table in tables:
        table.execute()


def main():

    # Create tables in the database file.
    tables = [
        commands.CreateEventsTable(),
        commands.CreateInventoryTable(),
        commands.CreateMedicationsTable(),
        commands.CreateReportingPeriodsTable(),
        commands.CreateStatusesTable(),
        commands.CreateUnitsTable(),
    ]

    create_tables(tables)
    # Build Medication Objects

    # Build Reporting Period Objects


if __name__ == "__main__":
    main()
