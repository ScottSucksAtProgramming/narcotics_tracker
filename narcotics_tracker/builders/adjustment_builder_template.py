"""Contains the template for the Adjustment Builder.

Abstract builders contain no implementation. Look at the documentation for the 
Reporting Period Builder module for more information.

Classes:
    Adjustment: Defines the interface for the Adjustment Builder.
"""
from abc import ABC, abstractmethod


class Adjustment(ABC):
    """Defines the interface for the Adjustment Builder."""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def set_adjustment_id(self) -> None:
        pass

    @abstractmethod
    def set_adjustment_date(self) -> None:
        pass

    @abstractmethod
    def set_event_code(self) -> None:
        pass

    @abstractmethod
    def set_medication_code(self) -> None:
        pass

    @abstractmethod
    def set_adjustment_amount(self) -> None:
        pass

    @abstractmethod
    def set_reference_id(self) -> None:
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
