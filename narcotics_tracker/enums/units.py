#
# * ------------------------- Documentation -------------------------------- #
# Module:  units.py
# Contains the Unit class, and related classes.
#
#
# Modification History
# 07-30-2022 | SRK | Module Created

# ------------------------------ Tasks ------------------------------------- #
# Todo: I can create a new medication.
# Todo: I can save medication to a database.
# Todo: I can delete a medication.
# Todo: I can update a medication.
# Todo: I can retrieve a medication's properties.

from enum import Enum


class Unit(Enum):
    """Enum of dose units.

    Available units:

    MCG

    MG

    G"""

    MG = "mg"
    MCG = "mcg"
    G = "G"
