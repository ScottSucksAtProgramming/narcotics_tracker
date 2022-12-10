"""Scripts to run Current Inventory Report. For demo purposes."""

import os
from typing import Any

from narcotics_tracker import reports


def main():
    """Main Function."""
    os.system("clear")
    totals = reports.ReturnCurrentInventory().run()

    strings = _make_strings(totals)

    print("Current Wantagh-Levittown VAC Narcotics Inventory:")
    print("--------------------------------------------------")
    for string in strings:
        print(string)


def _make_strings(db_totals: list[dict[str, Any]]) -> list[str]:
    strings: list[str] = []

    for item in db_totals:
        string = f"{item['name']}: {item['amount']} {item['unit']}"
        strings.append(string)

    return strings


if __name__ == "__main__":
    main()
