"""Handles integration testing of the ReturnCurrentReportingPeriod Report.

Classes:
    Test_ReturnCurrentReportingPeriod: Integration tests the ReturnCurrentReportingPeriod 
        Report.
"""

from narcotics_tracker.items.reporting_periods import ReportingPeriod
from narcotics_tracker.reports.return_current_reporting_period import (
    ReturnCurrentReportingPeriod,
)
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class Test_ReturnCurrentReportingPeriod:
    """Integration tests the ReturnCurrentReportingPeriod Report.

    Behaviors Tested:
        - Report returns the current reporting period as an object.
        - Report returns correct ReportingPeriod.
    """

    def test_report_returns_ReportingPeriod_object(self, setup_integration_db) -> None:
        sq_man = SQLiteManager("integration_test.db")

        period = ReturnCurrentReportingPeriod(sq_man).execute()

        assert isinstance(period, ReportingPeriod)

    def test_report_returns_correct_ReportingPeriod(self, setup_integration_db) -> None:
        sq_man = SQLiteManager("integration_test.db")

        period = ReturnCurrentReportingPeriod(sq_man).execute()

        expected = "Reporting Period #2200001: Start Date: 07-23-2022 00:00:00, End Date: None, Current Status: OPEN."

        assert str(period) == expected
