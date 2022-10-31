"""Contains the commands for Events.

Please see the package documentation for more information.

Classes:

    AddEvent: Adds an Event to the database.

    DeleteEvent: Deletes a Event from the database by its ID or code.

    ListEvents: Returns a list of Events.

    UpdateEvent: Updates a Event with the given data and criteria.

    ReturnEventModifier: Returns an Event's modifier.
"""
from typing import TYPE_CHECKING, Union

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.events import Event
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddEvent(Command):
    """Adds an Event to the database.

    Methods:
        execute: Executes add row operation, returns a success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(self, event: "Event") -> str:
        """Executes add row operation, returns a success message.

        Args:
            event (Event): The Event object to be added to the
                database.
        """
        event_info = vars(event)
        table_name = event_info.pop("table")

        self._receiver.add(table_name, event_info)

        return f"Event added to {table_name} table."


class DeleteEvent(Command):
    """Deletes a Event from the database by its ID or code.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(self, event_identifier: Union[int, str]) -> str:
        """Executes the delete operation and returns a success message.

        Args:
            event_identifier (str, int): The event code or id number
                of the Event to be deleted.
        """
        if type(event_identifier) is int:
            criteria = {"id": event_identifier}

        if type(event_identifier) is str:
            criteria = {"event_code": event_identifier}

        self._receiver.remove("events", criteria)

        return f"Event {event_identifier} deleted."


class ListEvents(Command):
    """Returns a list of Events.

    Methods:
        execute: Executes the command and returns a list of Events.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(
        self, criteria: dict[str, any] = {}, order_by: str = None
    ) -> list[tuple]:
        """Executes the command and returns a list of Events.

        Args:
            criteria (dict[str, any]): The criteria of Events to be
                returned as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        cursor = self._receiver.read("events", criteria, order_by)
        return cursor.fetchall()


class UpdateEvent(Command):
    """Updates a Event with the given data and criteria.

    Method:
        execute: Executes the update operation and returns a success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(self, data: dict[str, any], criteria: dict[str, any]) -> str:
        """Executes the update operation and returns a success message.

        Args:
            data (dict[str, any]): The new data to update the Event
            with as a dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which
                Events are to be updated as a dictionary mapping the
                column name to its value.
        """
        self._receiver.update("events", data, criteria)

        return f"Event data updated."


class ReturnEventModifier(Command):
    """Returns an Event's modifier.

    Methods:
        execute: Executes the command and returns the modifier.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceManager().persistence

    def execute(self, event_code: str) -> int:
        """Executes the command and returns the modifier."""
        criteria = {"event_code": event_code}
        cursor = self._receiver.read("events", criteria)
        return cursor.fetchall()[0][4]
