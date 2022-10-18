"""Contains the concrete builder for the Adjustment DataItems.

Classes:

    AdjustmentBuilder: Builds and returns an Adjustment object.
"""


from narcotics_tracker.builders.builder_interface import BuilderInterface


class AdjustmentBuilder(BuilderInterface):
    """Builds and returns an Adjustment DataItem."""

    _

    def reset(self) -> None:
        """Resets the builder to build a new DataItem."""

    def set_table(self) -> None:
        """Sets the name of the table the DataItem belongs to."""

    def set_id(self) -> None:
        """Sets the numeric ID of the DataItem."""

    def set_created_date(self) -> None:
        """Sets the unix timestamp of when the DataItem was created."""

    def set_modified_date(self) -> None:
        """Sets the unix timestamp of when the DataItem was last modified."""

    def set_modified_by(self) -> None:
        """Sets the name of the user who last modified the DataItem."""

    def build(self) -> DataItem:
        """Returns the constructed DataItem."""
