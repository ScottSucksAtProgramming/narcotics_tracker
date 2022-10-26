"""Contains the interface for concrete DataItem builders.

Classes:
    BuilderInterface: Defines the interface for concrete DataItem builders.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from narcotics_tracker.items.interfaces.dataitem_interface import DataItem


class BuilderInterface(ABC):
    """Defines the interface for concrete DataItem builders.

    Abstract Methods:
        build: Should return the constructed DataItem Object.

        _reset: Should remove all attributes values.
    """

    @abstractmethod
    def build(self) -> "DataItem":
        """Should return the constructed DataItem Object."""

    @abstractmethod
    def _reset(self) -> None:
        """Should remove all attributes values."""
