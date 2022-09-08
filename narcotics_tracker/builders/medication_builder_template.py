"""Contains the template for the Medication Builder.

Abstract builders contain no implementation. Look at the documentation for the 
Reporting Period Builder module for more information.

Classes:
    Medication: Defines the interface for the Medication Builder.
"""
from abc import ABC, abstractmethod


class Medication(ABC):
    """Defines the interface for the Medication Builder."""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def set_medication_id(self) -> None:
        pass

    @abstractmethod
    def set_name(self) -> None:
        pass

    @abstractmethod
    def set_code(self) -> None:
        pass

    @abstractmethod
    def set_container(self) -> None:
        pass

    @abstractmethod
    def set_fill_amount(self) -> None:
        pass

    @abstractmethod
    def set_dose_and_unit(self) -> None:
        pass

    @abstractmethod
    def set_concentration(self) -> None:
        pass

    @abstractmethod
    def set_status(self) -> None:
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
