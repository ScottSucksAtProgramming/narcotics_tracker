# Introducing Narcotics Tracker v0.2.5.

| Version | Release Date | Audience   |
| :------ | :----------- | :--------- |
| 0.3.0   | 11/07/2022   | Developers |

**Message from ScottSucksAtProgramming:**

> Hooray! Version 0.3.0 is here! This is not a gigantic update but it marks the
> completion of the primary goal I had for this project. With a single command
> the Narcotics Tracker can now print out all the information required for the
> NYS Semi-Annual Controlled Substance Inventory Form for EMS Agencies'
> (DOH-3848). This will make reporting each period far far easier than doing it
> manually.

## Reports Package

The Reports Package has been added to the main directory of the Narcotics
Tracker.

### Interface

The Report Module within the Interfaces sub-package contains the protocol for
reports. It is similar to the Command Protocol and is using the Command Design
Pattern for its implementation. The receiver can be set via the initializer.
The run method will execute the report and return the results.

### Return Medication Stock Report

This report returns the current amount of a specified medication in the
inventory. Amount is currently returned as a float. This may be adjusted later
to return a dictionary to conform to the other reports.

### Return Current Inventory

THis report returns the current amount of all 'active' medications in the
'medications' table in the inventory. This report is designed to be used for
regular inventory stock counts. Where the physical inventory count can be
compared to the return value of this report. This report currently returns the
data as a list of dictionaries.

### Bi-Annual Narcotics Inventory Report

This is the big guy! This will cycle through all active medications from the
'medications' table and all data from the current, 'open' reporting period to
return the following:

    -   Starting amount of the medication in milliliters.
    -   Amount of the medication received from orders in milliliters.
    -   Amount of the medication used by providers in milliliters.
    -   Amount of the medication wasted by providers in milliliters.
    -   Amount of the medication destroyed at a reverse distributor in milliliters.
    -   Amount of the medication lost or stolen in milliliters.
    -   Final amount of the medication in milliliters.

When adjustments are up to date, this report should be accurate and can be used
to complete this report without issue.

## Next Up!

The next release will see the implementation of a command line interface! Wish
me luck!
