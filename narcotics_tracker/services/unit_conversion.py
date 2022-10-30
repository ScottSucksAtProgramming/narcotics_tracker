"""Handles conversion between different units.

Classes:
    UnitConverter: Converts between different units of measurement.
"""


from typing import Union


class ConversionManager:
    """Converts between different units of measurement.

    Methods:

        to_standard: Converts the amount from the preferred to standard unit.

        to_preferred: Converts the amount from the standard to preferred unit.

        to_milliliters: Converts and returns the amount in milliliters.
    """

    decimals = {"std": -8, "mcg": -6, "mg": -3, "g": 0}

    def to_standard(self, amount: Union[int, float], starting_unit: str) -> float:
        """Converts the amount from the preferred to standard unit.

            Args:
                amount (int / float): Amount to be converted.

                starting_unit (str): The preferred unit of measurement's
                    abbreviation. Must be 'g' mg' 'mcg' or, 'ml'.

        Returns:
            float: The converted amount.
        """

        exponent = self.decimals[starting_unit] - self.decimals["std"]

        return amount * (10**exponent)

    def to_preferred(self, amount: Union[int, float], preferred_unit: str) -> float:
        """Converts the amount from the standard to preferred unit.

        Args:
            amount (int / float): Amount to be converted.

            preferred_unit (str): The preferred unit of measurement's
                abbreviation. Must be 'g' mg' 'mcg' or, 'ml'.

        Returns:
            float: The converted amount.
        """

        exponent = self.decimals["std"] - self.decimals[preferred_unit]
        return amount * (10**exponent)

    def to_milliliters(
        self, amount: Union[int, float], preferred_unit: str, concentration: float
    ) -> float:
        """Converts and returns the amount in milliliters.

        Args:
            amount (int / float): Amount to be converted.

            preferred_unit (str): The preferred unit of measurement's
                abbreviation. Must be 'g' mg' 'mcg' or, 'ml'.

            concentration (float): The medication's concentration.

        Returns:
            float: The converted amount.
        """

        adjusted_amount = self.to_preferred(amount, preferred_unit)

        return adjusted_amount / concentration
