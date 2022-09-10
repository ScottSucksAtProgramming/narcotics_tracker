"""Contains the concrete builder for the Adjustment class.

Builders are used to construct objects. The abstract builder templates define 
the interface for the concrete builders which are used to define the object's 
attributes and instantiate them.

Using the builders is the preferred method for creating objects in the 
narcotics tracker. They allow for an easy-to-understand, step-by step-approach 
to building to objects as well as performing other calculations and obtaining 
information from the database as necessary.

Classes:

    AdjustmentBuilder: Builds and returns Inventory Adjustment objects.
"""
import sqlite3

from narcotics_tracker import (
    database,
    inventory,
    medications,
    reporting_periods,
)
from narcotics_tracker.builders import adjustment_builder_template
from narcotics_tracker.utils import unit_converter


class AdjustmentBuilder(adjustment_builder_template.Adjustment):
    """Builds and returns Inventory Adjustment objects.

    The AdjustmentBuilder class is used to construct Inventory Adjustment
    objects. There are two types of methods: 'set' methods can be called to
    manually set attributes for the object; 'assign' methods perform
    calculations and are used as part of the build method to assign other
    attributes like the created date, or unit conversions.

    Look at the Adjustment Class documentation in the Inventory Module for
    more information on how to use the Adjustment objects.

    How To Use:

        1. Create a database connection using the database.Database() context
        manager.

        2. Initialize the builder by assigning it to a variable and passing a
        database connection:
            ```adj_builder = adjustment_builder.AdjustmentBuilder(database_connection)```

        3. Call the following methods and pass the required values:
        ```set_adjustment_id()```; ```set_adjustment_date()```;
        ```set_event_code()```; ```set_medication_code()```;
        ```set_adjustment_amount()```; ```set_reference_id()```; and
        ```set_modified_by()```;

        4. Call the `build()` method to return an Adjustment object. The
        ```build()``` method will convert the adjustment_amount to the
        amount_in_mcg and assign the correct reporting_period based on the
        adjustment_date. If you would like assign these manually it's
        recommended to do so after the object has been created.

    Initializer:

    Instance Methods:

    Exceptions:

    """

    def __init__(self, db_connection: sqlite3.Connection) -> None:
        """Initializes the adjustment builder. Sets all attributes to None."""
        self.database_connection = db_connection
        self.adjustment_id = None
        self.adjustment_date = None
        self.event_code = None
        self.medication_code = None
        self.amount_in_preferred_unit = None
        self.amount_in_mcg = None
        self.reporting_period_id = None
        self.reference_id = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def build(self) -> "inventory.Adjustment":
        """Returns the Adjustment object. Assigns the Adjustment's properties.

        This is the last method to be called as part of the building process.
        It will return the Adjustment object with all of its properties set.

        Returns:
            inventory.Adjustment: The inventory adjustment object.
        """
        if self.amount_in_mcg == None:
            self.assign_amount_in_mcg()

        if self.reporting_period_id == None:
            self.assign_reporting_period(self.database_connection)

        return inventory.Adjustment(self)

    def set_adjustment_id(self, adjustment_id: int = None) -> None:
        """Sets the adjustment's id number. Should not be called by the user.

        This method will set the adjustment's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the adjustment is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            adjustment_id (int): The adjustment's unique id. Defaults to None.
        """
        self.adjustment_id = adjustment_id

    def set_adjustment_date(self, adjustment_date: str) -> None:
        """Sets the date which the adjustment happened.

        Args:
            adjustment_date (str): The date when the adjustment occurred.
                Formatted as YYYY-MM-DD HH:MM:SS.
        """
        self.adjustment_date = database.return_datetime(adjustment_date)

    def set_event_code(self, event_code: str) -> None:
        """Sets the unique event_code of the adjustment.

        The event_code is the unique identifier for the event which occurred.
        Valid events are ones which are saved in the event_types table of the
        database. Using event_codes which are not listed in that table will
        throw an error when trying to save the item to the inventory table.

        Args:
            event_code (str): Unique identifier for the event from the
            event_types table.
        """
        self.event_code = event_code

    def set_medication_code(self, medication_code: str) -> None:
        """Sets the medication_code of the medication which was adjusted.

        The medication_code is the unique identifier for the medication which
        was adjusted. Valid medications are stored in the medications table.
        Using invalid medication codes with throw and error when saving the
        adjustment to the database.

        Args:
            medication_code (str): Unique identifier of the medication from
                the medications table.
        """
        self.medication_code = medication_code

    def set_adjustment_amount(self, amount: float) -> None:
        """Sets the amount of medication changed in this adjustment.

        Specify the amount using the preferred unit and as a positive number.

        Args:
            adjustment_amount (float): The amount of medication that was
            changed. Should be denoted in the preferred unit of measurement
            and always as a positive number.
        """
        self.amount_in_preferred_unit = amount

    def set_reference_id(self, reference_id: str) -> None:
        """Sets the reference ID for the adjustment.

        Args:
            reference_id (str): The unique identifier of the origin of the
                adjustment event.
        """
        self.reference_id = reference_id

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who created the adjustment.

        Args:
            modified_by (str): The identifier of the user who created the
                adjustment.
        """
        self.modified_by = modified_by

    def assign_all_attributes(self, properties: dict) -> None:
        """Sets all properties of the adjustment.

        Args:
            properties (dict): The properties of the adjustment. Dictionary
                keys are formatted as the adjustment property names.
        """
        self.set_adjustment_id(properties["adjustment_id"])
        self.adjustment_date = properties["adjustment_date"]
        self.set_event_code(properties["event_code"])
        self.set_medication_code(properties["medication_code"])
        self.assign_amount_in_mcg(properties["amount_in_mcg"])
        self.set_reference_id(properties["reference_id"])
        self.assign_reporting_period(
            self.database_connection, properties["reporting_period_id"]
        )
        self.assign_created_date(properties["created_date"])
        self.assign_modified_date(properties["modified_date"])
        self.set_modified_by(properties["modified_by"])

    def assign_amount_in_mcg(self, amount: float = None) -> None:
        """Manually sets (or calculates) the amount_in_mcg attribute.

        If an amount is passed it will be set directly. Otherwise the
        correct amount will be assigned by converting the
        adjustment_amount from the medication's preferred unit to micrograms
        and multiplying it against the event's operator.

        Note: This method is not intended to be called when building an
        Adjustment.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.

            amount (float): The amount of medication changed in micrograms.
                Optional. Defaults to None.
        """
        if amount:
            self.amount_in_mcg = amount
            return

        preferred_unit = medications.return_preferred_unit(
            self.medication_code, db_connection=self.database_connection
        )

        converted_amount = unit_converter.UnitConverter.to_mcg(
            self.amount_in_preferred_unit, preferred_unit
        )

        operator = self.return_event_operator()

        self.amount_in_mcg = converted_amount * operator

    def return_event_operator(self) -> int:
        sql_query = (
            f"""SELECT operator FROM events WHERE event_code ='{self.event_code}'"""
        )

        return self.database_connection.return_data(sql_query)[0][0]

    def assign_created_date(self, created_date: str) -> None:
        """Manually sets the created_date attribute.

        Note: This method is not intended to be called when building an
        Adjustment.

        Args:
            created_date (str): The date the adjustment object was created.
                Must be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.created_date = database.return_datetime(created_date)

    def assign_modified_date(self, modified_date: str) -> None:
        """Manually sets the modified_date attribute.

        Note: This method is not intended to be called when building an
        Adjustment.

        Args:
            modified_date (str): The date the adjustment was last modified.
                Must be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.modified_date = database.return_datetime(modified_date)

    def assign_reporting_period(
        self, db_connection: sqlite3.Connection, reporting_period: int = None
    ) -> None:
        """Manually sets (or calculates) the Reporting Period ID.

        If a reporting_period is passed it will be assigned directly.
        Otherwise the correct reporting period will be assigned based on the
        adjustment_date.

        Note: This method is not intended to be called when building an
        Adjustment.

        Args:
            db_connection (sqlite3.Connection): The connection to the
                database.

            reporting_period (int): The numeric identifier of the reporting
                period which the adjustment fits in. Optional. Defaults to
                None.
        """
        if reporting_period:
            self.reporting_period_id = reporting_period
            return

        _, periods = reporting_periods.return_periods(db_connection)

        for period in periods:
            if period[1] <= self.adjustment_date and self.adjustment_date <= period[2]:
                self.reporting_period_id = period[0]
                return
            else:
                self.reporting_period_id = None
