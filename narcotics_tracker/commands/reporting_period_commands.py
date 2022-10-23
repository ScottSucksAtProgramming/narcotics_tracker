"""Contains the commands for Reporting Periods.

Please see the package documentation for more information.
"""

from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.sqlite_commands_interface import SQLiteCommand


class DeleteReportingPeriod(SQLiteCommand):
    """Deletes a ReportingPeriod from the database by its ID."""

    def __init__(self, receiver: SQLiteManager, reporting_period_id: int) -> None:
        """Sets the SQLiteManager and reporting_period_id."""
        self.receiver = receiver
        self.target_id = reporting_period_id

    def execute(self) -> str:
        """Execute the delete operation and returns a success message."""
        self.receiver.delete("reporting_periods", {"id": self.target_id})

        return f"Reporting Period #{self.target_id} deleted."


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
        self.receiver = receiver
        self.criteria = criteria
        self.order_by = order_by

    def execute(self) -> list[tuple]:
        """Executes the command and returns a list of Reporting Periods."""

        cursor = self.receiver.select("reporting_periods", self.criteria, self.order_by)
        return cursor.fetchall()


class UpdateReportingPeriod(SQLiteCommand):
    """Update a ReportingPeriod with the given data and criteria."""

    def __init__(
        self, receiver: SQLiteManager, data: dict[str, any], criteria: dict[str, any]
    ) -> None:
        """Sets the SQLiteManager, updates data, and selection criteria."""
        self.receiver = receiver
        self.data = data
        self.criteria = criteria

    def execute(self) -> str:
        """Executes the update operation and returns a success message."""
        self.receiver.update("reporting_periods", self.data, self.criteria)

        return f"Reporting Period data updated."
