"""Contains the Test_Database class used to test the database module.

Classes:

    Test_Database: Contains all unit tests for the database module.

"""

import os

from narcotics_tracker import database, medication
from narcotics_tracker.utils import date


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

    def test_database_can_create_database_file(self, test_db, database_test_set_up):
        """Tests that Database can create a database file.

        Asserts that the database file exists in os path.
        """
        test_db = test_db
        db = database.Database()
        db.connect(test_db)

        assert os.path.exists("data/test_database.db")

    def test_database_can_connect_to_database(self, database_test_set_up):
        """Tests that connection can be made to the database.

        Asserts that the database_connection is not None.
        """
        db = database.Database()

        db.connect("test_database.db")
        assert db.database_connection is not None

    def test_database_can_delete_database(self, database_test_set_up):
        """Tests that Database can delete a database.

        Creates a database, then deletes it.
        Asserts that the database is not in the list of databases."""

        db = database.Database()
        db.connect("test_database.db")
        db.delete_database("test_database.db")

        assert os.path.exists("data/test_database.db") == False

    def test_database_can_create_table(self, database_test_set_up):
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

    def test_database_can_return_list_of_tables(self, database_test_set_up):
        """Tests that the writer can return a list of tables.

        Creates two tables, asserts that both tables exist in the list."""

        db = database.Database()
        db.connect("test_database.db")

        db.create_table("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")
        db.create_table("""CREATE TABLE IF NOT EXISTS test_table_2 (data TEXT)""")

        data = db.return_table_names()

        assert "test_table" in data and "test_table_2" in data

    def test_database_can_return_columns(self, database_test_set_up):
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

    def test_database_can_delete_table(self, database_test_set_up):
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

    def test_database_can_rename_table(self, database_test_set_up):
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

    def test_database_can_add_column_to_table(self, database_test_set_up):
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

    def test_database_can_rename_column_in_table(self, database_test_set_up):
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

    def test_database_can_write_data_to_table(self, database_test_set_up):
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

    def test_created_date_is_none_returns_false_if_created_date_is_set(self, test_med):
        """Tests if the function returns false when created date is set.

        Loads test_med, a mock object with a created date set.

        Asserts that the function returns 'False'.
        """
        test_med = test_med

        assert database.Database.created_date_is_none(test_med) == False

    def test_created_date_set_is_none_returns_true_when_set_to_None(self, test_med):
        """Tests if the function returns true when created date is None.

        Loads test_med, a mock object with a created date set. Sets the created
        date to None.

        Asserts that the function returns 'True'.
        """
        test_med = test_med
        test_med.created_date = None

        assert database.Database.created_date_is_none(test_med) == True

    def test_medication_can_be_created_from_stored_data(
        self, test_med, database_test_set_up
    ):
        """Test that a medication object can be created from stored data.
        
        Loads test_med, saved it to the database, then loads the data from 
        the saved database and creates a medication object from the data.
        
        Asserts that the new medication object has the same type as a \
        medication object.
        """
        test_med = test_med

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(medication.return_table_creation_query())
        test_med.save(db)

        new_med = db.load_medication("Un-69420-9001")

        assert isinstance(new_med, medication.Medication)

    def test_loaded_med_has_type_Medication(self, test_med, database_test_set_up):
        """Tests that loaded medications are medication objects.

        Saves test_med to database. Loads test_med from database to new_med.

        Asserts new_med is an instance of 'medication.Medication'.
        """

        test_med = test_med

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(medication.return_table_creation_query())
        test_med.save(db)

        medication_code = "Un-69420-9001"

        new_med = db.load_medication(medication_code)

        assert isinstance(new_med, medication.Medication)
