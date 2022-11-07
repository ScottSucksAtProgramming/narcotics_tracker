"""Script which runs the Bi-Annual Narcotics Report. For demo purposes."""


from narcotics_tracker import reports

if __name__ == "__main__":
    report = reports.biannual_inventory.BiAnnualNarcoticsInventory().execute()
    print(report)
