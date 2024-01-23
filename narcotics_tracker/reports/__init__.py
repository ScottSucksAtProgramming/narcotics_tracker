"""Contains the modules required to return reports regarding the inventory.

Reports:
    ReturnCurrentInventory: Returns the current stock for all active
        medications in the inventory.

    ReturnMedicationStock: Returns the current amount on hand for a specific
        medication.
"""
# pyright: reportUnusedImport=false
from narcotics_tracker.reports.biannual_inventory import BiAnnualNarcoticsInventory
from narcotics_tracker.reports.return_current_inventory import ReturnCurrentInventory
from narcotics_tracker.reports.return_medication_stock import ReturnMedicationStock
