"""Returns the current stock for a single medication.

Classes:
    ReturnMedicationStock: Returns the current amount on hand for a specific
        medication.
"""
from typing import TYPE_CHECKING, Optional, Union

from narcotics_tracker import commands
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.items.medications import Medication
from narcotics_tracker.reports.interfaces.report import Report
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class ReturnMedicationStock(Report):
    """Returns the current amount on hand for a specific medication."""

    _receiver = ServiceManager().persistence
    _medication: "Medication"

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        self._reset()

    def _reset(self) -> None:
        """Resets the report to be run again."""
        self._medication = Medication(
            table=None,
            id=None,
            created_date=None,
            modified_by=None,
            modified_date=None,
            medication_amount=None,
            medication_code=None,
            medication_name=None,
            fill_amount=None,
            concentration=None,
            preferred_unit=None,
            status=None,
        )

    def set_medication(self, medication: "Medication") -> "Report":
        """sets the target medication by its code."""
        self._medication = medication
        return self

    def run(self) -> float:
        """Runs the report and returns the amount of the medication on hand.

        Args:
            med_code (str): The code of the medication.

        Results:
            float: Current stock of the medication in the standard unit.
        """
        amounts = self._return_adjustment_amounts(self._medication)
        result = sum(amounts)
        self._reset()

        return result

    def _return_adjustment_amounts(
        self, medication: "Medication"
    ) -> list[Union[float, int]]:
        """Returns a list of all adjustment amounts for the specified med_code."""
        medication_code = medication.medication_code

        if medication_code is None:
            raise ValueError

        criteria: NTTypes.sqlite_types = {"medication_code": medication_code}
        adjustment_list = (
            commands.ListAdjustments(self._receiver)
            .set_parameters(criteria=criteria)
            .execute()
        )
        print(adjustment_list)

        return self._extract_adjustment_amounts(adjustment_list)

    def _extract_adjustment_amounts(self, adjustments_list: list["Adjustment"]):
        """Extracts amounts from a list of adjustment data. Returns as a list."""
        amounts_list: list[Union[int, float]] = []

        for adjustment in adjustments_list:
            if adjustment.amount is not None:
                amounts_list.append(adjustment.amount)

        return amounts_list
