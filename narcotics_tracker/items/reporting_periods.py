"""Defines the reporting period for medication tracking.

Classes:
    ReportingPeriod: A period of time for medication tracking.
"""

from dataclasses import dataclass

from narcotics_tracker.items.data_items import DataItem


@dataclass
class ReportingPeriod(DataItem):
    """A period of time for medication tracking.

    Attributes:
        start_date (int): Unix timestamp of when the reporting period opened.
        end_date (int): Unix timestamp of when the reporting period closed.
        status (str): Status of the reporting period.

    """

    start_date: int
    end_date: int
    status: str

    def __str__(self):
        return f"Reporting Period #{self.id}: Start Date: {self.start_date}, End Date: {self.end_date}, Current Status: {self.status}."
