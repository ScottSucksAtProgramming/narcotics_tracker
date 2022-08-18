"""Contains the UnitConverter class which converts between units.

Classes:
    UnitConverter: Converts between different units of measurement.
"""
from narcotics_tracker.enums.units import Unit


class UnitConverter:
    """Converts between different units of measurement.

    Methods:
        to_mcg: Converts from a specified unit to micrograms.
        to_mg: Converts from a specified unit to milligrams.
        to_G: Converts from a specified unit to grams.
    """

    def to_mcg(amount: float, unit: Unit) -> float:
        """Converts from a specified unit to micrograms.

        Args:
            amount (float): The amount to convert.

        Returns:
            amount (float): The amount converted to micrograms.
        """
        if unit == Unit.MG.value:
            return amount * 10**3

        elif unit == Unit.G.value:
            return amount * 10**6

        elif unit == Unit.MCG.value:
            return amount

    def to_mg(amount: float, unit: Unit) -> float:
        """Converts from a specified unit to milligrams.

        Args:
            amount (float): The amount to convert.

        Returns:
            float: The amount converted to milligrams.
        """
        if unit == Unit.G.value:
            return amount * 10**3

        elif unit == Unit.MCG.value:
            return amount / 10**3

        elif unit == Unit.MG.value:
            return amount

    def to_G(amount: float, unit: Unit) -> float:
        """Converts from a specified unit to grams.

        Args:
            amount (float): The amount to convert.

        Returns:
            float: The amount converted to Grams.
        """
        if unit == Unit.MG.value:
            return amount / 10**3

        elif unit == Unit.MCG.value:
            return amount / 10**6

        elif unit == Unit.G.value:
            return amount
