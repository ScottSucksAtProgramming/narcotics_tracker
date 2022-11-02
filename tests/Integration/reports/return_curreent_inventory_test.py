"""Handles integration testing of the ReturnCurrentInventory Report.

Classes:
    Test_ReturnCurrentInventory: Integration tests the ReturnCurrentInventory 
        Report.
"""

from narcotics_tracker.reports.return_current_inventory import ReturnCurrentInventory
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class Test_ReturnCurrentInventory:
    """Integration tests the ReturnCurrentInventory Report.

    Behaviors Tested:
        - Report returns correct results from database.
    """

    def test_report_returns_correct_results(self, setup_integration_db) -> None:
        sq_man = SQLiteManager("integration_test.db")

        results = ReturnCurrentInventory(sq_man).execute()

        expected = [
            {"code": "fentanyl", "name": "Fentanyl", "unit": "mcg", "amount": 190},
            {"code": "midazolam", "name": "Midazolam", "unit": "mg", "amount": 288.4},
            {"code": "morphine", "name": "Morphine", "unit": "mg", "amount": 250},
        ]

        assert results == expected
