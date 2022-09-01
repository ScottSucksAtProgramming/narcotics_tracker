"""Contains the classes and tests which test the events type module.

Classes:

    Test_EventTypesModule: Contains all unit tests for the event_types module.

    Test_EventTypeAttributes: Contains unit tests for EventType's attributes.

    Test_EventTypesMethods: Contains unit tests for the EventType's methods.
"""

from narcotics_tracker import database, event_types


class Test_EventTypesModule:
    """Contains all unit tests for the event types module.

    Behaviors Tested:
        - Event Types module can be accessed.
        - Method return_table_creation_query returns correct string.
        - Method return_event_types returns all event_types.
        - Method return_operator returns expected result.
    """

    def test_event_types_module_can_be_accessed(self) -> None:
        """Tests that the event_types module exists and can be accessed.

        Asserts that calling event_types.__doc__ does not return 'None'.
        """
        assert event_types.__doc__ != None

    def test_return_table_creation_query_returns_expected_string(self) -> None:
        """Tests that the table_creation_query returns the correct string.

        Calls event_types.return_table_creation_query().

        Asserts that expected_query is returned.
        """
        expected_query = """CREATE TABLE IF NOT EXISTS event_types (
            EVENT_ID INTEGER PRIMARY KEY,
            EVENT_CODE TEXT UNIQUE,                
            EVENT_NAME TEXT,
            DESCRIPTION TEXT,
            OPERATOR INTEGER,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""

        assert event_types.return_table_creation_query() == expected_query

    def test_return_event_types_returns_expected_event_types(
        self, test_event_type, reset_database
    ) -> None:
        """Tests that the return_event_types method returns the expected event_types.

        Loads and saves test_event_type. Creates and save. 2nd_event_type
        Calls event_types.return_event_types().

        Asserts that event_types.return_event_types() returns expected data.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(event_types.return_table_creation_query())

        test_event_type = test_event_type

        test_event_type.save(db)

        event_types_list = event_types.return_event_types(db)

        assert (
            "Event Type Test Event. Code: TEST. Used for testing the EventType Class."
            in event_types_list
        )

    def test_return_operator_returns_expected_integer(self, test_event_type) -> None:
        """Tests that return_operator returns the event types operator.

        Loads test_event_type. Calls test_event_type.return_operator().

        Asserts that method returns '-1'.
        """
        db = database.Database()
        db.connect("test_database_2.db")
        test_event_type = test_event_type
        test_event_type.event_code = "LOSS"

        assert event_types.return_operator(test_event_type.event_code, db) == -1


