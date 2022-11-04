"""Contains the BiAnnualNarcoticsInventory Report.

Classes:
"""
from typing import TYPE_CHECKING

from narcotics_tracker import commands, reports
from narcotics_tracker.reports.interfaces.report import Report
from narcotics_tracker.services.interfaces.conversion import ConversionService
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.items.reporting_periods import ReportingPeriod
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class BiAnnualNarcoticsInventory(Report):
    """Returns information required for the Bi-Annual Narcotics Report."""

    _receiver = ServiceManager().persistence
    _converter = ServiceManager().conversion

    def __init__(
        self,
        receiver: "PersistenceService" = None,
        converter: "ConversionService" = None,
    ) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.

            converter(ConversionService, optional): Service which converts
                medication amounts. Defaults to ConverterManager.
        """
        if receiver:
            self._receiver = receiver
        if converter:
            self._converter = converter

    def execute(self) -> dict[str, int]:
        self._period = self._get_current_reporting_period()
        self._medications = self._get_active_medications()
        self._report = self._build_report_dictionary()

    def _get_current_reporting_period(self) -> "ReportingPeriod":
        criteria = {"status": "OPEN"}
        data = commands.ListReportingPeriods(self._receiver).execute(criteria)[-1]

        return commands.LoadReportingPeriod().execute(data)

    def _get_active_medications(self) -> list["Medication"]:
        medication_list = []
        criteria = {"status": "ACTIVE"}
        order = "medication_code"

        active_meds = commands.ListMedications(self._receiver).execute(criteria, order)

        for med_data in active_meds:
            medication = commands.LoadMedication().execute(med_data)
            medication_list.append(medication)

        return medication_list

    def _build_report_dictionary(self) -> dict[dict]:
        period_id = self._period.id
        report = {period_id: {}}

        for medication in self._medications:
            report[period_id][medication.medication_code] = {
                "name": medication.medication_name,
                "unit": medication.preferred_unit,
                "concentration": medication.concentration,
            }

        return report

    def _get_last_periods_inventory(self, medication: "Medication") -> int:
        criteria = {
            "event_code": "IMPORT",
            "medication_code": medication.medication_code,
        }
        raw_amt = commands.ListAdjustments(self._receiver).execute(criteria)[0][4]

        return self._converter.to_milliliters(
            raw_amt,
            medication.preferred_unit,
            medication.concentration,
        )


0
