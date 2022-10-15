"""Contains implementation and representation of Medication Containers.

#* Background

All controlled substance medications come in containers which store a specific 
amount of the medication and its solvent. When purchasing medications they are 
often ordered by the container. All Medications require their container to be 
specified.

#* Intended Use

The module and the Container Class defined below allow for the creation of 
Container Objects. It is highly recommended to use the Container Builder 
Module contained within the Builders Package to create these objects. 
Instructions for using builders can be found within that package.

#* Containers in the Database

Containers are stored in the 'containers' table of the database with their 
numeric id, code, name and creation / modification information specified. 
Medication objects must declare which container the medication comes in and 
are limited to the items listed in the 'containers' table.

The Narcotics Tracker comes with a selection of pre-defined containers. Refer 
to the Standard Items Module inside the Setup Package for more information.

#* Classes:

    Container: Defines Containers and instantiates them as objects.
    
#* Functions:

    return_table_creation_query: Returns the query needed to create the 
        'containers' table.

    return_containers: Returns the 'containers' table as lists of strings and 
        values.

    parse_container_data: Returns a Container's attributes as a dictionary.
"""
import sqlite3
from typing import Union

from persistence import database


def return_table_creation_query() -> str:
    """Returns the query needed to create the 'containers' table.

    Returns:

        str: The sql query needed to create the 'containers' table.
    """
    return """CREATE TABLE IF NOT EXISTS containers (
            CONTAINER_ID INTEGER PRIMARY KEY,
            CONTAINER_CODE TEXT UNIQUE,                
            CONTAINER_NAME TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""


def return_containers(db_connection: sqlite3.Connection) -> Union[list[str], list]:
    """Returns the 'containers' table as lists of strings and values.

    Args:

        db_connection (sqlite3.Connection): The database connection.

    Returns:

        containers_string_list (list[str]): The contents of the table as a list of
            strings.

        containers_values_list (list): The contents of the table as a list of
            values.
    """
    sql_query = (
        """SELECT container_id, container_code, container_name FROM containers"""
    )

    containers_strings_list = []
    containers_values_list = []

    containers_data = db_connection.return_data(sql_query)
    for container in containers_data:
        containers_strings_list.append(
            f"Container {container[0]}: {container[2]}. Code: '{container[1]}'."
        )
        containers_values_list.append((container[0], container[1], container[2]))

    return containers_strings_list, containers_values_list


def parse_container_data(container_data) -> dict:
    """Returns a Container's attributes as a dictionary.

    Args:

        container_data (list): The Container's data.

    Returns:

        attributes (dict): Dictionary object containing the attributes of the
            Container.
    """
    attributes = {}

    attributes["container_id"] = container_data[0][0]
    attributes["container_code"] = container_data[0][1]
    attributes["container_name"] = container_data[0][2]
    attributes["created_date"] = container_data[0][3]
    attributes["modified_date"] = container_data[0][4]
    attributes["modified_by"] = container_data[0][5]

    return attributes


class Container:
    """Defines Containers and instantiates them as objects.

    This class defines Containers within the Narcotics Tracker. Containers are
    the vessels which hold medications. When controlled substance medications
    are ordered an amount of containers is specified. Each Medication must
    specify the container they come in and are limited to the items listed in
    the 'containers' table.

    Containers can be declared, created and managed using this class. They are
    stored in the 'containers' table.

    Attributes:

        container_id (int): Numeric identifier of each Container. Assigned by
        the database.

       container_code (str): Unique identifier of each Container. Assigned by
       the user. Used to interact with the Container in the database.

        container_code (str): Name of the Container.

        created_date (str): The date the Container was created in the
            table.

        modified_date (str): The date the Container was last modified.

        modified_by (str): Identifier of the user who last modified the
            Container.

    Initializer:

        def __init__(self, builder=None) -> None:

            Initializes an instance of n Container using the builder.

    Instance Methods:
        __repr__: Returns a string expression of the Container Object.

        save: Saves a new Container to the table in the database.

        read: Returns the data of the Container as a tuple.

        update: Updates the Container in the 'containers' table.

        return_attributes: Returns the attributes of the Container Object as a
            tuple.

        delete: Deletes the Container from the database.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of n Container using the builder.

        Containers are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of Containers to the Builder
        Package.

        Refer to the documentation for the ContainerBuilder Class for more
        information.

        Args:

            builder (container_builder.ContainerBuilder): The builder used
                to construct the Container Object.
        """
        self.container_id = builder.container_id
        self.container_code = builder.container_code
        self.container_name = builder.container_name
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """Returns a string expression of the Container Object.

        Returns:

            str: The string describing the Container Object.
        """
        return f"Unit Number {self.container_id}: {self.container_name}. Code: '{self.container_code}'."

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new Container to the table in the database.

        This method will not overwrite a Container already saved in the
        database. Use the `update()` to adjust a Container's attributes.

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
        """Returns the data of the Container as a tuple.

        This method makes no changes to the data.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:

            tuple: A tuple containing the Container's attribute values
                in the order of the 'containers' table's columns.
        """
        sql_query = """SELECT * from containers WHERE container_code = ?"""

        values = (self.container_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the Container in the 'containers' table.

        This method will overwrite the Container's data if it already exists
        within the database. An error will be returned if the container_code
        does not already exist in the database. Use the save method to save
        new Containers in the database.

        Assigns a new modified_date.

        Args:

            db_connection (sqlite3.Connection): The connection to the database.

        Raises:

            IndexError: An Index Error will be raised if the container_code is
            not found on the Containers table.

        How to use:

            1. Use the `containers.return_containers()` method to return a
                list of Containers. Identify the container_code of the
                Container you wish to update.

            2. Use the database.load_container() method, passing in the
                container_code and assigning it to a variable to create a
                Container Object.

            3. Modify the attributes as necessary and call this method on the
                Container Object to send the new values to the database.

            #! Note: If the container_code is being changed use the save()
            #! method to create a new Container entry in the table and use
            #! the delete() method to remove the old entry.
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

    def return_attributes(self) -> tuple:
        """Returns the attributes of the Container Object as a tuple.

        Returns:

            tuple: The attributes of the Container. Follows the order of the
                columns in the 'containers` table.
        """

        return (
            self.container_id,
            self.container_code,
            self.container_name,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )

    def delete(self, db_connection: sqlite3.Connection) -> None:
        """Deletes the Container from the database.

        The delete method will delete the Container from the database
        entirely.

        #! Note: Deleting an item from the database is irreversible.

        Args:

            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM containers WHERE container_id = ?"""
        values = (self.container_id,)
        db_connection.write_data(sql_query, values)
