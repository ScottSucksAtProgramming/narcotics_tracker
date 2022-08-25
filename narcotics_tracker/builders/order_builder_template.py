"""Contains the abstract builder for the Order class.

Abstract builders contain no implementation. Look at the documentation for the 
order_builder module for more information.

Classes:
    Order: Defines the interface for the order builder.
"""

from abc import ABC, abstractmethod


class Order(ABC):
    """Defines the interface for the order builder."""

    @abstractmethod
    def set_order_id(self) -> None:
        pass

    @abstractmethod
    def set_po_number(self) -> None:
        pass

    @abstractmethod
    def set_date_ordered(self) -> None:
        pass

    @abstractmethod
    def set_medication_code(self) -> None:
        pass

    @abstractmethod
    def set_containers_amount(self) -> None:
        pass

    @abstractmethod
    def set_supplier(self) -> None:
        pass

    @abstractmethod
    def set_supplier_order_number(self) -> None:
        pass

    @abstractmethod
    def set_dea_form_number(self) -> None:
        pass

    @abstractmethod
    def set_date_received(self) -> None:
        pass

    @abstractmethod
    def set_packages_received(self) -> None:
        pass

    @abstractmethod
    def set_comments(self) -> None:
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
