"""Handles the defining and building of Adjustment Objects.

Classes:

    AdjustmentBuilder: Assigns attributes and returns Adjustment Objects.
"""
from narcotics_tracker import commands
from narcotics_tracker.builders.dataitem_builder import DataItemBuilder
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.typings import DateType, NTTypes


class AdjustmentBuilder(DataItemBuilder):
    """Assigns attributes and returns Adjustment Objects.

    This class inherits methods and attributes from the DataItemBuilder.
    Review the documentation for more information.

    Methods:

        build: Validates attributes and returns the Adjustment object.

        set_adjustment_date: Sets the adjustment date to the passed integer.

        set_event_code: Sets the event code attribute to the passed string.

        set_medication_code: Sets the medication code to the passed string.

        set_adjustment_amount: Sets the adjustment amount to the passed float.

        set_reference_id: Sets the reference id attribute to the passed string.

        set_reporting_period_id: Sets the reporting period id attribute to the
            passed integer.
    """

    _dataitem: Adjustment = Adjustment(
        table="inventory",
        id=None,
        created_date=None,
        modified_date=None,
        modified_by=None,
        adjustment_date=None,
        event_code=None,
        medication_code=None,
        amount=None,
        reference_id=None,
        reporting_period_id=None,
    )

    def _reset(self) -> None:
        """Prepares the builder to create a new Adjustment."""
        self._dataitem = Adjustment(
            table="inventory",
            id=None,
            created_date=None,
            modified_date=None,
            modified_by=None,
            adjustment_date=None,
            event_code=None,
            medication_code=None,
            amount=None,
            reference_id=None,
            reporting_period_id=None,
        )

    def build(self) -> Adjustment:
        """Validates attributes and returns the Adjustment object."""
        self._convert_adjustment_amount_to_standard()
        self._apply_event_modifier()

        adjustment = self._dataitem
        self._reset()
        return adjustment

    def _convert_adjustment_amount_to_standard(self) -> None:
        """Converts the adjustment amount in the standard unit."""
        med_code = self._dataitem.medication_code
        if med_code is None:
            return
        amount = self._dataitem.amount
        preferred_unit = commands.ReturnPreferredUnit().set_id(med_code).execute()
        converted_amount = self._service_provider.conversion.to_standard(
            amount, preferred_unit
        )
        self._dataitem.amount = converted_amount

    def _apply_event_modifier(self) -> None:
        """Retrieves the event modifier and applies it to the the amount."""
        event_code = self._dataitem.event_code
        if event_code is None:
            return

        event_modifier = commands.ReturnEventModifier().set_id(event_code).execute()

        self._dataitem.amount = self._dataitem.amount * event_modifier

    def set_adjustment_date(self, date: DateType) -> "AdjustmentBuilder":
        """Sets the adjustment date to the passed value.

        Args:
            adjustment_date (int): Unix timestamp of when the adjustment
                occurred.
        """
        valid_date = self._validate_date(date)
        self._dataitem.adjustment_date = valid_date
        return self

    def set_event_code(self, event_code: str) -> "AdjustmentBuilder":
        """Sets the event code attribute to the passed string.

        Args:
            event_code (str): Unique code of the event which occurred. Must
                match an event stored in the events table.
        """
        self._dataitem.event_code = event_code
        return self

    def set_medication_code(self, medication_code: str) -> "AdjustmentBuilder":
        """Sets the medication code to the passed string.

        Args:
            medication_code (str): Unique code of the medication being
                adjusted. Must match a medication stored in the medications
                table.
        """
        self._dataitem.medication_code = medication_code
        return self

    def set_adjustment_amount(self, adjustment_amount: float) -> "AdjustmentBuilder":
        """Sets the adjustment amount to the passed float.

        Args:
            adjustment_amount (float): The amount of medication being adjusted.
        """
        self._dataitem.amount = adjustment_amount
        return self

    def set_reference_id(self, reference_id: str) -> "AdjustmentBuilder":
        """Sets the reference id attribute to the passed string.

        Args:
            reference_id (str): Identifier of the document containing
                additional information regarding the adjustment.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.reference_id = reference_id
        return self

    def set_reporting_period_id(self, reporting_period_id: int) -> "AdjustmentBuilder":
        """Sets the reporting period id attribute to the passed integer.

        Args:
            reporting_period_id (str): Identifier of the document containing
                additional information regarding the adjustment.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.reporting_period_id = reporting_period_id
        return self
