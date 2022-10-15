"""Contains the concrete builder for the Unit class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    UnitBuilder: Builds and returns Unit objects.
"""
from narcotics_tracker import units
from narcotics_tracker.builders import unit_builder_template
from persistence import database


class UnitBuilder(unit_builder_template.Unit):
    """Builds and returns Unit objects.

    There are two types of methods: 'set' methods can be called to manually
    set attributes for the object; 'assign' methods perform calculations and
    are used as part of the build method to assign other attributes like the
    created date, or unit conversions.

    Look at the Unit Class documentation in the Units Module for
    more information on how to use the Unit objects.

    How To Use:

        1. Initialize the builder by assigning it to a variable:

            `u_builder = unit_builder.UnitBuilder()`

        2. Call the following methods and pass the required values:

            `set_unit_name()`; `set_unit_code()`; `set_container()`; and

            `set_modified_by()`;

        3. Call the `build()` method to return an Unit object.

    Initializer:

        def __init__(self) -> None:

        Initializes unit builder. Sets all attributes to None.

    Instance Methods:

        build: Returns the Unit object. Assigns the Unit's attributes.

        set_unit_code: Sets the unique code of the Unit.

        set_unit_name: Sets the Unit's name.

        set_modified_by: Sets the identifier of the user who modified the
            Unit.

        assign_all_attributes: Sets all attributes of the Unit.

        assign_unit_id: Manually sets the Unit's id. Should not be called by
            the user.

        assign_created_date: Manually sets the created_date attribute.

        assign_modified_date: Manually sets the modified_date attribute.
    """

    def __init__(self) -> None:
        """Initializes unit builder. Sets all attributes to None."""
        self.unit_id = None
        self.unit_code = None
        self.unit_name = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def build(self) -> "units.Unit":
        """Returns the Unit object. Assigns the Unit's attributes.

        This is the last method to be called as part of the building process.
        It will return the Unit object with all of its attributes set.
        The concentration is calculated using the calculate_concentration
        method.

        Returns:
            unit.Unit: The Unit object.
        """

        return units.Unit(self)

    def set_unit_code(self, unit_code: str) -> None:
        """Sets the unique code of the Unit.

        The Units unique code is used to identify the Unit within
        the database and the Narcotics Tracker. This code is set by the user
        as an easy reference to the Unit. Units without a code are
        not retrievable from the database.

        Args:
            code (str): Identifier for this specific Unit.
        """
        self.unit_code = unit_code

    def set_unit_name(self, unit_name: str) -> None:
        """Sets the Unit's name.

        Args:
            name (str): The Unit's name.
        """
        self.unit_name = unit_name

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who modified the Unit.

        This method will set the Unit's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the
                Unit.
        """
        self.modified_by = modified_by

    def assign_all_attributes(self, attributes: dict) -> None:
        """Sets all attributes of the Unit.

        Args:
            attributes (dict): The attributes of the Unit. Dictionary keys are
                formatted as the Unit attribute names.
        """
        self.assign_unit_id(attributes["unit_id"])
        self.set_unit_code(attributes["unit_code"])
        self.set_unit_name(attributes["unit_name"])
        self.assign_created_date(attributes["created_date"])
        self.assign_modified_date(attributes["modified_date"])
        self.set_modified_by(attributes["modified_by"])

    def assign_unit_id(self, unit_id: int) -> None:
        """Manually sets the Unit's id. Should not be called by the user.

        This method will set the Unit's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the Unit is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            unit_id (int): The Unit's numeric id.
        """
        self.unit_id = unit_id

    def assign_created_date(self, created_date: str) -> None:
        """Manually sets the created_date attribute.

        This method will set the Unit's created_date.

        Args:
            created_date (str): The Unit's created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.created_date = database.return_datetime(created_date)

    def assign_modified_date(self, modified_date: str) -> None:
        """Manually sets the modified_date attribute.

        This method will set the Unit's modified_date.

        Args:
            modified_date (str): The Unit's created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.modified_date = database.return_datetime(modified_date)
