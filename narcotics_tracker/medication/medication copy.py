"""Contains the MedicationBuilder class."""

# ------------------------------ Tasks ------------------------------------- #


from abc import ABC, abstractmethod
from narcotics_tracker.medication import containers, medication
from narcotics_tracker.units import units, unit_converter
from narcotics_tracker.medication import medication_status


class MedicationBuilder(ABC):
    """
    The MedicationBuilder interface defines methods to build a medication.
    """

    name = None
    code = None
    container_type = None
    fill_amount = None
    dose = None
    unit = None
    concentration = None
    status = None
    created_date = None
    modified_date = None
    modified_by = None

    def __init__(self, name: str):
        self.name = name

    def set_container_type(self, container_type: containers.Container):
        if container_type not in containers.Container:
            raise TypeError("Incorrect container type.")
        self.container_type = container_type

    def set_code(self, code: str):
        self.code = code

    def set_dose_and_unit(self, dose: float, unit: units.Unit):
        if unit not in units.Unit:
            raise TypeError("Incorrect unit type.")

        self.dose = unit_converter.UnitConverter.to_mcg(dose, unit.value)
        self.unit = unit

    def set_fill_amount(self, fill_amount: float):
        self.fill_amount = fill_amount

    def set_concentration(self, concentration: float):
        self.concentration = concentration

    def set_status(self, status: medication_status.MedicationStatus):
        if status not in medication_status.MedicationStatus:
            raise TypeError("Incorrect status type.")
        self.status = status

    def finalize(self):
        """
        Returns a Medication object.
        """
        return medication.Medication(
            self.name,
            self.code,
            self.container_type,
            self.fill_amount,
            self.dose,
            self.unit,
            self.concentration,
            self.status,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )
