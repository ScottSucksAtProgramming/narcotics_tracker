"""Contains the classes which test the ReturnMedicationStock Report.

Classes:
    Test_ReturnMedicationStock: Integration tests the ReturnMedicationStock 
        Report.
"""
from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.reports.return_medication_stock import ReturnMedicationStock
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class Test_ReturnMedicationStock:
    """Integration tests the ReturnMedicationStock Report.

    Behaviors Tested:
        - Returns correct results from SQLite3 database.
    """

    def test_report_returns_correct_results(self, setup_integration_db):
        sq_man = SQLiteManager("integration_test.db")
        med_builder = MedicationBuilder()
        med_builder.set_medication_code("fentanyl")
        med_builder.set_medication_name("Fentanyl")
        med_builder.set_fill_amount(2)
        med_builder.set_medication_amount(100)
        med_builder.set_preferred_unit("mcg")
        med_builder.set_concentration()
        med_builder.set_status("ACTIVE")
        med_builder.set_created_date(1)
        med_builder.set_modified_date(1)
        med_builder.set_modified_by("SRK")
        med = med_builder.build()
        current_fentanyl = ReturnMedicationStock(sq_man).set_medication(med).run()

        assert current_fentanyl == 379000.0
