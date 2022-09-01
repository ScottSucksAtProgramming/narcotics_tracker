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
    """Builds and returns ReportingPeriod objects.

    Initializer:

    Instance Methods:

    Exceptions:

    """

    def __init__(self) -> None:
        """Initializes reporting period builder. Sets all attributes to None."""
        self.period_id = None
        self.starting_date = None
        self.ending_date = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def set_period_id(self, period_id: int) -> None:
        """Sets the period's id number. Should not be called by the user.

        This method will set the ReportingPeriod's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the ReportingPeriod is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            period_id (int): The ReportingPeriod's numeric id.
        """
        self.period_id = period_id

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

    def set_created_date(self, created_date: str) -> None:
        """Sets the ReportingPeriod's created_date.

        This method will set the ReportingPeriod's created_date.

        Args:
            created_date (str): The ReportingPeriod's created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.created_date = database.return_datetime(created_date)

    def set_modified_date(self, modified_date: str) -> None:
        """Sets the ReportingPeriod's modified_date.

        This method will set the ReportingPeriod's modified_date.

        Args:
            modified_date (str): The ReportingPeriod's created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.modified_date = database.return_datetime(modified_date)

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the ReportingPeriod's modified_by attribute.

        This method will set the ReportingPeriod's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the
                reporting period.
        """
        self.modified_by = modified_by

    def set_all_properties(self, properties: dict) -> None:
        """Sets all properties of the ReportingPeriod.

        Args:
            properties (dict): The properties of the ReportingPeriod.
                Dictionary keys are formatted as the ReportingPeriod attribute
                names.
        """
        self.set_period_id(properties["period_id"])
        self.set_starting_date(properties["starting_date"])
        self.set_ending_date(properties["ending_date"])
        self.set_created_date(properties["created_date"])
        self.set_modified_date(properties["modified_date"])
        self.set_modified_by(properties["modified_by"])

    def build(self) -> "reporting_periods.ReportingPeriodType":
        """Assigns attributes and returns a ReportingType Object.

        This is the last method to be called as part of the building process.
        It will return the ReportingPeriodType object with all of its
        properties set.


        Returns:
            reporting_periods.ReportingPeriodType: The ReportingPeriod Object.
        """

        return reporting_periods.ReportingPeriod(self)
