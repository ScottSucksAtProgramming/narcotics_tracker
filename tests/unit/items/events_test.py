"""Unit tests the Events Module.

Classes:

    Test_Event: Unit tests the Event Class.
"""

from narcotics_tracker.items.events import Event


class Test_Event:
    """Unit tests the Event Class.

    Behaviors Tested:
        - Events class can be accessed.
        - Events return expected id.
        - Events return expected event_code.
        - Events return expected event_name.
        - Events return expected description.
        - Events return expected modifier.
        - Events return expected string.
        - Events return expected dictionary.
    """

    test_event = Event(
        table="events",
        id=-1,
        event_code="test_event",
        event_name="Test Event",
        description="An event used for testing.",
        modifier=999,
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="SRK",
    )

    def test_event_class_can_be_accessed(self) -> None:
        assert Event.__doc__ != None

    def test_event_returns_expected_id(self) -> None:
        assert self.test_event.id == -1

    def test_event_returns_expected_event_code(self) -> None:
        assert self.test_event.event_code == "test_event"

    def test_event_returns_expected_event_name(self) -> None:
        assert self.test_event.event_name == "Test Event"

    def test_event_returns_expected_description(self) -> None:
        assert self.test_event.description == "An event used for testing."

    def test_event_returns_expected_modifier(self) -> None:
        assert self.test_event.modifier == 999

    def test_event_return_expected_string(self) -> None:
        assert (
            str(self.test_event)
            == "Event #-1: Test Event (test_event) An event used for testing."
        )

    def test_event_return_expected_dictionary(self) -> None:
        assert vars(self.test_event) == {
            "table": "events",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "SRK",
            "event_code": "test_event",
            "event_name": "Test Event",
            "description": "An event used for testing.",
            "modifier": 999,
        }
