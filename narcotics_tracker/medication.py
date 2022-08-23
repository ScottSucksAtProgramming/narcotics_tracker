"""Defines the representation of controlled substance medications.

Inventory tracking of controlled substance medications requires information 
from the medications themselves. This module defines the Medication class 
which stores the information needed to track medications. The Medication class 
also handles the saving, updating and deleting of medications from the 
database.

See the builder module for information on creating medications.
See the database module for information on interacting with the database.
Tests are located in the tests/unit/medication_tests.py file.

Classes:

    Medication: Represents controlled substance medications.

Functions:

    return_table_creation_query: Returns query to create medication table.

    parse_medication_data: Returns medication data from database as dictionary.
"""


import sqlite3

from narcotics_tracker import database
from narcotics_tracker.builders import medication_builder
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.utils import date, utilities


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the medication table."""

    return """CREATE TABLE IF NOT EXISTS medication (
            MEDICATION_ID INTEGER PRIMARY KEY,
            CODE TEXT UNIQUE,                
            NAME TEXT,
            CONTAINER_TYPE TEXT,
            FILL_AMOUNT REAL,
            DOSE REAL,
            UNIT TEXT,
            CONCENTRATION REAL,
            STATUS TEXT,
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT
            )"""


def parse_medication_data(medication_data) -> dict:
    """Returns medication data from the database as a dictionary.

    Args:
        medication_data (list): The medication data

    Returns:
        properties (dict): Dictionary objects contains the properties of
            the medication."""

    properties = {}

    properties["medication_id"] = medication_data[0][0]
    properties["name"] = medication_data[0][2]
    properties["code"] = medication_data[0][1]
    properties["container_type"] = utilities.enum_from_string(
        containers.Container, medication_data[0][3]
    )
    properties["fill_amount"] = medication_data[0][4]
    properties["dose"] = medication_data[0][5]
    properties["unit"] = utilities.enum_from_string(units.Unit, medication_data[0][6])
    properties["concentration"] = medication_data[0][7]
    properties["status"] = utilities.enum_from_string(
        medication_statuses.MedicationStatus, medication_data[0][8]
    )
    properties["created_date"] = medication_data[0][9]
    properties["modified_date"] = medication_data[0][10]
    properties["modified_by"] = medication_data[0][11]

    return properties


class Medication:
    """Represents controlled substance medications in the Narcotics Tracker.

    Each medication has attributes that assist in tracking the medication
    including it's dose, fill amount, and concentration. This class defines
    the attributes and behaviors of controlled substance medications and
    handles the storing, updating and deletion of medication data within the
    database. Any aspect related to medication should be handled by this
    class.

    Initializer:

        def __init__(self, builder=None) -> None:

            Initializes the medication object using the MedicationBuilder.

            Medications are complex objects with many attributes. The Builder
            Pattern was used to separate the creation of medications to the
            Builder Package. Refer to the documentation for the
            MedicationBuilder for more information.

            Args:
                builder (builder.MedicationMedicationBuilder): The builder
                    used to construct the medication object.

    Attributes:

        medication_id (int): The numeric identifier of the medication in the
            database.

        code (str): The unique identifier for the specific medication.

        name (str): The name of the medication.

        container_type (containers.Container): The type of container the
            medication comes in.

        fill_amount (float): The amount of the solvent in the container.
            Measured in milliliters (ml).

        dose (float): The amount of medication in the container.

        preferred_unit (units.Unit): The unit of measurement the medication is
            commonly measured in.

        concentration (float): The concentration of the medication to its
            solvent.

        status (medication_status.MedicationStatus): The status of the
            medication.

        created_date (str): The date the medication was first entered into the
            database.

        modified_date (str): The date the medication was last modified in the
            database

        modified_by (str): The user who last modified the medication in the
            database.

    Instance Methods:

        __repr__: Returns a string expression of the medication object.

        save: Saves a new medication to the database.

        update: Updates an existing medication in the database.

        delete: Deletes a medication from the database.

        return_attributes: Returns a medication's attributes.

    Static Methods:

        parse_medication_data: Converts medication data into a dictionary.

        return_table_creation_query: Returns SQL query to for medication table.

    """

    def __init__(self, builder=None) -> None:
        """Initializes the medication object using the MedicationBuilder.

        Medications are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of medications to the
        Builder Package. Refer to the documentation for the MedicationBuilder
        for more information.

        Args:
            builder (builder.MedicationBuilder): The builder used to
            construct the medication object.
        """

        self.medication_id = builder.medication_id
        self.code = builder.code
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
        """Returns a string expression of the medication object.

        Returns:
            str: The string describing the medication object
        """

        return (
            f"Medication Object {self.medication_id} for {self.name} with "
            f"code {self.code}. Container type: {self.container_type.value}. "
            f"Fill amount: {self.fill_amount} ml. "
            f"Dose: {self.dose} {self.preferred_unit.value}. "
            f"Concentration: {self.concentration}. "
            f"Status: {self.status.value}. Created on {self.created_date}. "
            f"Last modified on {self.modified_date} by {self.modified_by}."
        )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new medication to the database.

        The save method will only write the medication into the table if it
        does not already exist. Use the update method to update the
        medication'a properties.

        Uses the date module to set the created if it is None. Sets the
        modified date.

        Args:
            db_connection (sqlite3.Connection): The database connection.
        """

        sql_query = """INSERT OR IGNORE INTO medication VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = date.return_date_as_string()
        self.modified_date = date.return_date_as_string()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def update(self, db_connection: sqlite3.Connection, code: str) -> None:
        """Updates an existing medication in the database.

        The update method will overwrite the medication data if it already
        exists within the database. Use the save method to create a new
        medication.

        Sets the modified date, and will set the created date if it is None.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

            code (str): The unique identifier for the medication.
        """

        sql_query = """UPDATE medication 
            SET MEDICATION_ID = ?, 
                CODE = ?, 
                NAME = ?, 
                CONTAINER_TYPE = ?, 
                FILL_AMOUNT = ?, 
                DOSE = ?, 
                UNIT = ?, 
                CONCENTRATION = ?, 
                STATUS = ?, 
                CREATED_DATE = ?, 
                MODIFIED_DATE = ?, 
                MODIFIED_BY = ? 
            WHERE CODE = ?"""

        if database.Database.created_date_is_none(self):
            self.created_date = date.return_date_as_string()
        self.modified_date = date.return_date_as_string()

        values = self.return_attributes() + (code,)

        db_connection.write_data(sql_query, values)

    def delete(self, db_connection: sqlite3.Connection):
        """Delete the medication from the database.

        The delete will delete the medication from the database entirely.
        Note: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """

        sql_query = """DELETE FROM medication WHERE medication_id = ?"""
        values = (self.medication_id,)
        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the medication as a tuple.

        Returns:
            tuple: The attributes of the medication. Follows the order of the
                columns in the medication table.
        """

        return (
            self.medication_id,
            self.code,
            self.name,
            self.container_type.value,
            self.fill_amount,
            self.dose,
            self.preferred_unit.value,
            self.concentration,
            self.status.value,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )
