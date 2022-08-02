"""Contains the Medication class."""

# ------------------------------ Tasks ------------------------------------- #


from narcotics_tracker.medication.containers import Container
from narcotics_tracker.units.units import Unit
from narcotics_tracker.medication.medication_status import MedicationStatus


class Medication:
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
        created_date (str): The date the medication was added to the database.
        modified_date (str): The date the medication was last modified in the
            database.
        modified_by (str): The user that last modified the medication.
    """

    def __init__(
        self,
        name: str,
        code: str,
        container_type: Container,
        fill_amount: float,
        dose: float,
        unit: Unit,
        concentration: float,
        status: MedicationStatus,
        created_date: str,
        modified_date: str,
        modified_by: str,
    ):
        """Initializes a Medication object."""

        self.name = name
        self.code = code
        self.container_type = container_type
        self.fill_amount = fill_amount
        self.dose = dose
        self.unit = unit
        self.concentration = concentration
        self.status = status
        self.created_date = created_date
        self.modified_date = modified_date
        self.modified_by = modified_by

    def __repr__(self) -> str:
        return (
            f"{self.code}: {self.name} - {self.dose}{self.unit.value} "
            f"in a {self.fill_amount}ml {self.container_type.value} "
            f"({self.concentration}{self.unit.value}/ml) - Status: "
            f"{self.status.value} - Created on: {self.created_date} - Last "
            f"Modified on: {self.modified_date} by {self.modified_by}."
        )

    @property
    def container_type(self) -> Container:
        """Gets the container type."""
        return self._container_type

    @container_type.setter
    def container_type(self, container_type: Container):
        """Sets the medication's container type. Ensures that the container
        type is valid."""
        if container_type not in Container:
            raise TypeError("Incorrect container type.")
        self._container_type = container_type

    @property
    def unit(self) -> Unit:
        """Gets the dose unit."""
        return self._unit

    @unit.setter
    def unit(self, unit: Unit):
        """Sets the medication's unit. Ensures that the unit is valid."""
        if unit not in Unit:
            raise TypeError("Incorrect dose unit.")
        self._unit = unit

    @property
    def status(self) -> MedicationStatus:
        """Gets the medication' status."""
        return self._status

    @status.setter
    def status(self, status: MedicationStatus):
        """Sets the medication's status. Ensures that the status is valid."""
        if status not in MedicationStatus:
            raise TypeError("Incorrect medication status entered.")
        self._status = status
