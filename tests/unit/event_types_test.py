"""Contains the classes and tests which test the events type module.

Classes:
"""

from narcotics_tracker import event_types


class Test_EventTypesModule:
    """Contains all unit tests for the event types module.

    Behaviors Tested:
        - Event Types module can be accessed.
        - Method return_table_creation_query returns correct string.
        - Method return_event_types returns all event_types.
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
            DESCRIPTION TEXT
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT
            )"""

        assert event_types.return_table_creation_query() == expected_query

    # def test_return_event_types_returns_expected_event_types(
    #     self, test_event_type, database_test_set_up
    # ) -> None:
    #     """Tests that the show method returns the expected reporting event_types.

    #     Loads and saves test_event_type. Calls event_types.show().

    #     Asserts that event_types.show() returns expected data.
    #     """
    #     db = database.Database()
    #     db.connect("test_database.db")
    #     db.create_table(event_types.return_table_creation_query())

    #     test_event_type = test_event_type
    #     test_event_type.save(db)

    #     data = event_types.return_event_types(db)
    #     assert data == [
    #         (9001, "02-29-0001", "01-35-0000", "08-26-2022", "08-25-2022", "Cinder")
    #     ]


class Test_EventTypeAttributes:
    """Contains all unit tests for the EventType Class' attributes.

    # ! Behaviors Tested:
    # !     - Period class can be accessed.
    # !     - Period objects can be created.
    # !     - period_id attribute returns correct value.
    # !     - starting_date attribute returns correct value.
    # !     - ending_date attribute returns correct value.
    # !     - created_date attribute returns correct value.
    # !     - modified_date attribute returns correct value.
    # !     - modified_by attribute returns correct value.
    """


class Test_EventTypeMethods:
    """Contains all unit tests for the EventType Class' methods.

    Behaviors Tested:
        - __init__ sets attributes correctly.
        - __repr__ returns correct string.
    # !     - Can save ReportingPeriod to database.
    # !     - Can update ReportingPeriod starting date.
    # !     - Can update ReportingPeriod ending date.
    # !     - return_attributes returns the correct values.
    # !     - Can delete reporting period from database.
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
