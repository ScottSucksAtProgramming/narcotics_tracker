"""Contains classes to test the Database Module.

Classes:

    Test_Database: Contains all unit tests for the database module.

"""

import os

from narcotics_tracker import events, medications, reporting_periods
from narcotics_tracker.persistence.database import SQLiteManager


class Test_Database:
    """Contains all unit tests for the database module.

    Attributes:
        test_database: The database file used for testing.

    Behaviors Tested:
        - Database object can be created.
        - Database object can create a database file.
        - Database object can connect to a database.
        - Database object can delete a database.
        - Database object can create tables.
        - Database object can return list of tables.
        - Database object can return columns in a table.
        - Database object can delete tables.
        - Database object can update tables.
        - Database object can return data from a table.
        - Database object can write data to a table.
        - Static method: created_date_is_none returns True if no created date.
        - Static method: created_date_is_none returns False if created date.
        - Database object can create medication object from data.

    """

    def test_database_object_can_be_created(self):
        """Tests that SQLiteManager object can be created.

        Asserts that the object is an instance of Database.
        """
        with SQLiteManager("test_database.db") as db:
            print(type(db))

            assert isinstance(db, SQLiteManager)

    def test_database_can_create_database_file(self, reset_database):
        """Tests that Database can create a database file.

        Asserts that the database file exists in os path.
        """
        with SQLiteManager("test_database.db") as db:
            assert os.path.exists("data/test_database.db")

    def test_database_can_connect_to_database(self, reset_database):
        """Tests that connection can be made to the database.

        Asserts that the database_connection is not None.
        """
        with SQLiteManager("test_database.db") as db:
            assert db.connection is not None

    def test_database_can_delete_database(self, reset_database):
        """Tests that Database can delete a database.

        Creates a database, then deletes it.
        Asserts that the database is not in the list of databases
        """
        with SQLiteManager("test_database.db") as db:
            db.delete_database("test_database.db")

        assert os.path.exists("data/test_database.db") == False

    def test_database_can_write_data_to_table(self, reset_database):
        """Tests that Database can write data to a table.

        Creates a table, writes data to the table.

        Asserts that the data written is returned when querying the table.
        """
        with SQLiteManager("test_database.db") as db:
            db.create_table("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")

            db.write_data(
                """INSERT INTO test_table (data) VALUES(?)""",
                ["This is the data"],
            )

            data = db.return_data("""SElECT * FROM test_table""")

        assert "This is the data" in data[0]

    def test_created_date_is_none_returns_false_if_created_date_is_set(
        self, test_medication
    ):
        """Tests if the function returns false when created date is set.

        Loads test_medication, a mock object with a created date set.

        Asserts that the function returns 'False'.
        """
        test_medication = test_medication

        assert SQLiteManager.created_date_is_none(test_medication) == False

    def test_created_date_set_is_none_returns_true_when_set_to_None(
        self, test_medication
    ):
        """Tests if the function returns true when created date is None.

        Loads test_medication, a mock object with a created date set. Sets the created
        date to None.

        Asserts that the function returns 'True'.
        """
        test_medication = test_medication
        test_medication.created_date = None

        assert SQLiteManager.created_date_is_none(test_medication) == True

    def test_medication_can_be_loaded_from_stored_data(
        self, test_medication, reset_database
    ):
        """Test that a medication object can be loaded from stored data.
        
        Loads test_medication, saved it to the database, then loads the data from 
        the saved database and creates a medication object from the data.
        
        Asserts that the new medication object has the same type as a \
        medication object.
        """
        test_medication = test_medication

        with SQLiteManager("test_database.db") as db:
            db.create_table(medications.return_table_creation_query())
            test_medication.save(db)

            new_med = db.load_medication("Un-69420-9001")

        assert isinstance(new_med, medications.Medication)

    def test_event_can_be_loaded_from_stored_data(self, test_event, reset_database):
        """Test that a event_type object can be loaded from stored data.

        Loads test_event, saved it to the database, then loads the data
        from the saved database and creates a event_type object from the data.

        Asserts that the new event_type object has the same type as a
        event_type object.
        """
        test_event = test_event

        with SQLiteManager("test_database.db") as db:
            db.create_table(events.return_table_creation_query())
            test_event.save(db)

            new_event = db.load_event("TEST")

        assert isinstance(new_event, events.Event)

    def test_reporting_period_can_be_loaded_from_stored_data(
        self, test_period, reset_database
    ):
        """Test that a reporting_period object can be loaded from stored data.

        Loads test_period, saves it to the database, then loads the data
        from the database and creates a ReportingPeriod object from the data.

        Asserts that the new ReportingPeriod object has the same type as a
        ReportingPeriod object.
        """
        test_period = test_period

        with SQLiteManager("test_database.db") as db:
            db.create_table(reporting_periods.return_table_creation_query())
            test_period.save(db)

            new_period = db.load_reporting_period(9001)

        assert isinstance(new_period, reporting_periods.ReportingPeriod)

    def test_can_return_current_datetime(self) -> None:
        """Tests to see if the Database class can get the current date time.

        Asserts that the returned datetime is not 'None'.
        """

        assert database.return_datetime() != None

    def test_can_format_unixepoch_datetime_to_readable_string(self) -> None:
        """Tests that unixepoch datetimes can be converted to strings.

        Asserts that the datetime int '505026000' returns 01-02-1986"""

        assert (
            database.format_datetime_from_unixepoch(505026000) == "1986-01-02 00:00:00"
        )
