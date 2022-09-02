"""Contains implementation and representation of Dosage Units.

The units table is a vocabulary control table which stores a library of 
different Dosage Units which can be used to define medication attributes and 
perform conversions within the Narcotics Tracker.. 

This module handles the creation of the units table, returns various 
unit data from the database and parses the raw data returned from the 
database into a usable format. It houses the Unit Class which defines and 
instantiates the units as objects.

Multiple modules including the Medication and Inventory Module make use of 
dosage units.

The database module contains information on communicating with the database.

Classes:
    Unit: Defines units and instantiates them as objects.
    
Functions:

    return_table_creation_query: Returns the query needed to create the table.

    return_units: Returns contents of units as a list of strings.

    parse_unit_data: Returns unit data as a dictionary.
"""

import sqlite3

from narcotics_tracker import database


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the Units Table.

    Returns:
        str: The sql query needed to create the Units Table.
    """
    return """CREATE TABLE IF NOT EXISTS units (
            UNIT_ID INTEGER PRIMARY KEY,
            UNIT_CODE TEXT UNIQUE,                
            UNIT_NAME TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""


def return_units(db_connection: sqlite3.Connection) -> str:
    """Returns the contents of the units table.

    Args:
        db_connection (sqlite3.Connection): The database connection.

    Returns:
        table_contents (str): The contents of the table as a string.
    """
    sql_query = """SELECT unit_id, unit_code, unit_name FROM units"""

    periods_string_list = []
    periods_values_list = []

    periods_data = db_connection.return_data(sql_query)

    for period in periods_data:
        periods_string_list.append(
            f"Unit Number {period[0]}: {period[2]}. Code: '{period[1]}'."
        )
        periods_values_list.append((period[0], period[1], period[2]))
    return periods_string_list, periods_values_list


def parse_unit_data(unit_data) -> dict:
    """Returns unit data from the database as a dictionary.

    Args:
        unit_data (list): The unit's raw data.

    Returns:
        properties (dict): Dictionary objects contains the properties of
            the unit."""

    properties = {}

    properties["unit_id"] = unit_data[0][0]
    properties["unit_code"] = unit_data[0][1]
    properties["unit_name"] = unit_data[0][2]
    properties["created_date"] = unit_data[0][3]
    properties["modified_date"] = unit_data[0][4]
    properties["modified_by"] = unit_data[0][5]

    return properties


class Unit:
    """Defines Units and instantiates them as objects.

    Each controlled substance medication contains a dose which is measured in
    a specific unit. The most common units are milligrams and micrograms. The
    New York State Department of Health paperwork requires medications to be
    tracked in milligrams regardless of the unit the medication is generally
    measured in. Reporting paperwork requires medications to be calculated in
    milliliters and the dosage unit of the medication is required to help with
    those conversions.

    The Narcotics Tracker separates units into two categories:

        Preferred Unit: The preferred unit is the unit which the medication is
            dosed in and how it is commonly referred to by providers.
            Fentanyl's preferred unit is micrograms, Morphine and Midazolam
            use milligrams for their preferred unit.

        Standard Unit: The Narcotics Tracker needs to be able to convert
            between different units and store all medication amounts in a
            standard way. This is the 'Standard Unit'. The Standard Unit for
            the Narcotics Tracker is micrograms (mcg). Unless presenting a
            dose to the user or requesting dosage information from the user
            the program will handle and store all medication amounts in
            micrograms.

    Units can be declared, created and managed using this class. Medications
    will be limited to using the units stored in the units table.

    Attributes:

        unit_id (int): Numeric identifier of each unit. Assigned by the
            database.

       unit_code (str): Unique identifier of each unit type. Assigned by the
            user. Used to interact with the unit in the database.

        unit_name (str): Name of the unit.

        created_date (str): The date the unit type was created in the
            table.

        modified_date (str): The date the unit type was last modified.

        modified_by (str): Identifier of the user who last modified the
            unit type.

    Initializer:

    Instance Methods:
        __repr__: Returns a string expression of the unit.

        save: Saves a new unit to the units table in the database.

        read: Returns the data of the unit from the database as a tuple.

        update: Updates the unit in the units table of the
            database.

        delete: Deletes the unit from the database.

        return_attributes: Returns the attributes of the units object as
            a tuple.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of an Unit using the UnitBuilder.

        Units are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of Units to the
        Builder Package.

        Refer to the documentation for the UnitBuilder Class for more
        information.

        Args:
            builder (unit_builder.UnitBuilder): The builder used to
                construct the Unit object.
        """
        self.unit_id = builder.unit_id
        self.unit_code = builder.unit_code
        self.unit_name = builder.unit_name
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """Returns a string expression of the unit.

        Returns:
            str: The string describing the unit specifying the event
                type's name, code and description.
        """
        return (
            f"Unit Number {self.unit_id}: {self.unit_name}. Code: '{self.unit_code}'."
        )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new unit to the units table in the database.

        The save method will only write the unit into the table if it does
        not already exist. Use the update method to update the unit's
        attributes.

        Assigns a created_date and modified_date.

        Args:
            db_connection (sqlite3.Connection): The database connection.
        """
        sql_query = """INSERT OR IGNORE INTO units VALUES (
            ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def read(self, db_connection: sqlite3.Connection) -> tuple:
        """Returns the data of the unit from the database as a tuple.

        This function will make no changes to the data.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:
            tuple: A tuple containing the unit's attribute values.
        """
        sql_query = """SELECT * from units WHERE unit_code = ?"""

        values = (self.unit_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the unit in the units table of the database.

        The update method will overwrite the unit's data if it already
        exists within the database. Use the save method to store new
        units in the database.

        How to use:
            Use the units.return_units() method to return a list
            of units.

            Use the database.load_unit() method, passing in the
            unit_code of the unit you wish to update.

            Modify the attributes as necessary and call this method to update
            the attributes in the database.

            If you are changing the unit_code use the save() method to create
            a new unit entry in the table and use the delete method to
            remove the old entry.

        Assigns a new modified_date.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

            unit_code (str): The unique identifier of the unit.

        Raises:

            IndexError: An Index Error will be raised if the unit_code is not
            found on the units table.
        """
        sql_query = """UPDATE units 
            SET unit_id = ?, 
                unit_code = ?, 
                unit_name = ?, 
                created_date = ?, 
                modified_date = ?, 
                modified_by = ? 
            WHERE unit_code = ?"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes() + (self.unit_code,)

        db_connection.write_data(sql_query, values)

    def delete(self, db_connection: sqlite3.Connection):
        """Deletes the unit from the database.

        The delete method will delete the unit from the database
        entirely. Note: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM units WHERE unit_id = ?"""
        values = (self.unit_id,)
        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the units object as a tuple.

        Returns:
            tuple: The attributes of the units. Follows the order
            of the columns in the units table.
        """

        return (
            self.unit_id,
            self.unit_code,
            self.unit_name,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )
