"""Contains the interface for concrete DataItem builders.

Classes:
    BuilderInterface: Defines the protocol for concrete DataItem builders.
"""

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from narcotics_tracker.items.interfaces.dataitem_interface import DataItem


class Builder(Protocol):
    """Defines the protocol for concrete DataItem builders.

    Abstract Methods:
        build: Should return the constructed DataItem Object.

        _reset: Should remove all attributes values.
    """

    def build(self) -> "DataItem":
        """Returns the constructed DataItem Object."""

    def _reset(self) -> None:
        """Removes all attributes values from the builder."""
