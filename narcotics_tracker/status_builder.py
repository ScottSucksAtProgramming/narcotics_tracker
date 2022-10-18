"""Contains the concrete builder for the Status class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    StatusBuilder: Builds and returns Status objects.
"""
from narcotics_tracker import database
from narcotics_tracker.builders import status_builder_template
from narcotics_tracker.items import statuses


class StatusBuilder(status_builder_template.Status):
    """Builds and returns Status objects.

    There are two types of methods: 'set' methods can be called to manually
    set attributes for the object; 'assign' methods perform calculations and
    are used as part of the build method to assign other attributes like the
    created date, or unit conversions.

    Look at the Status Class documentation in the Statuses Module for
    more information on how to use the Status objects.

    How To Use:

        1. Initialize the builder by assigning it to a variable:

            `stat_builder = status_builder.StatusBuilder()`

        2. Call the following methods and pass the required values:

            `set_status_code()`; `set_status_name()`;

            `set_description()`; and `set_modified_by()`;

        3. Call the `build()` method to return an Status object.

    Initializer:

        def __init__(self) -> None:

        Initializes status builder. Sets all attributes to None.

    Instance Methods:

        build: Returns the Status object and assigns attributes.

        set_status_code: Sets the unique code of the Status.

        set_status_name: Sets the proper name of the Status.

        set_description: Sets the description of the Status.

        set_modified_by: Sets the identifier of the user who modified the
            Status.

        assign_all_attributes: Sets all attributes of the status.

        assign_status_id: Manually sets the Status's id. Not be called by the
            user.

        assign_created_date: Manually sets the created_date attribute.

        assign_modified_date: Manually sets the modified_date attribute.

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

    def build(self) -> "statuses.status":
        """Returns the Status object and assigns attributes.

        This is the last method to be called as part of the building process.
        It will return the Status object with all of its
        properties set.


        Returns:
            statuses.Status: The Status Object.
        """

        return statuses.Status(self)

    def set_status_code(self, status_code: str) -> None:
        """Sets the unique code of the Status.

        The status code is the unique identifier for the status. It is used to
        interact with the status in the database. The status code should be
        the lower case abbreviation of the status.

        Args:
            status_code (str): The unique identifier for the status. It is
            recommended that the statuses' code should be the common lowercase
            abbreviation for the status.
        """
        self.status_code = status_code

    def set_status_name(self, status_name: str) -> None:
        """Sets the proper name of the Status.

        Args:
            status_name (str): The proper name for the status.
        """
        self.status_name = status_name

    def set_description(self, description: str) -> None:
        """Sets the description of the Status.

        Args:
            status_description (str): The proper description for the status.
        """
        self.description = description

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who modified the Status.

        This method will set the Status's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the Status.
        """
        self.modified_by = modified_by

    def assign_all_attributes(self, attributes: dict) -> None:
        """Sets all attributes of the status.

        Args:
            attributes (dict): The attributes of the status.
                Dictionary keys are formatted as the status attribute
                names.
        """
        self.assign_status_id(attributes["status_id"])
        self.set_status_code(attributes["status_code"])
        self.set_status_name(attributes["status_name"])
        self.set_description(attributes["description"])
        self.assign_created_date(attributes["created_date"])
        self.assign_modified_date(attributes["modified_date"])
        self.set_modified_by(attributes["modified_by"])

    def assign_status_id(self, status_id: int) -> None:
        """Manually sets the Status's id. Not be called by the user.

        This method will set the Status's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the Status is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            status_id (int): The Status's numeric id.
        """
        self.status_id = status_id

    def assign_created_date(self, created_date: str) -> None:
        """Manually sets the created_date attribute.

        Note: This method is not intended to be called when building a Status.

        Args:
            created_date (str): The date the Status object was created. Must
                be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.created_date = database.return_datetime(created_date)

    def assign_modified_date(self, modified_date: str) -> None:
        """Manually sets the modified_date attribute.

        Note: This method is not intended to be called when building a
        Status.

        Args:
            modified_date (str): The date the Status was last modified. Must
                be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.modified_date = database.return_datetime(modified_date)
