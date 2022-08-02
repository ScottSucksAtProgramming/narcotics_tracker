"""Contains the Medication class."""

# ------------------------------ Tasks ------------------------------------- #


from narcotics_tracker.medication import containers
from narcotics_tracker.units import units
from narcotics_tracker.medication import medication_status


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
        container_type: containers.Container,
        fill_amount: float,
        dose: float,
        unit: units.Unit,
        concentration: float,
        status: medication_status.MedicationStatus,
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
            f"Medication Object for {self.code}: {self.name} - {self.dose}"
            f"{self.unit.value} in a {self.fill_amount}ml "
            f"{self.container_type.value} ({self.concentration}"
            f"{self.unit.value}/ml) - Status: {self.status.value} - Created "
            f"on: {self.created_date} - Last Modified on: "
            f"{self.modified_date} by {self.modified_by}."
        )

    @property
    def container_type(self) -> containers.Container:
        """Gets the container type."""
        return self._container_type

    @container_type.setter
    def container_type(self, container_type: containers.Container):
        """Sets the medication's container type. Ensures that the container
        type is valid."""
        if container_type not in containers.Container:
            raise TypeError("Incorrect container type.")
        self._container_type = container_type

    @property
    def unit(self) -> units.Unit:
        """Gets the dose unit."""
        return self._unit

    @unit.setter
    def unit(self, unit: units.Unit):
        """Sets the medication's unit. Ensures that the unit is valid."""
        if unit not in units.Unit:
            raise TypeError("Incorrect dose unit.")
        self._unit = unit

    @property
    def status(self) -> medication_status.MedicationStatus:
        """Gets the medication' status."""
        return self._status

    @status.setter
    def status(self, status: medication_status.MedicationStatus):
        """Sets the medication's status. Ensures that the status is valid."""
        if status not in medication_status.MedicationStatus:
            raise TypeError("Incorrect medication status entered.")
        self._status = status
