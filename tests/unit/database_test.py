"""Contains the Test_Database class used to test the database module.

Classes:

    Test_Database: Contains all unit tests for the database module.

"""

import os

from narcotics_tracker import database, event_types, medications, reporting_periods


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
        """Tests that Database object can be created.

        Asserts that the object is an instance of Database.
        """
        db = database.Database()

        assert isinstance(db, database.Database)

    def test_database_can_create_database_file(self, test_database, reset_database):
        """Tests that Database can create a database file.

        Asserts that the database file exists in os path.
        """
        db = database.Database()
        db.connect("test_database.db")

        assert os.path.exists("data/test_database.db")

    def test_database_can_connect_to_database(self, reset_database):
        """Tests that connection can be made to the database.

        Asserts that the database_connection is not None.
        """
        db = database.Database()

        db.connect("test_database.db")
        assert db.database_connection is not None

    def test_database_can_delete_database(self, reset_database):
        """Tests that Database can delete a database.

        Creates a database, then deletes it.
        Asserts that the database is not in the list of databases."""

        db = database.Database()
        db.connect("test_database.db")
        db.delete_database("test_database.db")

        assert os.path.exists("data/test_database.db") == False

    def test_database_can_create_table(self, reset_database):
        """Tests that Database can create a table.

        Creates a table.

        Asserts that the table name is returned when querying table names from
        the database.
        """
        db = database.Database()
        db.connect("test_database.db")

        db.create_table("""CREATE TABLE IF NOT EXISTS test_table (test_column TEXT)""")

        tables = db.return_table_names()

        assert "test_table" in tables

    def test_database_can_return_list_of_tables(self, reset_database):
        """Tests that the writer can return a list of tables.

        Creates two tables, asserts that both tables exist in the list."""

        db = database.Database()
        db.connect("test_database.db")

        db.create_table("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")
        db.create_table("""CREATE TABLE IF NOT EXISTS test_table_2 (data TEXT)""")

        data = db.return_table_names()

        assert "test_table" in data and "test_table_2" in data

    def test_database_can_return_columns(self, reset_database):
        """Tests that Database can return list of columns from table.

        Creates a table with columns 'data' and 'number'. Gets list of columns.

        Asserts that the columns exist in list of column names."""

        db = database.Database()
        db.connect("test_database.db")

        db.create_table(
            """CREATE TABLE IF NOT EXISTS test_table (data TEXT, number INTEGER)"""
        )

        columns = db.return_columns("""SElECT * FROM test_table""")

        # Assert
        assert "data" in columns and "number" in columns

    def test_database_can_delete_table(self, reset_database):
        """Tests that Database can delete a table.

        Creates table if it doesn't already exist, then deletes it.

        Asserts that the table is not in the final list of tables."""

        # Arrange
        db = database.Database()
        db.connect("test_database.db")

        db.create_table("""CREATE TABLE IF NOT EXISTS test_table (test_column TEXT)""")

        db.delete_table(
            """DROP
                TABLE IF EXISTS test_table"""
        )
        final_tables = db.return_table_names()

        assert "test_table" not in final_tables

    def test_database_can_rename_table(self, reset_database):
        """Tests that Database can rename a table.

        Creates 'old_table'. Renames 'old_table' to 'new_table'.

        Asserts that 'new_table' is in the final list of tables and
        'old_table' is not.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table("""CREATE TABLE IF NOT EXISTS old_table (data TEXT)""")

        db.update_table("""ALTER TABLE old_table RENAME TO new_table""")
        tables = db.return_table_names()

        assert "new_table" in tables and "old_table" not in tables

    def test_database_can_add_column_to_table(self, reset_database):
        """Test that Database can add a column to a table.

        Creates a table, adds a column.

        Asserts that the column is returned in the list of columns.
        """
        db = database.Database()
        db.connect("test_database.db")

        db.create_table("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")

        db.update_table("""ALTER TABLE test_table ADD COLUMN new_column REAL""")
        columns = db.return_columns("""SELECT * FROM 'test_table'""")

        assert "new_column" in columns

    def test_database_can_rename_column_in_table(self, reset_database):
        """Tests that Database can rename a column in a table.

        Creates a table, adds a column, renames the column.

        Asserts that thew new column name is in the list and the old name is
        not.
        """
        # Arrange
        db = database.Database()
        db.connect("test_database.db")

        db.create_table("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")

        db.update_table("""ALTER TABLE test_table RENAME COLUMN data TO new_data""")

        columns = db.return_columns("""SElECT * FROM test_table""")
        assert "new_data" in columns

    def test_database_can_write_data_to_table(self, reset_database):
        """Tests that Database can write data to a table.

        Creates a table, writes data to the table.

        Asserts that the data written is returned when querying the table.
        """

        db = database.Database()
        db.connect("test_database.db")
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

        assert database.Database.created_date_is_none(test_medication) == False

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

        assert database.Database.created_date_is_none(test_medication) == True

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

        db = database.Database()
        db.connect("test_database.db")
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

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(event_types.return_table_creation_query())
        test_event.save(db)

        new_event = db.load_event_type("TEST")

        assert isinstance(new_event, event_types.EventType)

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

        db = database.Database()
        db.connect("test_database.db")
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
