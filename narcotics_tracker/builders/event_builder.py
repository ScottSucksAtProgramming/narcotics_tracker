"""Contains the concrete builder for the Event DataItems.

Classes:

    EventBuilder: Builds and returns an Event object.
"""


from narcotics_tracker.builders.builder_interface import BuilderInterface
from narcotics_tracker.items.events import Event


class EventBuilder(BuilderInterface):
    """Builds and returns an Event Object.

    Methods:

        _reset: Prepares the builder to create a new Event.
        build: Returns the constructed Event.
        set_event_code: Sets the event code attribute to the passed string.
        set_event_name: Sets the event name attribute to the passed string.
        set_description: Sets the event description to the passed string.
        set_modifier: Sets the modifier attribute to the passed integer.
    """

    _dataitem = Event(
        table=None,
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
            table=None,
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
        """Returns the constructed Event."""
        event = self._dataitem
        self._reset()
        return event

    def set_event_code(self, event_code: str) -> BuilderInterface:
        """Sets the event code attribute to the passed string.

        event_code (str): Unique code of the event which occurred. Must match
            an event stored in the events table.
        """
        self._dataitem.event_code = event_code
        return self

    def set_event_name(self, event_name: str) -> BuilderInterface:
        """Sets the event name attribute to the passed string.

        event_name (str): Name of the event.
        """
        self._dataitem.event_name = event_name
        return self

    def set_description(self, description: str) -> BuilderInterface:
        """Sets the event description to the passed string.

        Args:
            description (str): Description of the event.
        """
        self._dataitem.description = description
        return self

    def set_modifier(self, modifier: int) -> BuilderInterface:
        """Sets the modifier attribute to the passed integer.

        Args:
            modifier (int): (+1 / -1) Integer which determines if the event
                adds or removes amounts from the inventory.

        Returns:
            self: The instance of the builder.
        """
        self._dataitem.modifier = modifier
        return self
