"""Contains tests for the database module."""

from narcotics_tracker import database, medication
from narcotics_tracker.utils import date


class Test_DatabaseClass:
    """Tests the behaviors of the Database Writer"""

    def test_connect_to_database(self):
        """Tests that the writer can connect to the database"""

        db = database.Database()

        db.connect("test_database.db")

        assert db.database_connection is not None

    def test_create_table(self):
        """Tests that the writer can create a table."""

        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS test_table")

        table_name = "test_table"
        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

        db.create_table("""CREATE TABLE IF NOT EXISTS test_table (test_column TEXT)""")

        tables = db.return_data(sql_query)

        assert (table_name,) in tables

    def test_get_tables(self):
        """Tests that the writer can read data from a table."""

        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS test_read_table")

        sql_create_table = """
                CREATE TABLE IF NOT EXISTS test_read_table (
                data TEXT,
                PRIMARY KEY (data)
                )
            """
        db.create_table(sql_create_table)

        values = ["test"]
        sql_write_data = """INSERT OR IGNORE INTO test_read_table (data) VALUES(?)"""

        db.write_data(sql_write_data, values)
        table_name = ["test_read_table"]

        data = db.return_tables(
            """SELECT * FROM sqlite_master WHERE type='table' and name=(?) """,
            table_name,
        )[0][4]

        assert values[0] in data

    def test_get_columns(self):
        """Tests that the writer can get the columns in a table."""

        # Arrange
        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS test_get_columns_table")

        sql_create_table = """
                CREATE TABLE IF NOT EXISTS test_get_columns_table (
                data TEXT,
                PRIMARY KEY (data)
                )
            """
        db.create_table(sql_create_table)

        # Act
        columns = db.return_columns("""SElECT * FROM test_get_columns_table""")

        # Assert
        assert "data" == columns[0][0]

    def test_delete_table(self):
        """Tests that the writer can delete a table."""

        # Arrange
        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS test_delete_table")

        sql_find_table = """SELECT name FROM sqlite_master WHERE type='table';"""
        sql_create_table = (
            """CREATE TABLE IF NOT EXISTS test_delete_table (test_column TEXT)"""
        )

        db.create_table(sql_create_table)

        # Act
        db.delete_table("DROP TABLE IF EXISTS test_delete_table")
        tables = db.return_data(sql_find_table)

        # Assert
        assert ("test_delete_table",) not in tables

    def test_update_table_rename(self):
        """Tests that the writer can rename a table."""
        # Arrange
        db = database.Database()
        db.connect("test_database.db")

        db.delete_table("DROP TABLE IF EXISTS old_table")
        db.delete_table("DROP TABLE IF EXISTS new_table")

        sql_create_table = """
                CREATE TABLE IF NOT EXISTS old_table (
                data TEXT,
                PRIMARY KEY (data)
                )
            """
        db.create_table(sql_create_table)

        sql_insert_data = """INSERT OR IGNORE INTO old_table (data) VALUES(?)"""
        values = ["test"]
        db.write_data(sql_insert_data, values)

        # Act
        sql_rename_table = """ALTER TABLE old_table RENAME TO new_table"""
        db.update_table(sql_rename_table)

        # Assert
        assert db.return_data("""SElECT * FROM new_table""") == [("test",)]

    def test_update_table_add_column(self):
        """Tests that the writer can add a column to a table."""

        # Arrange
        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS test_add_column_table")

        sql_create_table = """
                CREATE TABLE IF NOT EXISTS test_add_column_table (
                data TEXT,
                PRIMARY KEY (data)
                )
            """
        db.create_table(sql_create_table)

        # Act
        sql_add_column = (
            """ALTER TABLE test_add_column_table ADD COLUMN new_column REAL"""
        )
        db.update_table(sql_add_column)
        columns = db.return_columns("""SElECT * FROM test_add_column_table""")

        # Assert
        assert "new_column" == columns[1][0]

    def test_update_table_rename_column(self):
        """Tests that the writer can rename a column in a table."""

        # Arrange
        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS test_rename_column_table")

        sql_create_table = """
                CREATE TABLE IF NOT EXISTS test_rename_column_table (
                data TEXT,
                PRIMARY KEY (data)
                )
            """
        db.create_table(sql_create_table)

        # Act
        sql_rename_column = (
            """ALTER TABLE test_rename_column_table RENAME COLUMN data TO new_data"""
        )
        db.update_table(sql_rename_column)

        # Assert
        column_name = db.return_columns("""SElECT * FROM test_rename_column_table""")[
            0
        ][0]
        assert column_name == "new_data"

    def test_write_data(self):
        """Tests that the writer can write data to a table."""

        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS test_write_data_table")

        sql_create_table = """
                CREATE TABLE IF NOT EXISTS test_write_data_table (
                data TEXT,
                PRIMARY KEY (data)
                )
            """

        db.delete_table("DROP TABLE IF EXISTS test_write_data_table")

        db.create_table(sql_create_table)
        values = ["test"]
        sql = """INSERT INTO test_write_data_table (data) VALUES(?)"""

        db.write_data(sql, values)

        assert db.return_data("""SElECT * FROM test_write_data_table""") == [("test",)]

    def test_created_date_has_value(self, test_med):
        """Checks to see if the created date is None."""

        test_med = test_med

        assert database.Database.created_date_is_none(test_med) == False

    def test_created_date_set_if_none(self, test_med):
        """Checks to see if the created date is initially set to none it is
        replaced with current date.
        """

        test_med = test_med
        db = database.Database()
        db.connect("test_database.db")

        test_med.created_date = None

        test_med.save(db)

        assert test_med.created_date == date.get_date_as_string()

    def test_load_medication(self, test_med):
        """Checks to see if the medication data is correctly loaded from
        database."""

        test_med = test_med

        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS medications")
        db.create_table(medication.return_table_creation_query())
        test_med.save(db)

        medication_code = "Un-69420-9001"

        new_med = db.load_medication(medication_code)

        assert new_med.concentration == 7.712476391512054

    def test_loaded_med_has_type_Medication(self, test_med):
        """Checks to see if the medication data is correctly loaded from
        database."""

        test_med = test_med

        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS medications")
        db.create_table(medication.return_table_creation_query())
        test_med.save(db)

        medication_code = "Un-69420-9001"

        new_med = db.load_medication(medication_code)

        assert isinstance(new_med, medication.Medication)
