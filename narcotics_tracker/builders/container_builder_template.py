"""Contains the template for the Container Builder.

Abstract builders contain no implementation. Look at the documentation for the 
Reporting Period Builder module for more information.

Classes:
    Container: Defines the interface for the Container Builder.
"""
from abc import ABC, abstractmethod


class Container(ABC):
    """Defines the interface for the Container builder."""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def set_container_id(self) -> None:
        pass

    @abstractmethod
    def set_container_code(self) -> None:
        pass

    @abstractmethod
    def set_container_name(self) -> None:
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
