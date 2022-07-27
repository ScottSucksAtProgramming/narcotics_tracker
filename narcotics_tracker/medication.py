#
# * ----------------------------- Documentation ------------------------------ #
# Module:  medication.py
# Contains the Medication class, and related classes.
#
#
# Modification History
# 07-27-2022 | SRK | Module Created


from enum import Enum


class Container(Enum):
    """Enum of medication container types."""

    VIAL = "Vial"
    AMPULE = "Ampule"
    PRE_FILLED_SYRINGE = "Pre-filled Syringe"
    PRE_MIXED_BAG = "Pre-mixed Bag"


class DoseUnit(Enum):
    """Enum of dose units."""

    MG = "mg"
    MCG = "mcg"
    G = "G"


class Medication:
    """Model of a medication."""

    def __init__(
        self,
        name: str,
        manufacturer: str,
        ndc_number: str,
        box_quantity: int,
        container_type: Container,
        fill_amount_in_milliliters: float,
        strength_in_mg: float,
        dose_unit: DoseUnit,
        concentration: float,
    ):
        """Initialize a medication."""
        self.name = name
        self.manufacturer = manufacturer
        self.ndc_number = ndc_number
        self.box_quantity = box_quantity
        self.container_type = container_type
        self.fill_amount_in_milliliters = fill_amount_in_milliliters
        self.strength_in_mg = strength_in_mg
        self.dose_unit = dose_unit
        self.concentration = concentration

    @property
    def container_type(self) -> Container:
        """Gets the container type."""
        return self._container_type

    @container_type.setter
    def container_type(self, container_type: Container):
        """Sets the container type."""
        if container_type not in Container:
            raise TypeError("Incorrect container type.")
        self._container_type = container_type

    @property
    def dose_unit(self) -> DoseUnit:
        """Gets the dose unit."""
        return self._dose_unit

    @dose_unit.setter
    def dose_unit(self, dose_unit: DoseUnit):
        """Sets the dose unit."""
        if dose_unit not in DoseUnit:
            raise TypeError("Incorrect dose unit.")
        self._dose_unit = dose_unit


"""
What can I do with a medication?
- I can create a new medication.
- I can delete a medication.
- I can update a medication.
- I can retrieve a medication's properties.

Inventory Management - This like likely going to be a different class.
- I can order a medication.
- I can waste a medication.
- I can destroy a medication.
"""
