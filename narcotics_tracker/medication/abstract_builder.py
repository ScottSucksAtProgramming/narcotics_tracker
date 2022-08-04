"""Contains the MedicationBuilder class."""


from abc import ABC, abstractmethod


class Builder(ABC):
    """The MedicationBuilder interface defines methods to build a medication."""

    @property
    @abstractmethod
    def build(self) -> None:
        pass

    @abstractmethod
    def set_name(self) -> None:
        pass

    @abstractmethod
    def set_code(self) -> None:
        pass

    @abstractmethod
    def set_container_type(self) -> None:
        pass

    @abstractmethod
    def set_fill_amount(self) -> None:
        pass

    @abstractmethod
    def set_dose_and_unit(self) -> None:
        pass

    @abstractmethod
    def set_status(self) -> None:
        pass
