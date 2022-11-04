"""Handles conversion between different units.

Controlled substance medications are measured in different units. 

The Preferred Unit is the unit that the medication is commonly measured in. 

The Standard Unit is a measurement of mass stored as an integer in the data 
repository. The Standard Unit allows for precision to be preserved to a 
minimum of two decimal places regardless of the preferred unit. 

Reports sent to the NYS Department of Health and Bureau of Narcotic 
Enforcement require medication amounts to be converted to volume. The 
medication's concentration enables conversion this conversion. Volumes are 
always reported in milliliters.

Classes:
    UnitConverter: Converts between different units of measurement.
"""


from typing import Union

from narcotics_tracker.services.interfaces.conversion import ConversionService


class ConversionManager(ConversionService):
    """Converts between different units of measurement.

    Methods:

        to_standard: Returns an amount of medication in the standard unit.

        to_preferred: Returns an amount of medication in its preferred unit.

        to_milliliters: Returns the volume of a medication (in ml) using its
            concentration.
    """

    _decimals = {"std": -8, "mcg": -6, "mg": -3, "g": 0}

    def to_standard(self, amount: Union[int, float], preferred_unit: str) -> float:
        """Returns an amount of medication in the standard unit.

            Args:
                amount (int / float): Amount of medication in its preferred
                    unit.

                preferred_unit (str): The unit_code of the medication's
                    preferred unit. Valid unit_codes: 'mcg', 'mg', 'g', 'std'.

        Returns:
            float: The converted amount.
        """
        exponent = self._decimals[preferred_unit] - self._decimals["std"]
        result = amount * (10**exponent)

        return round(result, 2)

    def to_preferred(self, amount: Union[int, float], preferred_unit: str) -> float:
        """Returns an amount of medication in its preferred unit.

        Args:
            amount (int / float): Amount of medication in the standard unit.

            preferred_unit (str): The unit_code of the medication's preferred
                unit. Valid unit_codes: 'mcg', 'mg', 'g', 'std'.

        Returns:
            float: The amount of the medication in it's preferred unit.
        """
        exponent = self._decimals["std"] - self._decimals[preferred_unit]
        raw_conversion = amount * (10**exponent)
        result = round(raw_conversion, 2)

        return round(result, 2)

    def to_milliliters(
        self, amount: Union[int, float], preferred_unit: str, concentration: float
    ) -> float:
        """Returns the volume of a medication (in ml) using its concentration.

        Args:
            amount (int / float): Amount of medication in the standard unit.

            preferred_unit (str): The medication's preferred unit of mass.

            concentration (float): The medication's concentration.

        Returns:
            float: The volume of the medication in milliliters.
        """
        converted_amount = self.to_preferred(amount, preferred_unit)
        result = converted_amount / concentration

        return round(result, 2)
