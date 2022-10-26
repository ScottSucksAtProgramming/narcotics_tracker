"""Adds all inventory adjustments to the WLVAC Inventory."""

from narcotics_tracker import commands
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.utils.datetime_manager import DateTimeManager

adjustment_list = []

dt_man = DateTimeManager()
sq_man = SQLiteManager("inventory_wlvac.db")

fentanyl_june_2022 = Adjustment(
    table="inventory",
    id=None,
    created_date=dt_man.return_current_datetime(),
    modified_date=dt_man.return_current_datetime(),
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
    created_date=dt_man.return_current_datetime(),
    modified_date=dt_man.return_current_datetime(),
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
    created_date=dt_man.return_current_datetime(),
    modified_date=dt_man.return_current_datetime(),
    modified_by="SRK",
    adjustment_date=dt_man.convert_to_timestamp("07-22-2022 17:00:00"),
    event_code="IMPORT",
    medication_code="morphine",
    amount=690000,
    reference_id="Narcotics Bi-Annual Report - June 2022 - Wantagh-Levittown VAC",
    reporting_period_id=2200000,
)


def main() -> None:
    # adjustment = Adjustment()
    attributes = vars(Adjustment())
    print(attributes)
    # new_adjustment = adj_builder.build()


if __name__ == "__main__":
    main()
