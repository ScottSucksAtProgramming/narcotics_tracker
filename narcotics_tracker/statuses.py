"""Contains the implementation and representation of Object Statuses.

#* Background

It is likely that information in the inventory will be changed over time. 
Statuses were added to the Narcotics Tracker to record those changes and 
present users with information on items which are no longer being used, or are 
waiting for an update. An EMS agency may switch from one concentration of a 
controlled substance medication to a different one, or track a purchase order 
of medications through various stages. Statuses will assist the user in 
keeping track of these changes.

#* Intended Use

This module and the Status Class defined below allow for the creation of 
Status Objects. It is highly recommended to use the Status Builder Module 
contained within the Builders Package to create these objects. Instructions 
for using builders can be found within that package.

#* Statuses in the Database

Statuses are stored in the 'statuses' table of the database with their numeric 
ID, code, name, description and creation / modification information specified. 
Medication objects must specify their status and are limited to the statuses 
listed in the table.

The Narcotics Tracker comes with a selection of pre-defined statuses. Refer to 
the Standard Items Module inside the Setup Package for more information.

#* Classes:

    Status: Defines statuses and instantiates them as objects.
    
#* Functions:

    return_table_creation_query: Returns the query needed to create the 
        'statuses' table.

    return_status: Returns the contents of the statuses table as lists of 
        strings and values.

    parse_status_data: Returns a Status's attributes from the database as a 
        dictionary.
"""

import sqlite3
from typing import Union

from narcotics_tracker.persistence import database


def return_table_creation_query() -> str:
    """Returns the query needed to create the 'statuses' table.

    Returns:

        str: The sql query needed to create the 'statuses' table.
    """
    return """CREATE TABLE IF NOT EXISTS statuses (
            STATUS_ID INTEGER PRIMARY KEY,
            STATUS_CODE TEXT UNIQUE,                
            STATUS_NAME TEXT,
            DESCRIPTION TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""


def return_statuses(db_connection: sqlite3.Connection) -> Union[list[str], list]:
    """Returns the 'statuses' table as lists of strings and values.

    Args:

        db_connection (sqlite3.Connection): The database connection.

    Returns:

        status_string_list (list[str]): The contents of the table as a list of
            strings.

        status_values_list (list): The contents of the table as a list of
            values.
    """
    sql_query = (
        """SELECT status_id, status_code, status_name, description FROM statuses"""
    )

    status_string_list = []
    status_values_list = []

    status_data = db_connection.return_data(sql_query)

    for status in status_data:
        status_string_list.append(
            f"Status {status[0]}: {status[2]}. Code: '{status[1]}'. {status[3]}"
        )
        status_values_list.append((status[0], status[1], status[2], status[3]))

    return status_string_list, status_values_list


def parse_status_data(status_data) -> dict:
    """Returns a Status's attributes from the database as a dictionary.

    Args:

        status_data (list): The Status' data.

    Returns:

        attributes (dict): Dictionary object containing the attributes of the
            status.
    """
    attributes = {}

    attributes["status_id"] = status_data[0][0]
    attributes["status_code"] = status_data[0][1]
    attributes["status_name"] = status_data[0][2]
    attributes["description"] = status_data[0][3]
    attributes["created_date"] = status_data[0][4]
    attributes["modified_date"] = status_data[0][5]
    attributes["modified_by"] = status_data[0][6]

    return attributes


class Status:
    """Defines Statuses and instantiates them as objects.

    This class defines Statuses within the Narcotics Tracker. Statuses are
    used by various objects to denote their current condition.

    Statuses can be declared, created and managed using this class.
    Database items are limited to using the status stored in the 'statuses'
    table.

    Attributes:

        status_id (int): Numeric identifier of each Status. Assigned by the
            database.

        status_code (str): Unique identifier of each unit type. Assigned by the
            user. Used to interact with the unit in the database.

        status_code (str): Name of the unit.

        description (str): A string describing the status and how it should
            be used.

        created_date (str): The date the unit type was created in the
            table.

        modified_date (str): The date the unit type was last modified.

        modified_by (str): Identifier of the user who last modified the
            unit type.

    Initializer:

        def __init__(self, builder=None) -> None:

            Initializes an instance of a Status using the StatusBuilder.

    Instance Methods:
        __repr__: Returns a string expression of the Status.

        save: Saves a new Status to the 'statuses' table in the database.

        read: Returns the data of the Status from the database as a tuple.

        update: Updates the Status in the 'statuses' table of the database.

        return_attributes: Returns the attributes of the Status Object as a
            tuple.

        delete: Deletes the Status from the database.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of a Status using the StatusBuilder.

        Statuses are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of status to the
        Builder Package.

        Refer to the documentation for the StatusBuilder Class for more
        information.

        Args:

            builder (status_builder.StatusBuilder): The builder used to
                construct the Status object.
        """
        self.status_id = builder.status_id
        self.status_code = builder.status_code
        self.status_name = builder.status_name
        self.description = builder.description
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """

        Returns:Returns a string expression of the Status.

            str: The string describing the Status.
        """
        return f"Status {self.status_id}: {self.status_name}. Code: '{self.status_code}'. {self.description}"

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new Status to the 'statuses' table in the database.

        This method will not overwrite a Status already saved in the database.
        Use the `update()` to adjust a Status's attributes.

        Assigns a created_date and modified_date.

        Args:

            db_connection (sqlite3.Connection): The database connection.
        """
        sql_query = """INSERT OR IGNORE INTO statuses VALUES (
            ?, ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def read(self, db_connection: sqlite3.Connection) -> tuple:
        """Returns the data of the Status from the database as a tuple.

        This method makes no changes to the data.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:

            tuple: A tuple containing the Status's attribute values in the
                order of the table's columns.
        """
        sql_query = """SELECT * from statuses WHERE status_code = ?"""

        values = (self.status_code,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the Status in the 'statuses' table of the database.

        This method will overwrite the Status's data if it already exists within
        the database. An error will be returned if the Status_id does not
        already exist in the database. Use the save method to save new
        statuses in the database.

        Assigns a new modified_date.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

            status_code (str): The unique identifier of the Status.

        Raises:

            IndexError: An Index Error will be raised if the status_code is not
            found on the statuses table.

        How to use:

            1. Use the `statuses.return_status()` method to return a list of
                statuses. Identify the status_code of the status you wish to
                update.

            2. Use the database.load_status() method, passing in the
                status_code and assigning it to a variable to create a Status
                Object.

            3. Modify the attributes as necessary and call this method on the
                Status Object to send the new values to the database.

            #! Note: If the status_code is being changed use the save() method
            #! to create a new status entry in the table and use the delete()
            #! method to remove the old entry.
        """
        sql_query = """UPDATE statuses 
            SET status_id = ?, 
                status_code = ?, 
                status_name = ?, 
                description = ?,
                created_date = ?, 
                modified_date = ?, 
                modified_by = ? 
            WHERE status_code = ?"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes() + (self.status_code,)

        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the Status Object as a tuple.

        Returns:

            tuple: The attributes of the Status. Follows the order
            of the columns in the 'statuses' table.
        """

        return (
            self.status_id,
            self.status_code,
            self.status_name,
            self.description,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )

    def delete(self, db_connection: sqlite3.Connection) -> None:
        """Deletes the Status from the database.

        The delete method will delete the Status from the database
        entirely.

        #! Note: Deleting an item from the database is irreversible.

        Args:

            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM statuses WHERE status_id = ?"""
        values = (self.status_id,)
        db_connection.write_data(sql_query, values)
