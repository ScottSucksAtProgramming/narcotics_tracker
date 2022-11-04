"""Organizes and exports commands for the Narcotics Tracker.

The Command Pattern was implemented to provider greater flexibility when using 
the Narcotics Tracker. The modules within this package contain the various 
commands available. They have been imported into this module for easier 
importing throughout the project.

Interfaces:

    Command: Defines the protocol for commands which interact with the SQLite3 
        database.

Modules:

    Adjustment Commands: Contains the commands for Adjustments.

    Event Commands: Contains the commands for Events.

    Medication Commands: Contains the commands for Medications.

    Reporting Period Commands: Contains the commands for Reporting Periods.

    Status Commands: Contains the commands for Statuses.

    Table Commands: Contains commands which created and modify tables in the 
        SQLite3 database.

    Unit Commands: Contains the commands for Units.

How To Use:

    Commands allow for their receivers to be set in their initializer. If no 
    receiver is passes the default service is used. Each command relies on its 
    `execute` method trigger the command. The execute method accepts any 
    needed parameters by the receiver.

    ```python
    new_adjustment = Adjustment(...)

    commands.AddAdjustment().execute(new_adjustment)
    ```

    ```python
    modifier = command.ReturnEventModifier("LOSS")
    ```
"""

from narcotics_tracker.commands.adjustment_commands import (
    AddAdjustment,
    DeleteAdjustment,
    ListAdjustments,
    UpdateAdjustment,
)
from narcotics_tracker.commands.event_commands import (
    AddEvent,
    DeleteEvent,
    ListEvents,
    ReturnEventModifier,
    UpdateEvent,
)
from narcotics_tracker.commands.medication_commands import (
    AddMedication,
    DeleteMedication,
    ListMedications,
    ReturnPreferredUnit,
    UpdateMedication,
)
from narcotics_tracker.commands.reporting_period_commands import (
    AddReportingPeriod,
    DeleteReportingPeriod,
    ListReportingPeriods,
    LoadReportingPeriod,
    UpdateReportingPeriod,
)
from narcotics_tracker.commands.status_commands import (
    AddStatus,
    DeleteStatus,
    ListStatuses,
    UpdateStatus,
)
from narcotics_tracker.commands.table_commands import (
    CreateEventsTable,
    CreateInventoryTable,
    CreateMedicationsTable,
    CreateReportingPeriodsTable,
    CreateStatusesTable,
    CreateUnitsTable,
)
from narcotics_tracker.commands.unit_commands import (
    AddUnit,
    DeleteUnit,
    ListUnits,
    UpdateUnit,
)
