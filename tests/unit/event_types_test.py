"""Contains the classes and tests which test the events type module.

Classes:

    Test_EventsModule: Contains all unit tests for the events module.

    Test_EventAttributes: Contains unit tests for Event's attributes.

    Test_EventsMethods: Contains unit tests for the Event's methods.
"""

from narcotics_tracker import database, events


class Test_EventsModule:
    """Contains all unit tests for the event types module.

    Behaviors Tested:
        - Event Types module can be accessed.
        - Method return_table_creation_query returns correct string.
        - Method return_events returns all events.
        - Method return_operator returns expected result.
        - Method parse_event_data returns correct dictionary and values.
    """

    def test_events_module_can_be_accessed(self) -> None:
        """Tests that the events module exists and can be accessed.

        Asserts that calling events.__doc__ does not return 'None'.
        """
        assert events.__doc__ != None

    def test_return_table_creation_query_returns_expected_string(self) -> None:
        """Tests that the table_creation_query returns the correct string.

        Calls events.return_table_creation_query().

        Asserts that expected_query is returned.
        """
        expected_query = """CREATE TABLE IF NOT EXISTS events (
            EVENT_ID INTEGER PRIMARY KEY,
            EVENT_CODE TEXT UNIQUE,                
            EVENT_NAME TEXT,
            DESCRIPTION TEXT,
            OPERATOR INTEGER,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""

        assert events.return_table_creation_query() == expected_query

    def test_return_events_returns_expected_events(
        self, test_event, reset_database
    ) -> None:
        """Tests that the return_events method returns the expected events.

        Loads and saves test_event. Creates and save. 2nd_event_type
        Calls events.return_events().

        Asserts that events.return_events() returns expected data.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(events.return_table_creation_query())

        test_event = test_event

        test_event.save(db)

        events_list = events.return_events(db)

        assert (
            "Event Test Event. Code: TEST. Used for testing the Event Class."
            in events_list
        )

    def test_return_operator_returns_expected_integer(self, test_event) -> None:
        """Tests that return_operator returns the event types operator.

        Loads test_event. Calls test_event.return_operator().

        Asserts that method returns '-1'.
        """
        db = database.Database()
        db.connect("test_database_2.db")
        test_event = test_event
        test_event.event_code = "LOSS"

        assert events.return_operator(test_event.event_code, db) == -1

    def test_parse_event_data_returns_correct_values(
        self, reset_database, test_event
    ) -> None:
        """Tests if parse_event_data returns dictionary with correct data.

        Resets the database. Creates events table. Builds and saves
        test_event to database. Queries database for event type data and
        calls the parser.

        Asserts that dictionary returned assigns the correct data to correct
        keys.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(events.return_table_creation_query())

        test_event = test_event
        test_event.save(db)
        data = test_event.read(db)
        dictionary = events.parse_event_data(data)

        assert (
            dictionary["event_id"] == 2001
            and dictionary["event_code"] == "TEST"
            and dictionary["event_name"] == "Test Event"
            and dictionary["description"] == "Used for testing the Event Class."
            and dictionary["operator"] == -1
        )


class Test_EventAttributes:
    """Contains all unit tests for the Event Class' attributes.

    Behaviors Tested:
        - Event class can be accessed.
        - Event objects can be created.
        - event_id attribute returns correct value.
        - event_code attribute returns correct value.
        - event_name attribute returns correct value.
        - description attribute returns correct value.
        - operator attribute returns correct value.
        - created_date attribute returns correct value.
        - modified_date attribute returns correct value.
        - modified_by attribute returns correct value.
    """

    def test_event_class_can_be_accessed(self) -> None:
        """Tests that the Event Class exists and can be accessed.

        Asserts that calling Event.__doc__ does not return 'None'.
        """
        assert events.Event.__doc__ != None

    def test_can_create_event_type_objects(self, test_event) -> None:
        """Tests that objects can be created from the Event Class.

        Loads test_event.

        Asserts that test_event is an instance of the Event Class.
        """
        test_event = test_event

        assert isinstance(test_event, events.Event)

    def test_event_id_returns_correct_value(self, test_event) -> None:
        """Tests that the event_id attribute returns the correct value.

        Loads test_event. Sets the event_id to '9001'.

        Asserts test_event.event_id is '9001'.
        """
        test_event = test_event
        test_event.event_id = 2001

        assert test_event.event_id == 2001

    def test_event_code_returns_correct_value(self, test_event) -> None:
        """Tests that the event_code attribute returns the correct value.

        Loads test_event.

        Asserts that test_event.event_code is 'TEST'.
        """
        test_event = test_event

        assert test_event.event_code == "TEST"

    def test_event_name_returns_correct_value(self, test_event) -> None:
        """Tests that the event_name attributes returns the correct value.

        Loads test_event.

        Asserts that test_event.event_name is 'Test Event'
        """
        test_event = test_event

        assert test_event.event_name == "Test Event"

    def test_description_returns_correct_value(self, test_event) -> None:
        """Tests that the description attributes returns the correct value.

        Loads test_event.

        Asserts that test_event.description is 'Used for testing the Event Class.'
        """
        test_event = test_event

        assert test_event.description == "Used for testing the Event Class."

    def test_operator_returns_correct_value(self, test_event) -> None:
        """Tests that the operator attributes returns the correct value.

        Loads test_event.

        Asserts that test_event.operator is -1.
        """
        test_event = test_event

        assert test_event.operator == -1

    def test_created_date_returns_correct_value(self, test_event) -> None:
        """Tests that the created_date attributes returns the correct value.

        Loads test_event.

        Asserts that test_event.created_date is '08-26-2022'
        """
        test_event = test_event

        assert test_event.created_date == database.return_datetime(
            "2022-08-26 00:00:00"
        )

    def test_modified_date_returns_correct_value(self, test_event) -> None:
        """Tests that the modified_date attributes returns the correct value.

        Loads test_event.

        Asserts that test_event.modified_date is '08-01-2022'
        """
        test_event = test_event

        assert test_event.modified_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_by_returns_correct_value(self, test_event) -> None:
        """Tests that the modified_by attributes returns the correct value.

        Loads test_event.

        Asserts that test_event.modified_by is 'Bast'
        """
        test_event = test_event

        assert test_event.modified_by == "Bast"


class Test_EventMethods:
    """Contains all unit tests for the Event Class' methods.

    Behaviors Tested:
        - __init__ sets attributes correctly.
        - __repr__ returns correct string.
        - Can save Event to database.
        - Can read Event data from database.
        - Can load Event from database.
        - Can update Event in database.
        - Can delete Event from database.
        - return_attributes returns the correct values.
    """

    def test___init___sets_attributes_correctly(self, test_event) -> None:
        """Tests the initializer sets the objects attributes correctly.

        Loads test_event.

        Asserts that event_id, event_code, event_name and description
        attributes are set to the expected values.
        """
        test_event = test_event

        assert (
            test_event.event_id == 2001
            and test_event.event_code == "TEST"
            and test_event.event_name == "Test Event"
            and test_event.description == "Used for testing the Event Class."
        )

    def test___repr___returns_expected_string(self, test_event) -> None:
        """Tests that __repr__ returns correct string.

        Loads test_event. Calls str(test_event).

        Asserts that str(test_event) returns:
            'Event Type Test. Code: TEST. Used for testing the Event Class.'
        """
        test_event = test_event

        assert str(test_event) == (
            f"Event Type Test Event. Code: TEST. Used for testing the " f"Event Class."
        )

    def test_can_save_event_type_to_database(self, test_event, reset_database) -> None:
        """Tests that event types can be saved to the database.

        Loads test_event. Calls test_event.save. Calls db.return_data()
        using the event_id of '2001'.

        Asserts that returned data has event_code value of 'TEST'.
        """
        test_event = test_event

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(events.return_table_creation_query())

        test_event.save(db)

        data = db.return_data(
            """SELECT event_code FROM events WHERE event_id = '2001'"""
        )

        assert data[0][0] == "TEST"

    def test_can_read_event_type_from_database(
        self, reset_database, test_event
    ) -> None:
        """Tests to see if the event's data can be returned from database.

        Resets the database. Creates events table. Builds and saves
        test_event. Calls test_event.read().

        Asserts that data returned matches expected values.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(events.return_table_creation_query())

        test_event = test_event
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

    def test_can_load_event_from_database(self, reset_database, test_event) -> None:
        """Tests to see if an Event Type Object can be loaded from data.
        Loads and saves test_event. Creates loaded_event from data.

        Asserts that test_event and loaded_event_type return identical
        attributes.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(events.return_table_creation_query())

        test_event = test_event
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

    def test_can_update_event_type_in_database(
        self, reset_database, test_event
    ) -> None:
        """Tests to see if Event data can be updated.

        Resets database. Creates Event Type Table. Builds and saves
        test_event to database.Loads test_event as
        loaded_event_type. Changes Operator and updates database. Queries the
        data.

        Asserts that the returned data has the new operator.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(events.return_table_creation_query())

        test_event = test_event
        test_event.save(db)

        loaded_event_type = db.load_event("TEST")
        loaded_event_type.operator = +10

        loaded_event_type.update(db)

        data = db.return_data(
            """SELECT operator FROM events WHERE event_code = 'TEST'"""
        )[0][0]

        assert data == +10

    def test_can_delete_event_type_from_database(self, test_event, reset_database):
        """Tests that event types can be deleted from the database.

        Loads test_event. Saves it to database. Then deletes it. Gets data from
        events table.

        Asserts data is empty.
        """
        test_event = test_event

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(events.return_table_creation_query())

        test_event.save(db)
        test_event.delete(db)

        data = db.return_data("""SELECT * FROM events""")
        assert data == []

    def test_return_attributes(self, test_event):
        """Tests that the event types data is correctly returned.

        Loads test_event. Calls test_event.return_attributes().

        Asserts values returned are expected values.
        """
        test_event = test_event
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
