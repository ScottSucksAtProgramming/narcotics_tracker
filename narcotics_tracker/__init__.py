"""Tracks the inventory of controlled substances used at EMS agencies.

#* Title: Narcotics Tracker
#* Version: 0.2.5
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

    Custom Object Creation - Medications, Units of Measurement, Events, 
    specific Inventory Adjustments, Reporting Periods and Statuses can be 
    created allowing any EMS agency to customize the Narcotics Tracker to 
    their policies and procedures. These objects are collectively referred to 
    as DataItems as they are items which live in the database.

    Persistent Storage - The built-in SQLite3 Database library has been used 
    as the main data repository for the Narcotics Tracker. Tables have been 
    created to for each of the six DataItems. The Inventory Table serves as 
    the main table for the database;  It tracks each individual change to the 
    stock of a medication, called an Adjustment. Adjustments use data stored 
    in the Events Table, among others, to calculate how the adjustment affects 
    the stock and which medications are affected by it. The Medications Table 
    stores information on the controlled substances used by an EMS agency 
    including their concentration and preferred unit of measurement. These 
    data points are used to tally medication totals and calculate data 
    required when reporting to oversight agencies.
    
    Utility Services - Multiple utilities are used to manage the inventory of 
    controlled substances. The Service Provider feature provides quick and 
    easy access to these services and provides an interface that new services 
    can make use of without requiring changes to the code that relies on a 
    service.

    Flexible Design and Architecture - In the most recent update, the 
    structure of the Narcotics Tracker was rebuilt from the ground up to 
    improve the readability of the code and reduce its fragility. As a result 
    the code is well structured, easier to work with, and much more 
    extensible.

#*  Planned Features:

    #✓ Medications and Initial Development (v0.1.0 - Alpha) - Completed!
    #✓ Inventory Tracking (v0.2.0 - Alpha) - Completed!
    #✓ Code Architecture Improvement (v0.2.5 - Alpha) - Completed!!
    #TODO Basic Report Generation (v0.3.0 - Alpha) - Next Up!!
    #! Command Line Tools (v0.0.0 - Beta)
    #! Order Tracking (v0.1.0 - Beta)
    #! Lot Tracking (v0.2.0 - Beta)
    #! Destruction Tracking (v0.3.0 - Beta)
    #! User and Agent Management (v0.4.0 - Beta)
    #! Command Line Tools Redux (v0.5.0 - Beta)
    #! Console Interface (v0.6.0)
    #! GUI Interface (v0.7.0)

#*  Meet the Players:

    #* DataItems and Builders

        DataItems are individual objects which are stored in the database and 
        enable inventory management. They contain numerous attributes and the 
        Builder Design Pattern was used to help make constructing DataItems 
        easier. Each DataItem has its own builder which provides a step-wise 
        approach to assigning attributes and constructing the object. In 
        future updates Director Objects will be provided to walk end users 
        through the creation of DataItems.

        - Adjustments record specific changes to the stock of a medication.

        - Events classify the types of changes which commonly occur and 
            determine if amounts are added or removed from the stock.

        - Medications store relevant information about the controlled 
            substances. Adjustments must specify which medication(s) were 
            affected.

        - Reporting Periods allow for adjustments to be organized by their 
            date and are used to determine which adjustments need to be 
            reported.

        - Statuses provide additional information for Medications, Reporting 
            Periods and future additions to the Narcotics Tracker.

        - Units store information on how a medication is measured and are 
            integral to completing reports for oversight agencies.

    #* The Services

        Services provide utilities to help with the management of the 
        narcotics inventory. The Service Provider offers an easy way for these 
        services to be accessed.

        - The Persistence Service communicates directly with the SQLite 
            database. It stores items in the appropriate tables returns 
            requested data.

        - The DateTime Service provides date and time information and converts 
            between human readable dates and the unix timestamps which are 
            stored in the database.

        - The Conversion Service converts medication amounts between various 
            units of mass and volume.

    #* Commands

        In order to increase the flexibility of the Narcotics Tracker the 
        Command Design Pattern was implemented. Commands provide access to 
        simple and complex activities through a shared interface. 
        
        Each command allows for the specification of its intended receiver 
        during initialization. To trigger the command its 'execute' method is 
        called. Any required information can be passed into the execute method 
        which will pass it on to its target to complete the command. 
        Additional commands can be easily created using this interface.


#*  Release Notes:

        Version 0.1.0 - https://github.com/ScottSucksAtProgramming/narcotics_tracker/releases/tag/v0.1.0-alpha
        Version 0.2.0 - https://github.com/ScottSucksAtProgramming/narcotics_tracker/releases/tag/v0.2.0-alpha
        Version 0.2.5 - https://github.com/ScottSucksAtProgramming/narcotics_tracker/releases/tag/v0.2.5-alpha
"""
