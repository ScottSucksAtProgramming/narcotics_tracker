"""Contains the class defining a medications preferred unit of measurement.

Classes:
    Unit: Defines the acceptable values for the units of measurement.
"""
from enum import Enum


class Unit(Enum):
    """Defines the acceptable values for the units of measurement.

    Medications come in various units of measurement. The preferred dose is
    the dose which the controlled substance agents and providers use to
    describe the amount administered to a patient.

    Available units:
        - MCG
        - MG
        - G
    """

    MG = "mg"
    MCG = "mcg"
    G = "G"