class Test_EventTypeAttributes:
    """Contains all unit tests for the EventType Class' attributes.

    Behaviors Tested:
        - EventType class can be accessed.
        - EventType objects can be created.
        - event_id attribute returns correct value.
        - event_code attribute returns correct value.
        - event_name attribute returns correct value.
        - description attribute returns correct value.
        - operator attribute returns correct value.
        - created_date attribute returns correct value.
        - modified_date attribute returns correct value.
        - modified_by attribute returns correct value.
    """

    def test_event_type_class_can_be_accessed(self) -> None:
        """Tests that the EventType Class exists and can be accessed.

        Asserts that calling EventType.__doc__ does not return 'None'.
        """
        assert event_types.EventType.__doc__ != None

    def test_can_create_event_type_objects(self, test_event_type) -> None:
        """Tests that objects can be created from the EventType Class.

        Loads test_event_type.

        Asserts that test_event_type is an instance of the EventType Class.
        """
        test_event_type = test_event_type

        assert isinstance(test_event_type, event_types.EventType)

    def test_event_id_returns_correct_value(self, test_event_type) -> None:
        """Tests that the event_id attribute returns the correct value.

        Loads test_event_type. Sets the event_id to '9001'.

        Asserts test_event_type.event_id is '9001'.
        """
        test_event_type = test_event_type
        test_event_type.event_id = 2001

        assert test_event_type.event_id == 2001

    def test_event_code_returns_correct_value(self, test_event_type) -> None:
        """Tests that the event_code attribute returns the correct value.

        Loads test_event_type.

        Asserts that test_event_type.event_code is 'TEST'.
        """
        test_event_type = test_event_type

        assert test_event_type.event_code == "TEST"

    def test_event_name_returns_correct_value(self, test_event_type) -> None:
        """Tests that the event_name attributes returns the correct value.

        Loads test_event_type.

        Asserts that test_event_type.event_name is 'Test Event'
        """
        test_event_type = test_event_type

        assert test_event_type.event_name == "Test Event"

    def test_description_returns_correct_value(self, test_event_type) -> None:
        """Tests that the description attributes returns the correct value.

        Loads test_event_type.

        Asserts that test_event_type.description is 'Used for testing the EventType Class.'
        """
        test_event_type = test_event_type

        assert test_event_type.description == "Used for testing the EventType Class."

    def test_operator_returns_correct_value(self, test_event_type) -> None:
        """Tests that the operator attributes returns the correct value.

        Loads test_event_type.

        Asserts that test_event_type.operator is -1.
        """
        test_event_type = test_event_type

        assert test_event_type.operator == -1

    def test_created_date_returns_correct_value(self, test_event_type) -> None:
        """Tests that the created_date attributes returns the correct value.

        Loads test_event_type.

        Asserts that test_event_type.created_date is '08-26-2022'
        """
        test_event_type = test_event_type

        assert test_event_type.created_date == database.return_datetime(
            "2022-08-26 00:00:00"
        )

    def test_modified_date_returns_correct_value(self, test_event_type) -> None:
        """Tests that the modified_date attributes returns the correct value.

        Loads test_event_type.

        Asserts that test_event_type.modified_date is '08-01-2022'
        """
        test_event_type = test_event_type
        print(test_event_type.modified_date)

        assert test_event_type.modified_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_by_returns_correct_value(self, test_event_type) -> None:
        """Tests that the modified_by attributes returns the correct value.

        Loads test_event_type.

        Asserts that test_event_type.modified_by is 'Bast'
        """
        test_event_type = test_event_type

        assert test_event_type.modified_by == "Bast"


