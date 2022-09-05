"""Contains implementation and representation of event types.

The events table is a vocabulary control table which stores a library of 
different Event Types which can be used to make adjustments to the controlled 
substance inventory. 

This module handles the creation of the event table, returns various 
event type data from the database and parses the raw data returned from the 
database into a usable format. It houses the EventType Class which defines and 
instantiates the Event Types as objects.

The Inventory Module and Adjustment Class make use of the Event Types in order 
to adjust the inventory.

The Event Type Builder Module contains information on creating event types and 
specifying their attributes.

The database module contains information on communicating with the database.

Classes:
    EventType: Defines Event Types and instantiates them as objects.
    
Functions:

    return_table_creation_query: Returns the query needed to create the Table.

    return_events: Returns contents of events as a list of strings.

    return_operator: Returns an events' operator using it's code.

    parse_event_data: Returns event data as a dictionary.
"""

import sqlite3

from narcotics_tracker import database


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the Event Types Table.

    Returns:
        str: The sql query needed to create the Event Types Table.
    """
    return """CREATE TABLE IF NOT EXISTS events (
            EVENT_ID INTEGER PRIMARY KEY,
            EVENT_CODE TEXT UNIQUE,                
            EVENT_NAME TEXT,
            DESCRIPTION TEXT,
            OPERATOR INTEGER,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""


def return_events(db_connection: sqlite3.Connection) -> list[str]:
    """Returns the contents of the events table as a list of strings.

    Args:
        db_connection (sqlite3.Connection): The database connection.

    Returns:
        table_contents (list[str]): The contents of the table as a list of
            strings.
    """
    sql_query = """SELECT * FROM events"""

    events_list = []

    events_data = db_connection.return_data(sql_query)
    for event in events_data:
        events_list.append(f"Event {event[2]}. Code: {event[1]}. {event[3]}")

    return events_list


def return_operator(event_code: str, db_connection: sqlite3.Connection) -> int:
    """Returns an events' operator using it's code..

    Args:
        event_code (str): The unique identifier of the event.

        db_connection (sqlite3.Connection): The connection to the database.

    Returns:
        operator (int): The operator for the event type.
    """
    sql_query = """SELECT operator FROM events WHERE event_code =(?)"""
    values = [event_code]

    operator = db_connection.return_data(sql_query, values)

    return operator[0][0]


def parse_event_data(event_data) -> dict:
    """Returns event data from the database as a dictionary.

    Args:
        event_data (list): The event data

    Returns:
        properties (dict): Dictionary objects contains the properties of
            the event."""

    properties = {}

    properties["event_id"] = event_data[0][0]
    properties["event_code"] = event_data[0][1]
    properties["event_name"] = event_data[0][2]
    properties["description"] = event_data[0][3]
    properties["operator"] = event_data[0][4]
    properties["created_date"] = event_data[0][5]
    properties["modified_date"] = event_data[0][6]
    properties["modified_by"] = event_data[0][7]

    return properties


class Event:
    """Defines Event Types and instantiates them as objects.

    Multiple Event types can be declared, created and managed using this
    class. Event Types are NOT the specific events which actually change the
    inventory. Instead they are classifications of types of events. There is a
    set of standard events that come with the Narcotics Tracker.

    For information on creating actual inventory change events look at the
    inventory module.

    Events perform one of two operations: they either add or subtract a set
    amount of medication from the inventory. This is denoted using the
    operator property which can be set to +1 or -1 respectively.

    Attributes:
        event_id (int): Numeric identifier of each event type.
            Assigned by the database.

       event_code (str): Unique identifier of each event type. Assigned by the
            user. Used to interact with the event type in the database.

        event_name (str): Name of the event.

        description (str): Description of the event and when it should be
            used.

        operator (int): The operator of the inventory change. '+1' for adding
            stock. '-1' for removing stock. Gets multiplied against the
            adjustment amounts.

        created_date (str): The date the event type was created in the
            table.

        modified_date (str): The date the event type was last modified.

        modified_by (str): Identifier of the user who last modified the
            event type.

    Initializer:
        def __init__(self, builder=None) -> None:
            Initializes an instance of an EventType using the
            EventTypeBuilder.

            EventTypes are complex objects with many attributes. The Builder
            Pattern was used to separate the creation of EventTypes to the
            Builder Package.

            Refer to the documentation for the EventTypeBuilder Class for more
            information.

            Args:
                builder (event_builder.EventTypeBuilder): The builder
                    used to construct the EventType object.

    Instance Methods:
        __repr__: Returns a string expression of the event type.

        save: Saves a new event type to the events table in the database.

        read: Returns the data of the event type from the database as a tuple.

        update: Updates the event type in the events table of the
            database.

        delete: Deletes the event type from the database.

        return_attributes: Returns the attributes of the event types object as
            a tuple.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of an EventType using the EventTypeBuilder.

        EventTypes are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of EventTypes to the
        Builder Package.

        Refer to the documentation for the EventTypeBuilder Class for more
        information.

        Args:
            builder (event_builder.EventTypeBuilder): The builder used to
                construct the EventType object.
        """
        self.event_id = builder.event_id
        self.event_code = builder.event_code
        self.event_name = builder.event_name
        self.description = builder.description
        self.operator = builder.operator
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """Returns a string expression of the event type.

        Returns:
            str: The string describing the event type specifying the event
                type's name, code and description.
        """
        return (
            f"Event Type {self.event_name}. Code: {self.event_code}. "
            f"{self.description}"
        )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new event type to the events table in the database.

        The save method will only write the event into the table if it does
        not already exist. Use the update method to update the event's
        attributes.

        Assigns a created_date and modified_date.

        Args:
            db_connection (sqlite3.Connection): The database connection.
        """
        sql_query = """INSERT OR IGNORE INTO events VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def read(self, db_connection: sqlite3.Connection) -> tuple:
        """Returns the data of the event type from the database as a tuple.

        This function will make no changes to the data.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:
            tuple: A tuple containing the event type's attribute values.
        """
        sql_query = """SELECT * from events WHERE event_code = ?"""

        values = (self.event_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the event type in the events table of the database.

        The update method will overwrite the event's data if it already
        exists within the database. Use the save method to store new
        event types in the database.

        How to use:
            Use the events.return_events() method to return a list
            of event types.

            Use the database.load_event() method, passing in the
            event_code of the event type you wish to update.

            Modify the attributes as necessary and call this method to update
            the attributes in the database.

            If you are changing the event_code use the save() method to create
            a new event type entry in the table and use the delete method to
            remove the old entry.

        Assigns a new modified_date.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

            event_code (str): The unique identifier of the event.

        Raises:

            IndexError: An Index Error will be raised if the event_code is not
            found on the events table.
        """
        sql_query = """UPDATE events 
            SET EVENT_ID = ?, 
                EVENT_CODE = ?, 
                EVENT_NAME = ?, 
                DESCRIPTION = ?, 
                OPERATOR = ?, 
                CREATED_DATE = ?, 
                MODIFIED_DATE = ?, 
                MODIFIED_BY = ? 
            WHERE EVENT_CODE = ?"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes() + (self.event_code,)

        db_connection.write_data(sql_query, values)

    def delete(self, db_connection: sqlite3.Connection):
        """Deletes the event type from the database.

        The delete method will delete the event type from the database
        entirely. Note: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM events WHERE event_id = ?"""
        values = (self.event_id,)
        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the event types object as a tuple.

        Returns:
            tuple: The attributes of the event types. Follows the order
            of the columns in the events table.
        """

        return (
            self.event_id,
            self.event_code,
            self.event_name,
            self.description,
            self.operator,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )
