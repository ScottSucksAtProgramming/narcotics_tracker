"""Contains the commands for Reporting Periods.

Please see the package documentation for more information.

Classes:
    AddReportingPeriod: Adds a Reporting Period to the database.

    DeleteReportingPeriod: Deletes a Reporting Period from the database by its 
        ID or code.

    ListReportingPeriods: Returns a list of Reporting Periods.

    UpdateReportingPeriod: Updates a Reporting Period with the given data and 
        criteria. 
"""
from typing import TYPE_CHECKING, Optional

from narcotics_tracker.builders.interfaces.builder import Builder
from narcotics_tracker.builders.reporting_period_builder import ReportingPeriodBuilder
from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.services.service_manager import ServiceManager

if TYPE_CHECKING:
    from narcotics_tracker.items.reporting_periods import ReportingPeriod
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class AddReportingPeriod(Command):
    """Adds a Reporting Period to the database.

    Methods:
        execute: Executes add row operation, returns a success message.
    """

    _receiver = ServiceManager().persistence
    _reporting_period: "ReportingPeriod"

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def set_reporting_period(self, reporting_period: "ReportingPeriod") -> "Command":
        """Sets the reporting_period which will be added to the database.

        Args:
            reporting_period (ReportingPeriods): The reporting_period object
                to be added to the database.
        """
        self._reporting_period = reporting_period
        return self

    def execute(self) -> str:
        """Executes add row operation, returns a success message."""
        reporting_period_info = vars(self._reporting_period)
        table_name = reporting_period_info.pop("table")

        self._receiver.add(table_name, reporting_period_info)

        return f"Reporting Period added to {table_name} table."


class DeleteReportingPeriod(Command):
    """Deletes a Reporting Period from the database by its ID.

    Methods:
        execute: Executes the delete operation and returns a success message.
    """

    _receiver = ServiceManager().persistence

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self, reporting_period_id: int) -> str:
        """Executes the delete operation and returns a success message.

        Args:
            reporting_period_identifier (int): The id number of the Reporting
                Period to be deleted.
        """
        self._receiver.remove("reporting_periods", {"id": reporting_period_id})

        return f"Reporting Period #{reporting_period_id} deleted."


class ListReportingPeriods(Command):
    """Returns a list of Reporting Periods.

    Methods:
        execute: Executes the command and returns a list of Reporting Periods.
    """

    _receiver = ServiceManager().persistence

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self, criteria: dict[str] = {}, order_by: str = None) -> list[tuple]:
        """Executes the command and returns a list of Reporting Periods.

        Args:
            criteria (dict[str, any]): The criteria of Reporting Periods to be
                returned as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        cursor = self._receiver.read("reporting_periods", criteria, order_by)
        return cursor.fetchall()


class UpdateReportingPeriod(Command):
    """Updates a Reporting Period with the given data and criteria.

    Method:
        execute: Executes the update operation and returns a success message.
    """

    _receiver = ServiceManager().persistence

    def __init__(self, receiver: Optional["PersistenceService"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self, data: dict[str, any], criteria: dict[str, any]) -> str:
        """Executes the update operation and returns a success message.

        Args:
            data (dict[str, any]): The new data to update the ReportingPeriod
                with as a dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which
                ReportingPeriods are to be updated as a dictionary mapping the
                column name to its value.
        """
        self._receiver.update("reporting_periods", data, criteria)

        return f"Reporting Period data updated."


class LoadReportingPeriod(Command):
    """Returns a ReportingPeriod Object from data.

    Method:
        execute: Executes the command and returns the ReportingPeriod object.
    """

    _receiver = ReportingPeriodBuilder

    def __init__(self, receiver: "Builder" = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def execute(self, period_data: tuple[any]) -> "ReportingPeriod":
        """Executes the command and returns the ReportingPeriod object."""

        return (
            self._receiver()
            .set_id(period_data[0])
            .set_start_date(period_data[1])
            .set_end_date(period_data[2])
            .set_status(period_data[3])
            .set_created_date(period_data[4])
            .set_modified_date(period_data[5])
            .set_modified_by(period_data[6])
            .build()
        )
