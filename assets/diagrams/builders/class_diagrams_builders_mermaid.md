# Narcotics Tracker Builder Diagrams

## Builder Interface

```mermaid
class BuilderInterface {
    <<Abstract Base Class>>
    +build()
    -_reset()
}
```

## DataItem Builder
```mermaid
class DataItemBuilder {
    +__init__()
    -_reset() Exception
    +build() Exception
    +set_table()
    +set_id()
    +set_created_date()
    +set_modified_date()
    +set_modified_by
}
```

## Adjustment Builder
```mermaid
class AdjustmentBuilder {
    -DataItem _dataitem
    -_reset()
    +build() Adjustment
    +set_adjustment_date()
    +set_event_code()
    +set_medication_code()
    +set_adjustment_amount()
    +set_reference_id()
    +set_reporting_period_id()
}
```

## Event Builder
```mermaid
class EventBuilder {
    -DataItem _dataitem
    -_reset()
    +build() Event
    +set_event_code()
    +set_event_name()
    +set_description()
    +set_modifier()
}
```

## Medication Builder
```mermaid
class MedicationBuilder {
    -DataItem _dataitem
    -_reset()
    +build() Medication
    +set_medication_code()
    +set_medication_name()
    +set_fill_amoun()
    +set_medication_amount()
    +set_preferred_unit())
    +set_concentration()
    +set_status()
}
```


## Reporting Period Builder
```mermaid
class ReportingPeriodBuilder {
    -DataItem _dataitem
    -_reset()
    +build() ReportingPeriod
    +set_start_date()
    +set_end_date()
    +set_status()
}
```

## Status Builder
```mermaid
class StatusBuilder {
    -DataItem _dataitem
    -_reset()
    +build() Status
    +set_status_code()
    +set_status_name()
    +set_description()
}
```

## Unit Builder
```mermaid
class UnitBuilder {
    -DataItem _dataitem
    -_reset()
    +build() Unit
    +set_unit_code()
    +set_unit_name()
    +set_decimals()
}
```