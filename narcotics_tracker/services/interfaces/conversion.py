"""Defines the protocol for unit conversion services.

    Classes:
        ConversionService: Protocol for unit converters.
"""

from typing import Protocol, Union


class ConversionService(Protocol):
    """Protocol for unit converters.

    Classes using this protocol must be able to convert between the different
    units of measurement using the three methods declared below. Each method
    returns a float which is accepted by the database table.

    Unit converters are used to convert between the preferred unit of
    measurement stored in the medication table, the standard unit which is
    used for all medication amounts within the database. Unit converters are
    also responsible for converting a medication amount in mass to it's
    equivalent measurement in milliliters (volume). Bi-annual reports to the
    Department of Health and Bureau of Narcotics Enforcement require
    medication amounts in milliliters. This conversion is generally done using
    the concentration value stored in the medication's data.

    Review the documentation of the Units Package for more information on the
    various units used in the narcotics tracker.

    Methods:
        to_standard: Returns an amount of medication in the standard unit.

        to_preferred: Returns an amount of medication in the preferred unit.

        to_milliliters: Returns an amount of medication in milliliters.
    """

    def to_standard(self, amount: Union[int, float], preferred_unit: str) -> float:
        """Converts from preferred to standard unit."""

        return 0

    def to_preferred(self, amount: Union[int, float], preferred_unit: str) -> float:
        """Converts from standard to preferred unit."""

        return 0

    def to_milliliters(
        self, amount: Union[int, float], preferred_unit: str, concentration: float
    ) -> float:
        """Converts from the preferred unit to milliliters."""

        return 0
