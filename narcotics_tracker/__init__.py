"""Tracks the inventory of controlled substances used at EMS agencies.

Version: 0.2.0

Author: Scott Kostolni - (https://github.com/ScottSucksAtProgramming)

Special Thanks:
    Mom, thanks for being my software design mentor and entertaining my 
    onslaught of questions.

    Tina, thank you for listening to me go on and on about this project and 
    for reading my documentation to ensure I sound a little less like an idiot 
    than I actually am.

Purpose:
    Welcome to the Narcotics Tracker! This software is designed to assist 
    controlled substance agents working at EMS agencies with inventory 
    tracking and periodic reporting of controlled substance activities to 
    their governing agencies.

Motivation:
    I am a controlled substance agent working in New York State. The tracking 
    of controlled substances is complicated and requires multiple forms and 
    processes. I have wished for a single place where all of that information 
    can be stored and easily accessed. This software is intended to fill that 
    need.

Current Completed Features:
    Database Object Creation - Medications, Medication Containers, Units of 
    Measurement, Events, Inventory Adjustments, Reporting Periods and Statuses 
    can be created using the Builder Modules for each item.

    Database and Table Creation - Tables have been defined for all Database 
    Objects and can be stored. The Database Class now functions as a context 
    manager for better resource management.

Planned Features:
    Inventory Tracking (v0.2.0 - alpha) - Completed!

    Code Architecture Improvement (v0.2.5 - Alpha)

    Command Line Tools (v1.0.0)

    Order Tracking (v1.1.0)

    Lot Tracking (v1.2.0)

    Destruction Tracking (v1.3.0)

    User and Agent Management (v1.4.0)

    Report Generation (v1.5.0)

    Console Interface (v1.6.0)

    GUI Interface (v1.7.0)

Packages:
    Builders: Assists with the building of complex objects.

    Enums: Package Removed in v0.2.0 - alpha.

    Setup: Contains standard items for populating the database.

    Utils: Contains utility functions used in the software.

Modules:

    Containers: Contains implementation and representation of Medication 
        Containers.

    Database: Defines the database model for the narcotics tracker.

    Events: Contains the implementation and representation of Events.

    Inventory: Contains the implementation and representation of Inventory 
        Adjustments.

    Medications: Contains the implementation and representation of Medication 
        Objects.

    Reporting Periods: Contains the implementation and representation of 
        Reporting Period Objects.

    Statuses: Contains the implementation and representation of Object 
        Statuses.

    Units: Contains implementation and representation of Units of Measurement.


Release Notes:

Version 0.1.0 - https://github.com/ScottSucksAtProgramming/narcotics_tracker/releases/tag/v0.1.0-alpha

Version 0.2.0 - https://github.com/ScottSucksAtProgramming/narcotics_tracker/releases/tag/v0.2.0-alpha
"""
