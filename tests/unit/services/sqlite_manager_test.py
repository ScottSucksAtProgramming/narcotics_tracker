"""Contains classes to test the SQLite Manager Module.

Classes:

    Test_SQLiteManager: Tests the SQLiteManager class.

"""

import os

from narcotics_tracker.services.sqlite_manager import SQLiteManager


class Test_SQLiteManager:
    """Tests the SQLiteManager class.

    SQLiteManager Behaviors Tested:
        - Can be instantiated.
        - Can create a database file.
        - Can connect to a database.
        - Can delete database files.
        - Can create tables.
        - Can add data.
        - Can delete data.
        - Can order returned data.
        - Can update data.
    """

    def test_SQLiteManager_object_can_be_instantiated(self):
        db = SQLiteManager("test_database.db")

        assert isinstance(db, SQLiteManager)

    def test_SQLiteManager_can_create_database_file(self, reset_database):
        db = SQLiteManager("test.db")
        assert os.path.exists("data/test.db")
        db.delete_database()

    def test_SQLiteManager_can_connect_to_database(self, reset_database):
        db = SQLiteManager("test_database.db")
        assert db.connection is not None

    def test_SQLiteManager_can_delete_database_file(self, reset_database):
        db = SQLiteManager("test_database.db")
        db.delete_database()

        assert os.path.exists("data/test_database.db") == False

    def test_SQLiteManager_can_create_tables(self, reset_database):
        db = SQLiteManager("test_database.db")
        db.create_table("test_table", {"data": "TEXT NOT NULL"})

        db = SQLiteManager("test_database.db")
        cursor = db._execute("""SELECT name FROM sqlite_master WHERE type = 'table'""")
        table_name = cursor.fetchall()[0][0]

        assert table_name == "test_table"

    def test_SQLiteManager_can_add_data(self, reset_database):
        db = SQLiteManager("test_database.db")
        db.create_table("test_table", {"data": "TEXT"})

        db.add("test_table", {"data": "Hello"})

        cursor = db.read("test_table")
        data = cursor.fetchall()[0][0]

        assert data == "Hello"

    def test_SQLiteManager_can_delete_data(self, reset_database):
        db = SQLiteManager("test_database.db")
        db.create_table("test_table", {"data": "TEXT"})
        db.add("test_table", {"data": "Hello"})

        db.remove("test_table", {"data": "Hello"})

        cursor = db.read("test_table")
        data = cursor.fetchall()

        assert data == []

    def test_SQLiteManager_can_order_returned_data(self, reset_database):
        db = SQLiteManager("test_database.db")
        db.create_table("test_table", {"number": "INTEGER"})
        db.add("test_table", {"number": "17"})
        db.add("test_table", {"number": "1"})
        db.add("test_table", {"number": "99999999"})
        db.add("test_table", {"number": "8211986"})

        cursor = db.read("test_table", order_by="number")
        data = cursor.fetchall()

        assert data == [(1,), (17,), (8211986,), (99999999,)]

    def test_SQLiteManager_can_update_data(self, reset_database):
        db = SQLiteManager("test_database.db")
        db.create_table("test_table", {"number": "INTEGER", "word": "TEXT"})
        db.add("test_table", {"number": 17, "word": "Cow"})

        db.update("test_table", {"number": 7, "word": "Pig"}, {"number": 17})

        cursor = db.read("test_table")
        results = cursor.fetchall()
        assert results == [(7, "Pig")]
