"""Returns the current stock for a single medication.

Classes:
    ReturnMedicationStock: Returns the current amount on hand for a specific
        medication.
"""
from typing import TYPE_CHECKING, Optional, Union

from narcotics_tracker import commands
from narcotics_tracker.reports.interfaces.report import Report
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class ReturnMedicationStock(Report):
    """Returns the current amount on hand for a specific medication."""

    _receiver = ServiceManager().persistence
    _medication_code: str

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def set_medication(self, med_code: str):
        """sets the target medication by its code."""
        self._medication_code = med_code

    def run(self) -> float:
        """Runs the report and returns the amount of the medication on hand.

        Args:
            med_code (str): The code of the medication.

        Results:
            float: Current stock of the medication in the standard unit.
        """
        amounts = self._return_adjustment_amounts()

        return sum(amounts)

    def _return_adjustment_amounts(
        self,
    ) -> list[Union[float, int]]:
        """Returns a list of all adjustment amounts for the specified med_code."""
        criteria: NTTypes.sqlite_types = {"medication_code": self._medication_code}
        adj_data: list[NTTypes.adjustment_data_type] = (
            commands.ListAdjustments(self._receiver).set_parameters(criteria).execute()
        )

        return self._extract_adjustment_amounts(adj_data)

    def _extract_adjustment_amounts(
        self, adjustments_list: list[NTTypes.adjustment_data_type]
    ):
        """Extracts amounts from a list of adjustment data. Returns as a list."""
        amounts_list: list[Union[int, float]] = []

        for adjustment in adjustments_list:
            amounts_list.append(adjustment[4])

        return amounts_list
