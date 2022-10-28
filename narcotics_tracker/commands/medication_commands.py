"""Contains the commands for Medications.

Please see the package documentation for more information.
"""
from typing import TYPE_CHECKING, Union

from narcotics_tracker.commands.interfaces.command_interface import Command
from narcotics_tracker.services import sqlite_manager
from narcotics_tracker.services.service_provider import ServiceProvider

if TYPE_CHECKING:
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.services.interfaces.persistence_interface import (
        PersistenceService,
    )


class ReturnPreferredUnit(Command):
    """Returns the preferred unit for the specified medication.

    Methods:
        execute: Executes the command, returns results."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which
                communicates with the data repository. Defaults to
                SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, medication_code: str) -> str:
        """Executes the command, returns results."""
        criteria = {"medication_code": medication_code}

        cursor = self._receiver.read("medications", criteria)
        return cursor.fetchall()[0][4]


class AddMedication(Command):
    """Adds an Medication to the database.

    Methods:
        execute: Executes the command, returns success message.
    """

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which
                communicates with the data repository. Defaults to
                SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, medication: "Medication") -> str:
        """Executes the command, returns success message."""

        medication_info = vars(medication)
        table_name = medication_info.pop("table")

        self._receiver.add(table_name, medication_info)

        return f"Medication added to {table_name} table."


class DeleteMedication(Command):
    """Deletes a Medication from the database by its ID or code."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which
                communicates with the data repository. Defaults to
                SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, medication_identifier: Union[str, int]) -> str:
        """Execute the delete operation and returns a success message."""
        if type(medication_identifier) is int:
            criteria = {"id": medication_identifier}

        if type(medication_identifier) is str:
            criteria = {"medication_code": medication_identifier}

        self._receiver.remove("medications", criteria)

        return f"Medication {medication_identifier} deleted."


class ListMedications(Command):
    """Returns a list of Medications."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which
                communicates with the data repository. Defaults to
                SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, criteria: dict[str] = {}, order_by: str = None) -> list[tuple]:
        """Executes the command and returns a list of Medications."""

        cursor = self._receiver.read("medications", criteria, order_by)
        return cursor.fetchall()


class UpdateMedication(Command):
    """Update a Medication with the given data and criteria."""

    def __init__(self, receiver: "PersistenceService" = None) -> None:
        """Initializes the command.

        Args:
            receiver (PersistenceService, optional): Object which
                communicates with the data repository. Defaults to
                SQLiteManager.
        """
        if receiver:
            self._receiver = receiver
        else:
            self._receiver = ServiceProvider().start_services()[0]

    def execute(self, data: dict[str, any], criteria: dict[str, any]) -> str:
        """Executes the update operation and returns a success message."""
        self._receiver.update("medications", data, criteria)

        return f"Medication data updated."
