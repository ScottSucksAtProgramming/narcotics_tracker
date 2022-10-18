"""Contains the concrete builder for the Event class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    EventBuilder: Builds and returns Event objects.
"""
from narcotics_tracker import database
from narcotics_tracker.builders import event_builder_template
from narcotics_tracker.items import events


class EventBuilder(event_builder_template.Event):
    """Builds and returns Event objects.

    There are two types of methods: 'set' methods can be called to manually
    set attributes for the object; 'assign' methods perform calculations and
    are used as part of the build method to assign other attributes like the
    created date, or unit conversions.

    Look at the Event Class documentation in the Events Module for
    more information on how to use the Event objects.

    How To Use:

        1. Initialize the builder by assigning it to a variable:

            `e_builder = event_builder.EventBuilder()`

        3. Call the following methods and pass the required values:

            `set_event_code()`; `set_event_name()`; `set_event_description()`;

            `set_operator()`; and `set_modified_by()`;

        4. Call the `build()` method to return an Event object.

    Initializer:

        def __init__(self) -> None:
        '''Initializes the event_type builder. Sets all attributes to None.'''

    Instance Methods:

        build: Returns the Event object. Assigns the Event's attributes.

        set_event_code: Sets the Event's code.

        set_event_name: Sets the Event's name.

        set_description: Sets the Event's description.

        set_operator: Sets the Event's operator.

        set_modified_by: ets the identifier of the user who modified the
            Event.

        assign_all_attributes: Assigns all attributes of the Event.

        assign_event_id: Manually sets the Container's id. Should not be
            called by the user.

        assign_created_date: Manually sets the created_date attribute.

        assign_modified_date: Manually sets the modified_date attribute.
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

    def build(self) -> "events.Event":
        """Returns the Event object. Assigns the Event's attributes.

        This is the last method to be called as part of the building process.
        It will return the Event object with all of its attributes set.


        Returns:
            event_types.Event: The event_types Event object.
        """

        return events.Event(self)

    def set_event_code(self, event_code: str) -> None:
        """Sets the Event's code.

        This method will set the Event's code which is used to the Event in
        the database.

        Args:
            event_code (str): The Event's unique id.
        """
        self.event_code = event_code

    def set_event_name(self, event_name: str) -> None:
        """Sets the Event's name.

        This method will set the Event's name.

        Args:
            event_name (str): The Event's name
        """
        self.event_name = event_name

    def set_description(self, description: str) -> None:
        """Sets the Event's description.

        This method will set the Event's description.

        Args:
            description (str): Description of the Event.
        """
        self.description = description

    def set_operator(self, operator: int) -> None:
        """Sets the Event's operator.

        This method will set the Event's operator used to determine if the
        Event will Add or Remove medication from the inventory.

        Args:
            operator (int): The Event's operator (-1 or +1)
        """
        self.operator = operator

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who modified the Event.

        This method will set the Event's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the Event.
        """
        self.modified_by = modified_by

    def assign_all_attributes(self, attributes: dict) -> None:
        """Assigns all attributes of the Event.

        This method is intended to be called when loading an Event from the
            database.

        Args:
            attributes (dict): The attributes of the Event. Dictionary keys
            are formatted as the Event attribute names.
        """
        self.assign_event_id(attributes["event_id"])
        self.set_event_code(attributes["event_code"])
        self.set_event_name(attributes["event_name"])
        self.set_description(attributes["description"])
        self.set_operator(attributes["operator"])
        self.assign_created_date(attributes["created_date"])
        self.assign_modified_date(attributes["modified_date"])
        self.set_modified_by(attributes["modified_by"])

    def assign_event_id(self, event_id: int) -> None:
        """Manually sets the Event's id. Should not be called by the user.

        This method will set the Event's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the Event is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            event_id (int): The Event's numeric id.
        """
        self.event_id = event_id

    def assign_created_date(self, created_date: str) -> None:
        """Manually sets the created_date attribute.

        Note: This method is not intended to be called when building an Event.

        Args:
            created_date (str): The date the Event object was created. Must be
                in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.created_date = database.return_datetime(created_date)

    def assign_modified_date(self, modified_date: str) -> None:
        """Manually sets the modified_date attribute.

        Note: This method is not intended to be called when building an Event.

        Args:
            modified_date (str): The date the Event was last modified. Must be
                 in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.modified_date = database.return_datetime(modified_date)
