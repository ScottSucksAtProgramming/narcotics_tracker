"""Handles the defining and building of Status Objects.

Classes:

    StatusBuilder: Assigns attributes and returns Status Objects.
"""


from narcotics_tracker.builders.dataitem_builder import DataItemBuilder
from narcotics_tracker.items.statuses import Status


class StatusBuilder(DataItemBuilder):
    """Assigns attributes and returns Status Objects.

    Methods:

        _reset: Prepares the builder to create a new Status.
        build: Returns the constructed Status.
        set_status_code: Sets the status_code attribute to the passed string.
        set_status_name: Sets the status_name attribute to the passed string.
        set_description: Sets the description attribute to the passed string.
    """

    _dataitem = Status(
        table="statuses",
        id=None,
        created_date=None,
        modified_date=None,
        modified_by=None,
        status_code=None,
        status_name=None,
        description=None,
    )

    def _reset(self) -> None:
        """Prepares the builder to create a new Status."""
        self._dataitem = Status(
            table="statuses",
            id=None,
            created_date=None,
            modified_date=None,
            modified_by=None,
            status_code=None,
            status_name=None,
            description=None,
        )

    def build(self) -> Status:
        """Returns the constructed Status."""
        self._dataitem.created_date = self._service_provider.datetime.validate(
            self._dataitem.created_date
        )
        self._dataitem.modified_date = self._service_provider.datetime.validate(
            self._dataitem.modified_date
        )

        status = self._dataitem
        self._reset()
        return status

    def set_status_code(self, status_code: str) -> "StatusBuilder":
        """Sets the status_code attribute to the passed string.

        Args:
            status_code (str): Unique code for the status.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.status_code = status_code
        return self

    def set_status_name(self, status_name: str) -> "StatusBuilder":
        """Sets the status_name attribute to the passed string.

        Args:
            status_name (str): Name of the status.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.status_name = status_name
        return self

    def set_description(self, description: str) -> "StatusBuilder":
        """Sets the description attribute to the passed string.

        Args:
            description (str): Description of the status.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.description = description
        return self
