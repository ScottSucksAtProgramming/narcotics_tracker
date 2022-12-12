"""Returns the current stock for all active medications.

Classes:
    ReturnCurrentInventory: Returns the current stock for all active
        medications in the inventory.

"""
from typing import TYPE_CHECKING, Any, Optional

from narcotics_tracker import commands, reports
from narcotics_tracker.reports.interfaces.report import Report
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class ReturnCurrentInventory(Report):
    """Returns the current stock for all active medications in the inventory."""

    _receiver = ServiceManager().persistence
    _converter = ServiceManager().conversion

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def run(self) -> list[dict[Any, Any]]:
        """Runs Report. Returns results as a list of dictionaries.

        Returns:
            list[dict]: List of dictionaries each mapping the medications
                name, code, preferred unit and current total stock (in the
                preferred unit).
        """
        medication_list = self._retrieve_medications()
        list_with_amounts = self._add_amounts(medication_list)

        return self._convert_amounts_to_preferred(list_with_amounts)

    def _retrieve_medications(self) -> list[dict[str, str]]:
        """Returns the code, name, and unit for all active medications."""
        medication_list: list[dict[str, str]] = []
        criteria: NTTypes.sqlite_types = {"status": "ACTIVE"}
        active_meds = (
            commands.ListMedications(self._receiver)
            .set_parameters(criteria, "id")
            .execute()
        )

        for med_data in active_meds:
            med_info = {"code": med_data[1], "name": med_data[2], "unit": med_data[4]}
            medication_list.append(med_info)

        return medication_list

    def _add_amounts(
        self, medication_info: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """Adds current amounts for each medication in the list and returns it."""
        other_report: "Report" = reports.ReturnMedicationStock(self._receiver)

        for med in medication_info:
            other_report.set_medication(med["code"])
            amount = other_report.run()
            med["amount"] = amount

        return medication_info

    def _convert_amounts_to_preferred(
        self, medication_info: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """Converts amount for each med to preferred unit and returns the list.

        Note: Amounts are rounded to two decimal places.
        """
        for med in medication_info:
            converted_amount = self._converter.to_preferred(med["amount"], med["unit"])
            med["amount"] = round(converted_amount, 2)

        return medication_info
