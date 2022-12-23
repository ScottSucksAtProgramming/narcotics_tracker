"""Contains type aliases used throughout the Narcotics Tracker."""

from typing import TYPE_CHECKING, Any, TypeVar, Union

from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from narcotics_tracker.commands.table_commands import (
        CreateEventsTable,
        CreateInventoryTable,
        CreateMedicationsTable,
        CreateReportingPeriodsTable,
        CreateStatusesTable,
        CreateUnitsTable,
    )

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment
    from narcotics_tracker.items.events import Event
    from narcotics_tracker.items.interfaces.dataitem_interface import DataItem
    from narcotics_tracker.items.medications import Medication
    from narcotics_tracker.items.reporting_periods import ReportingPeriod
    from narcotics_tracker.items.statuses import Status
    from narcotics_tracker.items.units import Unit


ColumnName: TypeAlias = str
ColumnValue: TypeAlias = Union[str, float]
SQLiteDict: TypeAlias = dict[ColumnName, ColumnValue]

FormattedString: TypeAlias = str
UnixTimestamp: TypeAlias = int
DateType: TypeAlias = Union[FormattedString, UnixTimestamp]


class NTTypes:
    """Contains types used throughout the Narcotics Tracker."""

    medication_data_type = tuple[
        int, str, str, float, str, float, float, str, int, int, str
    ]

    adjustment_data_type = tuple[int, int, str, str, float, int, str, int, int, str]

    reporting_period_data_type = tuple[int, int, int, str, int, int, str]

    table_command_types = Union[
        "CreateEventsTable",
        "CreateInventoryTable",
        "CreateMedicationsTable",
        "CreateReportingPeriodsTable",
        "CreateStatusesTable",
        "CreateUnitsTable",
    ]

    report_data = list[dict[Any, Any]]
