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

    test_reporting_period = (
        ReportingPeriodBuilder()
        .set_table("reporting_periods")
        .set_id(-1)
        .set_created_date(1666061200)
        .set_modified_date(1666061200)
        .set_modified_by("SRK")
        .set_start_date(1666061200)
        .set_end_date(1666061200)
        .set_status("unfinished")
        .build()
    )

    def test_ReportingPeriodBuilder_can_be_accessed(self) -> None:
        assert ReportingPeriodBuilder.__doc__ != None

    def test_returned_object_is_an_reporting_period(self) -> None:
        assert isinstance(self.test_reporting_period, ReportingPeriod)

    def test_returned_object_had_expected_attributes(self) -> None:
        assert vars(self.test_reporting_period) == {
            "table": "reporting_periods",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "SRK",
            "start_date": 1666061200,
            "end_date": 1666061200,
            "status": "unfinished",
        }
