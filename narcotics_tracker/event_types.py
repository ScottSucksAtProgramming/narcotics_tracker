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

    return_event_types: Returns contents of event_types as a list of strings.
"""

import sqlite3

from narcotics_tracker import database
from narcotics_tracker.utils import date


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the Event Types Table.

    Returns:
        str: The sql query needed to create the Event Types Table.
    """
    return """CREATE TABLE IF NOT EXISTS event_types (
            EVENT_ID INTEGER PRIMARY KEY,
            EVENT_CODE TEXT UNIQUE,                
            EVENT_NAME TEXT,
            DESCRIPTION TEXT,
            OPERATOR INTEGER,
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT
            )"""


def return_event_types(db_connection: sqlite3.Connection) -> list[str]:
    """Returns the contents of the event_types table as a list of strings.

    Args:
        db_connection (sqlite3.Connection): The database connection.

    Returns:
        table_contents (list[str]): The contents of the table as a list of
            strings.
    """
    sql_query = """SELECT * FROM event_types"""

    event_types_list = []

    event_types_data = db_connection.return_data(sql_query)
    for event in event_types_data:
        event_types_list.append(f"Event Type {event[2]}. Code: {event[1]}. {event[3]}")

    return event_types_list


def return_operator(event_code: str, db_connection: sqlite3.Connection) -> int:
    """Obtains and returns the event_types' operator.

    Args:
        event_code (str): The unique identifier of the event.

        db_connection (sqlite3.Connection): The connection to the database.

    Returns:
        operator (int): The operator for the event type.
    """
    sql_query = """SELECT operator FROM event_types WHERE event_code =(?)"""
    values = [event_code]

    operator = db_connection.return_data(sql_query, values)

    return operator[0][0]


class EventType:
    """Defines the representation of Event Types for the project.

    Multiple Event types can be declared, created and managed using this
    class. Event Types are NOT the specific events which actually change the
    inventory. Instead they are classifications of types of events. There is a
    set of standard events that come with the Narcotics Tracker.

    For information on creating actual inventory change events look at the
    inventory module.

    Events perform one of two operations: they either add or subtract a set
    amount of medication from the inventory. This is denoted using the
    operator property which can be set to +1 or -1 respectively.

    Initializer:
        def __init__(self, event_code: str, event_name: str, description: str) -> None:

        Creates an instance of EventType and assigns attributes.

        Sets the event_id to None.

        Arguments:
            event_code (str): Unique identifier of each event type. Assigned
                by the user.

            event_name (str): Name of the event.

            description (str): Description of the event.

            operator (int): The operator of the inventory change. '+1' for
                adding stock. '-1' for removing stock.

    Attributes:
        event_id (int): Numeric identifier of each event type.
            Assigned by the database.

       event_code (str): Unique identifier of each event type. Assigned by the
            user.

        event_name (str): Name of the event.

        description (str): Description of the event.

        operator (int): The operator of the inventory change. '+1' for adding
            stock. '-1' for removing stock.

        created_date (str): The date the event type was created in the
            table.

        modified_date (str): The date the event type was last modified.

        modified_by (str): Identifier of the person who last modified the
            event type.

    Instance Methods:
        __repr__: Returns a string expression of the event type object.

        save: Saves a new event type to the database.

        update_code: Updates the code of the event type.

        update_name: Updates the name of the event type.

        update_description: Updates the description of the event type.

        update_operator: Updates the operator for the event type.

        delete: Deletes the event type from the database.

        return_attributes: Returns the event type's attributes as a tuple.
    """

    def __init__(
        self, event_code: str, event_name: str, description: str, operator: int
    ) -> None:
        """Creates an instance of EventType and assigns attributes.

        Sets the event_id to None.

        Arguments:
            event_code (str): Unique identifier of each event type. Assigned
                by the user.

            event_name (str): Name of the event.

            description (str): Description of the event.

            operator (int): The operator of the inventory change. '+1' for
                adding stock. '-1' for removing stock.
        """
        self.event_id = None
        self.event_code = event_code
        self.event_name = event_name
        self.description = description
        self.operator = operator
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

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new event type to the database.

        The save method will only write the event_type into the table if it does
        not already exist. Use the update method to update the event_type's
        attributes.

        Use the date module to set the created date if it is None. Sets the
        modified date.

        Args:
            db_connection (sqlite3.Connection): The database connection.
        """
        sql_query = """INSERT OR IGNORE INTO event_types VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = date.return_date_as_string()
        self.modified_date = date.return_date_as_string()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def update_code(
        self, new_event_code: str, db_connection: sqlite3.Connection
    ) -> None:
        """Updates the event code of the event type.

        Args:
            new_event_code (str): The new event id.

            db_connection (sqlite3.Connection) The database connection.
        """
        self.modified_date = date.return_date_as_string()

        sql_query = """UPDATE event_types SET event_code =(?) WHERE event_id = (?)"""
        values = (new_event_code, self.event_id)

        db_connection.write_data(sql_query, values)

    def update_name(
        self, new_event_name: str, db_connection: sqlite3.Connection
    ) -> None:
        """Updates the event id of the event type.

        Args:
            new_event_name (str): The new event name.

            db_connection (sqlite3.Connection) The database connection.
        """
        self.modified_date = date.return_date_as_string()

        sql_query = """UPDATE event_types SET event_name =(?) WHERE event_id = (?)"""
        values = (new_event_name, self.event_id)

        db_connection.write_data(sql_query, values)

    def update_description(
        self, new_description: str, db_connection: sqlite3.Connection
    ) -> None:
        """Updates the event id of the event type.

        Args:
            new_description (str): The new event name.

            db_connection (sqlite3.Connection) The database connection.
        """
        self.modified_date = date.return_date_as_string()

        sql_query = """UPDATE event_types SET description =(?) WHERE event_id = (?)"""
        values = (new_description, self.event_id)

        db_connection.write_data(sql_query, values)

    def update_operator(
        self, new_operator: int, db_connection: sqlite3.Connection
    ) -> None:
        """Updates the event id of the event type.

        Args:
            new_operator (int): The new operator. +1 if events add stock. -1
                if events remove stock.

            db_connection (sqlite3.Connection) The database connection.
        """
        self.modified_date = date.return_date_as_string()

        sql_query = """UPDATE event_types SET operator =(?) WHERE event_id = (?)"""
        values = (new_operator, self.event_id)

        db_connection.write_data(sql_query, values)

    def delete(self, db_connection: sqlite3.Connection):
        """Deletes the event type from the database.

        The delete method will delete the event type from the database
        entirely. Note: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM event_types WHERE event_id = ?"""
        values = (self.event_id,)
        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the event types as a tuple.

        Returns:
            tuple: The attributes of the event types. Follows the order
            of the columns in the event_types table.
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
