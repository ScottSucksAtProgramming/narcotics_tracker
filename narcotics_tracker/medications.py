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


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the medication table."""
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


def return_medication(db_connection: sqlite3.Connection) -> list[str]:
    """Returns the contents of the medications table as a list of strings.

    Args:
        db_connection (sqlite3.Connection): The database connection.

    Returns:
        table_contents (list[str]): The contents of the table as a list of
            strings.
    """
    sql_query = """SELECT * FROM medications"""

    medications_list = []

    medications_data = db_connection.return_data(sql_query)
    for event in medications_data:
        medications_list.append(
            f"{event[2]} {event[5]} {event[6]} in {event[4]} ml. Code: {event[1]}."
        )

    return medications_list


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
    properties["medication_code"] = medication_data[0][1]
    properties["container_type"] = medication_data[0][3]
    properties["fill_amount"] = medication_data[0][4]
    properties["dose"] = medication_data[0][5]
    properties["unit"] = medication_data[0][6]
    properties["concentration"] = medication_data[0][7]
    properties["status"] = medication_data[0][8]
    properties["created_date"] = medication_data[0][9]
    properties["modified_date"] = medication_data[0][10]
    properties["modified_by"] = medication_data[0][11]

    return properties


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
        """Returns a string expression of the medication object.

        Returns:
            str: The string describing the medication object
        """

        return (
            f"{self.name} {self.dose}{self.preferred_unit} in "
            f"{self.fill_amount}ml. Code: {self.medication_code}."
        )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new medication to the database.

        The save method will only write the medication into the table if it
        does not already exist. Use the update method to update the
        medication'a attributes.

        Uses the date module to set the created if it is None. Sets the
        modified date.

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
        """Returns the data of the medication from the database as a tuple.

        This function will make no changes to the data.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:
            tuple: A tuple containing the medication's attribute values.
        """
        sql_query = """SELECT * from medications WHERE medication_code = ?"""

        values = (self.medication_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection, code: str) -> None:
        """Updates an existing medication in the database.

        This method will overwrite the medication's data if it already
        exists within the database. Sets the modified date, and will set the
        created date if it is None.

        Use the save method to create a new medication.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

            code (str): The unique identifier for the medication.
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

        values = self.return_attributes() + (code,)

        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the medication as a tuple.

        Returns:
            tuple: The attributes of the medication. Follows the order of the
                columns in the medication table.
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
        """Deletes the medication from the database.

        This function deletes the medication from the database entirely.

        #! Important: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM medications WHERE medication_id = ?"""
        values = (self.medication_id,)
        db_connection.write_data(sql_query, values)
