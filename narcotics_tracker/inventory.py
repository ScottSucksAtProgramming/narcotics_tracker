"""Contains the implementation and representation of Inventory Adjustments.

#* Background

The inventory table is the main table used in the Narcotics Tracker. It stores 
Adjustments which are the specific events that make changes to the amount of 
controlled substances in the inventory, such as administration to a patient or 
sending drugs to a reverse distributor for destruction.

Multiple modules including Event Types, Medication, and the Database module 
will interact heavily with this table.

#* Intended Use

This module and the Adjustment Class defined below allow for the creation of 
Adjustment Objects. It is highly recommended to use the Adjustment Builder 
Module contained within the Builders Package to create these objects. 
Instructions for using builders can be found within that package.

#* Adjustments in the Database

Adjustments are stored in the 'inventory' table of the database with their 
numeric id, adjustment date, event code, medication code, amount, 
reporting period, reference id, and creation / modification information 
specified. Reports will make use of Adjustment's in the table to calculate 
medication amount on hand and print out various information for reporting to 
oversight organization.

#* Classes:

    Adjustment: Defines Inventory Adjustments and instantiates them as objects.

#* Functions:

    return_table_creation_query: Returns the query needed to create the 
        'inventory' table.

    parse_adjustment_data: Returns an Adjustment's attributes as a dictionary.
"""

import sqlite3

from narcotics_tracker import database


