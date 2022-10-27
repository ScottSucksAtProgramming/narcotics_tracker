"""Contains the commands for Reporting Periods.

Please see the package documentation for more information.
"""
from typing import TYPE_CHECKING

from narcotics_tracker.commands.interfaces.command_interface import SQLiteCommand
from narcotics_tracker.services.service_provider import ServiceProvider

if TYPE_CHECKING:
    from narcotics_tracker.items.reporting_periods import ReportingPeriod
    from narcotics_tracker.services.interfaces.persistence_interface import (
        PersistenceService,
    )


class AddReportingPeriod(SQLiteCommand):
    """Adds an ReportingPeriod to the database.

    Methods:
        execute: Executes the command, returns success message."""

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

    def execute(self, reporting_period: "ReportingPeriod") -> str:
        """Executes the command, returns success message."""

        reporting_period_info = vars(reporting_period)
        table_name = reporting_period_info.pop("table")

        self._receiver.add(table_name, reporting_period_info)

        return f"Reporting Period added to {table_name} table."


class DeleteReportingPeriod(SQLiteCommand):
    """Deletes a ReportingPeriod from the database by its ID."""

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

    def execute(self, reporting_period_id: int) -> str:
        """Execute the delete operation and returns a success message."""
        self._receiver.remove("reporting_periods", {"id": reporting_period_id})

        return f"Reporting Period #{reporting_period_id} deleted."


class ListReportingPeriods(SQLiteCommand):
    """Returns a list of Reporting Periods."""

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
        """Executes the command and returns a list of Reporting Periods."""

        cursor = self._receiver.read("reporting_periods", criteria, order_by)
        return cursor.fetchall()


class UpdateReportingPeriod(SQLiteCommand):
    """Update a ReportingPeriod with the given data and criteria."""

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
        self._receiver.update("reporting_periods", data, criteria)

        return f"Reporting Period data updated."
