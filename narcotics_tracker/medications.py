"""Defines the medication class."""


class Medications:
    """Model of a medication."""

    def __init__(self, name, manufacturer, ndc_number, container_type, box_quantity, fill_amount_in_milliliters, dosage_in_mg, dose_unit, concentration):
        """Initialize a medication."""
        self.name = name
        self.manufacturer = manufacturer
        self.ndc_number = ndc_number
        self.container_type = container_type
        self.box_quantity = box_quantity
        self.fill_amount_in_milliliters = fill_amount_in_milliliters
        self.dosage_in_mg = dosage_in_mg
        self.dose_unit = dose_unit
        self.concentration = concentration


fentanyl = Medications("Fentanyl", "Hamdani", "123456789",
                       "Vial", 25, 2, 0.1, "mcg", 0.05)
