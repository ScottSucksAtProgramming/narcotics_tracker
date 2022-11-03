"""Contains the classes which unit tests the report."""
from narcotics_tracker.reports.return_current_reporting_period import (
    ReturnCurrentReportingPeriod,
)
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class Test_NewReport:
    """Unit tests the report.

    Behaviors Tested:
        - Can return current reporting period data.
        - Can build reporting period from data.
    """

    def test_can_get_current_reporting_period(self, setup_integration_db):
        sq_man = SQLiteManager("integration_test.db")
        result = ReturnCurrentReportingPeriod(sq_man)._retrieve_period_data()

        assert result == (
            2200001,
            1658548800,
            None,
            "OPEN",
            1641013200,
            1641013200,
            "SRK",
        )

    def test_can_build_period_from_data(self, setup_integration_db):
        sq_man = SQLiteManager("integration_test.db")
        data = (
            2200001,
            1658548800,
            None,
            "OPEN",
            1641013200,
            1641013200,
            "SRK",
        )

        period = ReturnCurrentReportingPeriod(sq_man)._build_period_from_data(data)
        assert (
            str(period)
            == "Reporting Period #2200001: Start Date: 07-23-2022 00:00:00, End Date: None, Current Status: OPEN."
        )
