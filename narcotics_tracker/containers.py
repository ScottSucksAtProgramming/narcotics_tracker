"""Contains implementation and representation of Medication Containers.

The containers table is a vocabulary control table which stores a library of 
different Medication Containers which can be used to define medication attributes and 
perform conversions within the Narcotics Tracker.. 

This module handles the creation of the containers table, returns various 
container data from the database and parses the raw data returned from the 
database into a usable format. It houses the Container Class which defines and 
instantiates the containers as objects.

The Medication Module makes use of the containers.

The database module contains information on communicating with the database.

Classes:
    Container: Defines containers and instantiates them as objects.
    
Functions:

    return_table_creation_query: Returns the query needed to create the table.

    return_containers: Returns contents of containers as a list of strings.

    parse_container_data: Returns container data as a dictionary.
"""
import sqlite3

from narcotics_tracker import database


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the containers Table.

    Returns:
        str: The sql query needed to create the containers Table.
    """
    return """CREATE TABLE IF NOT EXISTS containers (
            CONTAINER_ID INTEGER PRIMARY KEY,
            CONTAINER_CODE TEXT UNIQUE,                
            CONTAINER_NAME TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""


def return_containers(db_connection: sqlite3.Connection) -> list[str]:
    """Returns the contents of the containers table as a list of strings.

    Args:
        db_connection (sqlite3.Connection): The database connection.

    Returns:
        table_contents (list[str]): The contents of the table as a list of
            strings.
    """
    sql_query = """SELECT * FROM containers"""

    containers_list = []

    containers_data = db_connection.return_data(sql_query)
    for container in containers_data:
        containers_list.append(
            f"Container {container[0]}: {container[2]}. Code: '{container[1]}'."
        )

    return containers_list


def parse_container_data(container_data) -> dict:
    """Returns container data from the database as a dictionary.

    Args:
        container_data (list): The container data

    Returns:
        properties (dict): Dictionary objects contains the properties of
            the container."""

    properties = {}

    properties["container_id"] = container_data[0][0]
    properties["container_code"] = container_data[0][1]
    properties["container_name"] = container_data[0][2]
    properties["created_date"] = container_data[0][3]
    properties["modified_date"] = container_data[0][4]
    properties["modified_by"] = container_data[0][5]

    return properties


class Container:
    """Defines Containers and instantiates them as objects.

    Containers can be declared, created and managed using this class. Medications
    will be limited to using the containers stored in the containers table.

    Attributes:

        container_id (int): Numeric identifier of each unit. Assigned by the
            database.

       container_code (str): Unique identifier of each unit type. Assigned by the
            user. Used to interact with the unit in the database.

        container_code (str): Name of the unit.

        created_date (str): The date the unit type was created in the
            table.

        modified_date (str): The date the unit type was last modified.

        modified_by (str): Identifier of the user who last modified the
            unit type.

    Initializer:

    Instance Methods:
        __repr__: Returns a string expression of the unit.

        save: Saves a new unit to the containers table in the database.

        read: Returns the data of the unit from the database as a tuple.

        update: Updates the unit in the containers table of the
            database.

        delete: Deletes the unit from the database.

        return_attributes: Returns the attributes of the containers object as
            a tuple.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of an Unit using the UnitBuilder.

        containers are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of containers to the
        Builder Package.

        Refer to the documentation for the UnitBuilder Class for more
        information.

        Args:
            builder (unit_builder.UnitBuilder): The builder used to
                construct the Unit object.
        """
        self.container_id = builder.container_id
        self.container_code = builder.container_code
        self.container_name = builder.container_name
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """Returns a string expression of the unit.

        Returns:
            str: The string describing the unit specifying the event
                type's name, code and description.
        """
        return f"Unit Number {self.container_id}: {self.container_name}. Code: '{self.container_code}'."

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new unit to the containers table in the database.

        The save method will only write the unit into the table if it does
        not already exist. Use the update method to update the unit's
        attributes.

        Assigns a created_date and modified_date.

        Args:
            db_connection (sqlite3.Connection): The database connection.
        """
        sql_query = """INSERT OR IGNORE INTO containers VALUES (
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
        sql_query = """SELECT * from containers WHERE container_code = ?"""

        values = (self.container_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the unit in the containers table of the database.

        The update method will overwrite the unit's data if it already
        exists within the database. Use the save method to store new
        containers in the database.

        How to use:
            Use the containers.return_containers() method to return a list
            of containers.

            Use the database.load_unit() method, passing in the
            container_code of the unit you wish to update.

            Modify the attributes as necessary and call this method to update
            the attributes in the database.

            If you are changing the container_code use the save() method to create
            a new unit entry in the table and use the delete method to
            remove the old entry.

        Assigns a new modified_date.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

            container_code (str): The unique identifier of the unit.

        Raises:

            IndexError: An Index Error will be raised if the container_code is not
            found on the containers table.
        """
        sql_query = """UPDATE containers 
            SET container_id = ?, 
                container_code = ?, 
                container_name = ?, 
                created_date = ?, 
                modified_date = ?, 
                modified_by = ? 
            WHERE container_code = ?"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes() + (self.container_code,)

        db_connection.write_data(sql_query, values)

    def delete(self, db_connection: sqlite3.Connection):
        """Deletes the unit from the database.

        The delete method will delete the unit from the database
        entirely. Note: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM containers WHERE container_id = ?"""
        values = (self.container_id,)
        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the containers object as a tuple.

        Returns:
            tuple: The attributes of the containers. Follows the order
            of the columns in the containers table.
        """

        return (
            self.container_id,
            self.container_code,
            self.container_name,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )
