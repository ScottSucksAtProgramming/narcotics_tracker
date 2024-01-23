"""Script which works with a personal database for testing."""

from typing import TYPE_CHECKING

from narcotics_tracker import commands
from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.builders.reporting_period_builder import ReportingPeriodBuilder
from narcotics_tracker.services.datetime_manager import DateTimeManager
from narcotics_tracker.services.interfaces.datetime import DateTimeService
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.items.reporting_periods import ReportingPeriod


dt_man = DateTimeManager()


def main():
    """Sets up the narcotics database for WLVAC."""
    # * Populate Database with WLVAC Medications.
    meds = build_wlvac_meds()

    for medication in meds:
        commands.AddMedication().set_medication(medication).execute()

    # * Populate Database with Reporting Periods for 2022.
    periods = build_reporting_periods()

    for period in periods:
        commands.AddReportingPeriod().set_reporting_period(period).execute()


def build_wlvac_meds() -> list["Medication"]:
    """Builds Medication Objects used at WLVAC and returns them as a list."""
    wlvac_medications: list["Medication"] = []
    med_builder = MedicationBuilder()
    med_builder.set_medication_code("fentanyl")
    med_builder.set_medication_name("Fentanyl")
    med_builder.set_fill_amount(2)
    med_builder.set_medication_amount(100)
    med_builder.set_preferred_unit("mcg")
    med_builder.set_concentration()
    med_builder.set_status("ACTIVE")
    med_builder.set_created_date(dt_man.return_current())
    med_builder.set_modified_date(dt_man.return_current())
    med_builder.set_modified_by("SRK")

    fentanyl = med_builder.build()
    wlvac_medications.append(fentanyl)

    med_builder = MedicationBuilder()
    med_builder.set_medication_name("Midazolam")
    med_builder.set_fill_amount(2)
    med_builder.set_medication_amount(10)
    med_builder.set_preferred_unit("mg")
    med_builder.set_concentration()
    med_builder.set_status("ACTIVE")
    med_builder.set_created_date(dt_man.return_current())
    med_builder.set_modified_date(dt_man.return_current())
    med_builder.set_modified_by("SRK")

    midazolam = med_builder.build()
    wlvac_medications.append(midazolam)

    med_builder = MedicationBuilder()
    med_builder.set_medication_code("morphine")
    med_builder.set_medication_name("Morphine")
    med_builder.set_fill_amount(1)
    med_builder.set_medication_amount(10)
    med_builder.set_preferred_unit("mg")
    med_builder.set_concentration()
    med_builder.set_status("ACTIVE")
    med_builder.set_created_date(dt_man.return_current())
    med_builder.set_modified_date(dt_man.return_current())
    med_builder.set_modified_by("SRK")

    morphine = med_builder.build()
    wlvac_medications.append(morphine)

    return wlvac_medications


def build_reporting_periods(
    dt_manager: "DateTimeService" = ServiceManager().datetime,
) -> list["ReportingPeriod"]:
    """Builds Reporting Period Objects for 2022 and returns them as a list."""
    periods: list["ReportingPeriod"] = []

    p_builder = ReportingPeriodBuilder()

    p_builder.set_start_date(dt_manager.convert_to_timestamp("01-01-2021 00:00:00"))
    p_builder.set_end_date(dt_manager.convert_to_timestamp("06-30-2021 23:59:59"))
    p_builder.set_status("CLOSED")
    p_builder.set_id(2100000)
    p_builder.set_created_date(dt_man.return_current())
    p_builder.set_modified_date(dt_man.return_current())
    p_builder.set_modified_by("SRK")

    jan_to_june_2021 = p_builder.build()
    periods.append(jan_to_june_2021)

    p_builder = ReportingPeriodBuilder()
    p_builder.set_start_date(dt_manager.convert_to_timestamp("07-01-2021 00:00:00"))
    p_builder.set_end_date(dt_manager.convert_to_timestamp("12-31-2021 23:59:59"))
    p_builder.set_status("CLOSED")
    p_builder.set_id()
    p_builder.set_created_date(dt_man.return_current())
    p_builder.set_modified_date(dt_man.return_current())
    p_builder.set_modified_by("SRK")

    july_to_december_2021 = p_builder.build()
    periods.append(july_to_december_2021)

    p_builder = ReportingPeriodBuilder()
    p_builder.set_start_date(dt_manager.convert_to_timestamp("01-20-2022 00:00:00"))
    p_builder.set_end_date(dt_manager.convert_to_timestamp("07-22-2022 23:59:59"))
    p_builder.set_status("CLOSED")
    p_builder.set_id(2200000)
    p_builder.set_created_date(dt_man.return_current())
    p_builder.set_modified_date(dt_man.return_current())
    p_builder.set_modified_by("SRK")

    jan_to_june_2022 = p_builder.build()
    periods.append(jan_to_june_2022)

    p_builder = ReportingPeriodBuilder()
    p_builder.set_start_date(dt_manager.convert_to_timestamp("07-23-2022 00:00:00"))
    p_builder.set_end_date(None)
    p_builder.set_status("OPEN")
    p_builder.set_id()
    p_builder.set_created_date(dt_man.return_current())
    p_builder.set_modified_date(dt_man.return_current())
    p_builder.set_modified_by("SRK")

    july_to_december_2022 = p_builder.build()

    periods.append(july_to_december_2022)

    return periods


if __name__ == "__main__":
    main()
