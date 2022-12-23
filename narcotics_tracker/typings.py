"""Contains type aliases used throughout the Narcotics Tracker."""

from typing import TYPE_CHECKING, Union

from typing_extensions import TypeAlias  # Will be typing.TypeAlias in Python 3.11

if TYPE_CHECKING:
    from narcotics_tracker.commands.table_commands import (
        CreateEventsTable,
        CreateInventoryTable,
        CreateMedicationsTable,
        CreateReportingPeriodsTable,
        CreateStatusesTable,
        CreateUnitsTable,
    )

ColumnName: TypeAlias = str
ColumnValue: TypeAlias = Union[str, float]
SQLiteDict: TypeAlias = dict[ColumnName, ColumnValue]

FormattedStringDate: TypeAlias = str
UnixTimestamp: TypeAlias = int
DateType: TypeAlias = Union[FormattedStringDate, UnixTimestamp]

TableName: TypeAlias = str
ID: TypeAlias = int
CreatedDate: TypeAlias = UnixTimestamp
ModifiedDate: TypeAlias = UnixTimestamp
UserID: TypeAlias = str
ModifiedBy: TypeAlias = UserID
AdjustmentDate: TypeAlias = UnixTimestamp
EventCode: TypeAlias = str
MedicationCode: TypeAlias = str
Amount: TypeAlias = float
ReportingPeriodID: TypeAlias = int
ReferenceID: TypeAlias = str

AdjustmentData: TypeAlias = tuple[
    ID,
    AdjustmentDate,
    EventCode,
    MedicationCode,
    Amount,
    ReportingPeriodID,
    ReferenceID,
    CreatedDate,
    ModifiedDate,
    ModifiedBy,
]


class NTTypes:
    """Contains types used throughout the Narcotics Tracker."""

    medication_data_type = tuple[
        int, str, str, float, str, float, float, str, int, int, str
    ]

    reporting_period_data_type = tuple[int, int, int, str, int, int, str]

    table_command_types = Union[
        "CreateEventsTable",
        "CreateInventoryTable",
        "CreateMedicationsTable",
        "CreateReportingPeriodsTable",
        "CreateStatusesTable",
        "CreateUnitsTable",
    ]

    report_data = list[dict[object, object]]
