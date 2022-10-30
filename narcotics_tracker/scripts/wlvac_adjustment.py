"""Adds all inventory adjustments to the WLVAC Inventory."""

from narcotics_tracker import commands
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.services.datetime_manager import DateTimeManager
from narcotics_tracker.services.service_provider import ServiceProvider
from narcotics_tracker.services.sqlite_manager import SQLiteManager

dt_man = DateTimeManager()
sq_man = SQLiteManager("inventory_wlvac.db")


def construct_adjustments(data: list[any]) -> list["Adjustment"]:
    adjustment_list = []
    for data_set in data:
        adjustment = Adjustment(
            table="inventory",
            id=data_set[0],
            created_date=dt_man.return_current(),
            modified_date=dt_man.return_current(),
            modified_by="SRK",
            adjustment_date=data_set[1],
            event_code=data_set[2],
            medication_code=data_set[3],
            amount=data_set[4],
            reference_id=data_set[6],
            reporting_period_id=data_set[5],
        )
        adjustment_list.append(adjustment)

    return adjustment_list


adjustment = Adjustment(
    table="inventory",
    id=None,
    created_date=dt_man.return_current(),
    modified_date=dt_man.return_current(),
    modified_by="SRK",
    adjustment_date=dt_man.convert_to_timestamp("07-22-2022 17:00:00"),
    event_code="IMPORT",
    medication_code="fentanyl",
    amount=7450,
    reference_id="Narcotics Bi-Annual Report - June 2022 - Wantagh-Levittown VAC",
    reporting_period_id=2200000,
)

midazolam_june_2022 = Adjustment(
    table="inventory",
    id=None,
    created_date=dt_man.return_current(),
    modified_date=dt_man.return_current(),
    modified_by="SRK",
    adjustment_date=dt_man.convert_to_timestamp("07-22-2022 17:00:00"),
    event_code="IMPORT",
    medication_code="midazolam",
    amount=265360.0,
    reference_id="Narcotics Bi-Annual Report - June 2022 - Wantagh-Levittown VAC",
    reporting_period_id=2200000,
)

morphine_june_2022 = Adjustment(
    table="inventory",
    id=None,
    created_date=dt_man.return_current(),
    modified_date=dt_man.return_current(),
    modified_by="SRK",
    adjustment_date=dt_man.convert_to_timestamp("07-22-2022 17:00:00"),
    event_code="IMPORT",
    medication_code="morphine",
    amount=690000,
    reference_id="Narcotics Bi-Annual Report - June 2022 - Wantagh-Levittown VAC",
    reporting_period_id=2200000,
)


def main() -> None:

    service_provider = ServiceProvider(repository="inventory_wlvac.db")
    sq, dt, converter = service_provider.start_services()

    adjustment_data = []

    use_1 = [None, 1659212760, "USE", "fentanyl", -50, 2200000, "PCR# 220830"]
    adjustment_data.append(use_1)
    des_1 = [
        None,
        1661027838,
        "DESTRUCTION",
        "morphine",
        -440000,
        2200000,
        "RxRD# 37265",
    ]
    adjustment_data.append(des_1)
    des_2 = [
        None,
        1661027838,
        "DESTRUCTION",
        "midazolam",
        -363400,
        2200000,
        "RxRD# 37265",
    ]
    adjustment_data.append(des_2)
    des_3 = [None, 1661027838, "DESTRUCTION", "fentanyl", -3450, 2200000, "RxRD# 37265"]
    adjustment_data.append(des_3)
    use_2 = [None, 1661166388, "USE", "midazolam", -5000, 2200000, "PCR# 220920"]
    adjustment_data.append(use_2)
    use_3 = [None, 1661701387, "USE", "fentanyl", -60, 2200000, "PCR# 220945"]
    adjustment_data.append(use_3)
    use_4 = [None, 1662580020, "USE", "fentanyl", -100, 2200000, "PCR# 220976"]
    adjustment_data.append(use_4)
    use_5 = [None, 1665258240, "USE", "midazolam", -5000, 2200000, "PCR# 221095"]
    adjustment_data.append(use_5)
    use_6 = [None, 1666487700, "USE", "midazolam", -1600, 2200000, "PCR# 221144"]
    adjustment_data.append(use_6)

    adjustment_list = construct_adjustments(adjustment_data)

    for adjustment in adjustment_list:
        message = commands.AddAdjustment(sq, adjustment).execute()
        print(message)


if __name__ == "__main__":
    main()
