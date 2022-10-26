"""Contains the interface for unit conversion providers.

classes: 
    ConversionService: Interface for conversion providers.
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class ConversionService(Protocol):
    """Interface for conversion providers."""

    def to_standard(self) -> float:
        ...

    def to_preferred(self) -> float:
        ...

    def to_milliliters(self) -> float:
        ...
