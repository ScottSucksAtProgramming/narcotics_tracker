"""Contains modules which permanently store Narcotics Tracker data.

This package serves as the persistence layer for this project.

Modules:
    Database (database.py): Manages Communication with the SQlite3 database.
    Date Manager: (date_manager.py): Obtains and formats datetimes for the 
        SQLite3 database.
    SQLite_Command (sqlite_command.py): Contains the protocol for any commands 
        which affect the SQLite3 database.
"""
