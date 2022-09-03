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
