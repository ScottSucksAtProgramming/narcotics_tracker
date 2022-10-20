"""Handles conversion between different units.

Classes:
    UnitConverter: Converts between different units of measurement.
"""


from typing import Union


class UnitConverter:
    """Converts between different units of measurement.

    Methods:

        to_standard: Converts the amount from the preferred to standard unit.

        to_preferred: Converts the amount from the standard to preferred unit.

        to_milliliters: Converts and returns the amount in milliliters.
    """

    def __init__(
        self,
        amount: Union[int, float],
        preferred_unit: str,
        concentration: float = None,
    ) -> None:
        """Sets the amount and preferred_unit.

        Args:
            amount (int / float): Amount to be converted.

            preferred_unit (str): The preferred unit of measurement's
                abbreviation. Must be 'g' mg' 'mcg' or, 'ml'.

            concentration (float, optional): Medications concentration. Needed
                for unit to milliliter conversion.
        """
        self.amount = amount
        self.preferred_unit = preferred_unit
        self.concentration = concentration or None

    def to_standard(self) -> int:
        """Converts the amount from the preferred to standard unit.

        Returns:
            int: The converted amount.
        """
        decimals = {"mcg": -6, "mg": -3, "g": 0}
        exponent = decimals[self.preferred_unit] + 6

        return self.amount * (10**exponent)

    def to_preferred(self) -> int:
        """Converts the amount from the standard to preferred unit."""
        decimals = {"mcg": 6, "mg": 3, "g": 0}

        exponent = decimals[self.preferred_unit] - 6
        return self.amount * (10**exponent)

    def to_milliliters(self) -> float:
        """Converts and returns the amount in milliliters."""

        adjusted_amount = self.to_preferred()

        return adjusted_amount / self.concentration
