"""Contains the BiAnnualNarcoticsInventory Report.

Classes:
"""
from typing import TYPE_CHECKING, Any, Optional, Union

from narcotics_tracker import commands
from narcotics_tracker.reports.interfaces.report import Report
from narcotics_tracker.services.interfaces.conversion import ConversionService
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.items.reporting_periods import ReportingPeriod
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class BiAnnualNarcoticsInventory(Report):
    """Returns information required for the Bi-Annual Narcotics Report."""

    _receiver = ServiceManager().persistence
    _converter = ServiceManager().conversion
    _period: "ReportingPeriod"
    _medications: list["Medication"]
    _report: dict[Any, Any]

    def __init__(
        self,
        receiver: Optional["PersistenceService"] = None,
        converter: Optional["ConversionService"] = None,
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

    def run(self) -> dict[str, int]:
        self._period = self._get_current_reporting_period()
        self._medications = self._get_active_medications()
        self._report = self._build_report_dictionary(self._medications)

        for medication in self._medications:
            starting_amount = self._get_starting_amount(medication)
            self._report[self._period.id][medication.medication_code][
                "starting_amount"
            ] = starting_amount

        for medication in self._medications:
            amount_received = self._get_amount_received(medication)
            self._report[self._period.id][medication.medication_code][
                "amount_received"
            ] = amount_received

        for medication in self._medications:
            amount_used = self._get_amount_used(medication)
            self._report[self._period.id][medication.medication_code][
                "amount_used"
            ] = amount_used

        for medication in self._medications:
            amount_wasted = self._get_amount_wasted(medication)
            self._report[self._period.id][medication.medication_code][
                "amount_wasted"
            ] = amount_wasted

        for medication in self._medications:
            amount_destroyed = self._get_amount_destroyed(medication)
            self._report[self._period.id][medication.medication_code][
                "amount_destroyed"
            ] = amount_destroyed

        for medication in self._medications:
            amount_lost = self._get_amount_lost(medication)
            self._report[self._period.id][medication.medication_code][
                "amount_lost"
            ] = amount_lost

        for medication in self._medications:
            ending_amount = self._calculate_total_ending_amount(medication)
            self._report[self._period.id][medication.medication_code][
                "ending_amount"
            ] = ending_amount

        return self._report

    def _get_current_reporting_period(self) -> "ReportingPeriod":
        criteria = {"status": "OPEN"}
        data = (
            commands.ListReportingPeriods(self._receiver)
            .set_parameters(criteria)
            .execute()[-1]
        )

        return commands.LoadReportingPeriod().set_data(data).execute()

    def _get_active_medications(self) -> list["Medication"]:
        medication_list: list["Medication"] = []
        criteria = {"status": "ACTIVE"}
        order = "medication_code"

        medication_list = (
            commands.ListMedications(self._receiver)
            .set_parameters(criteria, order)
            .execute()
        )

        return medication_list

    def _build_report_dictionary(self, med_list: list["Medication"]) -> dict[Any, Any]:
        period_id = self._period.id
        report: dict[Any, Any] = {period_id: {}}

        for medication in med_list:
            report[period_id][medication.medication_code] = {
                "name": medication.medication_name,
                "unit": medication.preferred_unit,
                "concentration": medication.concentration,
            }

        return report

    def _get_starting_amount(self, medication: "Medication") -> Union[float, int]:
        """Returns the amount in milliliters."""
        adjustment: "Adjustment"
        criteria = {
            "event_code": "IMPORT",
            "medication_code": medication.medication_code,
            "reporting_period_id": self._period.id,
        }

        adjustment = (
            commands.ListAdjustments(self._receiver)
            .set_parameters(criteria)
            .execute()[0]
        )
        raw_amt: Union[float, int] = adjustment.amount if adjustment.amount else 0

        return self._converter.to_milliliters(
            raw_amt,
            medication.preferred_unit,
            medication.concentration,
        )

    def _get_amount_received(self, medication: "Medication") -> float:
        """Returns the total amount of medication ordered in ml."""
        criteria = {
            "event_code": "ORDER",
            "medication_code": medication.medication_code,
            "reporting_period_id": self._period.id,
        }
        adj_list = (
            commands.ListAdjustments(self._receiver).set_parameters(criteria).execute()
        )
        if not adj_list:
            return 0

        amounts = self._extract_amounts(adj_list)

        return self._converter.to_milliliters(
            amounts,
            medication.preferred_unit,
            medication.concentration,
        )

    def _get_amount_used(self, medication: "Medication") -> float:
        """Returns the total amount of medication used in ml."""
        criteria = {
            "event_code": "USE",
            "medication_code": medication.medication_code,
            "reporting_period_id": self._period.id,
        }
        adj_list = (
            commands.ListAdjustments(self._receiver).set_parameters(criteria).execute()
        )

        if not adj_list:
            return 0

        amounts = self._extract_amounts(adj_list)
        raw_amt = sum(amounts) * -1

        return self._converter.to_milliliters(
            raw_amt,
            medication.preferred_unit,
            medication.concentration,
        )

    def _get_amount_wasted(self, medication: "Medication") -> float:
        """Returns the total amount of medication wasted in ml."""
        criteria = {
            "event_code": "WASTE",
            "medication_code": medication.medication_code,
            "reporting_period_id": self._period.id,
        }
        adj_list = (
            commands.ListAdjustments(self._receiver).set_parameters(criteria).execute()
        )

        if not adj_list:
            return 0

        amounts = self._extract_amounts(adj_list)
        raw_amt = sum(amounts) * -1

        return self._converter.to_milliliters(
            raw_amt,
            medication.preferred_unit,
            medication.concentration,
        )

    def _get_amount_destroyed(self, medication: "Medication") -> float:
        """Returns the total amount of medication destroyed in ml."""
        criteria = {
            "event_code": "DESTROY",
            "medication_code": medication.medication_code,
            "reporting_period_id": self._period.id,
        }
        adj_list = (
            commands.ListAdjustments(self._receiver).set_parameters(criteria).execute()
        )

        if not adj_list:
            return 0

        amounts = self._extract_amounts(adj_list)
        raw_amt = sum(amounts) * -1

        return self._converter.to_milliliters(
            raw_amt,
            medication.preferred_unit,
            medication.concentration,
        )

    def _get_amount_lost(self, medication: "Medication") -> float:
        """Returns the total amount of medication lost in ml."""
        criteria = {
            "event_code": "LOSS",
            "medication_code": medication.medication_code,
            "reporting_period_id": self._period.id,
        }
        adj_list = (
            commands.ListAdjustments(self._receiver).set_parameters(criteria).execute()
        )

        if not adj_list:
            return 0

        amounts = self._extract_amounts(adj_list)
        raw_amt = sum(amounts) * -1

        return self._converter.to_milliliters(
            raw_amt,
            medication.preferred_unit,
            medication.concentration,
        )

    def _extract_amounts(
        self, adjustment_list: list["Adjustment"]
    ) -> list[Union[int, float]]:
        amounts: list[Union[int, float]] = []
        for adjustment in adjustment_list:
            if adjustment.amount is not None:
                amounts.append(adjustment.amount)

        return amounts

    def _calculate_total_ending_amount(self, medication: "Medication") -> Optional[int]:
        code = medication.medication_code
        starting = self._report[self._period.id][code]["starting_amount"]
        received = self._report[self._period.id][code]["amount_received"]
        used = self._report[self._period.id][code]["amount_used"]
        wasted = self._report[self._period.id][code]["amount_wasted"]
        destroyed = self._report[self._period.id][code]["amount_destroyed"]
        lost = self._report[self._period.id][code]["amount_lost"]

        ending_amount: int = starting
        ending_amount += received
        ending_amount -= used
        ending_amount -= wasted
        ending_amount -= destroyed
        ending_amount -= lost
        ending_amount = round(ending_amount, 2)

        return ending_amount
