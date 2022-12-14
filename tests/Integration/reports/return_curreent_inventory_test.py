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

        results = ReturnCurrentInventory(sq_man).run()

        expected = [
            {
                "code": "fentanyl",
                "name": "Fentanyl",
                "unit": "mcg",
                "current_amount": 379000.0,
            },
            {
                "code": "midazolam",
                "name": "Midazolam",
                "unit": "mg",
                "current_amount": 28840000.0,
            },
            {
                "code": "morphine",
                "name": "Morphine",
                "unit": "mg",
                "current_amount": 25000000.0,
            },
        ]

        assert results == expected
