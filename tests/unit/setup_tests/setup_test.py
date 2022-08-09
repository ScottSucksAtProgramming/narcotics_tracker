"""Contains tests for the setup module."""

import os

from narcotics_tracker.setup import setup
from narcotics_tracker.database import database


class TestSetup:
    def test_setup_creates_database_file(self):
        """Tests to see if the medication table can be created."""
        setup.create_medication_table()
        assert os.path.exists("narcotics_tracker/data/inventory.db")

    def test_setup_creates_medication_table(self):
        """Tests to see if the medication table can be created."""
        db = database.Database()
        db.connect("inventory.db")

        setup.create_medication_table()

        assert db.read_database("SELECT * FROM medication") == []
