"""Script which runs the Bi-Annual Narcotics Report. For demo purposes."""


from narcotics_tracker import reports
from narcotics_tracker.reports.interfaces.report import Report

if __name__ == "__main__":
    biannual_report: "Report" = reports.BiAnnualNarcoticsInventory()
    result: dict[str, int] = biannual_report.run()
    print(result)
