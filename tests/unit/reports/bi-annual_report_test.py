"""Contains the classes which unit tests the report."""
from narcotics_tracker import commands
from narcotics_tracker.reports.biannual_inventory import BiAnnualNarcoticsInventory
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class Test_BiAnnualNarcoticsInventory:
    """Unit tests the report.

    Behaviors Tested:
        -
    """

    def test_can_return_current_reporting_period(self, setup_integration_db) -> None:
        sq_man = SQLiteManager("integration_test.db")

        bi_annual_inventory = BiAnnualNarcoticsInventory(sq_man)
        result = bi_annual_inventory._get_current_reporting_period()
        assert result.id == 2200001

    def test_can_get_active_medications(self, setup_integration_db) -> None:
        sq_man = SQLiteManager("integration_test.db")
        bi_annual_inventory = BiAnnualNarcoticsInventory(sq_man)
        med_list = bi_annual_inventory._get_active_medications()

        assert (
            med_list[0].medication_code == "fentanyl"
            and med_list[1].medication_code == "midazolam"
            and med_list[2].medication_code == "morphine"
        )

    def test_can_add_initial_report_data(self, setup_integration_db) -> None:
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        report._medications = report._get_active_medications()

        report_dict = report._build_report_dictionary()

        expected_dict = {
            2200001: {
                "fentanyl": {
                    "concentration": 50.0,
                    "name": "Fentanyl",
                    "unit": "mcg",
                },
                "midazolam": {
                    "concentration": 5.0,
                    "name": "Midazolam",
                    "unit": "mg",
                },
                "morphine": {
                    "concentration": 10.0,
                    "name": "Morphine",
                    "unit": "mg",
                },
            }
        }

        assert report_dict == expected_dict

    def test_can_return_medication_starting_amount(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        fent_data = commands.ListMedications(sq_man).execute({"id": 1})[0]
        fentanyl = commands.LoadMedication().execute(fent_data)

        amount = report._get_last_periods_inventory(fentanyl)

        assert amount == 149
