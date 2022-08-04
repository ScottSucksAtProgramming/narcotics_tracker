#
# * ------------------------- Documentation -------------------------------- #
# Module:  medication.py
# Contains the Medication class, and related classes.
#
#
# Modification History
# 07-27-2022 | SRK | Module Created

from enum import Enum


class Container(Enum):
    """Enum of medication container types.

    Available container types:

    VIAL

    AMPULE

    PRE_FILLED_SYRINGE

    PRE_MIXED_BAG
    """

    VIAL = "Vial"
    AMPULE = "Ampule"
    PRE_FILLED_SYRINGE = "Pre-filled Syringe"
    PRE_MIXED_BAG = "Pre-mixed Bag"
