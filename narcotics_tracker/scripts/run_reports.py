"""Scripts to run Current Inventory Report. For demo purposes."""

import os
from typing import Any

from narcotics_tracker import reports
from narcotics_tracker.services.sqlite_manager import SQLiteManager


def main():
    """
    The main function clears the console, retrieves the current inventory using reports.ReturnCurrentInventory().run(),
    converts the inventory data to strings, and then prints the Wantagh-Levittown VAC Narcotics Inventory.
    """
    os.system("clear")
    totals = reports.ReturnCurrentInventory().run()

    strings = _make_strings(totals)

    print("Current Wantagh-Levittown VAC Narcotics Inventory:")
    print("--------------------------------------------------")
    for string in strings:
        print(string)


def _make_strings(db_totals: list[dict[str, Any]]) -> list[str]:
    """
    Generate a list of strings based on the input list of dictionaries.

    :param db_totals: A list of dictionaries containing 'name', 'amount', and 'unit' keys.
    :return: A list of strings created from the input dictionaries.
    """
    strings: list[str] = []

    for item in db_totals:
        string = f"{item['name']}: {item['current_amount']} {item['unit']}"
        strings.append(string)

    return strings


if __name__ == "__main__":
    main()
