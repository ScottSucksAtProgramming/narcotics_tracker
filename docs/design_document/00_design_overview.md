# 0.0 - Project Overview

| Section | Version | Created    | Updated    |
| :------ | :------ | :--------- | :--------- |
| 0.0     | 0.2.5   | 08/01/2022 | 10/25/2022 |

{{TOC}}

The **Narcotics Tracker** is a python application created to assisted with the inventory management of controlled substance medications for EMS agencies. It is currently in development. For the most up-to-date information regarding this project please review the [GitHub Repository](https://github.com/ScottSucksAtProgramming/narcotics_tracker).

## Development Team: 
**Lead Developer: Scott Kostolni**
- [GitHub](https://github.com/ScottSucksAtProgramming/narcotics_tracker/commits?author=ScottSucksAtProgramming)
- [Linkedin](https://www.linkedin.com/in/scottkostolni/) 

## Frameworks and Technologies
- [Python](https://www.python.org)
- [Pendulum](https://pendulum.eustace.io)
- [SQlite3](https://www.sqlite.org/index.html)

## Specifications and Requirements

    1. Inventory tracking of controlled substance activities including:
        - Ordering of controlled substances.
        - Provider administration and waste of controlled substances.
        - Destruction of controlled substances through reverse distributors and pharmacies.
        - Loss of controlled substance medications.
        - Lot disbursement.
    2. Configureable DataItems to accomodate a variety EMS agencies.
        - Medications
        - Inventory Adjustments
        - Event Types
        - Reporting Periods
        - Statuses
        - Units
        - Purchase Orders
        - Destruction Orders
    3. Report generation
        - Breakdown of inventory adjustments.
        - On demand calculation of inventory amounts on hand.
        - Conversion between different units of mass and volume.
    4. Command Line User Interface
    5. Console User Interface
    6. Graphical User Interface
    
[Design Document Table of Contents](01_table_of_contents.md)