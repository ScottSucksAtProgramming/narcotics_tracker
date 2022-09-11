"""Assists in converting medications between different units of measurement.

Classes:
    UnitConverter: Converts between different units of measurement.
"""


class UnitConverter:
    """Converts between different units of measurement.

    Methods:
        to_mcg: Converts from a specified unit to micrograms.
        to_mg: Converts from a specified unit to milligrams.
        to_G: Converts from a specified unit to grams.
    """

    def to_mcg(amount: float, starting_unit: str) -> float:
        """Converts from a specified unit to micrograms.

        Args:
            amount (float): The amount to convert.

            unit

        Returns:
            amount (float): The amount converted to micrograms.
        """
        if starting_unit == "mg":
            return amount * 10**3

        elif starting_unit == "g":
            return amount * 10**6

        elif starting_unit == "mcg":
            return amount

    def to_mg(amount: float, starting_unit: str) -> float:
        """Converts from a specified unit to milligrams.

        Args:
            amount (float): The amount to convert.

        Returns:
            float: The amount converted to milligrams.
        """
        if starting_unit == "g":
            return amount * 10**3

        elif starting_unit == "mcg":
            return amount / 10**3

        elif starting_unit == "mg":
            return amount

    def to_G(amount: float, starting_unit: str) -> float:
        """Converts from a specified unit to grams.

        Args:
            amount (float): The amount to convert.

        Returns:
            float: The amount converted to Grams.
        """
        if starting_unit == "mg":
            return amount / 10**3

        elif starting_unit == "mcg":
            return amount / 10**6

        elif starting_unit == "g":
            return amount
