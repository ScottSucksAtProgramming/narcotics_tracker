"""Contains implementation and representation of Statuses.

The status table is a vocabulary control table which stores a library of 
different Statuses which can be used to define various item attributes within 
the Narcotics Tracker.

This module handles the creation of the status table, returns various 
status data from the database and parses the raw data returned from the 
database into a usable format. It houses the status Class which defines and 
instantiates the status as objects.

The Medication Module makes use of the status.

The database module contains information on communicating with the database.

Classes:
    status: Defines status and instantiates them as objects.
    
Functions:

    return_table_creation_query: Returns the query needed to create the table.

    return_status: Returns contents of status as a list of strings.

    parse_status_data: Returns status data as a dictionary.
"""
import sqlite3

from narcotics_tracker import database


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the status Table.

    Returns:
        str: The sql query needed to create the status Table.
    """
    return """CREATE TABLE IF NOT EXISTS statuses (
            STATUS_ID INTEGER PRIMARY KEY,
            STATUS_CODE TEXT UNIQUE,                
            STATUS_NAME TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""


def return_statuses(db_connection: sqlite3.Connection) -> list[str]:
    """Returns the contents of the status table as a list of strings.

    Args:
        db_connection (sqlite3.Connection): The database connection.

    Returns:
        table_contents (list[str]): The contents of the table as a list of
            strings.
    """
    sql_query = """SELECT * FROM statuses"""

    status_list = []

    status_data = db_connection.return_data(sql_query)
    for status in status_data:
        status_list.append(f"Status {status[0]}: {status[2]}. Code: '{status[1]}'.")

    return status_list


def parse_status_data(status_data) -> dict:
    """Returns status data from the database as a dictionary.

    Args:
        status_data (list): The status data

    Returns:
        properties (dict): Dictionary objects contains the properties of
            the status."""

    properties = {}

    properties["status_id"] = status_data[0][0]
    properties["status_code"] = status_data[0][1]
    properties["status_name"] = status_data[0][2]
    properties["created_date"] = status_data[0][3]
    properties["modified_date"] = status_data[0][4]
    properties["modified_by"] = status_data[0][5]

    return properties


class Status:
    """Defines status and instantiates them as objects.

    status can be declared, created and managed using this class. Medications
    will be limited to using the status stored in the status table.

    Attributes:

        status_id (int): Numeric identifier of each unit. Assigned by the
            database.

       status_code (str): Unique identifier of each unit type. Assigned by the
            user. Used to interact with the unit in the database.

        status_code (str): Name of the unit.

        created_date (str): The date the unit type was created in the
            table.

        modified_date (str): The date the unit type was last modified.

        modified_by (str): Identifier of the user who last modified the
            unit type.

    Initializer:

    Instance Methods:
        __repr__: Returns a string expression of the unit.

        save: Saves a new unit to the status table in the database.

        read: Returns the data of the unit from the database as a tuple.

        update: Updates the unit in the status table of the
            database.

        delete: Deletes the unit from the database.

        return_attributes: Returns the attributes of the status object as
            a tuple.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of an Unit using the UnitBuilder.

        status are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of status to the
        Builder Package.

        Refer to the documentation for the UnitBuilder Class for more
        information.

        Args:
            builder (unit_builder.UnitBuilder): The builder used to
                construct the Unit object.
        """
        self.status_id = builder.status_id
        self.status_code = builder.status_code
        self.status_name = builder.status_name
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """Returns a string expression of the unit.

        Returns:
            str: The string describing the unit specifying the event
                type's name, code and description.
        """
        return (
            f"Status {self.status_id}: {self.status_name}. Code: '{self.status_code}'."
        )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new unit to the status table in the database.

        The save method will only write the unit into the table if it does
        not already exist. Use the update method to update the unit's
        attributes.

        Assigns a created_date and modified_date.

        Args:
            db_connection (sqlite3.Connection): The database connection.
        """
        sql_query = """INSERT OR IGNORE INTO statuses VALUES (
            ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def read(self, db_connection: sqlite3.Connection) -> tuple:
        """Returns the data of the unit from the database as a tuple.

        This function will make no changes to the data.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:
            tuple: A tuple containing the unit's attribute values.
        """
        sql_query = """SELECT * from statuses WHERE status_code = ?"""

        values = (self.status_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the unit in the status table of the database.

        The update method will overwrite the unit's data if it already
        exists within the database. Use the save method to store new
        status in the database.

        How to use:
            Use the status.return_status() method to return a list
            of status.

            Use the database.load_unit() method, passing in the
            status_code of the unit you wish to update.

            Modify the attributes as necessary and call this method to update
            the attributes in the database.

            If you are changing the status_code use the save() method to create
            a new unit entry in the table and use the delete method to
            remove the old entry.

        Assigns a new modified_date.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

            status_code (str): The unique identifier of the unit.

        Raises:

            IndexError: An Index Error will be raised if the status_code is not
            found on the status table.
        """
        sql_query = """UPDATE statuses 
            SET status_id = ?, 
                status_code = ?, 
                status_name = ?, 
                created_date = ?, 
                modified_date = ?, 
                modified_by = ? 
            WHERE status_code = ?"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes() + (self.status_code,)

        db_connection.write_data(sql_query, values)

    def delete(self, db_connection: sqlite3.Connection):
        """Deletes the unit from the database.

        The delete method will delete the unit from the database
        entirely. Note: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM statuses WHERE status_id = ?"""
        values = (self.status_id,)
        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the status object as a tuple.

        Returns:
            tuple: The attributes of the status. Follows the order
            of the columns in the status table.
        """

        return (
            self.status_id,
            self.status_code,
            self.status_name,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )
