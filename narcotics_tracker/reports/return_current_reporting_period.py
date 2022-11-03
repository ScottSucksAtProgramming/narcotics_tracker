"""Returns the current reporting period.

Classes:

"""
from typing import TYPE_CHECKING

from narcotics_tracker import commands
from narcotics_tracker.builders.reporting_period_builder import ReportingPeriodBuilder
from narcotics_tracker.reports.interfaces.report import Report
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.reporting_periods import ReportingPeriod
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class ReturnCurrentReportingPeriod(Report):
    """Returns the current reporting period."""

    _receiver = ServiceManager().persistence

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self) -> "ReportingPeriod":
        """Runs the report and returns the current Reporting Period."""
        period_data = self._retrieve_period_data()

        return self._build_period_from_data(period_data)

    def _retrieve_period_data(self) -> tuple:
        criteria = {"status": "OPEN"}
        order_by = "start_date"
        period_data = commands.ListReportingPeriods(self._receiver).execute(
            criteria, order_by
        )[-1]

        return period_data

    def _build_period_from_data(self, data: tuple[any]) -> "ReportingPeriod":
        period = (
            ReportingPeriodBuilder()
            .set_id(data[0])
            .set_start_date(data[1])
            .set_end_date(data[2])
            .set_status(data[3])
            .set_created_date(data[4])
            .set_modified_date(data[5])
            .set_modified_by(data[6])
            .build()
        )
        return period
