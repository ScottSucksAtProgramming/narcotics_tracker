Mermaid Code!

classDiagram

```mermaid
class DatabaseItems {
    <<Abstract Base Class>>
    + String Table_Name
    + Dict Column_Info
    + Integer ID
    + Integer Created_Date
    + Integer Modified_Date
    + String Modified_By
    + Save(CommandInterface)
    + Load(CommandInterface)
    + Update(CommandInterface)
    }

class Adjustments {
    <<DataClass / Invoker>>
    + Unixepoch AdjustmentDate
    + String EventCode*
    + String MedicationCode*
    + Integer AdjustmentAmount
    + String ReferenceID
}
class Events {
    <<DataClass / Invoker>>
    + String Code
    + String Name
    + String Description
    + Integer Modifier

}

class Medications {
    <<DataClass / Invoker>>
    + String MedicationCode
    + String MedicationName
    + Float FillAmount
    + Float MedicationAmount
    + Unit PreferredUnit*
    + Float Concentration
}
class ReportingPeriods {
    <<DataClass / Invoker>>
    + Unixepoch StartDate
    + Unixepoch EndDate
}
class Statuses {
    <<DataClass / Invoker>>
    + String StatusCode
    + String StatusName
    + String Description
}
class Units {
    <<DataClass / Invoker>>
    + String UnitCode
    + String UnitName
    + Integer Decimals
}

class Database {
    <<Receiver>>
    + Table Events
    + Table Inventory
    + Table Medications
    + Table ReportingPeriods
    + Table Statuses
    + Table Units
}

class CommandInterface {
    <<Protocol>>
    + execute()
}

class Commands {
    + CommandInterface
}

DatabaseItems <|-- Events : Inherits From
DatabaseItems <|-- Adjustments : Inherits From
DatabaseItems <|-- Medications : Inherits From
DatabaseItems <|-- ReportingPeriods : Inherits From
DatabaseItems <|-- Statuses : Inherits From
DatabaseItems <|-- Units : Inherits From

Commands ..|> CommandInterface : Implements

CommandInterface <|.. DatabaseItems : Uses

Database <-- Commands : Acts On
```
