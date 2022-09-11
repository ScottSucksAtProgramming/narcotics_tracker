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
    """The ContainerBuilder class is used to construct Container objects.
    There are two types of methods: 'set' methods can be called to manually
    set attributes for the object; 'assign' methods perform calculations and
    are used as part of the build method to assign other attributes like the
    created date, or unit conversions.

    Look at the Container Class documentation in the Containers Module for
    more information on how to use the Container objects.

    How To Use:

        1. Create a database connection using the database.Database() context
        manager.

        2. Initialize the builder by assigning it to a variable and passing a
        database connection:
            ```cont_builder = container_builder.ContainerBuilder(database_connection)```

        3. Call the following methods and pass the required values:
        ```set_container_code()```; ```set_container_name()```; and
        ```set_modified_by()```;

        4. Call the `build()` method to return a Container object.

    Initializer:

        def __init__(self) -> None:
        '''Initializes container builder. Sets all attributes to None.'''
        self.container_id = None
        self.container_code = None
        self.container_name = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    Instance Methods:

        build(): Returns the Container object. Assigns the Container's
            attributes.

        set_container_code(): Sets the unique code for the Container.

        set_container_name(): Sets the Container's name.

        set_modified_by(): Sets the identifier of the user who modified the
            Container.

        assign_all_attributes(): Assigns all attributes of the Container.

        assign_container_id(): Sets the container's id number. Should not be
            called by the user.

        assign_created_date(); Manually sets the created_date attribute.

        assign_modified_date(): Manually sets the modified_date attribute.
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
        """Returns the Container object. Assigns the Container's attributes.

        This is the last method to be called as part of the building process.
        It will return the Container object with all of its attributes set.

        Returns:
            containers.containerType: The Container Object.
        """

        return containers.Container(self)

    def set_container_code(self, container_code: str) -> None:
        """Sets the unique code for the Container.

        The container code is the unique identifier used to find the Container
        in the database.

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

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who modified the Container.

        This method will set the Container's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the
                container.
        """
        self.modified_by = modified_by

    def assign_all_attributes(self, attributes: dict) -> None:
        """Assigns all attributes of the Container.

        This method is intended to be called when loading a Container from
        the database.

        Args:
            attributes (dict): The attributes of the Container.
                Dictionary keys are formatted as the Container attribute
                names.
        """
        self.assign_container_id(attributes["container_id"])
        self.set_container_code(attributes["container_code"])
        self.set_container_name(attributes["container_name"])
        self.assign_created_date(attributes["created_date"])
        self.assign_modified_date(attributes["modified_date"])
        self.set_modified_by(attributes["modified_by"])

    def assign_container_id(self, container_id: int) -> None:
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

    def assign_created_date(self, created_date: str) -> None:
        """Manually sets the created_date attribute.

        Note: This method is not intended to be called when building a
        Container.

        Args:
            created_date (str): The date the container object was created.
                Must be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.created_date = database.return_datetime(created_date)

    def assign_modified_date(self, modified_date: str) -> None:
        """Manually sets the modified_date attribute.

        Note: This method is not intended to be called when building a
        Container.

        Args:
            modified_date (str): The date the Container was last modified.
                Must be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.modified_date = database.return_datetime(modified_date)
