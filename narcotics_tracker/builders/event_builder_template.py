"""Contains the template for the Event Builder.

Abstract builders contain no implementation. Look at the documentation for the 
Reporting Period Builder module for more information.

Classes:
    Event: Defines the interface for the Event Builder.
"""
from abc import ABC, abstractmethod


class Event(ABC):
    """Defines the interface for the Event Builder."""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def assign_event_id(self) -> None:
        pass

    @abstractmethod
    def set_event_code(self) -> None:
        pass

    @abstractmethod
    def set_event_name(self) -> None:
        pass

    @abstractmethod
    def set_description(self) -> None:
        pass

    @abstractmethod
    def set_operator(self) -> None:
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
    def build(self) -> None:
        pass
