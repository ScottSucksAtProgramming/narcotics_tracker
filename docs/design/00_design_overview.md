# Design Doc Part 0 - Overview / Table of Contents

|Section | Version | Created    | Updated    |
|:-------| :------ | :--------- | :--------- |
|   0    | 0.1.0   | 08/01/2022 | 08/24/2022 |

{{TOC}}

## Summary

Welcome to the **Narcotics Tracker**! This software is designed to assist controlled substance agents working at EMS agencies with inventory tracking and periodic reporting of controlled substance activities to their governing agencies.

### Motivation
I am a controlled substance agent working in New York State. The tracking of controlled substances is complicated and requires multiple forms and processes. I have wished for a single place where all of that information can be stored and easily accessed. This software is intended to fill that need.

### Goals

The **Narcotics Tracker** will provide a single place to enter all changes to an agencies controlled substance inventory. Each change in the inventory can be entered peridoically where the data can be queried to return information requried for reporting and compliance with tracking specifications.

##### Project Specifications
    1. Inventory tracking of all controlled substances used by an EMS agency.
    2. Ability to create agency specific medications.
    3. Tracking of medication lots as they as disbursed to sub-stocks.
    4. Tracking of medication orders.
    5. Tracking of medication destruction.
    6. Tracking of medication administration.
    7. Tracking of medication waste.
    8. Built in reports which can be generated at the users request which fulfill the New York State and DEA requirements.
    9. A simple but powerful console user interface.
    10. A graphical user interface.

I am a self-taught programmer looking to improve my knowledge and experience in soft-ware design by building projects which have practical applications.

##### Personal Learning Goals 
    1. Increase my knowledge and experience with Python.
    2. Learn about Object Oriented Programming.
    3. Practice and gain experience with Test Driven Development
    4. Gain knowledge on the storage, and manipulation, of data and the use of databases.
    5. Potentially branch out into GUI development with Python or different languages as necessary.
    6. To put out a product which I may be able to use to help generate extra income though licensing and service contracts.

## Development Roadmap / Progress

I'm not entirely sure where the best place to begin is. I do not have a enough
experience to know how to design this kind of software. I'll be using a lot of
trial and error. Here is my imagined development Path.

-   [x] Medication Creation and Management
  -   [x] Builder Pattern
-   [x] Communication with a Database
-   [ ] Inventory Management
-   [ ] Medication Use 
-   [ ] Medication Waste
-   [ ] Medication Destruction
-   [ ] Medication Orders
-   [ ] Lot Management
-   [ ] Agent Management
-   [ ] Provider Management
-   [ ] Report Generation
-   [ ] Console User Interface
-   [ ] Graphical User Interface

## Table Of Contents

* [Medications](01_medications.md)
* [Database](02.database.md)
* [Inventory](03_inventory.md)
* Medication Use
* Medication Waste
* Medication Destruction
* [Medication Orders](07_orders.md)
* Lot Management
* Agent Management
* Provider Management
* Report Generation
* Console UI
* Graphical UI
