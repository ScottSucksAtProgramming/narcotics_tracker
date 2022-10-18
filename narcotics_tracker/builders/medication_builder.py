"""Contains the concrete builder for the Medication DataItems.

Classes:

    MedicationBuilder: Builds and returns an Medication object.
"""


from narcotics_tracker.builders.builder_interface import BuilderInterface
from narcotics_tracker.items.medications import Medication


class MedicationBuilder(BuilderInterface):
    """Builds and returns an Medication Object.

    Methods:

        _reset: Prepares the builder to create a new Medication.
        build: Returns the constructed Medication.
        set_medication_code: Sets the medication code to the passed string.
        set_medication_name: Sets the medication name to the passed string.
        set_fill_amount: Sets the fill amount to the passed integer.
        set_medication_amount: Sets the amount to the passed integer.
        set_preferred_unit: Sets the preferred unit to the passed string.
        set_concentration: Calculates the concentration, unless overridden.

    """

    _dataitem = Medication(
        table=None,
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
            table=None,
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
        """Returns the constructed Medication."""
        medication = self._dataitem
        self._reset()
        return medication

    def set_medication_code(self, medication_code: str) -> BuilderInterface:
        """Sets the medication code to the passed string.

        Args:
            medication_code (str): Unique code of the medication.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.medication_code = medication_code
        return self

    def set_medication_name(self, medication_name: str) -> BuilderInterface:
        """Sets the medication name attribute to the passed string.

        medication_name (str): Name of the medication.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.medication_name = medication_name
        return self

    def set_fill_amount(self, fill_amount: int) -> BuilderInterface:
        """Sets the fill amount to the passed integer.

        Args:
            fill_amount (int): The amount of liquid in the medication
                container.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.fill_amount = fill_amount
        return self

    def set_medication_amount(self, medication_amount: int) -> BuilderInterface:
        """Sets the amount to the passed integer.

        Args:
            medication_amount (int): The amount of medication suspended in the
                liquid.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.medication_amount = medication_amount
        return self

    def set_preferred_unit(self, preferred_unit: str) -> BuilderInterface:
        """Sets the preferred unit to the passed string.

        Args:
            preferred_unit (str): Unit of measurement the medication is
                measured in. Must match a unit_code in the units table.

        Returns:
            self: The MedicationBuilder instance.
        """
        self._dataitem.preferred_unit = preferred_unit
        return self

    def set_concentration(self, concentration: float = None) -> BuilderInterface:
        """Calculates the concentration, unless overridden.

        Will calculate the concentration based on the fill_amount and
        medication_amount. If a concentration is passed, that will be used
        instead.

        Args:
            concentration (float, optional): Concentration of medication to
                the liquid. Defaults to None.

        Returns:
            self: The instance of the builder.
        """
        if concentration:
            self._dataitem.concentration = concentration
        else:
            concentration = (
                self._dataitem.medication_amount / self._dataitem.fill_amount
            )
            self._dataitem.concentration = concentration

        return self

    def set_status(self, status: str) -> BuilderInterface:
        """Sets the status attribute to the passed string.

        Args:
            status (str): Status of the medication. Must match a status_code
                in the statuses table.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.status = status
        return self
