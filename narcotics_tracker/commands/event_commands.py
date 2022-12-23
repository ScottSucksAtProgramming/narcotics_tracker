"""Contains the commands for Events.

Please see the package documentation for more information.

Classes:

    AddEvent: Adds an Event to the database.

    DeleteEvent: Deletes a Event from the database by its ID or code.

    ListEvents: Returns a list of Events.

    UpdateEvent: Updates a Event with the given data and criteria.

    ReturnEventModifier: Returns an Event's modifier.
"""
from typing import TYPE_CHECKING, Optional, Union

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import SQLiteDict

if TYPE_CHECKING:
    from narcotics_tracker.items.events import Event
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddEvent(Command):
    """Adds an Event to the database.

    Methods:
        execute: Executes add row operation, returns a success message.
    """

    _event: "Event"

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_event(self, event: "Event") -> "Command":
        """Sets the event which will be added to the database.

        Args:
            event (Event): The Event object to be added to the
                database.
        """
        self._event: "Event" = event
        return self

    def execute(self) -> str:
        """Executes add row operation, returns a success message."""
        event_info = vars(self._event)
        table_name = event_info.pop("table")

        self._receiver.add(table_name, event_info)

        return f"Event added to {table_name} table."


class DeleteEvent(Command):
    """Deletes a Event from the database by its ID or code.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    _criteria: SQLiteDict
    _event_identifier: Union[int, str]

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_id(self, event_identifier: Union[int, str]) -> "Command":
        """Sets the ID of the Event to be deleted.

        Args:
            event_id (str, int): The event code or id number of the Event to
                be deleted.
        """
        self._event_identifier = event_identifier
        return self

    def execute(self) -> str:
        """Executes the delete operation and returns a success message."""
        if isinstance(self._event_identifier, int):
            self._criteria = {"id": self._event_identifier}

        if isinstance(self._event_identifier, str):
            self._criteria = {"event_code": self._event_identifier}

        self._receiver.remove("events", self._criteria)

        return f"Event {self._event_identifier} deleted."


class ListEvents(Command):
    """Returns a list of Events.

    Methods:
        execute: Executes the command and returns a list of Events.
    """

    _criteria: SQLiteDict = {}
    _order_by: Optional[str] = None

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_parameters(
        self,
        criteria: Optional[SQLiteDict] = None,
        order_by: Optional[str] = None,
    ) -> "Command":
        """Sets the criteria and order_by column.

        Args:
            criteria (dict[str, any]): The criteria of Event to be returned as
                a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        if criteria:
            self._criteria = criteria

        if order_by:
            self._order_by = order_by

        return self

    def execute(self) -> list[tuple["Event"]]:
        """Executes the command and returns a list of Events."""
        cursor = self._receiver.read("events", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateEvent(Command):
    """Updates a Event with the given data and criteria.

    Method:
        execute: Executes the update operation and returns a success message.
    """

    _data: SQLiteDict
    _criteria: SQLiteDict

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_data(self, data: SQLiteDict, criteria: SQLiteDict) -> "Command":
        """Sets the data and criteria for the update.

        Args:
            data (dict[str, any]): The new data to update the Event with as a
                dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which events are
                to be updated as a dictionary mapping the column name to its
                value.
        """
        self._data = data
        self._criteria = criteria

        return self

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._receiver.update("events", self._data, self._criteria)

        return "Event data updated."


class ReturnEventModifier(Command):
    """Returns an Event's modifier.

    Methods:
        execute: Executes the command and returns the modifier.
    """

    _criteria: SQLiteDict
    _event_identifier: Union[int, str]

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def set_id(self, event_identifier: Union[int, str]) -> "Command":
        """Sets the ID of the Event to be deleted.

        Args:
            event_id (str, int): The event code or id number of the Event to
                be deleted.
        """
        self._event_identifier = event_identifier
        return self

    def execute(self) -> int:
        """Executes the command and returns the modifier."""
        if isinstance(self._event_identifier, int):
            self._criteria = {"id": self._event_identifier}

        if isinstance(self._event_identifier, str):
            self._criteria = {"event_code": self._event_identifier}

        cursor = self._receiver.read("events", self._criteria)
        return cursor.fetchall()[0][4]
