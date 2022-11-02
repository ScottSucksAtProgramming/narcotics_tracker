"""Contains the classes which test the ReturnMedicationStock Report.

Classes:
    Test_ReturnMedicationStock: Integration tests the ReturnMedicationStock 
        Report.
"""
from narcotics_tracker.reports.return_medication_stock import ReturnMedicationStock
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class Test_ReturnMedicationStock:
    """Integration tests the ReturnMedicationStock Report.

    Behaviors Tested:
        - Returns correct results from SQLite3 database.
    """

    def test_report_returns_correct_results(self, setup_integration_db):
        sq_man = SQLiteManager("integration_test.db")

        current_fentanyl = ReturnMedicationStock(sq_man).execute("fentanyl")

        assert current_fentanyl == 19000
