"""Defines the medication class."""


class Medication:
    """Model of a medication."""

    def __init__(
        self,
        name: str,
        manufacturer: str,
        ndc_number: str,
        box_quantity: int,
        container_type: str,
        fill_amount_in_milliliters: float,
        dosage_in_mg: float,
        dose_unit: str,
        concentration: float,
    ):
        """Initialize a medication."""
        self.name = name
        self.manufacturer = manufacturer
        self.ndc_number = ndc_number
        self.box_quantity = box_quantity
        self.container_type = container_type
        self.fill_amount_in_milliliters = fill_amount_in_milliliters
        self.dosage_in_mg = dosage_in_mg
        self.dose_unit = dose_unit
        self.concentration = concentration


fentanyl = Medication(
    "Fentanyl", "Umbrella Corp", "123456789", "Vial", 25, 2, 0.1, "mcg", 0.05
)
