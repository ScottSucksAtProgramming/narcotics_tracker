"""Contains the items which are stored in the database.

#* Background

    The classes defined within the modules of this package represent the items 
    which enable tracking of controlled substance medications. The DataItems 
    Class is an abstract base class which defines the interface for all other 
    items. The other modules inherit following attributes: table, id, 
    created_date, modified_date, and modified_by. Each child class is required 
    to implement the '__str__' method to provide a description of the item 
    understandable by the user.

    Medications represent the controlled substances which are being tracked 
    and contain information required to complete tracking. Different 
    medications use different units of measurement; These are defined in the 
    Units class. When the amount of medication in the inventory is changed and 
    Adjustment is created to reflect the change. Controlled substance activity 
    must be tracked; The Event class defines the type of events which can 
    occur and are listed as part of an adjustment. Events also determine 
    whether they add or remove medication amounts from the inventory. Every 6 
    months EMS agencies are required to send reports to the various oversight 
    agencies. Each six month blocks is recorded as a Reporting Period listing 
    its start date and end date. Medications, reporting periods and future 
    items may require a way to track their status. Statuses are defined using 
    the Status class.

#* Intended Use

    Data Items are only responsible for tracking the values assigned to their 
    attributes. The '__str__' returns a message which the user can use to 
    quickly identify the item. These items should contain no other methods.

    Data Items contain a large number of attributes, making them difficult to 
    construct. The Builders Package contains builders for each Data Item and 
    should be used to created them. Review the documentation for the builders 
    for more information.

    Python's 'vars' method returns a dictionary mapping the attribute names 
    with their values. The first key 'table' maps to the name of the SQLite3 
    Database table the item lives in. The rest of the keys match the column 
    names and can be used to construct SQL statements for saving them into the 
    database.

#* Modules:

    Database_Items: Defines the interface for items stored in the database.
    Adjustments: Defines the changes which occur to the inventory.
    Events: Defines the type of events which can affect the inventory.
    Medications: Defines the medications which are tracked.
    Reporting_Periods: Defines the reporting period for medication tracking.
    Statuses: Defines the statuses for other data items.
    Units: Defines the units of measurements for medications.
"""
