"""Defines the representation of the inventory table and inventory events.

This module handles the creation of the inventory table. The Events class 
defines the representation of the events or lines in the inventory which will 
adjust the actual inventory amounts. 

See the database module for information on interacting with the database.
Tests are located in the tests/unit/inventory_test.py file.

Classes:

    Event: Defines the events that adjust the inventory amounts.

Functions:

    return_table_creation_query: Returns query to create the inventory table.

    #! parse_medication_data: Returns medication data from database as dictionary.
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
            FOREIGN KEY (EVENT_CODE) REFERENCES event_types (EVENT_CODE) ON UPDATE CASCADE,
            FOREIGN KEY (MEDICATION_CODE) REFERENCES medications (MEDICATION_CODE) ON UPDATE CASCADE,
            FOREIGN KEY (REPORTING_PERIOD_ID) REFERENCES reporting_periods (PERIOD_ID) ON UPDATE CASCADE
            )"""


class Adjustment:
    """Defines the representation of inventory changes.

    Event Types have been declared in the event_types module and EventTypes
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

        preferred_unit = self.database_connection.return_data(
            """SELECT preferred_unit FROM medications WHERE medication_code = (?)""",
            [self.medication_code],
        )[0][0]

        medication_name = self.database_connection.return_data(
            """SELECT name FROM medications WHERE medication_code = (?)""",
            [self.medication_code],
        )[0][0]

        event_name = self.database_connection.return_data(
            """SELECT event_name FROM event_types WHERE event_code = (?)""",
            [self.event_code],
        )[0][0]

        return (
            f"Adjustment Number {self.adjustment_id}: "
            f"{self.amount_in_preferred_unit} {preferred_unit} of "
            f"{medication_name} {event_name} on "
            f"{database.format_datetime_from_unixepoch(self.adjustment_date)}."
        )

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

    def save(self) -> None:
        """Saves a new adjustment to the database.

        The save method will only write the adjustment into the table if it
        does not already exist. Use the update methods to update the
        adjustment's attributes.

        Sets created date if created date is None.
        """

        sql_query = """INSERT OR IGNORE INTO inventory VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        if database.Database.created_date_is_none(self):
            self.created_date = database.return_datetime()
        self.modified_date = database.return_datetime()

        values = self.return_attributes()

        self.database_connection.write_data(sql_query, values)

    def update_adjustment_date(self, new_adjustment_date: str) -> None:
        """Updates the adjustment date of the adjustment.

        Args:
            new_adjustment_date (str): The new starting date in format
                YYY-MM-DD HH:MM:SS.
        """
        new_modified_date = database.return_datetime()

        sql_query = (
            """UPDATE inventory SET adjustment_date =(?) WHERE adjustment_id = (?)"""
        )
        values = (database.return_datetime(new_adjustment_date), self.adjustment_id)

        self.database_connection.write_data(sql_query, values)

        values = (new_modified_date, self.adjustment_id)
        self.database_connection.write_data(
            """UPDATE inventory SET modified_date = (?) WHERE adjustment_id= (?)""",
            values,
        )

    def return_event_codes(self) -> list[str]:
        """Queries the database for event codes.

        Returns:
            list[str]: List of event codes.
        """
        valid_event_codes = []
        event_codes = self.database_connection.return_data(
            """SELECT event_code FROM event_types"""
        )
        for event in event_codes:
            valid_event_codes.append(event[0])
        return valid_event_codes

    def return_event_attributes(self, event_code) -> list[str]:
        """Queries the database for and event's attributes.

        Returns:
            list[str]: List of the events attributes.
        """
        event_attributes_list = []
        event_data = self.database_connection.return_data(
            """SELECT * FROM event_types WHERE event_code =(?)""", [event_code]
        )[0]
        for event in event_data:
            event_attributes_list.append(event)
        return event_attributes_list

    def event_code_is_invalid(self, new_event_code) -> bool:
        """Checks the event code is listed in the event_types table.

        Returns:
            bool: True if event_code in event_types table, otherwise false.
        """
        event_codes_list = self.return_event_codes()

        if new_event_code in event_codes_list:
            return False
        else:
            return True

    def compare_operators(self, new_event_code) -> int:
        """Compares event operators and returns adjusted amount_in_mcg."""
        old_event_operator = self.return_event_attributes(self.event_code)[4]
        new_event_operator = self.return_event_attributes(new_event_code)[4]

        if old_event_operator != new_event_operator:
            new_amount_in_mcg = self.amount_in_mcg * -1
            self.amount_in_mcg = new_amount_in_mcg
        return self.amount_in_mcg

    def update_event_code(self, new_event_code: str) -> None:
        """Updates the adjustment date of the adjustment.

        Args:
            new_event_code (str): The new event_code.
        """
        # Check if new event code is valid.
        if self.event_code_is_invalid(new_event_code):
            raise ValueError

        # Compare operators and return adjusted amount_in_mcg.
        self.amount_in_mcg = self.compare_operators(new_event_code)

        # Get current modified date.
        self.modified_date = database.return_datetime()

        # Update the database.
        sql_query = """UPDATE inventory SET event_code =(?), quantity_in_mcg = (?), modified_date = (?) WHERE adjustment_id = (?)"""
        values = (
            new_event_code,
            self.amount_in_mcg,
            self.modified_date,
            self.adjustment_id,
        )

        self.database_connection.write_data(sql_query, values)

    def delete(self):
        """Delete the adjustment from the database.

        The delete will delete the adjustment from the database entirely.
        Note: This is irreversible.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.
        """

        sql_query = """DELETE FROM inventory WHERE adjustment_id = ?"""
        values = (self.adjustment_id,)
        self.database_connection.write_data(sql_query, values)
