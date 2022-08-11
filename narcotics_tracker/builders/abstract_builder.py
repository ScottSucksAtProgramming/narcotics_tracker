"""Contains the MedicationBuilder class."""


from abc import ABC, abstractmethod


class MedicationBuilder(ABC):
    """The MedicationBuilder interface defines methods to build a medication."""

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

    @property
    @abstractmethod
    def build(self) -> None:
        pass
