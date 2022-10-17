"""Contains the classes and tests which test the events type module.

Classes:

    Test_EventsModule: Contains all unit tests for the events module.

    Test_EventAttributes: Contains unit tests for Event's attributes.

    Test_EventsMethods: Contains unit tests for the Event's methods.
"""

from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.items import events
from narcotics_tracker.items.events import Event


class Test_EventsModule:
    """Contains all unit tests for the event types module.

    Behaviors Tested:
        - Can be accessed.
    """

    def test_events_module_can_be_accessed(cls) -> None:
        assert events.__doc__ != None


class Test_EventAttributes:
    """Contains all unit tests for the Event Class' attributes.

    Behaviors Tested:
        - Can be accessed.
        - Event objects can be created.
        - Attribute event_id returns expected value.
        - Attribute event_code returns expected value.
        - Attribute event_name returns expected value.
        - Attribute description returns expected value.
        - Attribute modifier returns expected value.
    """

    test_event = Event(
        table="events",
        column_info=None,
        id=-1,
        event_code="test_event",
        event_name="Test Event",
        description="An event used for testing.",
        modifier=999,
        created_date=None,
        modified_date=None,
        modified_by="System",
    )

    def test_event_class_can_be_accessed(cls) -> None:
        assert Event.__doc__ != None

    def test_can_create_event_type_objects(cls) -> None:
        assert isinstance(cls.test_event, Event)

    def test_event_id_returns_correct_value(cls) -> None:
        assert cls.test_event.id == -1

    def test_event_code_returns_correct_value(cls) -> None:
        assert cls.test_event.event_code == "test_event"

    def test_event_name_returns_correct_value(cls) -> None:
        assert cls.test_event.event_name == "Test Event"

    def test_description_returns_correct_value(cls) -> None:
        assert cls.test_event.description == "An event used for testing."

    def test_operator_returns_correct_value(cls) -> None:
        assert cls.test_event.modifier == 999


class Test_EventMethods:
    """Contains all unit tests for the Event Class' methods.

    Behaviors Tested:
        - __str__ returns correct string.
        - Can save Event to database.
        - Can read Event data from database.
        - Can load Event from database.
        - Can update Event in database.
        - Can delete Event from database.
        - return_attributes returns the correct values.
    """

    test_event = Event(
        table="events",
        column_info=None,
        id=-1,
        event_code="test_event",
        event_name="Test Event",
        description="An event used for testing.",
        modifier=999,
        created_date=None,
        modified_date=None,
        modified_by="System",
    )

    def test___str___returns_expected_string(cls) -> None:
        assert str(cls.test_event) == "ID: -1 | Test Event: An event used for testing."

    def test_can_save_event_type_to_database(cls, reset_database) -> None:
        with SQLiteManager("test_database.db") as db:
            db.create_table(
                "events",
                {
                    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                    "event_code": "TEXT NOT NULL",
                    "event_name": "TEXT NOT NULL",
                    "description": "TEXT NOT NULL",
                    "modifier": "INTEGER NOT NULL",
                    "created_date": "INTEGER NOT NULL",
                    "modified_date": "INTEGER NOT NULL",
                    "modified_by": "TEXT NOT NULL",
                },
            )

            cls.test_event.add()

            data = db.return_data(
                """SELECT event_code FROM events WHERE event_id = '999'"""
            )

        assert data[0][0] == "test_event"

    def test_can_read_event_type_from_database(cls, reset_database, test_event) -> None:
        """Tests to see if the event's data can be returned from database.

        Resets the database. Creates events table. Builds and saves
        test_event. Calls test_event.read().

        Asserts that data returned matches expected values.
        """
        with SQLiteManager("test_database.db") as db:
            db.create_table(events.return_table_creation_query())

            test_event.save(db)

            data = test_event.read(db)[0]
            expected = [
                2001,
                "TEST",
                "Test Event",
                "Used for testing the Event Class.",
                -1,
            ]

        assert (
            data[0] == expected[0]
            and data[1] == expected[1]
            and data[2] == expected[2]
            and data[3] == expected[3]
            and data[4] == expected[4]
        )

    def test_can_load_event_from_database(cls, reset_database) -> None:
        """Tests to see if an Event Type Object can be loaded from data.
        Loads and saves test_event. Creates loaded_event from data.

        Asserts that test_event and loaded_event_type return identical
        attributes.
        """
        with SQLiteManager("test_database.db") as db:
            db.create_table(events.return_table_creation_query())

            test_event.save(db)

            loaded_event_type = db.load_event("TEST")

        assert (
            loaded_event_type.return_attributes()[0]
            == test_event.return_attributes()[0]
            and loaded_event_type.return_attributes()[1]
            == test_event.return_attributes()[1]
            and loaded_event_type.return_attributes()[2]
            == test_event.return_attributes()[2]
            and loaded_event_type.return_attributes()[3]
            == test_event.return_attributes()[3]
            and loaded_event_type.return_attributes()[4]
            == test_event.return_attributes()[4]
        )

    def test_can_update_event_type_in_database(cls, reset_database, test_event) -> None:
        """Tests to see if Event data can be updated.

        Resets database. Creates Event Type Table. Builds and saves
        test_event to database.Loads test_event as
        loaded_event_type. Changes Operator and updates database. Queries the
        data.

        Asserts that the returned data has the new operator.
        """
        with SQLiteManager("test_database.db") as db:
            db.create_table(events.return_table_creation_query())

            test_event.save(db)

            loaded_event_type = db.load_event("TEST")
            loaded_event_type.operator = +10

            loaded_event_type.update(db)

            data = db.return_data(
                """SELECT operator FROM events WHERE event_code = 'TEST'"""
            )[0][0]

        assert data == +10

    def test_can_delete_event_type_from_database(cls, test_event, reset_database):
        """Tests that event types can be deleted from the database.

        Loads test_event. Saves it to database. Then deletes it. Gets data from
        events table.

        Asserts data is empty.
        """

        with SQLiteManager("test_database.db") as db:
            db.create_table(events.return_table_creation_query())

            test_event.save(db)
            test_event.delete(db)

            data = db.return_data("""SELECT * FROM events""")
        assert data == []

    def test_return_attributes(cls):
        """Tests that the event types data is correctly returned.

        Loads test_event. Calls test_event.return_attributes().

        Asserts values returned are expected values.
        """

        assert test_event.return_attributes() == (
            2001,
            "TEST",
            "Test Event",
            "Used for testing the Event Class.",
            -1,
            database.return_datetime("2022-08-26 00:00:00"),
            database.return_datetime("2022-08-01 00:00:00"),
            "Bast",
        )
