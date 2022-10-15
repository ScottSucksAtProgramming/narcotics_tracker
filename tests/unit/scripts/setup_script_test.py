"""Contains the Test_Setup class and all tests for the setup module.

Classes:
    Test_Setup: Contains all unit tests for the setup module."""

import os

from narcotics_tracker.persistence import database
from scripts import setup


class Test_Setup:
    """Contains all unit tests for the setup module.

    Behaviors Tested:
        - Setup can create database file.
        - Setup can create medication table.
    """

    def test_setup_can_create_database_file(self, reset_database):
        """Tests to see if the database file can be created.

        Connects to 'test_database.db'.

        Asserts that 'data/test_database.db' exists.
        """
        with database.Database("test_database.db") as db:

            assert os.path.exists("data/test_database.db")

    def test_setup_can_create_medications_table(self, reset_database):
        """Tests to see if the medication table can be created.

        Connects to 'test_database.db'. Creates medication table. Returns
        table names.

        Asserts that 'medications' is in list of table names.
        """
        with database.Database("test_database.db") as db:

            setup.create_medications_table(db)

            data = db.return_table_names()

        assert "medications" in data

    def test_setup_can_create_reporting_periods_table(self, reset_database) -> None:
        """Tests to see if the reporting_periods table can be created.

        Connects to 'test_database.db'. Creates reporting_periods table.
        Returns table names.

        Asserts that 'reporting_period' is in list of table names.
        """
        with database.Database("test_database.db") as db:

            setup.create_reporting_periods_table(db)

            data = db.return_table_names()

        assert "reporting_periods" in data

    def test_setup_can_create_event_types_table(self, reset_database) -> None:
        """Tests to see if the event_types table can be created.

        Connects to 'test_database.db'. Creates event_types table.
        Returns table names.

        Asserts that 'events' is in list of table names.
        """
        with database.Database("test_database.db") as db:

            setup.create_events_table(db)

            data = db.return_table_names()

        assert "events" in data

    def test_setup_can_populate_events_table(self, reset_database) -> None:
        """Tests that the setup script adds the standard events to the table.

        Resets the database. Creates table and calls
        populate_database_with_standard_events(). Queries events table.

        Asserts that the returned data contains 6 items.
        """
        with database.Database("test_database.db") as db:
            setup.create_events_table(db)
            setup.populate_database_with_standard_events(db)

            data = db.return_data("""SELECT event_name FROM events""")

        assert len(data) == 6

    def test_setup_can_populate_units_table(self, reset_database) -> None:
        """Tests that the setup script adds the standard units to the table.

        Resets the database. Creates table and calls
        populate_database_with_standard_units(). Queries units table.

        Asserts that the returned data contains 4 items.
        """
        with database.Database("test_database.db") as db:
            setup.create_units_table(db)
            setup.populate_database_with_standard_units(db)

            data = db.return_data("""SELECT unit_code FROM units""")

        assert len(data) == 4
