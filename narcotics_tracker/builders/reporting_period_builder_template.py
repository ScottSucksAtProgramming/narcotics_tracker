"""Contains the abstract builder for the ReportingPeriod class.

Abstract builders contain no implementation. Look at the documentation for the 
Reporting Period Builder module for more information.

Classes:
    ReportingPeriod: Defines the interface for the reporting period builder.
"""
from abc import ABC, abstractmethod


class ReportingPeriod(ABC):
    """Defines the interface for the reporting period builder."""

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
