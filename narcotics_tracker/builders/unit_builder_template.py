"""Contains the abstract builder for the Unit class.

Abstract builders contain no implementation. Look at the documentation for the 
Unit Builder module for more information.

Classes:
    Unit: Defines the interface for the Unit builder.
"""
from abc import ABC, abstractmethod


class Unit(ABC):
    """Defines the interface for the Unit builder."""

    @abstractmethod
    def set_unit_id(self) -> None:
        pass

    @abstractmethod
    def set_unit_code(self) -> None:
        pass

    @abstractmethod
    def set_unit_name(self) -> None:
        pass

    @abstractmethod
    def set_created_date(self) -> None:
        pass

    @abstractmethod
    def set_modified_date(self) -> None:
        pass

    @abstractmethod
    def set_modified_by(self) -> None:
        pass

    @abstractmethod
    def build(self) -> None:
        pass
