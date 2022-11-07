"""Defines the reporting period for medication tracking.

Classes:
    ReportingPeriod: A period of time for medication tracking.
"""
from dataclasses import dataclass

from narcotics_tracker.items.interfaces.dataitem_interface import DataItem
from narcotics_tracker.services.service_manager import ServiceManager


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

    def __str__(self) -> str:
        start_date = ServiceManager().datetime.convert_to_string(self.start_date)
        if self.end_date is not None:
            end_date = ServiceManager().datetime.convert_to_string(self.end_date)
        else:
            end_date = "None"
        return f"Reporting Period #{self.id}: Start Date: {start_date}, End Date: {end_date}, Current Status: {self.status}."
