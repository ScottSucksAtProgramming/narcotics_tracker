"""Handles the defining and building of Event Objects.

Classes:

    EventBuilder: Assigns attributes and returns Event Objects.
"""


from narcotics_tracker.builders.dataitem_builder import DataItemBuilder
from narcotics_tracker.items.events import Event


class EventBuilder(DataItemBuilder):
    """Assigns attributes and returns Event Objects.

    This class inherits methods and attributes from the DataItemBuilder.
    Review the documentation for more information.

    Methods:

        build: Validates attributes and returns the Event Object.

        set_event_code: Sets the event code attribute to the passed string.

        set_event_name: Sets the event name attribute to the passed string.

        set_description: Sets the event description to the passed string.

        set_modifier: Sets the modifier attribute to the passed integer.
    """

    _dataitem = Event(
        table="events",
        id=None,
        created_date=None,
        modified_date=None,
        modified_by=None,
        event_code=None,
        event_name=None,
        description=None,
        modifier=None,
    )

    def _reset(self) -> None:
        """Prepares the builder to create a new Event."""
        self._dataitem = Event(
            table="events",
            id=None,
            created_date=None,
            modified_date=None,
            modified_by=None,
            event_code=None,
            event_name=None,
            description=None,
            modifier=None,
        )

    def build(self) -> Event:
        """Validates attributes and returns the Event Object."""
        self._dataitem.created_date = self._service_provider.datetime.validate(
            self._dataitem.created_date
        )
        self._dataitem.modified_date = self._service_provider.datetime.validate(
            self._dataitem.modified_date
        )

        event = self._dataitem
        self._reset()
        return event

    def set_event_code(self, event_code: str) -> "EventBuilder":
        """Sets the event code attribute to the passed string.

        event_code (str): Unique code of the event which occurred. Must match
            an event stored in the events table.
        """
        self._dataitem.event_code = event_code
        return self

    def set_event_name(self, event_name: str) -> "EventBuilder":
        """Sets the event name attribute to the passed string.

        event_name (str): Name of the event.
        """
        self._dataitem.event_name = event_name
        return self

    def set_description(self, description: str) -> "EventBuilder":
        """Sets the event description to the passed string.

        Args:
            description (str): Description of the event.
        """
        self._dataitem.description = description
        return self

    def set_modifier(self, modifier: int) -> "EventBuilder":
        """Sets the modifier attribute to the passed integer.

        Args:
            modifier (int): (+1 / -1) Integer which determines if the event
                adds or removes amounts from the inventory.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.modifier = modifier
        return self
