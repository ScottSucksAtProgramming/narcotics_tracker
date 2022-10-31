"""Adds all inventory adjustments to the WLVAC Inventory."""

from typing import TYPE_CHECKING

from narcotics_tracker import commands
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment


def main() -> None:

    adjustment_data = return_adjustments_data()

    adjustment_list = construct_adjustments(adjustment_data)

    for adjustment in adjustment_list:
        message = commands.AddAdjustment().execute(adjustment)
        print(message)


def construct_adjustments(data: list[any]) -> list["Adjustment"]:
    adjustment_list = []
    for data_set in data:
        adjustment = (
            AdjustmentBuilder()
            .set_table("inventory")
            .set_id(data_set[0])
            .set_created_date()
            .set_modified_date()
            .set_modified_by("SRK")
            .set_adjustment_date(data_set[1])
            .set_event_code(data_set[2])
            .set_medication_code(data_set[3])
            .set_adjustment_amount(data_set[4])
            .set_reporting_period_id(data_set[5])
            .set_reference_id(data_set[5])
            .build()
        )
        adjustment_list.append(adjustment)

    return adjustment_list


def return_adjustments_data() -> list[list]:
    return [
        [
            None,
            "07-22-2022 17:00:00",
            "IMPORT",
            "fentanyl",
            745,
            2200001,
            "Narcotics Bi-Annual Report - June 2022 - Wantagh-Levittown VAC",
        ],
        [
            None,
            "07-22-2022 17:00:00",
            "IMPORT",
            "midazolam",
            663.4,
            2200001,
            "Narcotics Bi-Annual Report - June 2022 - Wantagh-Levittown VAC",
        ],
        [
            None,
            "07-22-2022 17:00:00",
            "IMPORT",
            "morphine",
            690,
            2200001,
            "Narcotics Bi-Annual Report - June 2022 - Wantagh-Levittown VAC",
        ],
        [None, 1659212760, "USE", "fentanyl", 50, 2200001, "PCR# 220830"],
        [None, 1661027838, "DESTRUCTION", "morphine", 440, 2200001, "RxRD# 37265"],
        [None, 1661027838, "DESTRUCTION", "midazolam", 363.4, 2200001, "RxRD# 37265"],
        [None, 1661027838, "DESTRUCTION", "fentanyl", 345, 2200001, "RxRD# 37265"],
        [None, 1661166388, "USE", "midazolam", 5, 2200001, "PCR# 220920"],
        [None, 1661701387, "USE", "fentanyl", 60, 2200001, "PCR# 220945"],
        [None, 1662580020, "USE", "fentanyl", 100, 2200001, "PCR# 220976"],
        [None, 1665258240, "USE", "midazolam", 5, 2200001, "PCR# 221095"],
        [None, 1666487700, "USE", "midazolam", 1.6, 2200001, "PCR# 221144"],
    ]


if __name__ == "__main__":
    main()
