"""Contains the commands for Events.

Please see the package documentation for more information.
"""
from typing import TYPE_CHECKING, Union

from narcotics_tracker.commands.interfaces.command_interface import Command
from narcotics_tracker.services.service_provider import ServiceProvider

if TYPE_CHECKING:
    from narcotics_tracker.items.events import Event
    from narcotics_tracker.services.interfaces.persistence_interface import (
        PersistenceService,
    )


class ReturnEventModifier(Command):
    """Return's an event's modifier.

    Methods:
        execute: Executes the command and returns the modifier.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, event_code: str) -> int:
        """Executes the command and returns the modifier."""
        criteria = {"event_code": event_code}
        cursor = self._receiver.read("events", criteria)
        return cursor.fetchall()[0][4]


class AddEvent(Command):
    """Adds an Event to the database.

    Methods:
        execute: Executes the command, returns success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, event: "Event") -> str:
        """Executes the command, returns success message."""
        event_info = vars(event)
        table_name = event_info.pop("table")

        self._receiver.add(table_name, event_info)

        return f"Event added to {table_name} table."


class DeleteEvent(Command):
    """Deletes an Event from the database by its ID or code."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, event_identifier: Union[int, str]) -> str:
        """Execute the delete operation and returns a success message."""
        if type(event_identifier) is int:
            criteria = {"id": event_identifier}

        if type(event_identifier) is str:
            criteria = {"event_code": event_identifier}

        self._receiver.remove("events", criteria)

        return f"Event {event_identifier} deleted."


class ListEvents(Command):
    """Returns a list of Events."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, criteria: dict[str] = {}, order_by: str = None) -> list[tuple]:
        """Executes the command and returns a list of Events."""
        cursor = self._receiver.read("events", criteria, order_by)
        return cursor.fetchall()


class UpdateEvent(Command):
    """Update an Event with the given data and criteria."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, data: dict[str, any], criteria: dict[str, any]) -> str:
        """Executes the update operation and returns a success message."""
        self._receiver.update("events", data, criteria)

        return f"Event data updated."
