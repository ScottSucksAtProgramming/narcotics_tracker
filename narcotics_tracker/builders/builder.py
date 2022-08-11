"""Contains the ObjectBuilder class."""


from narcotics_tracker import medication
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.utils import unit_converter
from narcotics_tracker.builders import abstract_builder


class ObjectBuilder(abstract_builder.MedicationBuilder):
    """Builds an object using the specified abstract builder."""

    def __init__(self) -> None:
        pass

    def set_medication_id(self, medication_id) -> None:
        self.medication_id = medication_id

    def set_name(self, name: str) -> None:
        self.name = name

    def set_code(self, code: str) -> None:
        """Sets the unique code of the medication.

        Example: Fentanyl -> fent1, fent2, morph1, midaz5

        Args:
            code (str): Identifier for this specific medication instance.
        """
        self.code = code

    def set_container(self, container_type: containers.Container) -> None:
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

    def set_fill_amount(self, fill_amount: float) -> None:

        self.fill_amount = fill_amount

    def set_dose_and_unit(self, dose: float, unit: units.Unit) -> None:
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

    def set_concentration(self, concentration: float) -> None:
        self.concentration = concentration

    def set_status(self, status: medication_statuses.MedicationStatus) -> None:
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

        if status not in medication_statuses.MedicationStatus:
            raise TypeError("Incorrect status type.")
        self.status = status

    def set_created_date(self, created_date: str) -> None:
        self.created_date = created_date

    def set_modified_date(self, modified_date: str) -> None:
        self.modified_date = modified_date

    def set_modified_by(self, modified_by: str) -> None:
        self.modified_by = modified_by

    def calculate_concentration(self):
        """Calculates the concentration of the medication."""

        self.concentration = self.dose / self.fill_amount

    def set_all_properties(self, properties: dict) -> None:
        """Sets all properties of the medication.

        Args:
            properties (dict): The properties of the medication.
        """
        self.set_medication_id(properties["medication_id"])
        self.set_name(properties["name"])
        self.set_code(properties["code"])
        self.set_container(properties["container_type"])
        self.set_fill_amount(properties["fill_amount"])
        self.set_dose_and_unit(properties["dose"], properties["unit"])
        self.set_concentration(properties["concentration"])
        self.set_status(properties["status"])
        self.set_created_date(properties["created_date"])
        self.set_modified_date(properties["modified_date"])
        self.set_modified_by(properties["modified_by"])

    def reset(self) -> None:
        self._medication = medication.Medication()

    @property
    def build(self) -> medication.Medication:
        self.calculate_concentration()

        return medication.Medication(self)