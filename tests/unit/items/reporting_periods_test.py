"""Unit tests the Reporting Periods Module.

Classes:

    Test_ReportingPeriod: Unit tests the ReportingPeriod Class.
"""

from narcotics_tracker.items.reporting_periods import ReportingPeriod


class Test_ReportingPeriod:
    """Unit tests the ReportingPeriod Class.

    Behaviors Tested:
        - ReportingPeriods class can be accessed.
        - ReportingPeriods return expected id.
        - ReportingPeriods return expected start_date.
        - ReportingPeriods return expected end_date.
        - ReportingPeriods return expected status.
        - ReportingPeriods return expected string.
        - ReportingPeriods return expected dictionary.
    """

    test_period = ReportingPeriod(
        table="reporting_periods",
        id=-1,
        start_date=1666061200,
        end_date=1666061200,
        status="unfinished",
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="SRK",
    )

    def test_reportingperiod_class_can_be_accessed(self) -> None:
        assert ReportingPeriod.__doc__ != None

    def test_period_returns_expected_id(self) -> None:
        assert self.test_period.id == -1

    def test_period_returns_expected_start_date(self) -> None:
        assert self.test_period.start_date == 1666061200

    def test_period_returns_expected_end_date(self) -> None:
        assert self.test_period.end_date == 1666061200

    def test_period_returns_expected_status(self) -> None:
        self.test_period.status == "unfinished"

    def test_periods_return_expected_string(self) -> None:
        assert (
            str(self.test_period)
            == "Reporting Period #-1: Start Date: 1666061200, End Date: 1666061200, Current Status: unfinished."
        )

    def test_periods_return_expected_dictionary(self) -> None:
        assert vars(self.test_period) == {
            "table": "reporting_periods",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "SRK",
            "start_date": 1666061200,
            "end_date": 1666061200,
            "status": "unfinished",
        }
