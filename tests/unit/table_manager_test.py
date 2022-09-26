"""Handles testing of the table writer for the SQLite3 database."""

import pytest

from narcotics_tracker import table_manager


class Test_TableManager:
    """Tests the TableManager class.

    Behaviors Tested:
        - Tests that TableManager Class can be accessed.
        - Tests that TableManager Objects inherits from TableManager Class.
        - Tests that TableManager class has methods from its parent classes.
        - Tests that the TableManager can connect to the database.
        - Tests that TableManager sets the filename when initialized.
        - Tests that TableManager raises ValueError if given a bad filename.
        - Tests that the connect() method connects to the database file.
        - Tests that the disconnect() method closes the connection.
        - Tests that the filename can be changed using the setter method.
        - Tests that TableManger reconnects when changing the filename.
        - Tests that TableManager raises an exception if filename is invalid.
        - Tests that TableManager can create tables.
        - Tests that TableManager can return list of tables from the database.
        - Tests that TableManager can return list of columns from table.
        - Tests that read_columns() raises ValueError for bad table_name.
        - Tests that TableManager can verify a table exists.
        - Tests that TableManager can rename a table.
        - Tests that TableManager can add a column to a table.
        - Tests that TableManager can rename a column in a table.
        - Tests that TableManager can delete a table.
        - Tests that delete() raises ValueError if given a bad table_name.
    """

    def test_TableManager_class_exists(self):
        """Tests that TableManager Class can be accessed."""
        assert table_manager.TableManager.__doc__ != None

    def test_TableManager_class_inherits_from_table_manager_class(self) -> None:
        """Tests that TableManager Objects inherits from TableManager Class."""
        tm = table_manager.TableManager()

        assert isinstance(tm, table_manager.TableManager)

    def test_TableManager_class_has_expected_methods(self) -> None:
        """Tests that TableManager class has methods from its parent classes."""
        tm = table_manager.TableManager()

        expected_methods = [
            "__init__",
            "__enter__",
            "__exit__",
            "connect",
            "disconnect",
            "filename",
            "create",
            "read",
            "update",
            "delete",
        ]

        for method in expected_methods:
            assert hasattr(tm, method)

    def test_TableManager_can_connect_to_database_as_context_manager(self):
        """Tests that the TableManager can connect to the database."""
        with table_manager.TableManager("test_database.db") as tm:

            assert tm.connection != None

    def test_TableManager_sets_filename_correctly(self):
        """Tests that TableManager sets the filename when initialized."""
        with table_manager.TableManager("test_database.db") as tm:

            assert tm.filename == "test_database.db"

    def test_TableManager_returns_exception_with_bad_filename(self):
        """Tests that TableManager raises ValueError if given a bad filename."""

        with pytest.raises(ValueError):
            with table_manager.TableManager("test_database.exe") as tm:
                pass

    def test_connection_method_can_connect_to_database(self):
        """Tests that the connect() method connects to the database file."""
        tm = table_manager.TableManager("test_database.db")
        tm.connect()

        assert tm.connection != None

    def test_disconnect_method_closes_connection(self):
        """Tests that the disconnect() method closes the connection."""
        tm = table_manager.TableManager("test_database.db")
        tm.connect()
        tm.disconnect()

        assert tm.connection == None

    def test_filename_can_be_changed(self) -> None:
        """Tests that the filename can be changed using the setter method."""

        tm = table_manager.TableManager("test_database.db")
        tm.filename = "test_database_4.db"

        assert tm.filename == "test_database_4.db"

    def test_reconnects_when_changing_filename(self) -> None:
        """Tests that TableManger reconnects when changing the filename."""

        with table_manager.TableManager("test_database.db") as tm:
            original_connection = tm.connection

            tm.filename = "test_database_2.db"

            new_connection = tm.connection

            assert original_connection != new_connection

    def test_error_raised_if_filename_is_invalid(self) -> None:
        """Tests that TableManager raises an exception if filename is invalid."""

        tm = table_manager.TableManager("test_database.db")

        with pytest.raises(ValueError):
            tm.filename = "test_database.exe"

    def test_TableManager_can_create_tables(self, reset_database):
        """Tests that TableManager can create tables.

        Resets the test_database.db file. Creates test_table.

        Asserts that the test_table is exists in the database file.
        """
        with table_manager.TableManager("test_database.db") as tm:
            tm.create("""CREATE TABLE IF NOT EXISTS test_table (test_column TEXT)""")
            tables = tm.read()

        assert "test_table" in tables

    def test_TableManager_can_return_tables(self, reset_database):
        """Tests that TableManager can return list of tables from the database.

        Resets the test_database.db file. Creates 'test_table' and
        'test_table_2'.

        Asserts that both tables exist in the returned list.
        """
        with table_manager.TableManager("test_database.db") as tm:
            tm.create("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")
            tm.create("""CREATE TABLE IF NOT EXISTS test_table_2 (data TEXT)""")

            data = tm.read()

        assert "test_table" in data and "test_table_2" in data

    def test_TableManager_can_return_columns(self, reset_database):
        """Tests that TableManager can return list of columns from table.

        Creates a table with columns 'data' and 'number'. Gets list of
        columns.

        Asserts that the columns exist in list of column names.
        """
        with table_manager.TableManager("test_database.db") as tm:
            tm.create(
                """CREATE TABLE IF NOT EXISTS test_table (data TEXT, number INTEGER)"""
            )

            columns = tm.read_columns("test_table")

        assert "data" in columns and "number" in columns

    def test_read_columns_raises_ValueError_for_bad_table_names(self, reset_database):
        """Tests that read_columns() raises ValueError for bad table_name.

        Resets the database. Creates three tables with columns. Runs
        read_columns with a table name of "does_not_exist".

        Test passes if ValueError is raised.
        """
        with table_manager.TableManager("test_database.db") as tm:
            tm.create("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")
            tm.create("""CREATE TABLE IF NOT EXISTS test_table_2 (data TEXT)""")
            tm.create("""CREATE TABLE IF NOT EXISTS test_table_3 (data TEXT)""")

            with pytest.raises(ValueError):
                tm.read_columns("does not exist")

    def test_TableManager_can_verify_table_exists(self, reset_database) -> None:
        """Tests that TableManager can verify a table exists.

        Resets the database. Creates three tables. Runs _verify_table_exists()
        on the second table.

        Asserts that the returned boolean is True.
        """
        with table_manager.TableManager("test_database.db") as tm:
            tm.create("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")
            tm.create("""CREATE TABLE IF NOT EXISTS test_table_2 (data TEXT)""")
            tm.create("""CREATE TABLE IF NOT EXISTS test_table_3 (data TEXT)""")

            value = tm._verify_table_exists("test_table_2")

            assert value == True

    def test_TableManager_can_rename_table(self, reset_database):
        """Tests that TableManager can rename a table.

        Creates 'old_table'. Renames 'old_table' to 'new_table'.

        Asserts that 'new_table' is in the final list of tables and
        'old_table' is not.
        """
        with table_manager.TableManager("test_database.db") as tm:
            tm.create("""CREATE TABLE IF NOT EXISTS old_table (data TEXT)""")

            tm.update("""ALTER TABLE old_table RENAME TO new_table""")
            tables = tm.read()

        assert "new_table" in tables and "old_table" not in tables

    def test_TableManager_can_add_column_to_table(self, reset_database):
        """Tests that TableManager can add a column to a table.

        Creates a table, adds a column.

        Asserts that the column is returned in the list of columns.
        """
        with table_manager.TableManager("test_database.db") as tm:

            tm.create("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")

            tm.update("""ALTER TABLE test_table ADD COLUMN new_column REAL""")
            columns = tm.read_columns("test_table")

        assert "new_column" in columns

    def test_TableManager_can_rename_column_in_table(self, reset_database):
        """Tests that TableManager can rename a column in a table.

        Creates a table, adds a column, renames the column.

        Asserts that thew new column name is in the list and the old name is
        not.
        """
        with table_manager.TableManager("test_database.db") as tm:

            tm.create("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")

            tm.update("""ALTER TABLE test_table RENAME COLUMN data TO new_data""")

            columns = tm.read_columns("test_table")
        assert "new_data" in columns

    def test_TableManager_can_delete_table(self, reset_database):
        """Tests that TableManager can delete a table.

        Creates table if it doesn't already exist, then deletes it.

        Asserts that the table is not in the final list of tables."""
        with table_manager.TableManager("test_database.db") as tm:
            tm.create("""CREATE TABLE IF NOT EXISTS test_table (test_column TEXT)""")

            tm.delete("test_table")

            final_tables = tm.read()

        assert "test_table" not in final_tables

    def test_delete_raises_ValueError_when_bad_table_name_supplied(
        self, reset_database
    ):
        """Tests that delete() raises ValueError if given a bad table_name.

        Resets the database. Creates three tables with columns. Runs delete
        with a table name of "does_not_exist".

        Test passes if ValueError is raised.
        """
        with table_manager.TableManager("test_database.db") as tm:
            tm.create("""CREATE TABLE IF NOT EXISTS test_table (data TEXT)""")
            tm.create("""CREATE TABLE IF NOT EXISTS test_table_2 (data TEXT)""")
            tm.create("""CREATE TABLE IF NOT EXISTS test_table_3 (data TEXT)""")

            with pytest.raises(ValueError):
                tm.delete("does not exist")
