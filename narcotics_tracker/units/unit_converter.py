#
# * ------------------------ Documentation --------------------------------- #
# Module:  unit_converter.py
# This module will convert units of measurement.
#
#
# Modification History
# 07-30-2022 | SRK | Module Created

# ------------------------------ Tasks ------------------------------------- #
# Todo: We're gonna switch the program to always think in mcg. Allowing us to represent the values as integers, and use the converter to just move the decimal for the user.

from narcotics_tracker.units.units import Unit


class UnitConverter:
    """Utility to convert between units of medication dosages."""

    def to_mcg(amount: float, unit: Unit) -> float:
        """Converts dose to micrograms.

        Args:
            amount (float)

        Returns:
            float: amount in mcg
        """
        if unit == Unit.MG.value:
            return amount * 10**3

        elif unit == Unit.G.value:
            return amount * 10**6

        elif unit == Unit.MCG.value:
            return amount

    def to_mg(amount: float, unit: Unit) -> float:
        """Converts dose to milligrams.

        Args:
            amount (float)

        Returns:
            float: amount in milligrams.
        """
        if unit == Unit.G.value:
            return amount * 10**3

        elif unit == Unit.MCG.value:
            return amount / 10**3

        elif unit == Unit.MG.value:
            return amount

    def to_G(amount: float, unit: Unit) -> float:
        """Converts dose to Grams.

        Args:
            amount (float)

        Returns:
            float: amount in Grams.
        """
        if unit == Unit.MG.value:
            return amount / 10**3

        elif unit == Unit.MCG.value:
            return amount / 10**6

        elif unit == Unit.G.value:
            return amount
