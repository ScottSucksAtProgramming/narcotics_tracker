"""Contains the UnitConverter class."""

from narcotics_tracker.enums.units import Unit


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
