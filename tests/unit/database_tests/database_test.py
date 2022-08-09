"""Contains the TestDatabase class."""

from narcotics_tracker.database import database


class TestDatabase:
    """Tests the behaviors of the Database Writer"""

    def test_writer_can_connect_to_database(self):
        """Tests that the writer can connect to the database"""

        db_writer = database.Database()

        db_writer.connect("test_database.db")

        assert db_writer.database_connection is not None

    def test_writer_can_create_table(self):
        """Tests that the writer can create a table.

        If the table already exists, it will be deleted and recreated."""

        table_name = "test_table"

        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

        db_writer = database.Database()
        db_writer.connect("test_database.db")
        tables = db_writer.read_database(sql_query)
        if "test_table" in tables:
            db_writer.delete_table("DROP TABLE IF EXISTS test_table")

        db_writer.create_table(
            ("""CREATE TABLE IF NOT EXISTS test_table (test_column TEXT)""")
        )

        tables = db_writer.read_database(sql_query)

        assert (table_name,) in tables

    def test_writer_can_delete_table(self):
        """Tests that the writer can delete a table.

        If the table does not exist, it will not be deleted."""

        sql_find_table = """SELECT name FROM sqlite_master WHERE type='table';"""
        sql_create_table = (
            """CREATE TABLE IF NOT EXISTS test_table (test_column TEXT)"""
        )

        db_writer = database.Database()
        db_writer.connect("test_database.db")

        tables = db_writer.read_database(sql_find_table)
        if "test_table" not in tables:
            db_writer.create_table(sql_create_table)

        db_writer.delete_table("DROP TABLE IF EXISTS test_table")

        tables = db_writer.read_database(sql_find_table)

        assert ("test_table",) not in tables
