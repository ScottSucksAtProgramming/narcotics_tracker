"""Contains the concrete builder for the EventType class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    EventTypeBuilder: Builds and returns EventType objects.
"""
from narcotics_tracker import database, event_types
from narcotics_tracker.builders import event_type_builder_template


class EventTypeBuilder(event_type_builder_template.EventType):
    """Builds and returns EventType objects.

    Initializer:

    Instance Methods:

    Exceptions:

    """

    def __init__(self) -> None:
        """Initializes the event_type builder. Sets all attributes to None."""
        self.event_id = None
        self.event_code = None
        self.event_name = None
        self.description = None
        self.operator = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def set_event_id(self, event_id: int) -> None:
        """Sets the event's id number. Should not be called by the user.

        This method will set the event's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the event is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            event_id (int): The event's numeric id.
        """
        self.event_id = event_id

    def set_event_code(self, event_code: str) -> None:
        """Sets the event's code.

        This method will set the event's code.

        Args:
            event_code (str): The event's unique id.
        """
        self.event_code = event_code

    def set_event_name(self, event_name: str) -> None:
        """Sets the event's name.

        This method will set the event's name.

        Args:
            event_name (str): The event's name
        """
        self.event_name = event_name

    def set_description(self, description: str) -> None:
        """Sets the event's description.

        This method will set the event's description.

        Args:
            description (str): Description of the event.
        """
        self.description = description

    def set_operator(self, operator: int) -> None:
        """Sets the event's operator.

        This method will set the event's operator.

        Args:
            operator (int): The event's operator
        """
        self.operator = operator

    def set_created_date(self, created_date: str) -> None:
        """Sets the event's created_date.

        This method will set the event's created_date.

        Args:
            created_date (str): The event's created date in the format
                YYYY-MM-DD HH:MM:SS.
        """
        self.created_date = database.return_datetime(created_date)

    def set_modified_date(self, modified_date: str) -> None:
        """Sets the event's modified_date.

        This method will set the event's modified_date.

        Args:
            modified_date (str): The event's created date in the format
                YYYY-MM-DD HH:MM:SS.
        """
        self.modified_date = database.return_datetime(modified_date)

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the event's modified_by attribute.

        This method will set the event's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the row.
        """
        self.modified_by = modified_by

    def build(self) -> "event_types.EventType":
        """Returns the EventType object. Assigns the EventType's properties.

        This is the last method to be called as part of the building process.
        It will return the EventType object with all of its properties set.


        Returns:
            event_types.EventType: The event_types EventType object.
        """

        return event_types.EventType(self)
