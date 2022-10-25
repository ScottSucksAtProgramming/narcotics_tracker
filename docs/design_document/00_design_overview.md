# Design Doc Part 0 - Overview / Table of Contents

| Section | Version | Created    | Updated    |
| :------ | :------ | :--------- | :--------- |
| 0       | 0.2.5   | 08/01/2022 | 10/25/2022 |

{{TOC}}

## Summary

Welcome to the **Narcotics Tracker**! This software is designed to assist
controlled substance agents working at EMS agencies with inventory tracking and
periodic reporting of controlled substance activities to their governing
agencies.

Author: **Scott Kostolni**

### Motivation

I am a controlled substance agent working in New York State. The tracking of
controlled substances is complicated and requires multiple forms and processes.
I have wished for a single place where all required information can be stored
and easily accessed. This software is intended to fill that need.

I am hoping that I will be able to produce an application which can be useful
to other EMS agencies.

### Goals

The **Narcotics Tracker** will provide a single place to enter all changes to
an agencies controlled substance inventory. Each change in the inventory can be
entered periodically where the data can be queried to return information
required for reporting and compliance with tracking specifications.

##### Project Specifications

    1. Inventory tracking of all controlled substances used by an EMS agency.
    2. Ability to create agency specific medications, as well as statuses, reporting periods, and other needed data items.
    3. Tracking of medication lots as they as disbursed to sub-stocks.
    4. Tracking of medication orders.
    5. Tracking of medication destruction.
    6. Tracking of medication administration.
    7. Tracking of medication waste.
    8. Built in reports which can be generated at the users request which fulfill the New York State and DEA requirements.
    9. A simple but powerful console user interface.
    10. A graphical user interface.

I am a self-taught programmer looking to improve my knowledge and experience in
soft-ware design by building projects which have practical applications.

##### Personal Learning Goals

    1. Increase my knowledge and experience with Python.
    2. Learn about Object Oriented Programming.
    3. Practice and gain experience with Test Driven Development
    4. Gain knowledge on the storage, and manipulation, of data and the use of databases.
    5. Potentially branch out into GUI development with Python or different languages as necessary.
    6. To put out a product which I may be able to use to help generate extra income though licensing and service contracts.

## Development Roadmap / Progress

As this project has been progressing and my understanding of the problem I am
trying to solve increases there has been a large number of changes to the
structure and code of the **Narcotics Tracker**. Please review the [release
notes](https://github.com/ScottSucksAtProgramming/narcotics_tracker/tree/master/docs/releases) to see all the updates.

-   [x] Design
    -   [x] Outline program requirements.
    -   [x] Mock up database design.
    -   [x] Mock up class diagrams.
-   [x] Version 0.1.0 - Alpha - Released On August 24th, 2022
    -   [x] Medication creation
    -   [x] Container, Status and Unit creation.
    -   [x] Persistent data storage with an SQLite3 database.
    -   [x] Test suite development.
-   [x] Version 0.2.0 - Alpha - Released On September 14th, 2022
    -   [x] Event and Reporting Period creation.
    -   [x] Adjustment creation and the inventory management enabled.
    -   [x] Date Management enabled through SQLite3.
    -   [x] Database Context Manager added.
    -   [x] Continued expansion of the Test Suite.
-   [ ] Version 0.2.5 - Alpha - In progress!
    -   [ ] Design architecture rework.
    -   [ ] Design pattern implementation to reduce coupling and increase
            flexibility and ease of extension.
    -   [ ] Documentation update.
    -   [ ] Continued Test Suite expansion.
-   [ ] Version 0.3.0 - Alpha
    -   [ ] Basic Report Generation
-   [ ] Version 0.0.0 - Beta
    -   [ ] Command Line User Interface
-   [ ] Version 0.1.0 - Beta
    -   [ ] Order Tracking
-   [ ] Version 0.2.0 - Beta
    -   [ ] Order Tracking
-   [ ] Version 0.3.0 - Beta
    -   [ ] Destruction Tracking
-   [ ] Version 0.4.0 - Beta
    -   [ ] Controlled Substance Agent Management
-   [ ] Version 0.5.0 - Beta
    -   [ ] Command Line Tools Interface Update
-   [ ] Version 0.6.0 - Beta
    -   [ ] Console User Interface
-   [ ] Version 0.7.0 - Beta
    -   [ ] Graphical User Interface

## Design Document Contents

-   Persistence Layer
    -   [Database](02.database.md)
-   Use Case Layer
    -   Data Items
    -   [Medications](01_medications.md)
    -   Lot Management
    -   Inventory Management
        -   [Inventory](03_inventory.md)
        -   Medication Use
        -   Medication Waste
        -   Medication Destruction
    -   Order Management
        -   [Medication Orders](07_orders.md)
    -   Agent Management
    -   Provider Management
    -   Report Generation
-   User Interface Layer
    -   Command Line Interface
    -   Console User Interface
    -   Graphical User Interface
