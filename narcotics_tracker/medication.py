#
# * ------------------------- Documentation -------------------------------- #
# Module:  medication.py
# Contains the Medication class, and related classes.
#
#
# Modification History
# 07-27-2022 | SRK | Module Created

# ------------------------------ Tasks ------------------------------------- #
# Todo: I can create a new medication.
# Todo: I can save medication to a database.
# Todo: I can delete a medication.
# Todo: I can update a medication.
# Todo: I can retrieve a medication's properties.

from enum import Enum


class Unit(Enum):
    """Enum of dose units."""

    MG = "mg"
    MCG = "mcg"
    G = "G"


class Container(Enum):
    """Enum of medication container types."""

    VIAL = "Vial"
    AMPULE = "Ampule"
    PRE_FILLED_SYRINGE = "Pre-filled Syringe"
    PRE_MIXED_BAG = "Pre-mixed Bag"


class Medication:
    """Model of a medication."""

    def __init__(
        self,
        name: str,
        manufacturer: str,
        box_quantity: int,
        container_type: Container,
        fill_amount_in_milliliters: float,
        strength_in_milligrams: float,
        dose_unit: Unit,
        concentration: float,
    ):
        """Initialize a medication."""
        self.name = name
        self.manufacturer = manufacturer
        self.box_quantity = box_quantity
        self.container_type = container_type
        self.fill_amount_in_milliliters = fill_amount_in_milliliters
        self.strength_in_mg = strength_in_milligrams
        self.dose_unit = dose_unit
        self.concentration = concentration

    def __repr__(self) -> str:
        return (
            f"{self.name} - Manufacturer: {self.manufacturer}; Box "
            f"Quantity: {self.box_quantity}; Container Type: "
            f"{self.container_type.value}; Fill Amount: "
            f"{self.fill_amount_in_milliliters}; Strength: "
            f"{self.strength_in_mg} mg; Dose Unit: {self.dose_unit.value}; "
            f"Concentration: {self.concentration} mg/ml."
        )

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
    def dose_unit(self) -> Unit:
        """Gets the dose unit."""
        return self._dose_unit

    @dose_unit.setter
    def dose_unit(self, dose_unit: Unit):
        """Sets the dose unit."""
        if dose_unit not in Unit:
            raise TypeError("Incorrect dose unit.")
        self._dose_unit = dose_unit
