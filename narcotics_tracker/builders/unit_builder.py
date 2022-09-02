"""Contains the concrete builder for the Unit class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    UnitBuilder: Builds and returns Unit objects.
"""
from narcotics_tracker import database, units
from narcotics_tracker.builders import unit_builder_template


class UnitBuilder(unit_builder_template.Unit):
    """Builds and returns Unit objects.

    Initializer:

    Instance Methods:

    Exceptions:

    """

    def __init__(self) -> None:
        """Initializes unit builder. Sets all attributes to None."""
        self.unit_id = None
        self.unit_code = None
        self.unit_name = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def set_unit_id(self, unit_id: int) -> None:
        """Sets the unit's id number. Should not be called by the user.

        This method will set the unit's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the Unit is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            unit_id (int): The Unit's numeric id.
        """
        self.unit_id = unit_id

    def set_unit_code(self, unit_code: str) -> None:
        """Sets the Unit's unit_code.

        The unit code is the unique identifier for the unit. It is used to
        interact with the unit in the database. The unit code should be the
        lower case abbreviation of the unit.

        Args:
            unit_code (str): The unique identifier for the unit. It is
            recommended that the unit's code should be the common lowercase
            abbreviation for the dosage unit.
        """
        self.unit_code = unit_code

    def set_unit_name(self, unit_name: str) -> None:
        """Sets the Unit's name.

        Args:
            unit_name (str): The proper name for the dosage unit.
        """
        self.unit_name = unit_name

    def set_created_date(self, created_date: str) -> None:
        """Sets the Unit's created_date.

        This method will set the Unit's created_date.

        Args:
            created_date (str): The Unit's created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.created_date = database.return_datetime(created_date)

    def set_modified_date(self, modified_date: str) -> None:
        """Sets the Unit's modified_date.

        This method will set the Unit's modified_date.

        Args:
            modified_date (str): The Unit's created date in the
                format YYYY-MM-DD HH:MM:SS.
        """
        self.modified_date = database.return_datetime(modified_date)

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the Unit's modified_by attribute.

        This method will set the Unit's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the
                unit.
        """
        self.modified_by = modified_by

    def set_all_properties(self, properties: dict) -> None:
        """Sets all properties of the Unit.

        Args:
            properties (dict): The properties of the Unit.
                Dictionary keys are formatted as the Unit attribute
                names.
        """
        self.set_unit_id(properties["unit_id"])
        self.set_unit_code(properties["unit_code"])
        self.set_unit_name(properties["unit_name"])
        self.set_created_date(properties["created_date"])
        self.set_modified_date(properties["modified_date"])
        self.set_modified_by(properties["modified_by"])

    def build(self) -> "units.Unit":
        """Assigns attributes and returns a ReportingType Object.

        This is the last method to be called as part of the building process.
        It will return the UnitType object with all of its
        properties set.


        Returns:
            units.UnitType: The Unit Object.
        """

        return units.Unit(self)
