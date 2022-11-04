"""Contains the BiAnnualNarcoticsInventory Report.

Classes:
"""
from typing import TYPE_CHECKING

from narcotics_tracker import commands, reports
from narcotics_tracker.reports.interfaces.report import Report
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class BiAnnualNarcoticsInventory(Report):
    """Returns information required for the Bi-Annual Narcotics Report."""

    _receiver = ServiceManager().persistence

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def _get_current_reporting_period(self) -> None:
        criteria = {"status": "OPEN"}
        data = commands.ListReportingPeriods(self._receiver).execute(criteria)[-1]
        self._period = commands.LoadReportingPeriod().execute(data)

    def _get_active_medications(self) -> None:
        medication_list = []
        criteria = {"status": "ACTIVE"}
        active_meds = commands.ListMedications(self._receiver).execute(
            criteria, "medication_code"
        )

        for med_data in active_meds:
            medication_list.append()
            med_info = {
                med_data[1]: {
                    "name": med_data[2],
                    "unit": med_data[4],
                    "concentration": med_data[6],
                }
            }

        return medication_list
