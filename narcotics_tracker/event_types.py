"""Contains the representation and implementation of event types.

There are multiple events which can occur and change the controlled substance 
inventory. The Event Types module handle the creation and management of the 
event types and the Event Types Table within the database.

Please look at the database module for more information on communicating with 
the database.

Classes:
    EventType: Defines the representation of event types for the 
        project.

Functions:

    return_table_creation_query: Returns the query needed to create the Table.

    return_event_types: Returns the contents of the event_types table.
"""

import sqlite3


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the Event Types Table.

    Returns:
        str: The sql query needed to create the Event Types Table.
    """
    return """CREATE TABLE IF NOT EXISTS event_types (
            EVENT_ID INTEGER PRIMARY KEY,
            EVENT_CODE TEXT UNIQUE,                
            EVENT_NAME TEXT,
            DESCRIPTION TEXT
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT
            )"""


def return_event_types(db_connection: sqlite3.Connection) -> str:
    """Returns the contents of the event_types table.

    Args:
        db_connection (sqlite3.Connection): The database connection.

    Returns:
        table_contents (str): The contents of the table as a string.
    """
    sql_query = """SELECT * FROM event_types"""

    event_types = db_connection.return_data(sql_query)

    return event_types


class EventType:
    """Defines the representation of Event Types for the project.

    Initializer:
        def __init__(self, event_code: str, event_name: str, description: str) -> None:

        Creates an instance of EventType and assigns attributes.

        Sets the event_id to None.

        Arguments:
            event_code (str): Unique identifier of each event type. Assigned
                by the user.

            event_name (str): Name of the event.

            description (str): Description of the event.

    Attributes:
        event_id (int): Numeric identifier of each event type.
            Assigned by the database.

       event_code (str): Unique identifier of each event type. Assigned by the
            user.

        event_name (str): Name of the event.

        description (str): Description of the event.

        created_date (str): The date the event type was created in the
            table.

        modified_date (str): The date the event type was last modified.

        modified_by (str): Identifier of the person who last modified the
            event type.

    Instance Methods:
        __repr__: Returns a string expression of the event type object.

        save: Saves a new event type to the database.

        #! update_starting_date: Updates the starting date of the event type.

        #! update_ending_date: Updates the ending date of the event type.

        delete: Deletes the event type from the database.

        return_attributes: Returns the event type's attributes as a tuple.
    """

    def __init__(self, event_code: str, event_name: str, description: str) -> None:
        """Creates an instance of EventType and assigns attributes.

        Sets the event_id to None.

        Arguments:
            event_code (str): Unique identifier of each event type. Assigned
                by the user.

            event_name (str): Name of the event.

            description (str): Description of the event.
        """
        self.event_id = None
        self.event_code = event_code
        self.event_name = event_name
        self.description = description
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def __repr__(self) -> str:
        """Returns a string expression of the event type.

        Returns:
            str: The string describing the event type.
        """

        return (
            f"Event Type {self.event_name}. Code: {self.event_code}. "
            f"{self.description}"
        )
