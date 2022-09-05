"""Contains the abstract builder for the Status class.

Abstract builders contain no implementation. Look at the documentation for the 
Status Builder module for more information.

Classes:
    Status: Defines the interface for the Status builder.
"""
from abc import ABC, abstractmethod


class Status(ABC):
    """Defines the interface for the Status builder."""

    @abstractmethod
    def set_status_id(self) -> None:
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
    def set_created_date(self) -> None:
        pass

    @abstractmethod
    def set_modified_date(self) -> None:
        pass

    @abstractmethod
    def set_modified_by(self) -> None:
        pass

    @abstractmethod
    def set_all_properties(self) -> None:
        pass

    @abstractmethod
    def build(self) -> None:
        pass
