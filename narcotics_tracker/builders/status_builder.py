"""Contains the concrete builder for the Status class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    StatusBuilder: Builds and returns Status objects.
"""
from narcotics_tracker import database, statuses
from narcotics_tracker.builders import status_builder_template


class StatusBuilder(status_builder_template.Status):
    """Builds and returns Status objects.

    Initializer:

    Instance Methods:

    Exceptions:

    """

    def __init__(self) -> None:
        """Initializes status builder. Sets all attributes to None."""
        self.status_id = None
        self.status_code = None
        self.status_name = None
        self.description = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def set_status_id(self, status_id: int) -> None:
        """Sets the statuses' id number. Should not be called by the user.

        This method will set the statuses' id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the Status is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            status_id (int): The statuses' numeric id.
        """
        self.status_id = status_id

    def set_status_code(self, status_code: str) -> None:
        """Sets the statuses' status_code.

        The status code is the unique identifier for the status. It is used to
        interact with the status in the database. The status code should be the
        lower case abbreviation of the status.

        Args:
            status_code (str): The unique identifier for the status. It is
            recommended that the statuses' code should be the common lowercase
            abbreviation for the status.
        """
        self.status_code = status_code

    def set_status_name(self, status_name: str) -> None:
        """Sets the statuses' name.

        Args:
            status_name (str): The proper name for the status.
        """
        self.status_name = status_name

    def set_description(self, description: str) -> None:
        """Sets the statuses' description.

        Args:
            status_description (str): The proper description for the status.
        """
        self.description = description

    def set_created_date(self, created_date: str) -> None:
        """Sets the statuses' created_date.

        This method will set the statuses' created_date.

        Args:
            created_date (str): The statuses' created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.created_date = database.return_datetime(created_date)

    def set_modified_date(self, modified_date: str) -> None:
        """Sets the statuses' modified_date.

        This method will set the statuses' modified_date.

        Args:
            modified_date (str): The statuses' created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.modified_date = database.return_datetime(modified_date)

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the statuses' modified_by attribute.

        This method will set the statuses' modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the
                status.
        """
        self.modified_by = modified_by

    def set_all_properties(self, properties: dict) -> None:
        """Sets all properties of the status.

        Args:
            properties (dict): The properties of the status.
                Dictionary keys are formatted as the status attribute
                names.
        """
        self.set_status_id(properties["status_id"])
        self.set_status_code(properties["status_code"])
        self.set_status_name(properties["status_name"])
        self.set_description(properties["description"])
        self.set_created_date(properties["created_date"])
        self.set_modified_date(properties["modified_date"])
        self.set_modified_by(properties["modified_by"])

    def build(self) -> "statuses.status":
        """Assigns attributes and returns a status Object.

        This is the last method to be called as part of the building process.
        It will return the statusType object with all of its
        properties set.


        Returns:
            statuses.statusType: The status Object.
        """

        return statuses.Status(self)
