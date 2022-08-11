"""Contains tests for the setup module."""

import os

from narcotics_tracker import database, setup


class Test_SetupClass:
    def test_create_database_file(self):
        """Tests to see if the medication table can be created."""
        db = database.Database()
        db.connect("test_database.db")
        setup.create_medication_table(db)
        assert os.path.exists("data/test_database.db")

    def test_create_medication_table(self):
        """Tests to see if the medication table can be created."""
        db = database.Database()
        db.connect("test_database.db")

        setup.create_medication_table(db)

        data = db.read_data("SELECT * FROM sqlite_master WHERE type='table';")[0][4]

        assert (
            data
            != """medication (
                MEDICATION_ID INTEGER,
                NAME TEXT,
                CODE TEXT,
                CONTAINER_TYPE TEXT,
                FILL_AMOUNT REAL,
                DOSE REAL,
                UNIT TEXT,
                CONCENTRATION REAL,
                STATUS TEXT,
                CREATED_DATE TEXT,
                MODIFIED_DATE TEXT,
                MODIFIED_BY TEXT,
                PRIMARY KEY (CODE)
                )"""
        )
