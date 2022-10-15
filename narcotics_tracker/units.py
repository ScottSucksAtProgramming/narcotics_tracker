"""Contains implementation and representation of Units of Measurement.

#* Background

Controlled substance medications are suspensions in which the medication 
itself (the solute) is dissolved within a liquid (the solvent). Tracking 
controlled substance medications requires the use of three types of 
measurement: 

The Dose measures the amount of the medication itself and is denoted in metric 
units of mass: Grams (g), milligrams (mg), and micrograms (mcg). These units 
can be easily converted between. 

    #! Note: 1 Gram = 1,000 milligrams = 1,000,000 micrograms.

The Fill measures the amount of the liquid in which the medication is 
suspended in. Fill is denoted in metric units of volume: Liters (L) and 
milliliters (ml).

The Concentration or 'strength' of a medication is calculated by dividing its 
mass by the volume of the liquid it's dissolved in. Concentration is used to 
calculate the total amount of a controlled substance when reporting to New 
York State which requires the volume of the medications to be specified.

#* Preferred vs. Standard Units

The Narcotics Tracker divides Dosage Units into two categories. The Preferred 
Unit is the unit of measurement by which the controlled substance is generally 
referred and dosed by. To simplify math and standardize the inventory tracking 
of controlled substance medications all Dosage Amounts are converted into 
micrograms before being stored in the database. Medication amounts are 
converted back into their preferred unit when being shown to the users.

#* Intended Use

This module and the Unit Class defined below allow for the creation of Unit 
objects which represent the units of measurement within the Narcotics Tracker. 
It is highly recommended to use the Unit Builder Module contained within the 
Builders package to create these objects. Instructions for using builders can 
be found within that package.

The Unit Converter Module in the Utils Package performs calculations and 
conversions between the different units of measurement. Instructions for using 
the Unit Converter can be found within that module.

    #! Note: As of the current version the Unit Converter can only convert 
    #! between Grams, milligrams, and micrograms. This will be reviewed in a 
    #! later update.

#* Units in the Database

Units are stored within the 'units' table of the database with their numeric 
ID, name, code, and creation / modification information specified. Medication 
objects must specify their preferred unit and are limited to the units listed 
in the units table.

The Narcotics Tracker comes with a selection of pre-defined units. Refer to 
the Standard Items Module inside the Setup Package for more information.

#* Classes:

    Unit: Defines units and instantiates them as objects.
    
#* Functions:

    return_table_creation_query: Returns the query needed to create the 
        'units' table.

    return_units: Returns the contents of the units table as lists of strings 
        and values.

    parse_unit_data: Returns a Unit's attributes from the database as a 
        dictionary.
"""

import sqlite3
from typing import Union

from narcotics_tracker.persistence import database


def return_table_creation_query() -> str:
    """Returns the query needed to create the 'units' table.

    Returns:

        str: The sql query needed to create the 'units' Table.
    """
    return """CREATE TABLE IF NOT EXISTS units (
            UNIT_ID INTEGER PRIMARY KEY,
            UNIT_CODE TEXT UNIQUE,                
            UNIT_NAME TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""


def return_units(db_connection: sqlite3.Connection) -> Union[list[str], list]:
    """Returns the contents of the units table as lists of strings and values.

    Args:

        db_connection (sqlite3.Connection): The database connection.

    Returns:

        units_string_list (list): The Units in the table as a list of strings.

        units_values_list (list ): The Units in the table as a list of values.
    """
    sql_query = """SELECT unit_id, unit_code, unit_name FROM units"""

    units_string_list = []
    units_values_list = []

    periods_data = db_connection.return_data(sql_query)

    for period in periods_data:
        units_string_list.append(
            f"Unit Number {period[0]}: {period[2]}. Code: '{period[1]}'."
        )
        units_values_list.append((period[0], period[1], period[2]))
    return units_string_list, units_values_list


def parse_unit_data(unit_data) -> dict:
    """Returns a Unit's attributes from the database as a dictionary.

    This function is used to pass a Unit's data into the database.load_unit()
    method.

    Args:

        unit_data (list): The unit's raw data. Obtained using
        database.return_data().

    Returns:

        attributes (dict): Dictionary objects contains the attributes of
            the unit.
    """
    attributes = {}

    attributes["unit_id"] = unit_data[0][0]
    attributes["unit_code"] = unit_data[0][1]
    attributes["unit_name"] = unit_data[0][2]
    attributes["created_date"] = unit_data[0][3]
    attributes["modified_date"] = unit_data[0][4]
    attributes["modified_by"] = unit_data[0][5]

    return attributes


class Unit:
    """Defines Units and instantiates them as objects.

    This class defines Units of Measurements within the Narcotics Tracker.
    Units are used by the Medication objects to denote how amounts of that
    medication should be represented to the user and to convert the amount
    into the standard unit.

    Units can be declared, created and managed using this class. Medications
    are limited to using the units stored in the units table.

    Attributes:

        unit_id (int): Numeric identifier of each unit. Assigned by the
            database.

        unit_code (str): Unique identifier of each unit type. Assigned by the
            user. Used to interact with the unit in the database.


        unit_name (str): Proper name of the unit.

        created_date (str): The date on which the unit was first created in
            the units table.

        modified_date (str): The date on which the unit was last modified in
            the database.

        modified_by (str): Identifier of the user who last modified the
            unit in the database.

    Initializer:

        def __init__(self, builder=None) -> None:

            Initializes an instance of an Unit using the UnitBuilder.

    Instance Methods:

        __repr__: Returns a string expression of the unit.

        save: Saves a new unit to the units table in the database.

        read: Returns the data of the unit from the database as a tuple.

        update: Updates the unit in the units table of the
            database.

        return_attributes: Returns the attributes of the units object as a
            tuple.

        delete: Deletes the unit from the database.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of an Unit using the UnitBuilder.

        Units are complex objects with many attributes. The Builder
        Pattern is used to separate the creation of Units to the
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
        """Returns a string expression of the Unit.

        Returns:

            str: The string describing the Unit.
        """
        return (
            f"Unit Number {self.unit_id}: {self.unit_name}. Code: '{self.unit_code}'."
        )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new unit to the units table in the database.

        This method will not overwrite a Unit already saved in the database.
        Use the `update()` to adjust a Unit's attributes.

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

        This method makes no changes to the data.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:

            tuple: A tuple containing the unit's attribute values in the
                order of the table's columns.
        """
        sql_query = """SELECT * from units WHERE unit_code = ?"""

        values = (self.unit_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the unit in the units table of the database.

        This method will overwrite the Unit's data if it already exists within
        the database. An error will be returned if the unit_id does not
        already exist in the database. Use the save method to save new units
        in the database.

        Assigns a new modified_date.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

            unit_code (str): The unique identifier of the unit.

        Raises:

            IndexError: An Index Error will be raised if the unit_code is not
            found on the units table.

        How to use:

            1. Use the `units.return_units()` method to return a list of
                units. Identify the unit_code of the unit you wish to update.

            2. Use the database.load_unit() method, passing in the unit_code
                and assigning it to a variable to create a Unit Object.

            3. Modify the attributes as necessary and call this method on the
                Unit Object to send the new values to the database.

            #! Note: If the unit_code is being changed use the save() method
            #! to create a new unit entry in the table and use the delete
            #! method to remove the old entry.
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

    def return_attributes(self) -> tuple:
        """Returns the attributes of the Units object as a tuple.

        Returns:

            tuple: The attributes of the Units. Follows the order
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

    def delete(self, db_connection: sqlite3.Connection) -> None:
        """Deletes the Unit from the database.

        The delete method will delete the Unit from the database
        entirely.

        #! Note: Deleting an item from the database is irreversible.

        Args:

            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM units WHERE unit_id = ?"""
        values = (self.unit_id,)
        db_connection.write_data(sql_query, values)
