"""Contains the concrete builder for the ReportingPeriod DataItems.

Classes:

    ReportingPeriodBuilder: Builds and returns an ReportingPeriod object.
"""


from narcotics_tracker.builders.dataitem_builder import DataItemBuilder
from narcotics_tracker.items.reporting_periods import ReportingPeriod


class ReportingPeriodBuilder(DataItemBuilder):
    """Builds and returns an ReportingPeriod Object.

    Methods:

        _reset: Prepares the builder to create a new ReportingPeriod.
        build: Returns the constructed ReportingPeriod.
        set_start_date: Sets the start date attribute to the passed integer.
        set_end_date: Sets the end date attribute to the passed integer.

    """

    _dataitem = ReportingPeriod(
        table="reporting_periods",
        id=None,
        created_date=None,
        modified_date=None,
        modified_by=None,
        start_date=None,
        end_date=None,
        status=None,
    )

    def _reset(self) -> None:
        """Prepares the builder to create a new ReportingPeriod."""
        self._dataitem = ReportingPeriod(
            table="reporting_periods",
            id=None,
            created_date=None,
            modified_date=None,
            modified_by=None,
            start_date=None,
            end_date=None,
            status=None,
        )

    def build(self) -> ReportingPeriod:
        """Returns the constructed ReportingPeriod."""
        reporting_period = self._dataitem
        self._reset()
        return reporting_period

    def set_start_date(self, start_date: int) -> "ReportingPeriodBuilder":
        """Sets the start date attribute to the passed integer.

        Args:
            start_date (int): Unix timestamp of when the reporting period
                started.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.start_date = start_date
        return self

    def set_end_date(self, end_date: int) -> "ReportingPeriodBuilder":
        """Sets the end date attribute to the passed integer.

        Args:
            end_date (int): Unix timestamp of when the reporting period
                ended.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.end_date = end_date
        return self

    def set_status(self, status: str) -> "ReportingPeriodBuilder":
        """Sets the status attribute to the passed string.

        Args:
            status (str): Status of the reporting period. Must match a
                status_code in the statuses table.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.status = status
        return self
