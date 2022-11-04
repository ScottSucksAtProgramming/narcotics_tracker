"""Contains the classes which unit tests the report."""
from narcotics_tracker.reports.biannual_inventory import BiAnnualNarcoticsInventory
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class Test_BiAnnualNarcoticsInventory:
    """Unit tests the report.

    Behaviors Tested:
        -
    """

    def test_can_extract_reporting_period_id(self, setup_integration_db) -> None:
        sq_man = SQLiteManager("integration_test.db")

        bi_annual_inventory = BiAnnualNarcoticsInventory(sq_man)
        bi_annual_inventory._extract_reporting_period_id()
        assert bi_annual_inventory._period_id == 2200001
