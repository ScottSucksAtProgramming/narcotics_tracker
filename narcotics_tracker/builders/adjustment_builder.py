"""Contains the concrete builder for the adjustment class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    AdjustmentBuilder: Builds and returns inventory adjustment objects.
"""

from narcotics_tracker import database, event_types, inventory, medication, periods
from narcotics_tracker.builders import adjustment_builder_template
from narcotics_tracker.utils import unit_converter


class AdjustmentBuilder(adjustment_builder_template.Adjustment):
    """Builds and returns inventory adjustment objects.

    Initializer:

    Instance Methods:

    Exceptions:

    """

    def __init__(self) -> None:
        """Initializes the adjustment builder. Sets all attributes to None."""
        self.database_connection = None
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

    def set_database_connection(self, database_file: str) -> None:
        """Sets the connections to the database.

        Args:
            db_connection (sqlite3.Connection): Connection to the database.
        """
        db = database.Database()
        db.connect(database_file)

        self.database_connection = db

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

    def set_created_date(self, created_date: str) -> None:
        """Sets the adjustment's created date. Should not be called users.

        This method will set the adjustment's created date. The created date
        is set automatically when the adjustment is saved in the database.
        This method is useful in setting the created date when loading a
        adjustment from the database. It will override any created date set in
        the database table. Users should not call this method.

        Args:
            created_date (str): The date the adjustment was created.
        """
        self.created_date = created_date

    def set_modified_date(self, modified_date: str) -> None:
        """Sets the adjustment's modified date. Should not be called the user.

        This method will set the adjustment's modified by date. The modified
        by date is set automatically when the adjustment is updated in the
        database. This method is useful in setting the modified_by date when
        loading a adjustment from the database. It will override any modified
        by date set in the database table. Users should not call this method.

        Args:
            modified_date (str): The date the adjustment was last modified.
        """
        self.modified_date = modified_date

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who last modified the adjustment.

        Args:
            modified_by (str): The identifier of the user who last modified
                the adjustment."""
        self.modified_by = modified_by

    def calculate_amount_in_mcg(self) -> None:
        """Calculates and sets the adjustment amount in micrograms."""
        preferred_unit = medication.return_preferred_unit(
            self.medication_code, db_connection=self.database_connection
        )

        amount_in_mcg = unit_converter.UnitConverter.to_mcg(
            self.amount_in_preferred_unit, preferred_unit
        )

        operator = event_types.return_operator(
            self.event_code, self.database_connection
        )

        self.amount_in_mcg = amount_in_mcg * operator

    def assign_reporting_period(self) -> None:
        """Checks that adjustment_date and assigns the period it falls within."""

        # Todo: Get Reporting Periods with their start and end dates.
        _, reporting_periods = periods.return_periods(self.database_connection)

        # Todo: Compare the dates and assign the reporting_period's id as reporting_period_id.
        for period in reporting_periods:
            if period[1] <= self.adjustment_date and self.adjustment_date <= period[2]:
                self.reporting_period_id = period[0]
                return
            else:
                self.reporting_period_id = None

    def build(self) -> "inventory.Adjustment":
        """Returns the Adjustment object. Assigns the Adjustment's properties.

        This is the last method to be called as part of the building process.
        It will return the Adjustment object with all of its properties set.


        Returns:
            inventory.Adjustment: The inventory adjustment object.
        """
        self.calculate_amount_in_mcg()
        self.assign_reporting_period()

        return inventory.Adjustment(self)
