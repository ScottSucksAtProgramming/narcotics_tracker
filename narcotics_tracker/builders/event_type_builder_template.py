"""Contains the abstract builder for the EventType class.

Abstract builders contain no implementation. Look at the documentation for the 
adjustment_builder module for more information.

Classes:
    EventType: Defines the interface for the adjustment builder.
"""
from abc import ABC, abstractmethod


class EventType(ABC):
    """Defines the interface for the event_type builder."""

    @abstractmethod
    def set_event_id(self) -> None:
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
