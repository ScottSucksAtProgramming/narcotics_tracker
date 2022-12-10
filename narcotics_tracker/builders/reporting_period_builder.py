"""Handles the defining and building of Reporting Period Objects.

Classes:

    ReportingPeriodBuilder: Assigns attributes and returns Reporting Period
        Objects.
"""
from typing import Optional

from narcotics_tracker.builders.dataitem_builder import DataItemBuilder
from narcotics_tracker.items.reporting_periods import ReportingPeriod
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes


class ReportingPeriodBuilder(DataItemBuilder):
    """Assigns attributes and returns Reporting Period Objects.

    This class inherits methods and attributes from the DataItemBuilder.
    Review the documentation for more information.

    Methods:

        build: Validates attributes and returns the ReportingPeriod Object.

        set_start_date: Sets the start date attribute to the passed integer.

        set_end_date: Sets the end date attribute to the passed integer.

        set_status: Sets the status attribute to the passed string.
    """

    _dataitem: ReportingPeriod = ReportingPeriod(
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
        """Validates attributes and returns the ReportingPeriod Object."""
        self._dataitem.start_date = self._service_provider.datetime.validate(
            self._dataitem.start_date
        )

        self._reset()
        return self._dataitem

    def set_start_date(
        self, date: Optional[NTTypes.date_types] = None
    ) -> "ReportingPeriodBuilder":
        """Sets the start date attribute to the passed value.

        Args:
            start_date (int): Unix timestamp of when the reporting period
                started.

        Returns:
            self: The instance of the builder.
        """
        if isinstance(date, str):
            date = ServiceManager().datetime.convert_to_timestamp(date)

        if date is None:
            raise ValueError("Must provide a start date.")

        self._dataitem.start_date = date
        return self

    def set_end_date(
        self, date: Optional[NTTypes.date_types] = None
    ) -> "ReportingPeriodBuilder":
        """Sets the end date attribute to the passed integer.

        Args:
            end_date (int): Unix timestamp of when the reporting period
                ended.

        Returns:
            self: The instance of the builder.
        """
        if isinstance(date, str):
            date = ServiceManager().datetime.convert_to_timestamp(date)

        self._dataitem.end_date = date
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
