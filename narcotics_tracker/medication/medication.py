"""Contains the Medication class."""

from narcotics_tracker.medication import containers
from narcotics_tracker.units import units
from narcotics_tracker.medication import medication_status


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
    status: medication_status.MedicationStatus = None
    created_date: str = None
    modified_date: str = None
    modified_by: str = None

    def __init__(
        self,
        builder=None,
    ) -> None:
        self.name = builder.name
        self.code = builder.code
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

    def return_table_creation_query():
        """Return the query to create the medication table."""
        return """CREATE TABLE IF NOT EXISTS medication (
                MEDICATION_ID INTEGER,
                NAME TEXT,
                CODE TEXT,
                CONTAINER_TYPE TEXT,
                FILL_AMOUNT REAL,
                DOSE REAL,
                UNIT TEXT,
                CONCENTRATION REAL,
                STATUS TEXT,
                CREATED_DATE TEXT,
                MODIFIED_DATE TEXT,
                MODIFIED_BY TEXT,
                PRIMARY KEY (CODE)
                )"""

    def return_properties(self) -> tuple:
        """Return the properties of the medication.

        Returns:
            tuple: The properties of the medication.
        """
        return (
            self.medication_id,
            self.code,
            self.name,
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

    def save(self, db_connection, sql_query, values):
        """Write the medication to the database.

        Args:
            db_connection (sqlite3.Connection): The connection to the database.
            sql_query (str): The query to be executed.
            values (tuple): The values to be inserted into the query.
        """
        db_connection.write_data(sql_query, values)
