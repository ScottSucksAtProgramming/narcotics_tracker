"""Contains the Test_Setup class and all tests for the setup module.

Classes:
    Test_Setup: Contains all unit tests for the setup module."""

import os

from narcotics_tracker import database
from scripts import setup


class Test_Setup:
    """Contains all unit tests for the setup module.

    Behaviors Tested:
        - Setup can create database file.
        - Setup can create medication table.
    """

    def test_setup_can_create_database_file(self, database_test_set_up):
        """Tests to see if the database file can be created.

        Connects to 'test_database.db'.

        Asserts that 'data/test_database.db' exists.
        """
        db = database.Database()
        db.connect("test_database.db")

        assert os.path.exists("data/test_database.db")

    def test_setup_can_create_medication_table(self, database_test_set_up):
        """Tests to see if the medication table can be created.

        Connects to 'test_database.db'. Creates medication table. Returns
        table names.

        Asserts that 'medication' is in list of table names.
        """
        db = database.Database()
        db.connect("test_database.db")

        setup.create_medication_table(db)

        data = db.return_table_names()

        assert "medication" in data

    def test_setup_can_create_reporting_periods_table(
        self, database_test_set_up
    ) -> None:
        """Tests to see if the reporting_periods table can be created.

        Connects to 'test_database.db'. Creates reporting_periods table.
        Returns table names.

        Asserts that 'reporting_period' is in list of table names.
        """
        db = database.Database()
        db.connect("test_database.db")

        setup.create_reporting_periods_table(db)

        data = db.return_table_names()

        assert "reporting_periods" in data

    def test_setup_can_create_event_types_table(self, database_test_set_up) -> None:
        """Tests to see if the event_types table can be created.

        Connects to 'test_database.db'. Creates event_types table.
        Returns table names.

        Asserts that 'event_types' is in list of table names.
        """
        db = database.Database()
        db.connect("test_database.db")

        setup.create_event_types_table(db)

        data = db.return_table_names()

        assert "event_types" in data
