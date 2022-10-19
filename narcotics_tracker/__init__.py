"""Tracks the inventory of controlled substances used at EMS agencies.

#* Title: Narcotics Tracker
#* Version: 0.2.0
#* Author: Scott Kostolni - (https://github.com/ScottSucksAtProgramming)

#*  Special Thanks:

    Mom, thanks for being my software design mentor and entertaining my 
    onslaught of questions.

    Tina, thank you for listening to me go on and on about this project and 
    for reading my documentation to ensure I sound a little less like an idiot 
    than I actually am.

#*  Purpose:

    Welcome to the Narcotics Tracker! This software is designed to assist 
    controlled substance agents working at EMS agencies with inventory 
    tracking and periodic reporting of controlled substance activities to 
    their governing agencies.

#*  Motivation:

    I am a controlled substance agent working in New York State. The tracking 
    of controlled substances is complicated and requires multiple forms and 
    processes. I have wished for a single place where all of that information 
    can be stored and easily accessed. This software is intended to fill that 
    need.

#*  Current Completed Features:

    Database Object Creation - Medications, Medication Containers, Units of 
    Measurement, Events, Inventory Adjustments, Reporting Periods and Statuses 
    can be created using the Builder Modules for each item.

    Database and Table Creation - Tables have been defined for all Database 
    Objects and can be stored. The Database Class now functions as a context 
    manager for better resource management.

#*  Planned Features:

    #✓ Medications and Initial Development (v0.1.0 - Alpha) - Completed!
    #✓ Inventory Tracking (v0.2.0 - Alpha) - Completed!
    #Todo Code Architecture Improvement (v0.2.5 - Alpha) - In Progress
    #! Basic Report Generation (v0.3.0 - Alpha)
    #! Command Line Tools (v0.0.0 - Beta)
    #! Order Tracking (v0.1.0 - Beta)
    #! Lot Tracking (v0.2.0 - Beta)
    #! Destruction Tracking (v0.3.0 - Beta)
    #! User and Agent Management (v0.4.0 - Beta)
    #! Command Line Tools Redux (v0.5.0 - Beta)
    #! Console Interface (v1.6.0)
    #! GUI Interface (v1.7.0)

#*  Packages:

    Builders: Contains the builders for the DataItems used in the 
        Narcotics Tracker.
    Items: Contains the items which are stored in the database.
    Scripts: Contains various scripts which help to setup and use the 
        Narcotics Tracker.
    Setup: Contains the modules needed to set up the Narcotics Tracker 
        software.
    Utils: Contains utility helper modules and functions.

#*  Modules:

    Commands: Contains the commands for the SQLite3 Database.
    Database: Manages Communication with the SQLite3 Database.
    SQlite3 Interface: Defines the protocol for commands which interact with 
        the SQLite3 database.


#*  Release Notes:

        Version 0.1.0 - https://github.com/ScottSucksAtProgramming/narcotics_tracker/releases/tag/v0.1.0-alpha
        Version 0.2.0 - https://github.com/ScottSucksAtProgramming/narcotics_tracker/releases/tag/v0.2.0-alpha
"""
