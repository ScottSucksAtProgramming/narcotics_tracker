"""Contains the class defining controlled substance container types.

Classes:
    Containers: Defines the acceptable values for the container type.
"""
from enum import Enum


class Container(Enum):
    """Defines the acceptable values for the container type.

    Each medication comes in a variety of containers. The medications dose,
    fill amount and concentration are present in each container.

    Available container types:
        - VIAL
        - AMPULE
        - PRE_FILLED_SYRINGE
        - PRE_MIXED_BAG
    """

    VIAL = "Vial"
    AMPULE = "Ampule"
    PRE_FILLED_SYRINGE = "Pre-filled Syringe"
    PRE_MIXED_BAG = "Pre-mixed Bag"
