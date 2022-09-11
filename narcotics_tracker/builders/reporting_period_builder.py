"""Contains the concrete builder for the ReportingPeriod class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    ReportingPeriodBuilder: Builds and returns ReportingPeriod objects.
"""
from narcotics_tracker import database, reporting_periods
from narcotics_tracker.builders import reporting_period_builder_template


class ReportingPeriodBuilder(reporting_period_builder_template.ReportingPeriod):
    """Builds and returns Reporting Period objects.

    There are two types of methods: 'set' methods can be called to manually
    set attributes for the object; 'assign' methods perform calculations and
    are used as part of the build method to assign other attributes like the
    created date, or unit conversions.

    Look at the ReportingPeriod Class documentation in the Reporting Periods Module for
    more information on how to use the Reporting Period objects.

    How To Use:

        1. Create a database connection using the database.Database() context
        manager.

        2. Initialize the builder by assigning it to a variable and passing a
        database connection:
            ```p_builder = reporting_period_builder.ReportingPeriodBuilder(database_connection)```

        3. Call the following methods and pass the required values:
        ```set_starting_date()```; ```set_ending_date()```; and
        ```set_modified_by()```;

        4. Call the `build()` method to return an Reporting Period object.

    Initializer:

        def __init__(self) -> None:
        ```Initializes the Reporting Period Builder. Sets all attributes to
        None.```

    Instance Methods:

        build: Returns the Reporting Period object and assigns attributes.

        set_starting_date: Sets the ReportingPeriod's starting_date.

        set_ending_dated: Sets the ReportingPeriod's ending_date.

        set_modified_by: Sets the identifier of the user who modified the
            Reporting Period.

        assign_all_attributes: Assigns all attributes of the Reporting Period.

        assign_reporting_period_id: Manually sets the Reporting Period's id.
            Not be called by the user.

        assign_created_date: Manually sets the created_date attribute.

        assign_modified_date: Manually sets the modified_date attribute.
    """

    def __init__(self) -> None:
        """Initializes reporting Period builder. Sets all attributes to None."""
        self.period_id = None
        self.starting_date = None
        self.ending_date = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def build(self) -> "reporting_periods.ReportingPeriodType":
        """Returns the Reporting Period object and assigns attributes.

        This is the last method to be called as part of the building process.
        It will return the ReportingPeriodType object with all of its
        properties set.


        Returns:
            reporting_periods.ReportingPeriodType: The ReportingPeriod Object.
        """

        return reporting_periods.ReportingPeriod(self)

    def set_starting_date(self, starting_date: str) -> None:
        """Sets the ReportingPeriod's starting_date.

        This method will set the ReportingPeriod's starting_date.

        Args:
            starting_date (str): The date the reporting period started on.
                Formatted as YYYY-MM-DD HH:MM:SS.
        """
        self.starting_date = database.return_datetime(starting_date)

    def set_ending_date(self, ending_date: str) -> None:
        """Sets the ReportingPeriod's ending_date.

        This method will set the ReportingPeriod's ending_date.

        Args:
            ending_date (str): The date teh reporting period ended on.
                Formatted as YYYY-MM-DD HH:MM:SS.
        """
        self.ending_date = database.return_datetime(ending_date)

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who modified the Reporting Period.

        This method will set the Reporting Period's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the
                Reporting Period.
        """
        self.modified_by = modified_by

    def assign_all_attributes(self, attributes: dict) -> None:
        """Assigns all attributes of the Reporting Period.

        Args:
            attributes (dict): The attributes of the ReportingPeriod.
                Dictionary keys are formatted as the ReportingPeriod attribute
                names.
        """
        self.assign_period_id(attributes["period_id"])
        self.set_starting_date(attributes["starting_date"])
        self.set_ending_date(attributes["ending_date"])
        self.assign_created_date(attributes["created_date"])
        self.assign_modified_date(attributes["modified_date"])
        self.set_modified_by(attributes["modified_by"])

    def assign_period_id(self, period_id: int) -> None:
        """Manually sets the Reporting Period's id. Not be called by the user.

        This method will set the Reporting Period's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the Reporting Period is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            period_id (int): The Reporting Period's numeric id.
        """
        self.period_id = period_id

    def assign_created_date(self, created_date: str) -> None:
        """Manually sets the created_date attribute.

        Note: This method is not intended to be called when building an Medication.

        Args:
            created_date (str): The date the Medication object was created.
                Must be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.created_date = database.return_datetime(created_date)

    def assign_modified_date(self, modified_date: str) -> None:
        """Manually sets the modified_date attribute.

        Note: This method is not intended to be called when building a
        Reporting Period.

        Args:
            modified_date (str): The date the Reporting Period was last
                modified. Must be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.modified_date = database.return_datetime(modified_date)
