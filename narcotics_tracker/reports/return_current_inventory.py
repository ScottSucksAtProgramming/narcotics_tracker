"""Returns the current stock for all active medications.

Classes:
    ReturnCurrentInventory: Returns the current stock for all active
        medications in the inventory.

"""
from typing import TYPE_CHECKING, Optional

from narcotics_tracker import commands, reports
from narcotics_tracker.reports.interfaces.report import Report
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes, SQLiteDict

if TYPE_CHECKING:
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.services.interfaces.conversion import ConversionService
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class ReturnCurrentInventory(Report):
    """Returns the current stock for all active medications in the inventory.

    report = [
        {
            code: "fentanyl",
            name: "Fentanyl",
            unit: "mcg",
            "adjustments": [1, 2, 123.21],
            current_amount: 200
         }
    ]


    Step 1: Get List of Medications.
    Step 2: Add Medication data to Report
    Step 3: Retrieve Adjustments for each medication add to report.
    Step 4: Calculate Sum of Adjustments, add to report.
    """

    _active_medications: list["Medication"] = []
    _report: NTTypes.report_data = []
    _receiver: "PersistenceService" = ServiceManager().persistence
    _converter: "ConversionService" = ServiceManager().conversion

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
        """Resets the Report."""
        self._report = []
        self._active_medications = []

    def run(self) -> NTTypes.report_data:
        """Runs Report. Returns results as a list of dictionaries.

        Returns:
            list[dict]: List of dictionaries each mapping the medications
                name, code, preferred unit and current total stock (in the
                preferred unit).
        """
        # Step 1: Retrieve Active Medications - Store as variable.
        self._active_medications = self._retrieve_medications()

        # Step 2: Add Medication Data to Report.
        self._add_medication_data_to_report()

        # Step 3: Retrieve Adjustments for each medication add to report.
        for medication in self._active_medications:
            result = self._calculate_stock(medication)

            self._add_current_amount_to_report(result, medication)

        # list_with_amounts = self._add_amounts(medication_list)

        # return self._convert_amounts_to_preferred(list_with_amounts)

        return self._report

    def _retrieve_medications(self) -> list["Medication"]:
        """Returns the code, name, and unit for all active medications."""
        criteria: SQLiteDict = {"status": "ACTIVE"}
        return (
            commands.ListMedications(self._receiver)
            .set_parameters(criteria, "id")
            .execute()
        )

    def _add_medication_data_to_report(self) -> None:
        """Extracts pertinent data from Active Medications adds to report."""
        for medication in self._active_medications:
            med_info = {
                "code": medication.medication_code,
                "name": medication.medication_name,
                "unit": medication.preferred_unit,
            }
            self._report.append(med_info)

    def _add_current_amount_to_report(
        self, adjustment_list: float, medication: "Medication"
    ) -> None:
        """Adds a list of adjustments to the report dictionary."""
        for entry in self._report:
            if entry["code"] == medication.medication_code:
                entry["current_amount"] = adjustment_list

    def _calculate_stock(self, medication: "Medication") -> float:
        """Adds current amounts for each medication in the list and returns it."""
        stock_report = reports.ReturnMedicationStock(self._receiver)
        stock_report.set_medication(medication)
        return stock_report.run()
