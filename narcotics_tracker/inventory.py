"""Contains the implementation and representation of inventory adjustments.

The inventory table is the main table used in the Narcotics Tracker. It stores 
Adjustments which are the specific events that make changes to the inventory, 
such as administration to a patient or sending drugs to a reverse distributor 
for destruction.

Multiple modules including Event Types, Medication, and the Database module 
will interact heavily with this table.

This module handles the creation of the inventory table. The Adjustment class 
defines the representation of the inventory adjustments.

See the database module for information on interacting with the database.

Classes:

    Adjustment: Defines the events that adjust the inventory amounts.

Functions:

    return_table_creation_query: Returns query to create the inventory table.

    parse_adjustment_data: Returns adjustment data as dictionary.
"""

import sqlite3

from narcotics_tracker import database


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the inventory table."""
    return """CREATE TABLE IF NOT EXISTS inventory (
            ADJUSTMENT_ID INTEGER PRIMARY KEY,
            ADJUSTMENT_DATE INTEGER,
            EVENT_CODE TEXT,
            MEDICATION_CODE TEXT,
            QUANTITY_IN_MCG REAL,
            REPORTING_PERIOD_ID INTEGER,
            REFERENCE_ID TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT,
            FOREIGN KEY (EVENT_CODE) REFERENCES events (EVENT_CODE) ON UPDATE CASCADE,
            FOREIGN KEY (MEDICATION_CODE) REFERENCES medications (MEDICATION_CODE) ON UPDATE CASCADE,
            FOREIGN KEY (REPORTING_PERIOD_ID) REFERENCES reporting_periods (PERIOD_ID) ON UPDATE CASCADE
            )"""


def parse_adjustment_data(adjustment_data) -> dict:
    """Returns adjustment data from the database as a dictionary.

    Args:
        adjustment_data (list): The adjustment's attributes

    Returns:
        properties (dict): Dictionary objects contains the properties of
            the adjustment."""

    properties = {}

    properties["adjustment_id"] = adjustment_data[0][0]
    properties["adjustment_date"] = adjustment_data[0][1]
    properties["event_code"] = adjustment_data[0][2]
    properties["medication_code"] = adjustment_data[0][3]
    properties["amount_in_mcg"] = adjustment_data[0][4]
    properties["reporting_period_id"] = adjustment_data[0][5]
    properties["reference_id"] = adjustment_data[0][6]
    properties["created_date"] = adjustment_data[0][7]
    properties["modified_date"] = adjustment_data[0][8]
    properties["modified_by"] = adjustment_data[0][9]

    return properties


class Adjustment:
    """Defines the representation of inventory changes.

    Event Types have been declared in the events module and EventTypes
    class. Take a look at those items for information on created and declaring
    new event types.

    This Adjustment class handles the creation and management of the specific
    adjustments that change the stock. All of these adjustments will live
    within the inventory table. Each adjustment specifies the specific medication
    which was adjusted using it's code, the amount of medication which was
    changed (in the preferred unit) and which adjustment occurred.
    """

    def __init__(self, builder=None) -> None:
        """Initializes the adjustment object using the AdjustmentBuilder.

        Adjustments have a handful of attributes and require combining data
        from multiple tables. The Builder Pattern will allow for an easier to
        understand step-wise approach to building these objects. Refer to the
        documentation for the AdjustmentBuilder for more information.
        """
        self.database_connection = builder.database_connection
        self.adjustment_id = builder.adjustment_id
        self.adjustment_date = builder.adjustment_date
        self.event_code = builder.event_code
        self.medication_code = builder.medication_code
        self.amount_in_preferred_unit = builder.amount_in_preferred_unit
        self.amount_in_mcg = builder.amount_in_mcg
        self.reporting_period_id = builder.reporting_period_id
        self.reference_id = builder.reference_id
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """Returns a string expression of the adjustment object.

        Returns:
            str: The string describing the adjustment object
        """
        with database.Database("inventory.db") as db:

            preferred_unit = db.return_data(
                """SELECT preferred_unit FROM medications WHERE medication_code = (?)""",
                [self.medication_code],
            )[0][0]

            medication_name = db.return_data(
                """SELECT name FROM medications WHERE medication_code = (?)""",
                [self.medication_code],
            )[0][0]

            event_name = db.return_data(
                """SELECT event_name FROM events WHERE event_code = (?)""",
                [self.event_code],
            )[0][0]

            return (
                f"Adjustment Number {self.adjustment_id}: "
                f"{self.amount_in_preferred_unit} {preferred_unit} of "
                f"{medication_name} {event_name} on "
                f"{database.format_datetime_from_unixepoch(self.adjustment_date)}."
            )

    def save(self, db_connection: sqlite3.Connection) -> None:
        """Saves a new adjustment to the database.

        The save method will only write the adjustment into the table if it
        does not already exist. Use the update methods to update the
        adjustment's attributes.

        Sets created date if created date is None.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """

        sql_query = """INSERT OR IGNORE INTO inventory VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def read(self, db_connection: sqlite3.Connection) -> tuple:
        """Returns the data of the adjustment from the database as a tuple.

        This function will make no changes to the data.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:
            tuple: A tuple containing the adjustment's attribute values.
        """
        sql_query = """SELECT * from inventory WHERE adjustment_id = ?"""

        values = (self.adjustment_id,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the adjustment in the inventory table of the database.

        The update method will overwrite the adjustment's data if it already
        exists within the database. Use the save method to store new
        adjustments in the database.

        How to use:
            Use the inventory.return_adjustment() method to return a list
            of adjustments.

            Use the database.load_adjustment() method, passing in the
            adjustment_id of the adjustment you wish to update.

            Modify the attributes as necessary and call this method to update
            the attributes in the database.

            If you are changing the adjustment_id use the save() method to
            create a new adjustment entry in the table and use the delete
            method to remove the old entry.

        Assigns a new modified_date.

        Args:
            db_connection (sqlite3.Connection): The connection to the
            database.

            adjustment_id (str): The numeric identifier of the adjustment.

        Raises:

            IndexError: An Index Error will be raised if the adjustment_id is not
            found on the inventory table.
        """
        sql_query = """UPDATE inventory 
            SET ADJUSTMENT_ID = ?, 
                ADJUSTMENT_DATE = ?,
                EVENT_CODE = ?, 
                MEDICATION_CODE = ?, 
                QUANTITY_IN_MCG = ?, 
                REPORTING_PERIOD_ID = ?,
                REFERENCE_ID = ?,
                CREATED_DATE = ?, 
                MODIFIED_DATE = ?, 
                MODIFIED_BY = ? 
            WHERE ADJUSTMENT_ID = ?"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes() + (self.adjustment_id,)

        db_connection.write_data(sql_query, values)

    def delete(self, db_connection: sqlite3.Connection) -> None:
        """Delete the adjustment from the database.

        The delete will delete the adjustment from the database entirely.
        Note: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """

        sql_query = """DELETE FROM inventory WHERE adjustment_id = ?"""
        values = (self.adjustment_id,)
        db_connection.write_data(sql_query, values)

    def return_attributes(self) -> tuple:
        """Returns the attributes of the medication as a tuple.

        Returns:
            tuple: The attributes of the medication. Follows the order of the
                columns in the medication table.
        """

        return (
            self.adjustment_id,
            self.adjustment_date,
            self.event_code,
            self.medication_code,
            self.amount_in_mcg,
            self.reporting_period_id,
            self.reference_id,
            self.created_date,
            self.modified_date,
            self.modified_by,
        )
