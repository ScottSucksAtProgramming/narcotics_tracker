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


def return_table_creation_query() -> str:
    """Returns the sql query needed to create the inventory table."""
    return """CREATE TABLE IF NOT EXISTS inventory (
            INVENTORY_ID INTEGER PRIMARY KEY,
            EVENT_DATE TEXT,
            EVENT_CODE TEXT,
            MEDICATION_CODE TEXT,
            QUANTITY_IN_MCG REAL,
            REPORTING_PERIOD_ID INTEGER,
            REFERENCE_ID TEXT,
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT,
            FOREIGN KEY (EVENT_CODE) REFERENCES event_types (EVENT_CODE) ON UPDATE CASCADE ON DELETE RESTRICT,
            FOREIGN KEY (MEDICATION_CODE) REFERENCES medications (MEDICATION_CODE) ON UPDATE CASCADE ON DELETE RESTRICT,
            FOREIGN KEY (REPORTING_PERIOD_ID) REFERENCES reporting_periods (PERIOD_ID) ON UPDATE CASCADE ON DELETE RESTRICT
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
        self.reference_id = builder.reference_id
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by
