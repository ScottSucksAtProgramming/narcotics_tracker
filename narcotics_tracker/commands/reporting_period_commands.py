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

from narcotics_tracker.commands.interfaces.command import Command
from narcotics_tracker.items.reporting_periods import ReportingPeriod
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import ReportingPeriodData, SQLiteDict

if TYPE_CHECKING:
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

    _criteria: SQLiteDict
    _reporting_period_identifier: int

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

    def set_id(self, reporting_period_identifier: int) -> "Command":
        """Sets the ID of the Medication to be deleted.

        Args:
            medication_id (str, int): The medication code or id number of the
                Medication to be deleted.
        """
        self._reporting_period_identifier = reporting_period_identifier
        return self

    def execute(self) -> str:
        """Executes the delete operation and returns a success message.

        Args:
            reporting_period_identifier (int): The id number of the Reporting
                Period to be deleted.
        """
        self._receiver.remove(
            "reporting_periods", {"id": self._reporting_period_identifier}
        )

        return f"Reporting Period #{self._reporting_period_identifier} deleted."


class ListReportingPeriods(Command):
    """Returns a list of Reporting Periods.

    Methods:
        execute: Executes the command and returns a list of Reporting Periods.
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
            criteria (dict[str, any]): The criteria of Medication to be
                returned as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        if criteria:
            self._criteria = criteria

        if order_by:
            self._order_by = order_by

        return self

    def execute(self) -> list[tuple["ReportingPeriod"]]:
        """Executes the command and returns a list of Reporting Periods.

        Args:
            criteria (dict[str, any]): The criteria of Reporting Periods to be
                returned as a dictionary mapping column names to their values.

            order_by (str): The column name by which the results will be
                sorted.
        """
        cursor = self._receiver.read(
            "reporting_periods", self._criteria, self._order_by
        )
        return cursor.fetchall()


class UpdateReportingPeriod(Command):
    """Updates a Reporting Period with the given data and criteria.

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
            data (dict[str, any]): The new data to update the Medication with
                as a dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which
                medications are to be updated as a dictionary mapping the
                column name to its value.
        """
        self._data = data
        self._criteria = criteria

        return self

    def execute(self) -> str:
        """Executes the update operation and returns a success message.

        Args:
            data (dict[str, any]): The new data to update the ReportingPeriod
                with as a dictionary mapping column names to their values.

            criteria (dict[str, any]): The criteria to select which
                ReportingPeriods are to be updated as a dictionary mapping the
                column name to its value.
        """
        self._receiver.update("reporting_periods", self._data, self._criteria)

        return "Reporting Period data updated."


class LoadReportingPeriod(Command):
    """Returns a ReportingPeriod Object from data.

    Method:
        execute: Executes the command and returns the ReportingPeriod object.
    """

    _data: ReportingPeriodData

    def __init__(self, receiver: Optional["ReportingPeriod"] = None) -> None:
        """Initializes the command. Sets the receiver if passed.

        Args:
            receiver (PersistenceService, optional): Object which communicates
                with the data repository. Defaults to SQLiteManager.
        """
        if receiver:
            self._receiver = receiver

    def set_data(self, data: ReportingPeriodData) -> "Command":
        """Sets the data which will create the Medication

        Args:
            data (tuple[Union[str, int, float]]): A tuple of medication
                attributes retrieved from the database.
        """

        self._data = data

        return self

    def execute(self) -> "ReportingPeriod":
        """Executes the command and returns the ReportingPeriod object."""

        return ReportingPeriod(
            table="reporting_periods",
            id=self._data[0],
            start_date=self._data[1],
            end_date=self._data[2],
            status=self._data[3],
            created_date=self._data[4],
            modified_date=self._data[5],
            modified_by=self._data[6],
        )


def main():
    new_command = AddReportingPeriod()
    test_reporting_period = ReportingPeriod(
        table="reporting_periods",
        id=2300000,
        created_date=1690749986,
        modified_date=1690749986,
        modified_by="SRK",
        start_date=1672549200,
        end_date=1688183999,
        status="OPEN",
    )
    new_command.set_reporting_period(test_reporting_period).execute()
    # remove_command = DeleteReportingPeriod()
    # remove_command.set_id(2300000).execute()


if __name__ == "__main__":
    main()
