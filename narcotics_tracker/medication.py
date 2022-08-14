"""Contains the Medication class."""

from narcotics_tracker import database, date
from narcotics_tracker.builders import builder
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.utils import utilities


class Medication:
    """The template for medications.

    Attributes:
        medication_id (int): Numeric identifier for the medication.
        code (str): Unique identifier for the specific medication.
        name (str): Name of the medication.
        container_type (containers.Container): The type of container.
        fill_amount (float): Amount of the solvent in the container.
        dose (float): Amount of medication in the container.
        preferred_unit (units.Unit): The unit the medication is referred by.
        concentration (float): The concentration of the medication.
        status (medication_status.MedicationStatus): The status of the
            medication.
        created_date (str): The date the medication was created.
        modified_date (str): The date the medication was last modified.
        modified_by (str): The user who last modified the medication.
    """

    def __init__(self, builder=None) -> None:
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
        """Returns a string representation of the medication.

        Returns:
            str: The string representation of the medication.
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

    @staticmethod
    def return_table_creation_query():
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

    def return_attributes(self) -> tuple:
        """Returns the attributes of the medication as a tuple.

        Returns:
            tuple: The attributes of the medication.
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

    @staticmethod
    def parse_medication_data(medication_data) -> dict:
        """Converts the medication data from a sql query to a dictionary which
        can be used to load a new medication object.

        Args:
            medication_data (list): The medication data

        Returns:
            properties (dict): Dictionary objects contains the properties of
                the medication."""

        properties = {}

        properties["medication_id"] = medication_data[0][0]
        properties["name"] = medication_data[0][2]
        properties["code"] = medication_data[0][1]
        properties["container_type"] = utilities.Utilities.enum_from_string(
            containers.Container, medication_data[0][3]
        )
        properties["fill_amount"] = medication_data[0][4]
        properties["dose"] = medication_data[0][5]
        properties["unit"] = utilities.Utilities.enum_from_string(
            units.Unit, medication_data[0][6]
        )
        properties["concentration"] = medication_data[0][7]
        properties["status"] = utilities.Utilities.enum_from_string(
            medication_statuses.MedicationStatus, medication_data[0][8]
        )
        properties["created_date"] = medication_data[0][9]
        properties["modified_date"] = medication_data[0][10]
        properties["modified_by"] = medication_data[0][11]

        return properties

    def save(self, db_connection):
        """Writes the medication to the database.

        Will only write the medication if it does not already exist. Use the
            update method to update the medication.

        Args:
            db_connection (sqlite3.Connection): The connection to the database.
        """

        sql_query = """INSERT OR IGNORE INTO medication VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = date.get_date_as_string()
        self.modified_date = date.get_date_as_string()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def delete(self, db_connection):
        """Delete the medication from the database.

        Args:
            db_connection (sqlite3.Connection): The connection to the database.
            sql_query (str): The query to be executed.
            values (tuple): The values to be inserted into the query.
        """

        sql_query = """DELETE FROM medication WHERE medication_id = ?"""
        values = (self.medication_id,)
        db_connection.write_data(sql_query, values)

    def load(db_connection, code):

        sql_query = """SELECT * FROM medication WHERE CODE = ?"""
        values = (code,)

        result = db_connection.read_data(sql_query, values)
        medication_data = Medication.parse_medication_data(result)

        medication_builder = builder.MedicationBuilder()
        medication_builder.set_all_properties(medication_data)
        loaded_med = medication_builder.build()

        return loaded_med

    def update(self, db_connection, code):
        """Updates new medication data to an existing medication.

        Will overwrite the medication if it already exists. Use the save
        method to create a new medication.

        Args:
            db_connection (sqlite3.Connection): The connection to the database.
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
            self.created_date = date.get_date_as_string()
        self.modified_date = date.get_date_as_string()

        values = self.return_attributes() + (code,)

        db_connection.write_data(sql_query, values)
