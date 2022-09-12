"""Contains the implementation and representation of Medication Objects.

#* Background

In order for the Narcotics Tracker to track the inventory of controlled 
substances the medications have to be defined and their attributes stored.

Medications are the back bone of this program and a lot of detail went in 
designing medications which can provide the information needed to manage an 
agency's inventory. Refer to the Medication Class documentation for a 
breakdown of the attributes.

#* Intended Use

This module and the Medication Class defined below allow for the creation of 
Medication Objects. It is highly recommended to use the Medication Builder 
Module contained within the Builders Package to create these objects. 
Instructions for using builders can be found within that package.

#* Medications in the Database

Medications are stored in the 'medications' table of the database with their 
numeric id, code, name, container type, fill amount, dose and unit of 
measurement, concentration, status and creation / modification information 
specified. Inventory Adjustments must specify which medication were effected 
and are limited to the Medications listed in the table.

#* Classes:

    Medication: Defines Medications and instantiates them as objects.

#* Functions:

    return_table_creation_query: Returns the query needed to create the table.

    return_medications: Returns the 'medications' table as lists of strings 
        and values.

    parse_medication_data: Returns a Medications's attributes as a dictionary.

    return_preferred_unit: Queries the medications table for the preferred 
        unit of the medication.
"""


import sqlite3
from typing import Union

from narcotics_tracker import database
from narcotics_tracker.utils import unit_converter


def return_table_creation_query() -> str:
    """Returns the query needed to create the 'medications' table.

    Returns:

        str: The sql query needed to create the 'medications' table.
    """
    return """CREATE TABLE IF NOT EXISTS medications (
            MEDICATION_ID INTEGER PRIMARY KEY,
            MEDICATION_CODE TEXT UNIQUE,
            NAME TEXT,
            CONTAINER_TYPE TEXT,
            FILL_AMOUNT REAL,
            DOSE_IN_MCG REAL,
            PREFERRED_UNIT TEXT,
            CONCENTRATION REAL,
            STATUS TEXT,
            CREATED_DATE INT,
            MODIFIED_DATE INT,
            MODIFIED_BY TEXT,
            FOREIGN KEY (PREFERRED_UNIT) REFERENCES units (unit_code)  ON UPDATE CASCADE,
            FOREIGN KEY (CONTAINER_TYPE) REFERENCES containers (container_code)  ON UPDATE CASCADE,
            FOREIGN KEY (STATUS) REFERENCES statuses (status_code)  ON UPDATE CASCADE
            )"""


def return_medications(db_connection: sqlite3.Connection) -> Union[list[str], list]:
    """Returns the 'medications' table as lists of strings and values.

    Args:

        db_connection (sqlite3.Connection): The database connection.

    Returns:

        medications_string_list (list[str]): The contents of the table as a
        list of strings.

        medications_values_list (list): The contents of the table as a list of
            values.
    """
    sql_query = """SELECT medication_code, name, fill_amount, dose_in_mcg, preferred_unit FROM medications"""

    medications_string_list = []
    medications_values_list = []

    medications_data = db_connection.return_data(sql_query)
    for medication in medications_data:

        if medication[4] == "g":
            converted_dose = unit_converter.UnitConverter.to_G(medication[3], "mcg")
        if medication[4] == "mg":
            converted_dose = unit_converter.UnitConverter.to_mg(medication[3], "mcg")
        else:
            converted_dose = medication[5]

        medications_string_list.append(
            f"{medication[1]} {converted_dose} {medication[4]} in {medication[2]} ml. Code: {medication[0]}."
        )
        medications_values_list.append(
            (medication[0], medication[1], medication[2], converted_dose, medication[4])
        )

    return medications_string_list, medications_values_list


def parse_medication_data(medication_data) -> dict:
    """Returns a Medications's attributes as a dictionary.

    Args:

        medication_data (list): The Medication's data.

    Returns:

        attributes (dict): Dictionary object containing the attributes of the
            Medication.
    """
    attributes = {}

    attributes["medication_id"] = medication_data[0][0]
    attributes["name"] = medication_data[0][2]
    attributes["medication_code"] = medication_data[0][1]
    attributes["container_type"] = medication_data[0][3]
    attributes["fill_amount"] = medication_data[0][4]
    attributes["dose"] = medication_data[0][5]
    attributes["unit"] = medication_data[0][6]
    attributes["concentration"] = medication_data[0][7]
    attributes["status"] = medication_data[0][8]
    attributes["created_date"] = medication_data[0][9]
    attributes["modified_date"] = medication_data[0][10]
    attributes["modified_by"] = medication_data[0][11]

    return attributes


def return_preferred_unit(
    medication_code: str, db_connection: sqlite3.Connection
) -> str:
    """Queries the medications table for the preferred unit of the medication.

    Args:

        medication_code (str): The unique identifier for the medication from
            the medications table.

        db_connection (sqlite3.Connection): The connection to the database.

    Returns:

        preferred_unit (str): The preferred unit for the medication as a
            string.
    """
    sql_query = """SELECT preferred_unit FROM medications WHERE medication_code=(?)"""
    values = [medication_code]

    preferred_unit = db_connection.return_data(sql_query, values)

    return preferred_unit[0][0]


class Medication:
    """Defines Medications and instantiates them as objects.

    This call defines Medications within the Narcotics Tracker. They
    attributes are used to calculate the amounts of each Medication in the
    inventory.

    Medications can be declared, created and managed using this class.
    Adjustments are limited to affecting the Medications stored in the
    'medications' table.

    Initializer:

        def __init__(self, builder=None) -> None:

            Initializes an instance of a Medication using the builder.

    Attributes:

        medication_id (int): The numeric identifier of the Medication in the
            database. Assigned by the database.

        code (str): The unique identifier for the specific Medication.
            Assigned by the user. Used to interact with the Medication in the
            database.

        name (str): The proper name of the Medication.

        container_type (str): The type of container the
            Medication comes in. Limited by the items stored in the
            'containers' table.

        fill_amount (float): The amount of the solvent in the container.
            Measured in milliliters (ml).

        dose (float): The amount of Medication in the container.

        preferred_unit (str): The unit of measurement the Medication is
            commonly measured in. Limited to the items stored in the 'units'
            table.

        concentration (float): The concentration of the Medication to its
            solvent.

        status (str): The status of the Medication. Limited to the items
            stored in the 'statuses' table.

        created_date (str): The date the Medication was created in the
            table.

        modified_date (str): The date the Medication was last modified.

        modified_by (str): Identifier of the person who last modified the
            Medication.

    Instance Methods:

        __repr__: Returns a string expression of the Medication object.

        save: Saves a new Medication to the table in the database.

        read: Returns the data of the Medication as a tuple.

        update: Updates the Medication in the 'medications' table.

        return_attributes: Returns the attributes of the Medication Object as
            a tuple.

        delete: Deletes the Medication from the database.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of a Medication using the builder.

        Medications are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of Medication to the Builder
        Package.

        Refer to the documentation for the MedicationBuilder Class for more
        information.

        Args:

            builder (medication_builder.MedicationBuilder): The builder used
                to construct the Medication Object.
        """

        self.medication_id = builder.medication_id
        self.medication_code = builder.medication_code
        self.name = builder.name
        self.container_type = builder.container_type
        self.fill_amount = builder.fill_amount
        self.dose = builder.dose
        self.preferred_unit = builder.unit
        self.concentration = builder.concentration
        self.status = builder.status
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """Returns a string expression of the Medication Object.

        Returns:
            str: The string describing the Medication Object.
        """

        return (
            f"{self.name} {self.dose}{self.preferred_unit} in "
            f"{self.fill_amount}ml. Code: {self.medication_code}."
        )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new Medication to the table in the database.

        This method will not overwrite a Medication already saved in the
        database. Use the `update()` to adjust a Medication's attributes.

        Assigns a created_date and modified_date.

        Args:

            db_connection (sqlite3.Connection): The database connection.
        """

        sql_query = """INSERT OR IGNORE INTO medications VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def read(self, db_connection: sqlite3.Connection) -> tuple:
        """Returns the data of the Medication as a tuple.

        This method makes no changes to the data.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:

            tuple: A tuple containing the Medication's attribute values
                in the order of the 'medications' table's columns.
        """
        sql_query = """SELECT * from medications WHERE medication_code = ?"""

        values = (self.medication_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the Medication in the 'medications' table.

        This method will overwrite the Medication's data if it already exists
        within the database. An error will be returned if the medication_code
        does
        not already exist in the database. Use the save method to save new
        Medications in the database.

        Assigns a new modified_date.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Raises:

            IndexError: An Index Error will be raised if the medication_code
            is not found on the medications table.

        How to use:

            1. Use the `medications.return_medications()` method to return a
                list of medications. Identify the medication_code of the
                medication you wish to update.

            2. Use the database.load_medication() method, passing in the
                medication_code and assigning it to a variable to create a
                Medication Object.

            3. Modify the attributes as necessary and call this method on the
                Medication Object to send the new values to the database.

            #! Note: If the medication_code is being changed use the save()
            #! method to create a new medication entry in the table and use
            #! the delete() method to remove the old entry.
        """
        sql_query = """UPDATE medications 
            SET MEDICATION_ID = ?, 
                MEDICATION_CODE = ?, 
                NAME = ?, 
                CONTAINER_TYPE = ?, 
                FILL_AMOUNT = ?, 
                DOSE_IN_MCG = ?, 
                PREFERRED_UNIT = ?, 
                CONCENTRATION = ?, 
                STATUS = ?, 
                CREATED_DATE = ?, 
                MODIFIED_DATE = ?, 
                MODIFIED_BY = ? 
            WHERE MEDICATION_CODE = ?"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes() + (self.medication_code,)

        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the Medication Object as a tuple.

        Returns:

            tuple: The attributes of the Medication. Follows the order of the
                columns in the 'medications' table.
        """
        return (
            self.medication_id,
            self.medication_code,
            self.name,
            self.container_type,
            self.fill_amount,
            self.dose,
            self.preferred_unit,
            self.concentration,
            self.status,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )

    def delete(self, db_connection: sqlite3.Connection) -> None:
        """Deletes the Medication from the database.

        The delete method will delete the Medication from the database
        entirely.

        #! Note: Deleting an item from the database is irreversible.

        Args:

            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM medications WHERE medication_id = ?"""
        values = (self.medication_id,)
        db_connection.write_data(sql_query, values)
