"""Contains the unit tests for the ReportingPeriodBuilder.

Classes:
    Test_ReportingPeriodBuilder: Unit tests the ReportingPeriodBuilder.
"""


from narcotics_tracker.builders.reporting_period_builder import ReportingPeriodBuilder
from narcotics_tracker.items.reporting_periods import ReportingPeriod


class Test_ReportingPeriodBuilder:
    """Unit tests the ReportingPeriodBuilder.

    Behaviors Tested:
        - Can be accessed.
        - Returns a ReportingPeriod Object.
        - Returned object has expected attribute values.
    """

    def test_ReportingPeriodBuilder_can_be_accessed(self) -> None:
        assert ReportingPeriodBuilder.__doc__ != None

    def test_returned_object_is_an_reporting_period(
        self, test_reporting_period
    ) -> None:
        assert isinstance(test_reporting_period, ReportingPeriod)

    def test_returned_object_had_expected_attributes(
        self, test_reporting_period
    ) -> None:
        assert vars(test_reporting_period) == {
            "table": "reporting_periods",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "System",
            "start_date": 1666061200,
            "end_date": 1666061200,
            "status": "BROKEN",
        }
