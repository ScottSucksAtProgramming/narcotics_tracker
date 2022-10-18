"""Contains the unit tests for the EventBuilder.

Classes:
    Test_EventBuilder: Unit tests the EventBuilder.
"""


from narcotics_tracker.builders.event_builder import EventBuilder
from narcotics_tracker.items.events import Event


class Test_EventBuilder:
    """Unit tests the EventBuilder.

    Behaviors Tested:
        - Can be accessed.
        - Returns an event Object.
        - Returned object has expected attribute values.
    """

    test_event = (
        EventBuilder()
        .set_table("events")
        .set_id(-77)
        .set_created_date(1666117887)
        .set_modified_date(1666117887)
        .set_modified_by("System")
        .set_event_code("TEST")
        .set_event_name("Test Event")
        .set_description("An event used for testing.")
        .set_modifier(999)
        .build()
    )

    def test_EventBuilder_can_be_accessed(self) -> None:
        assert EventBuilder.__doc__ != None

    def test_returned_object_is_an_event(self) -> None:
        assert isinstance(self.test_event, Event)

    def test_returned_object_had_expected_attributes(self) -> None:
        assert vars(self.test_event) == {
            "table": "events",
            "id": -77,
            "created_date": 1666117887,
            "modified_date": 1666117887,
            "modified_by": "System",
            "event_code": "TEST",
            "event_name": "Test Event",
            "description": "An event used for testing.",
            "modifier": 999,
        }
