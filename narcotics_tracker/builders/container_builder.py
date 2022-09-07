"""Contains the concrete builder for the Container class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    ContainerBuilder: Builds and returns Container objects.
"""
from narcotics_tracker import database, containers
from narcotics_tracker.builders import container_builder_template


class ContainerBuilder(container_builder_template.Container):
    """Builds and returns Container objects.

    Initializer:

    Instance Methods:

    Exceptions:

    """

    def __init__(self) -> None:
        """Initializes container builder. Sets all attributes to None."""
        self.container_id = None
        self.container_code = None
        self.container_name = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def build(self) -> "containers.Container":
        """Assigns attributes and returns a Container Object.

        This is the last method to be called as part of the building process.
        It will return the containerType object with all of its
        properties set.


        Returns:
            containers.containerType: The Container Object.
        """

        return containers.Container(self)

    def set_all_properties(self, properties: dict) -> None:
        """Sets all properties of the Container.

        Args:
            properties (dict): The properties of the Container.
                Dictionary keys are formatted as the Container attribute
                names.
        """
        self.set_container_id(properties["container_id"])
        self.set_container_code(properties["container_code"])
        self.set_container_name(properties["container_name"])
        self.set_created_date(properties["created_date"])
        self.set_modified_date(properties["modified_date"])
        self.set_modified_by(properties["modified_by"])

    def set_container_id(self, container_id: int) -> None:
        """Sets the container's id number. Should not be called by the user.

        This method will set the container's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the Container is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            container_id (int): The Container's numeric id.
        """
        self.container_id = container_id

    def set_container_code(self, container_code: str) -> None:
        """Sets the Container's container_code.

        The container code is the unique identifier for the container. It is used to
        interact with the container in the database. The container code should be the
        lower case abbreviation of the container.

        Args:
            container_code (str): The unique identifier for the container. It is
            recommended that the container's code should be the common lowercase
            abbreviation for the dosage container.
        """
        self.container_code = container_code

    def set_container_name(self, container_name: str) -> None:
        """Sets the Container's name.

        Args:
            container_name (str): The proper name for the dosage container.
        """
        self.container_name = container_name

    def set_created_date(self, created_date: str) -> None:
        """Sets the Container's created_date.

        This method will set the Container's created_date.

        Args:
            created_date (str): The Container's created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.created_date = database.return_datetime(created_date)

    def set_modified_date(self, modified_date: str) -> None:
        """Sets the Container's modified_date.

        This method will set the Container's modified_date.

        Args:
            modified_date (str): The Container's created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.modified_date = database.return_datetime(modified_date)

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the Container's modified_by attribute.

        This method will set the Container's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the
                container.
        """
        self.modified_by = modified_by
