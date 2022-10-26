"""Contains the commands for Reporting Periods.

Please see the package documentation for more information.
"""

from narcotics_tracker.commands.interfaces.command_interface import SQLiteCommand
from narcotics_tracker.items.reporting_periods import ReportingPeriod
from narcotics_tracker.services.interfaces.persistence_interface import (
    PersistenceService,
)
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class AddReportingPeriod(SQLiteCommand):
    """Adds an ReportingPeriod to the database.

    Methods:
        execute: Executes the command, returns success message."""

    def __init__(
        self, receiver: PersistenceService, reporting_period: ReportingPeriod
    ) -> None:
        """Initializes the command. Sets the receiver and ReportingPeriod.

        Args:
            receiver (PersistenceManager): Persistence manager for the data
                repository.

            ReportingPeriod: The ReportingPeriod to be added to the database.
        """
        self._receiver = receiver
        self._reporting_period = reporting_period

    def execute(self) -> str:
        """Executes the command, returns success message."""

        self._extract_reporting_period_info()
        table_name = self._pop_table_name()

        self._receiver.add(table_name, self.reporting_period_info)

        return f"Reporting Period added to {table_name} table."

    def _extract_reporting_period_info(self) -> None:
        """Extracts ReportingPeriod attributes and stored as a dictionary."""
        self.reporting_period_info = vars(self._reporting_period)

    def _pop_table_name(self) -> str:
        """Removes and returns the table name from ReportingPeriod's attributes.

        Returns:
            string: Name of the table.
        """
        return self.reporting_period_info.pop("table")


class DeleteReportingPeriod(SQLiteCommand):
    """Deletes a ReportingPeriod from the database by its ID."""

    def __init__(self, receiver: SQLiteManager, reporting_period_id: int) -> None:
        """Sets the SQLiteManager and reporting_period_id."""
        self._target = receiver
        self._dataitem_id = reporting_period_id

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        self._target.remove("reporting_periods", {"id": self._dataitem_id})

        return f"Reporting Period #{self._dataitem_id} deleted."


class ListReportingPeriods(SQLiteCommand):
    """Returns a list of Reporting Periods."""

    def __init__(
        self,
        receiver: SQLiteManager,
        criteria: dict[str] = {},
        order_by: str = None,
    ):
        """Sets the SQLiteManager, criteria and order_by column.

        Args:
            receiver (SQLiteManager): SQLiteManager connected to the database.

            criteria (dict[str, any], optional): Criteria of Reporting Periods to be
                returned as a dictionary mapping column names to values.

            order_by (str, optional): Column name by which to sort the results.
        """
        self._target = receiver
        self._criteria = criteria
        self._order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Reporting Periods."""

        cursor = self._target.read("reporting_periods", self._criteria, self._order_by)
        return cursor.fetchall()


class UpdateReportingPeriod(SQLiteCommand):
    """Update a ReportingPeriod with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self._target = receiver
        self._data = data
        self._criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self._target.update("reporting_periods", self._data, self._criteria)

        return f"Reporting Period data updated."
