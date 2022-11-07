"""Scripts to run Current Inventory Report. For demo purposes."""

import os

from narcotics_tracker import reports


def main():
    os.system("clear")
    totals = reports.ReturnCurrentInventory().execute()

    strings = _make_strings(totals)

    print("Current Wantagh-Levittown VAC Narcotics Inventory:")
    print("--------------------------------------------------")
    for string in strings:
        print(string)


def _make_strings(db_totals: list[dict]) -> list[str]:
    strings = []

    for item in db_totals:
        string = f"{item['name']}: {item['amount']} {item['unit']}"
        strings.append(string)

    return strings


if __name__ == "__main__":
    main()
