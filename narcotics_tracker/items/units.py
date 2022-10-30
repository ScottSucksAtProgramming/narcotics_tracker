"""Defines the units of measurements for medications.

Classes:
    Unit: A unit of measurement for medications.
"""
from dataclasses import dataclass

from narcotics_tracker.items.interfaces.dataitem_interface import DataItem


@dataclass
class Unit(DataItem):
    """A unit of measurement for medications.

    Attributes:
        unit_code (str): Unique identifier for the unit.

        unit_name (str): Name of the unit.

        decimals (int): Number of decimal places for the unit.
    """

    unit_code: str
    unit_name: str
    decimals: int

    def __str__(self) -> str:
        return f"Unit #{self.id}: {self.unit_name} ({self.unit_code})."
