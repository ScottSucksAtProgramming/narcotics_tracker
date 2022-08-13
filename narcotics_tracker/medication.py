"""Contains the Medication class."""

from narcotics_tracker import date
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.utils import utilities


class Medication:
    """The template for medications.

    Attributes:
        medication_id (int): Numeric identifier for the medication.
        code (str): Unique identifier for the specific medication.
        name (str): Name of the medication.
        container_type (containers.ContainerType): The type of container.
        fill_amount (float): Amount of the solvent in the container.
        dose (float): Amount of medication in the container.
        unit (units.Unit): The unit of the medication.
        concentration (float): The concentration of the medication.
        status (medication_status.MedicationStatus): The status of the
            medication.
        created_date (str): The date the medication was created.
        modified_date (str): The date the medication was last modified.
        modified_by (str): The user who last modified the medication.
    """

    medication_id: int = None
    code: str = None
    name: str = None
    container_type: containers.Container = None
    fill_amount: float = None
    dose: float = None
    unit: units.Unit = None
    concentration: float = None
    status: medication_statuses.MedicationStatus = None
    created_date: str = None
    modified_date: str = None
    modified_by: str = None

    def __init__(
        self,
        builder=None,
    ) -> None:
        self.code = builder.code
        self.name = builder.name
        self.container_type = builder.container_type
        self.fill_amount = builder.fill_amount
        self.dose = builder.dose
        self.unit = builder.unit
        self.concentration = builder.concentration
        self.status = builder.status

    def __repr__(self) -> str:
        """Return a string representation of the medication.

        Returns:
            str: The string representation of the medication.
        """
        return (
            f"Medication Object {self.medication_id} for {self.name} with "
            f"code {self.code}. Container type: {self.container_type.value}. "
            f"Fill amount: {self.fill_amount} ml. "
            f"Dose: {self.dose} {self.unit.value}. "
            f"Concentration: {self.concentration}. "
            f"Status: {self.status.value}. Created on {self.created_date}. "
            f"Last modified on {self.modified_date} by {self.modified_by}."
        )

    @staticmethod
    def return_table_creation_query():
        """Return the query to create the medication table."""
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

    def return_properties(self) -> tuple:
        """Return the properties of the medication.

        Returns:
            tuple: The properties of the medication.
        """
        return (
            self.medication_id,
            self.name,
            self.code,
            self.container_type.value,
            self.fill_amount,
            self.dose,
            self.unit.value,
            self.concentration,
            self.status.value,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )

    def created_date_is_none(self) -> bool:
        """Return whether the created date is None.

        Returns:
            bool: Returns True if the created date is None.
        """
        if self.created_date is None:
            return True
        else:
            return False

    def save(self, db_connection):
        """Write the medication to the database.

        Args:
            db_connection (sqlite3.Connection): The connection to the database.
            sql_query (str): The query to be executed.
            values (tuple): The values to be inserted into the query.
        """

        sql_query = """INSERT OR IGNORE INTO medication VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        if self.created_date_is_none():
            self.created_date = date.get_date_as_string()
        self.modified_date = date.get_date_as_string()

        values = self.return_properties()
        db_connection.write_data(sql_query, values)

    def parse_medication_data(medication_data) -> dict:

        properties = {}

        properties["medication_id"] = medication_data[0][0]
        properties["name"] = medication_data[0][1]
        properties["code"] = medication_data[0][2]
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
