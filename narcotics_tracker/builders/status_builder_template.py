"""Contains the template for the Status Builder.

Abstract builders contain no implementation. Look at the documentation for the 
Unit Builder module for more information.

Classes:
    Status: Defines the interface for the Status Builder.
"""
from abc import ABC, abstractmethod


class Status(ABC):
    """Defines the interface for the Status Builder."""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def assign_status_id(self) -> None:
        pass

    @abstractmethod
    def set_status_code(self) -> None:
        pass

    @abstractmethod
    def set_status_name(self) -> None:
        pass

    @abstractmethod
    def set_description(self) -> None:
        pass

    @abstractmethod
    def assign_created_date(self) -> None:
        pass

    @abstractmethod
    def assign_modified_date(self) -> None:
        pass

    @abstractmethod
    def set_modified_by(self) -> None:
        pass

    @abstractmethod
    def assign_all_attributes(self) -> None:
        pass

    @abstractmethod
    def build(self) -> None:
        pass
