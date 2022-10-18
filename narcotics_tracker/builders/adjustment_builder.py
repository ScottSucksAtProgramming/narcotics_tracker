"""Contains the concrete builder for the Adjustment DataItems.

Classes:

    AdjustmentBuilder: Builds and returns an Adjustment object.
"""


from narcotics_tracker.builders.builder_interface import BuilderInterface
from narcotics_tracker.items.adjustments import Adjustment


class AdjustmentBuilder(BuilderInterface):
    """Builds and returns an Adjustment Object.

    Methods:

        _reset: Prepares the builder to create a new Adjustment.
        build: Returns the constructed Adjustment.
        set_adjustment_date: Sets the adjustment date to the passed integer.
        set_event_code: Sets the event code attribute to the passed string.
        set_medication_code: Sets the medication code to the passed string.
        set_adjustment_amount: Sets the adjustment amount to the passed float.
        set_reference_id: Sets the reference id attribute to the passed string.
    """

    _dataitem = Adjustment(
        table=None,
        id=None,
        created_date=None,
        modified_date=None,
        modified_by=None,
        adjustment_date=None,
        event_code=None,
        medication_code=None,
        adjustment_amount=None,
        reference_id=None,
        reporting_period_id=None,
    )
    _table_name = "inventory"

    def _reset(self) -> None:
        """Prepares the builder to create a new Adjustment."""
        self._adjustment = Adjustment(
            table=None,
            id=None,
            created_date=None,
            modified_date=None,
            modified_by=None,
            adjustment_date=None,
            event_code=None,
            medication_code=None,
            adjustment_amount=None,
            reference_id=None,
            reporting_period_id=None,
        )

    def build(self) -> Adjustment:
        """Returns the constructed Adjustment."""
        adjustment = self._adjustment
        self._reset()
        return adjustment

    def set_adjustment_date(self, adjustment_date: int) -> BuilderInterface:
        """Sets the adjustment date to the passed integer.

        Args:
            adjustment_date (int): Unix timestamp of when the adjustment
                occurred.
        """
        self._adjustment.adjustment_date = adjustment_date
        return self

    def set_event_code(self, event_code: str) -> BuilderInterface:
        """Sets the event code attribute to the passed string.

        event_code (str): Unique code of the event which occurred. Must match
            an event stored in the events table.
        """
        self._adjustment.event_code = event_code
        return self

    def set_medication_code(self, medication_code: str) -> BuilderInterface:
        """Sets the medication code to the passed string.

        medication_code (str): Unique code of the event which occurred. Must
        match a medication stored in the medications table.
        """
        self._adjustment.medication_code = medication_code
        return self

    def set_adjustment_amount(self, adjustment_amount: float) -> BuilderInterface:
        """Sets the adjustment amount to the passed float.

        Args:
            adjustment_amount (float): The amount of medication being adjusted.
        """
        self._adjustment.adjustment_amount = adjustment_amount
        return self

    def set_reference_id(self, reference_id: str) -> BuilderInterface:
        """Sets the reference id attribute to the passed string.

        Args:
            reference_id (str): Identifier of the document containing
                additional information regarding the adjustment.

        Returns:
            self: The instance of the builder.
        """
        self._adjustment.reference_id = reference_id
        return self