def return_table_creation_query() -> str:
    """Returns the query needed to create the 'inventory' table.

    Returns:

        str: The sql query needed to create the 'inventory' table.
    """
    return """CREATE TABLE IF NOT EXISTS inventory (
            ADJUSTMENT_ID INTEGER PRIMARY KEY,
            ADJUSTMENT_DATE INTEGER,
            EVENT_CODE TEXT,
            MEDICATION_CODE TEXT,
            AMOUNT_IN_MCG REAL,
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
    """Returns an Adjustment's attributes as a dictionary.

    Args:

        adjustment_data (list): The Adjustment's data.

    Returns:

        attributes (dict): Dictionary object containing the attributes of the
            Adjustment.
    """
    attributes = {}

    attributes["adjustment_id"] = adjustment_data[0][0]
    attributes["adjustment_date"] = adjustment_data[0][1]
    attributes["event_code"] = adjustment_data[0][2]
    attributes["medication_code"] = adjustment_data[0][3]
    attributes["amount_in_mcg"] = adjustment_data[0][4]
    attributes["reporting_period_id"] = adjustment_data[0][5]
    attributes["reference_id"] = adjustment_data[0][6]
    attributes["created_date"] = adjustment_data[0][7]
    attributes["modified_date"] = adjustment_data[0][8]
    attributes["modified_by"] = adjustment_data[0][9]

    return attributes


class Adjustment:
    """Defines Inventory Adjustments and instantiates them as objects.

    This class defines Adjustments within the Narcotics Tracker. Adjustments
    are the individual entries which change the amount of medication in the
    inventory.

    Adjustments can be declared, created and managed using this class. They
    are stored in the 'inventory' table.

    Initializer:

        def __init__(self, builder=None) -> None:

            Initializes an instance of an Adjustment using the builder.

    Attributes:

        adjustment_id (int): The numeric identifier of the Adjustment in the
            database. Assigned by the database.

        adjustment_date (int): The date on which the adjustment occurred.

        event_code (str): The unique event_code of the adjustment.

        medication_code (str): The unique medication_code of the medication
            which was effected by the adjustment.

        adjustment_amount (float): The amount of medication changed in this
            adjustment.

        reference_id (str): The identifier of the reference material which
            contains additional information regarding the adjustment.

        created_date (str): The date the Adjustment was created in the
            table.

        modified_date (str): The date the Adjustment was last modified.

        modified_by (str): Identifier of the person who last modified the
            Adjustment.

    Instance Methods:

        __repr__: Returns a string expression of the Adjustment Object.

        save: Saves a new Adjustment to the table in the database.

        read: Returns the data of the Adjustment as a tuple.

        update: Updates the Adjustment in the 'inventory' table.

        check_and_convert_amount_in_mcg: Checks if the event operator was
            changed and updates the amount.

        return_attributes: Returns the attributes of the Adjustment Object as
            a tuple.

        delete: Deletes the Adjustment from the database.
    """

    def __init__(self, builder=None) -> None:
        """Initializes an instance of an Adjustment using the builder.

        Adjustments are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of Adjustments to the Builder
        Package.

        Refer to the documentation for the AdjustmentBuilder Class for more
        information.

        Args:

            builder (adjustment_builder.AdjustmentBuilder): The builder used
                to construct the Adjustment Object.
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
        """Returns a string expression of the Adjustment Object.

        Returns:

            str: The string describing the Adjustment Object.
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
        """Saves a new Adjustment to the table in the database.

        This method will not overwrite a Adjustment already saved in the
        database. Use the `update()` to adjust a Adjustment's attributes.

        Assigns a created_date and modified_date.

        Args:

            db_connection (sqlite3.Connection): The database connection.
        """

        sql_query = """INSERT OR IGNORE INTO inventory VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes()

        db_connection.write_data(sql_query, values)

    def read(self, db_connection: sqlite3.Connection) -> tuple:
        """Returns the data of the Adjustment as a tuple.

        This method makes no changes to the data.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Returns:

            tuple: A tuple containing the Adjustment's attribute values
                in the order of the 'inventory' table's columns.
        """
        sql_query = """SELECT * from inventory WHERE adjustment_id = ?"""

        values = (self.adjustment_id,)

        data = db_connection.return_data(sql_query, values)

        return data

    def update(self, db_connection: sqlite3.Connection) -> None:
        """Updates the Adjustment in the 'inventory' table.

        This method will overwrite the Adjustment's data if it already exists
        within the database. An error will be returned if the adjustment_id
        does not already exist in the database. Use the save method to save
        new Adjustments in the database.

        Assigns a new modified_date.

        Args:

            db_connection (sqlite3.Connection): The connection to the
            database.

        Raises:

            IndexError: An Index Error will be raised if the adjustment_code
            is not found on the inventory table.

        How to use:

            1. Use the `inventory.return_adjustments()` method to return a
                list of adjustments. Identify the adjustment_id of the
                Adjustment you wish to update.

            2. Use the database.load_adjustment() method, passing in the
                adjustment_id and assigning it to a variable to create a
                Adjustment Object.

            3. Modify the attributes as necessary and call this method on the
                Adjustment Object to send the new values to the database.

            #! Note: If the adjustment_id is being changed use the save()
            #! method to create a new adjustment entry in the table and use
            #! the delete() method to remove the old entry.
        """
        sql_query = """UPDATE inventory 
            SET ADJUSTMENT_ID = ?, 
                ADJUSTMENT_DATE = ?,
                EVENT_CODE = ?, 
                MEDICATION_CODE = ?, 
                AMOUNT_IN_MCG = ?, 
                REPORTING_PERIOD_ID = ?,
                REFERENCE_ID = ?,
                CREATED_DATE = ?, 
                MODIFIED_DATE = ?, 
                MODIFIED_BY = ? 
            WHERE ADJUSTMENT_ID = ?"""

        self.check_and_convert_amount_in_mcg(db_connection)

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes() + (self.adjustment_id,)

        db_connection.write_data(sql_query, values)

    def check_and_convert_amount_in_mcg(
        self, db_connection: sqlite3.Connection
    ) -> None:
        """Checks if the event operator was changed and updates the amount.

        This method is called when an Adjustment is updated. It pulls the
        original operator from the events table, compares it to the new
        operator. If they are different the amount is adjusted appropriately.

        Args:

        db_connection (sqlite3.Connection): The database connection.
        """
        old_event_code = db_connection.return_data(
            f"""SELECT event_code FROM inventory WHERE adjustment_id='{self.adjustment_id}'"""
        )[0][0]

        old_operator = db_connection.return_data(
            f"""SELECT operator FROM events WHERE event_code = '{old_event_code}'"""
        )[0][0]

        new_operator = db_connection.return_data(
            f"""SELECT operator FROM events WHERE event_code = '{self.event_code}'"""
        )[0][0]

        if old_operator != new_operator:
            self.amount_in_mcg = self.amount_in_mcg * -1

    def return_attributes(self) -> tuple:
        """Returns the attributes of the Adjustment Object as a tuple.

        Returns:

            tuple: The attributes of the Adjustment. Follows the order of the
                columns in the 'inventory` table.
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

    def delete(self, db_connection: sqlite3.Connection) -> None:
        """Deletes the Adjustment from the database.

        The delete method will delete the Adjustment from the database
        entirely.

        #! Note: Deleting an item from the database is irreversible.

        Args:

            db_connection (sqlite3.Connection): The connection to the
                database.
        """
        sql_query = """DELETE FROM inventory WHERE adjustment_id = ?"""
        values = (self.adjustment_id,)
        db_connection.write_data(sql_query, values)
