"""Contains the Medication class."""

# ------------------------------ Tasks ------------------------------------- #

from narcotics_tracker.medication import containers
from narcotics_tracker.units import units
from narcotics_tracker.medication import medication_status
from narcotics_tracker.database import database


"""The Medication Class contains templates for an agency's medications.

Each EMS agency will have a set of controlled substance medications they
use as part of their narcotics program. This class will create medication
objects for each medication allowing them to be edited, retrieved, and
interacted with. It will also allow for medications to be saved to a the
database.

Attributes:
    name (str): The name of the medication.
    code (str): Unique identifier for the specific medication
        object.
    container_type (Container): The type of container the medication comes
        in.
    fill_amount (float): The amount of milliliters the medication is
        dissolved in. Always specified in milliliters.
    dose (float): The total amount of the medication in the container.
        Always represented in micrograms.
    unit (Unit): The unit in which the medication is described.
    concentration (float): The concentration of the medication within the
        container.
    status (MedicationStatus): The stats of the medication.
"""


class Medication:
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

    def save_to_database(self, sql_query, values):
        db = database.Database()
        db.connect("inventory.db")
        db.write_data(sql_query, values)
