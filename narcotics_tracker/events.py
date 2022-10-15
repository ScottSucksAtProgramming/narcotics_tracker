"""Contains the implementation and representation of Events.

#* Background

There are numerous ways that controlled substance medications can be added to 
or removed from the database. Events help specify why a medication amount was 
changed and whether or new the amount was added or removed. All Adjustments 
require an event to be specified.

#* Intended Use

The module and the Event class defined below allow for the creation of Event 
Objects. It is highly recommended to use the Event Builder Module contained 
within the Builders Package to create these objects. Instructions for using 
builders can be found within that package.

#* Events in the Database

Events are stored in the 'events' table of the database with their numeric id, 
code, name, description, and creation / modification information specified. 
Adjustment objects must specify the event which took place and are limited to 
the events listed in the table.

The Narcotics Tracker comes with a selection of pre-defined events. Refer to 
the Standard Items Module inside the Setup Package for more information.

#* Classes:
    
    Event: Defines Events and instantiates them as objects.
    
#* Functions:

    return_table_creation_query: Returns the query needed to create the 
        'events' table.

    return_events: Returns the 'events' table as lists of strings and values.

    return_operator: Returns an events' operator using it's code.

    parse_event_data: Returns an Event's attributes as a dictionary.
"""
import sqlite3
from typing import Union

from narcotics_tracker.persistence import database


def return_table_creation_query() -> str:
    """Returns the query needed to create the 'events' table.

    Returns:

        str: The sql query needed to create the 'events' table.
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


def return_events(db_connection: sqlite3.Connection) -> Union[list[str], list]:
    """Returns the 'events' table as lists of strings and values.

    Args:

        db_connection (sqlite3.Connection): The database connection.

    Returns:

        events_string_list (list[str]): The contents of the table as a list of
            strings.

        events_values_list (list): The contents of the table as a list of
            values.
    """
    sql_query = """SELECT event_code, event_name, description FROM events"""

    events_strings_list = []
    event_values_list = []

    events_data = db_connection.return_data(sql_query)

    for event in events_data:
        events_strings_list.append(f"Event {event[1]}. Code: {event[0]}. {event[2]}")
        event_values_list.append((event[0], event[1], event[2]))

    return events_strings_list, event_values_list


def parse_event_data(event_data) -> dict:
    """Returns an Event's attributes as a dictionary.

    Args:

        event_data (list): The Event's data.

    Returns:

        attributes (dict): Dictionary object containing the attributes of the
            Event.
    """
    attributes = {}

    attributes["event_id"] = event_data[0][0]
    attributes["event_code"] = event_data[0][1]
    attributes["event_name"] = event_data[0][2]
    attributes["description"] = event_data[0][3]
    attributes["operator"] = event_data[0][4]
    attributes["created_date"] = event_data[0][5]
    attributes["modified_date"] = event_data[0][6]
    attributes["modified_by"] = event_data[0][7]

    return attributes


class Event:
    """Defines Events and instantiates them as objects.

    This class defines Events within the Narcotics Tracker. Events determine
    whether the amount of an adjustment was added or removed from the stock
    and what happened to that medication. Inventory Adjustments must specify
    the event which occurred and are limited to the items listed in the
    'events' table.

    Events perform one of two operations: they either add or subtract a set
    amount of medication from the inventory. This is denoted using the
    operator attribute which can be set to +1 or -1 respectively.

    Events can be declared, created and managed using this class. They are
    stored in the 'events' table.

    Initializer:

        def __init__(self, builder=None) -> None:

            Initializes an instance of an Event using the builder.

    Attributes:

        event_id (int): Numeric identifier of the Event. Assigned by the
            database.

        event_code (str): Unique identifier of the Event. Assigned by the user.
            Used to interact with the Event in the database.

        event_name (str): Name of the Event.

        description (str): Description of the Event and when it should be
            used.

        operator (int): The operator of the inventory change. '+1' for adding
            stock. '-1' for removing stock. Gets multiplied against the
            adjustment amounts.

        created_date (str): The date the Event was created in the
            table.

        modified_date (str): The date the Event was last modified.

        modified_by (str): Identifier of the user who last modified the
            Event.

    Instance Methods:
        __repr__: Returns a string expression of the Event Object.

        save: Saves a new Event to the table in the database.

        read: Returns the data of the Event as a tuple.

        update: Updates the Event in the 'events' table.

        return_attributes: Returns the attributes of the Event Object as a
            tuple.

        delete: Deletes the Event from the database.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of an Event using the builder.

        Events are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of Events to the Builder
        Package.

        Refer to the documentation for the EventBuilder Class for more
        information.

        Args:

            builder (event_builder.EventBuilder): The builder used
                to construct the Event Object.
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
        """Returns a string expression of the Event Object.

        Returns:

            str: The string describing the Event Object.
        """
        return (
            f"Event {self.event_name}. Code: {self.event_code}. " f"{self.description}"
        )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new Event to the table in the database.

        This method will not overwrite a Event already saved in the
        database. Use the `update()` to adjust a Event's attributes.

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
        """Returns the data of the Event as a tuple.

        This method makes no changes to the data.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:

            tuple: A tuple containing the Event's attribute values
                in the order of the 'events' table's columns.
        """
        sql_query = """SELECT * from events WHERE event_code = ?"""

        values = (self.event_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the Event in the 'events' table.

        This method will overwrite the Event's data if it already exists
        within the database. An error will be returned if the event_code
        does not already exist in the database. Use the save method to save
        new Events in the database.

        Assigns a new modified_date.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Raises:

            IndexError: An Index Error will be raised if the event_code is not
            found on the events table.

        How to use:

            1. Use the `events.return_events()` method to return a
                list of Events. Identify the event_code of the
                Event you wish to update.

            2. Use the database.load_event() method, passing in the
                event_code and assigning it to a variable to create a
                Event Object.

            3. Modify the attributes as necessary and call this method on the
                Event Object to send the new values to the database.

            #! Note: If the event_id is being changed use the save()
            #! method to create a new Event entry in the table and use
            #! the delete() method to remove the old entry.
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

    def return_attributes(self) -> tuple:
        """Returns the attributes of the Event Object as a tuple.

        Returns:

            tuple: The attributes of the Event. Follows the order of the
                columns in the 'events` table.
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

    def delete(self, db_connection: sqlite3.Connection) -> None:
        """Deletes the Event from the database.

        The delete method will delete the Event from the database
        entirely.

        #! Note: Deleting an item from the database is irreversible.

        Args:

            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM events WHERE event_id = ?"""
        values = (self.event_id,)
        db_connection.write_data(sql_query, values)