class Test_EventTypeMethods:
    """Contains all unit tests for the EventType Class' methods.

    Behaviors Tested:
        - __init__ sets attributes correctly.
        - __repr__ returns correct string.
        - Can save EventType to database.
        - Can load EventType from database.
        - Can update EventType code.
        - Can update EventType name.
        - Can update EventType description.
        - Can update EventType operator.
        - return_attributes returns the correct values.
        - Can delete reporting period from database.
    """

    def test___init___sets_attributes_correctly(self, test_event_type) -> None:
        """Tests the initializer sets the objects attributes correctly.

        Loads test_event_type.

        Asserts that event_id, event_code, event_name and description
        attributes are set to the expected values.
        """
        test_event_type = test_event_type

        assert (
            test_event_type.event_id == 2001
            and test_event_type.event_code == "TEST"
            and test_event_type.event_name == "Test Event"
            and test_event_type.description == "Used for testing the EventType Class."
        )

    def test___repr___returns_expected_string(self, test_event_type) -> None:
        """Tests that __repr__ returns correct string.

        Loads test_event_type. Calls str(test_event_type).

        Asserts that str(test_event_type) returns:
            'Event Type Test. Code: TEST. Used for testing the EventType Class.'
        """
        test_event_type = test_event_type

        assert str(test_event_type) == (
            f"Event Type Test Event. Code: TEST. Used for testing the "
            f"EventType Class."
        )

    def test_can_save_event_type_to_database(
        self, test_event_type, reset_database
    ) -> None:
        """Tests that event types can be saved to the database.

        Loads test_event_type. Calls test_event_type.save. Calls db.return_data()
        using the event_id of '2001'.

        Asserts that returned data has event_code value of 'TEST'.
        """
        test_event_type = test_event_type

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(event_types.return_table_creation_query())

        test_event_type.save(db)

        data = db.return_data(
            """SELECT event_code FROM event_types WHERE event_id = '2001'"""
        )

        assert data[0][0] == "TEST"

    def test_can_load_event_from_database(
        self, reset_database, test_event_type
    ) -> None:
        """Tests to see if an Event Type Object can be loaded from data.
        Loads and saves test_event_type. Creates loaded_event from data.

        Asserts that test_event_type and loaded_event_type return identical
        attributes.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(event_types.return_table_creation_query())

        test_event_type = test_event_type
        test_event_type.save(db)

        loaded_event_type = db.load_event("TEST")

    def test_can_update_event_code(self, test_event_type, reset_database) -> None:
        """Tests that the event type's event code can be updated.

        Loads test_event_type. Updates event code to 'NEW CODE'. Queries the
        event code for the event_id of 2001.

        Asserts that test_event_type.event_code is 'NEW CODE'.
        """
        test_event_type = test_event_type

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(event_types.return_table_creation_query())
        test_event_type.save(db)

        test_event_type.update_code("NEW CODE", db)

        data = db.return_data(
            """SELECT event_code FROM event_types WHERE event_id = 2001"""
        )
        assert data[0][0] == "NEW CODE"

    def test_can_update_name(self, test_event_type, reset_database) -> None:
        """Tests that the event type's name can be updated.

        Loads test_event_type. Updates name to 'NEW NAME'. Queries the
        name for the event_id of 2001.

        Asserts that test_event_type.event_name is 'NEW NAME'.
        """
        test_event_type = test_event_type

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(event_types.return_table_creation_query())
        test_event_type.save(db)

        test_event_type.update_name("NEW NAME", db)

        data = db.return_data(
            """SELECT event_name FROM event_types WHERE event_id = 2001"""
        )
        assert data[0][0] == "NEW NAME"

    def test_can_update_description(self, test_event_type, reset_database) -> None:
        """Tests that the event type's description can be updated.

        Loads test_event_type. Updates description to 'This is the new description.'. Queries the
        description for the event_id of 2001.

        Asserts that test_event_type.description is 'This is the new description.'.
        """
        test_event_type = test_event_type

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(event_types.return_table_creation_query())
        test_event_type.save(db)

        test_event_type.update_description("This is the new description.", db)

        data = db.return_data(
            """SELECT description FROM event_types WHERE event_id = 2001"""
        )
        assert data[0][0] == "This is the new description."

    def test_can_update_operator(self, test_event_type, reset_database) -> None:
        """Tests that the event type's operator can be updated.

        Loads test_event_type. Updates event code to 'This is the new operator.'. Queries the
        event code for the event_id of 2001.

        Asserts that test_event_type.operator is -10.
        """
        test_event_type = test_event_type

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(event_types.return_table_creation_query())
        test_event_type.save(db)

        test_event_type.update_operator(-10, db)

        data = db.return_data(
            """SELECT operator FROM event_types WHERE event_id = 2001"""
        )
        assert data[0][0] == -10

    def test_can_delete_event_type_from_database(self, test_event_type, reset_database):
        """Tests that event types can be deleted from the database.

        Loads test_event_type. Saves it to database. Then deletes it. Gets data from
        event_types table.

        Asserts data is empty.
        """
        test_event_type = test_event_type

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(event_types.return_table_creation_query())

        test_event_type.save(db)
        test_event_type.delete(db)

        data = db.return_data("""SELECT * FROM event_types""")
        assert data == []

    def test_return_attributes(self, test_event_type):
        """Tests that the event types data is correctly returned.

        Loads test_event_type. Calls test_event_type.return_attributes().

        Asserts values returned are expected values.
        """
        test_event_type = test_event_type
        assert test_event_type.return_attributes() == (
            2001,
            "TEST",
            "Test Event",
            "Used for testing the EventType Class.",
            -1,
            database.return_datetime("2022-08-26 00:00:00"),
            database.return_datetime("2022-08-01 00:00:00"),
            "Bast",
        )
