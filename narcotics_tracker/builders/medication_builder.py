"""Handles the defining and building of Medication Objects.

Classes:

    MedicationBuilder: Assigns attributes and returns Medication Objects.
"""
from narcotics_tracker.builders.dataitem_builder import DataItemBuilder
from narcotics_tracker.items.medications import Medication


class MedicationBuilder(DataItemBuilder):
    """Assigns attributes and returns Medication Objects.

    This class inherits methods and attributes from the DataItemBuilder.
    Review the documentation for more information.

    Methods:

        build: Validates attributes and returns the Medication Object.

        set_medication_code: Sets the medication code to the passed string.

        set_medication_name: Sets the medication name attribute to the passed
            string.

        set_fill_amount: Sets the fill amount to the passed integer.

        set_medication_amount: Sets the amount to the passed integer.

        set_preferred_unit: Sets the preferred unit to the passed string.

        set_concentration: Sets the concentration to the passed value, or None.

        set_status: Sets the status attribute to the passed string.
    """

    _dataitem = Medication(
        table="medications",
        id=None,
        created_date=None,
        modified_date=None,
        modified_by=None,
        medication_code=None,
        medication_name=None,
        fill_amount=None,
        medication_amount=None,
        preferred_unit=None,
        concentration=None,
        status=None,
    )

    def _reset(self) -> None:
        """Prepares the builder to create a new Medication."""
        self._dataitem = Medication(
            table="medications",
            id=None,
            created_date=None,
            modified_date=None,
            modified_by=None,
            medication_code=None,
            medication_name=None,
            fill_amount=None,
            medication_amount=None,
            preferred_unit=None,
            concentration=None,
            status=None,
        )

    def build(self) -> Medication:
        """Validates attributes and returns the Medication Object."""
        self._dataitem.created_date = self._service_provider.datetime.validate(
            self._dataitem.created_date
        )
        self._dataitem.modified_date = self._service_provider.datetime.validate(
            self._dataitem.modified_date
        )

        if self._concentration_is_none:
            self._dataitem.concentration = self._calculate_concentration()

        self._dataitem.medication_amount = self._convert_medication_amount()

        medication = self._dataitem
        self._reset()

        return medication

    def _concentration_is_none(self) -> bool:
        """Returns true if the concentration is None, otherwise returns false."""
        if self._dataitem.concentration is not None:
            return False
        else:
            return True

    def _calculate_concentration(self) -> float:
        """Calculates and returns the medication's concentration."""
        return self._dataitem.medication_amount / self._dataitem.fill_amount

    def _convert_medication_amount(self) -> int:
        """Converts and returns the medication amount in the standard unit."""
        unit_converter = self._service_provider.conversion
        converted_amount = unit_converter.to_standard(
            self._dataitem.medication_amount, self._dataitem.preferred_unit
        )

        return converted_amount

    def set_medication_code(self, medication_code: str) -> "MedicationBuilder":
        """Sets the medication code to the passed string.

        Args:
            medication_code (str): Unique code of the medication.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.medication_code = medication_code
        return self

    def set_medication_name(self, medication_name: str) -> "MedicationBuilder":
        """Sets the medication name attribute to the passed string.

        medication_name (str): Name of the medication.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.medication_name = medication_name
        return self

    def set_fill_amount(self, fill_amount: int) -> "MedicationBuilder":
        """Sets the fill amount to the passed integer.

        Args:
            fill_amount (int): The amount of liquid in the medication
                container, in milliliters.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.fill_amount = fill_amount
        return self

    def set_medication_amount(self, medication_amount: int) -> "MedicationBuilder":
        """Sets the amount to the passed integer.

        Args:
            medication_amount (int): The amount of medication suspended in the
                liquid.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.medication_amount = medication_amount
        return self

    def set_preferred_unit(self, preferred_unit: str) -> "MedicationBuilder":
        """Sets the preferred unit to the passed string.

        Args:
            preferred_unit (str): Unit of measurement the medication is
                measured in. Must match a unit_code in the units table.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.preferred_unit = preferred_unit
        return self

    def set_concentration(self, concentration: float = None) -> "MedicationBuilder":
        """Sets the concentration to the passed value, or None."""
        if concentration:
            self._dataitem.concentration = concentration
        else:
            concentration = None

        return self

    def set_status(self, status: str) -> "MedicationBuilder":
        """Sets the status attribute to the passed string.

        Args:
            status (str): Status of the medication. Must match a status_code
                in the statuses table.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.status = status
        return self
