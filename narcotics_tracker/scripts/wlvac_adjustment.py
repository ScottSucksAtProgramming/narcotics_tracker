"""Adds all inventory adjustments to the WLVAC Inventory."""

from typing import TYPE_CHECKING, Any

from narcotics_tracker import commands
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment


def main() -> None:
    """Main Function"""

    adjustment_data = return_adjustments_data()

    adjustment_list = construct_adjustments(adjustment_data)

    for adjustment in adjustment_list:
        message = commands.AddAdjustment().set_adjustment(adjustment).execute()
        print(message)


def construct_adjustments(data: list[Any]) -> list["Adjustment"]:
    """Constructs adjustments returns in a list."""
    adjustment_list: list["Adjustment"] = []
    for data_set in data:
        adjustment_builder = AdjustmentBuilder()
        adjustment_builder.set_table("inventory")
        adjustment_builder.set_id(data_set[0])
        adjustment_builder.set_created_date()
        adjustment_builder.set_modified_date()
        adjustment_builder.set_modified_by("SRK")
        adjustment_builder.set_adjustment_date(data_set[1])
        adjustment_builder.set_event_code(data_set[2])
        adjustment_builder.set_medication_code(data_set[3])
        adjustment_builder.set_adjustment_amount(data_set[4])
        adjustment_builder.set_reporting_period_id(data_set[5])
        adjustment_builder.set_reference_id(data_set[6])
        adjustment = adjustment_builder.build()

        adjustment_list.append(adjustment)

    return adjustment_list


def return_adjustments_data() -> list[list[Any]]:
    """Returns data to build adjustments in a list."""
    return [
        # [
        #     None,
        #     "07-05-2023 00:00:00",
        #     "IMPORT",
        #     "fentanyl",
        #     304,
        #     2300001,
        #     "BiAnnual Narcotics Report - June 2023 - Wantagh-Levittown VAC - Final",
        # ],
        # [
        #     None,
        #     "07-05-2023 00:00:00",
        #     "IMPORT",
        #     "midazolam",
        #     273.4,
        #     2300001,
        #     "BiAnnual Narcotics Report - June 2023 - Wantagh-Levittown VAC - Final",
        # ],
        [
            None,
            "07-05-2023 00:00:00",
            "IMPORT",
            "morphine",
            230,
            2300001,
            "BiAnnual Narcotics Report - June 2023 - Wantagh-Levittown VAC - Final",
        ],
        # [None, "07-05-2023 00:00:00", "ORDER", "midazolam", 100, 2300001, "ORDER# 2023-001"],
        # [None, "07-19-2023 00:00:00", "DESTROY", "fentanyl", 14, 2300001, "RXRD# 23070500210831524"],
        [None, "07-19-2023 00:00:00", "DESTROY", "morphine", 20, 2300001, "RXRD# 23070500210831524"],
        # [None, "07-19-2023 00:00:00", "DESTROY", "midazolam", 133.4, 2300001, "RXRD# 23070500210831524"],
        [None, "09-04-2023 00:00:00", "USE", "morphine", .005, 2300001, "PCR# 230904-0114-WLVAC"],
        # [None, "09-06-2023 00:00:00", "USE", "fentanyl", 50, 2300001, "PCR# 230906-1519-WLVAC"],
        # [None, "09-16-2023 00:00:00", "USE", "midazolam", 5, 2300001, "PCR# 230916-2201-WLVAC"],
        # [None, "09-21-2023 00:00:00", "USE", "midazolam", 5, 2300001, "PCR# 230921-0135-WLVAC"],
        # [None, "09-21-2023 00:00:00", "ORDER", "midazolam", 150, 2300001, "ORDER# 2023-002"],
        # [None, "10-02-2023 00:00:00", "USE", "fentanyl", 100, 2300001, "PCR# 231002-0547-WLVAC"],
        # [None, "10-08-2023 00:00:00", "USE", "fentanyl", 100, 2300001, "PCR# 231008-1816-WLVAC"],
        [None, "10-11-2023 00:00:00", "USE", "morphine", .005, 2300001, "PCR# 231011-0120-WLVAC"],
        [None, "10-20-2023 00:00:00", "USE", "morphine", .003, 2300001, "PCR# 231020-2315-WLVAC"],
        # [None, "10-25-2023 00:00:00", "ORDER", "midazolam", 200, 2300001, "ORDER# 2023-001"],
        # [None, "11-14-2023 00:00:00", "USE", "fentanyl", 50, 2300001, "PCR# 231114-0140-WLVAC"],
        # [None, "12-06-2023 00:00:00", "USE", "fentanyl", 50, 2300001, "PCR# 231206-1827-WLVAC"],
        # [None, "01-04-2024 00:00:00", "USE", "midazolam", 5, 2300001, "PCR# 240104-2043-WLVAC"],
        # # DESTRUCTIONS
        # # ORDERS
        
        
        

    ]


if __name__ == "__main__":
    main()
