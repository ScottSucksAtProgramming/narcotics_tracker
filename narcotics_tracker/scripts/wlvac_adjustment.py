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
        [
            None,
            "01-01-2023 00:00:00",
            "IMPORT",
            "fentanyl",
            344,
            2300000,
            "BiAnnual Narcotics Report - December 2022 - Wantagh-Levittown VAC - Final",
        ],
        [
            None,
            "01-01-2023 00:00:00",
            "IMPORT",
            "midazolam",
            278.4,
            2300000,
            "BiAnnual Narcotics Report - December 2022 - Wantagh-Levittown VAC - Final",
        ],
        [
            None,
            "01-01-2023 00:00:00",
            "IMPORT",
            "morphine",
            245,
            2300000,
            "BiAnnual Narcotics Report - December 2022 - Wantagh-Levittown VAC - Final",
        ],
        [None, "03-06-2023 15:51:00", "USE", "fentanyl", 100, 2300000, "PCR# 230244"],
        [None, "04-03-2023 23:42:54", "USE", "morphine", 5, 2300000, "PCR# 230370"],
        [None, "04-04-2023 23:49:09", "USE", "fentanyl", 200, 2300000, "PCR# 230376"],
        [None, "04-04-2023 07:25:37", "USE", "morphine", 5, 2300000, "PCR# 230371"],
        [None, "04-10-2023 21:42:42", "USE", "fentanyl", 100, 2300000, "PCR# 230399"],
    ]


if __name__ == "__main__":
    main()
