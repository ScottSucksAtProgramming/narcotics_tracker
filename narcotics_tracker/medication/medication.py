"""Contains the Medication class."""

# ------------------------------ Tasks ------------------------------------- #

from narcotics_tracker.medication import containers
from narcotics_tracker.units import units
from narcotics_tracker.medication import medication_status

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
            f"Medication Object for {self.name} with code {self.code}."
            f"Container type: {self.container_type.value}"
            f"Fill amount: {self.fill_amount} ml"
            f"Dose: {self.dose} {self.unit.value}"
            f"Concentration: {self.concentration}"
            f"Status: {self.status.value}"
        )

    def return_table_creation_query():
        return """CREATE TABLE IF NOT EXISTS medication (
                NAME TEXT,
                CODE TEXT,
                CONTAINER_TYPE TEXT,
                FILL_AMOUNT REAL,
                DOSE REAL,
                UNIT TEXT,
                CONCENTRATION REAL,
                STATUS TEXT,
                PRIMARY KEY (CODE)
                )"""

    # def calculate_standard_dose(self, dose: int, unit: units.Unit) -> float:
    #     """Calculates the standard dose of the medication.

    #     Args:
    #         dose (float): The dose of the medication.
    #         unit (Unit): The unit of the dose.

    #     Returns:
    #         float: The standard dose of the medication.
    #     """

    #     return unit_converter.UnitConverter.to_mcg(dose, unit.value)

    # @property
    # def name(self) -> str:
    #     """Returns the name of the medication."""
    #     return self.name

    # @property
    # def code(self) -> str:
    #     """Returns the code of the medication."""
    #     return self.code

    # @property
    # def container_type(self) -> containers.Container:
    #     """Gets the container type."""
    #     return self.container_type

    # @property
    # def dose(self) -> float:
    #     """Returns the dose of the medication."""
    #     return self.dose

    # @property
    # def unit(self) -> units.Unit:
    #     """Gets the dose unit."""
    #     return self.unit

    # @property
    # def fill_amount(self) -> str:
    #     """Returns the fill_amount of the medication."""
    #     return self.fill_amount

    # @property
    # def concentration(self) -> float:
    #     """Returns the concentration of the medication."""
    #     return self.concentration

    # @property
    # def status(self) -> medication_status.MedicationStatus:
    #     """Gets the medication' status."""
    #     return self.status
