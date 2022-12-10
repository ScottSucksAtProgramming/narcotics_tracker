"""Handles the defining and building of Unit Objects.

Classes:

    UnitBuilder: Assigns attributes and returns Unit Objects.
"""
from narcotics_tracker.builders.dataitem_builder import DataItemBuilder
from narcotics_tracker.items.units import Unit


class UnitBuilder(DataItemBuilder):
    """Assigns attributes and returns Unit Objects.

    This class inherits methods and attributes from the DataItemBuilder.
    Review the documentation for more information.

    Methods:

        build: Validates attributes and returns the Unit object.

        set_unit_code: Sets the unit_code attribute to the passed string.

        set_unit_name: Sets the unit_name attribute to the passed string.

        set_decimals: Sets the decimals attribute to the passed integer.
    """

    _dataitem: Unit = Unit(
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
        """Validates attributes and returns the Unit object."""
        self._dataitem.created_date = self._service_provider.datetime.validate(
            self._dataitem.created_date
        )
        self._dataitem.modified_date = self._service_provider.datetime.validate(
            self._dataitem.modified_date
        )

        unit = self._dataitem
        self._reset()
        return unit

    def set_unit_code(self, unit_code: str) -> "UnitBuilder":
        """Sets the unit_code attribute to the passed string.

        Args:
            unit_code (str): Unique code for the unit.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.unit_code = unit_code
        return self

    def set_unit_name(self, unit_name: str) -> "UnitBuilder":
        """Sets the unit_name attribute to the passed string.

        Args:s
            unit_name (str): Name of the unit.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.unit_name = unit_name
        return self

    def set_decimals(self, decimals: int) -> "UnitBuilder":
        """Sets the decimals attribute to the passed integer.

        Args:
            decimals (int): Number of decimals places.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.decimals = decimals
        return self
