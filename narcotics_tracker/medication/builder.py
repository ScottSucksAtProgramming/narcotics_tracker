"""Contains the MedicationBuilder class."""

# ------------------------------ Tasks ------------------------------------- #


from narcotics_tracker.medication import (
    abstract_builder,
    containers,
    medication,
    medication_status,
)
from narcotics_tracker.units import units, unit_converter


class MedicationBuilder(abstract_builder.Builder):
    """The MedicationBuilder class builds a medication."""

    def __init__(self) -> None:
        pass

    def reset(self) -> None:
        self._medication = medication.Medication()

    @property
    def build(self) -> medication.Medication:
        self.calculate_concentration()

        return medication.Medication(self)

    def set_name(self, name: str):
        self.name = name

    def set_code(self, code: str):
        """Sets the unique code of the medication.

        Example: Fentanyl -> fent1, fent2, morph1, midaz5

        Args:
            code (str): Identifier for this specific medication instance.
        """
        self.code = code

    def set_container_type(self, container_type: containers.Container):
        """Sets the medication's container type.

        Ensures that the container is valid. Acceptable container types are:
            Container.VIAL,
            Container.AMPULE,
            Container.PRE_FILLED_SYRINGE,
            Container.PRE_MIXED_BAG

        Args:
            container_type (containers.Container): The type of container the
                medication comes in.

        Raises:
            TypeError: Raised if the container type is invalid.
        """
        if container_type not in containers.Container:
            raise TypeError("Incorrect container type.")
        self.container_type = container_type

    def set_dose_and_unit(self, dose: float, unit: units.Unit):
        """Sets the medication's dose and unit.

        Ensures that the unit is valid. Acceptable unit types are:
            Unit.MCG,
            Unit.MG,
            Unit.G,

        Args:
            dose (float): The amount of medication in the container.
            unit (units.Unit): The unit the medication is commonly referred
                by.

        Raises:
            TypeError: Raised if the unit is invalid.
        """
        if unit not in units.Unit:
            raise TypeError("Incorrect unit type.")

        self.dose = unit_converter.UnitConverter.to_mcg(dose, unit.value)
        self.unit = unit

    def set_fill_amount(self, fill_amount: float):
        self.fill_amount = fill_amount

    def calculate_concentration(
        self,
    ):
        """
        Calculates the concentration of the medication.
        """

        self.concentration = self.dose / self.fill_amount

    def set_status(self, status: medication_status.MedicationStatus):
        """Sets the medication's status.

        Ensures that the status is valid. Acceptable status types are:
            MedicationStatus.ACTIVE,
            MedicationStatus.INACTIVE,
            MedicationStatus.DISCONTINUED,

            Args:
                status (medication_status.MedicationStatus): The status of the
                    medication.

            Raises:
                TypeError: Raised if the status is invalid."""

        if status not in medication_status.MedicationStatus:
            raise TypeError("Incorrect status type.")
        self.status = status
