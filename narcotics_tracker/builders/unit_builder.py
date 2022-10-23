"""Contains the concrete builder for the Unit DataItems.

Classes:

    UnitBuilder: Builds and returns an Unit object.
"""


from narcotics_tracker.builders.builder_interface import BuilderInterface
from narcotics_tracker.items.units import Unit


class UnitBuilder(BuilderInterface):
    """Builds and returns an Unit Object.

    Methods:

        _reset: Prepares the builder to create a new Unit.
        build: Returns the constructed Unit.
        set_unit_code: Sets the unit_code attribute to the passed string.
        set_unit_name: Sets the unit_name attribute to the passed string.
        set_decimals: Sets the decimals attribute to the passed integer.
    """

    _dataitem = Unit(
        table="units",
        id=None,
        created_date=None,
        modified_date=None,
        modified_by=None,
        unit_code=None,
        unit_name=None,
        decimals=None,
    )

    def _reset(self) -> None:
        """Prepares the builder to create a new Unit."""
        self._dataitem = Unit(
            table="units",
            id=None,
            created_date=None,
            modified_date=None,
            modified_by=None,
            unit_code=None,
            unit_name=None,
            decimals=None,
        )

    def build(self) -> Unit:
        """Returns the constructed Status."""
        unit = self._dataitem
        self._reset()
        return unit

    def set_unit_code(self, unit_code: str) -> BuilderInterface:
        """Sets the unit_code attribute to the passed string.

        Args:
            unit_code (str): Unique code for the unit.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.unit_code = unit_code
        return self

    def set_unit_name(self, unit_name: str) -> BuilderInterface:
        """Sets the unit_name attribute to the passed string.

        Args:
            unit_name (str): Name of the unit.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.unit_name = unit_name
        return self

    def set_decimals(self, decimals: int) -> BuilderInterface:
        """Sets the decimals attribute to the passed integer.

        Args:
            decimals (int): Number of decimals places.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.decimals = decimals
        return self
