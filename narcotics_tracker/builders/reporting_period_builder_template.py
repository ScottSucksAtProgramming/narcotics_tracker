"""Contains the template for the Reporting Period Builder.

Abstract builders contain no implementation. Look at the documentation for the 
Reporting Period Builder module for more information.

Classes:
    ReportingPeriod: Defines the interface for the Reporting Period Builder.
"""
from abc import ABC, abstractmethod


class ReportingPeriod(ABC):
    """Defines the interface for the Reporting Period Builder."""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def set_period_id(self) -> None:
        pass

    @abstractmethod
    def set_starting_date(self) -> None:
        pass

    @abstractmethod
    def set_ending_date(self) -> None:
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
