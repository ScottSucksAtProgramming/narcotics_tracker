# Mermaid Data Item Class Diagrams
{{TOC}}

## DataItem - Inteface
```mermaid
class DataItem {
    <<Abstract Base Class>>
    +str table
    +int id
    +int created_date
    +int modified_date
    +str modified_by
    +__str__() str
}
```

## Adjustment
```mermaid
class Adjustment {
    +str table
    +int id
    +int created_date
    +int modified_date
    +str modified_by
    +int adjustment_date
    +str event_code
    +str medication_code
    +float amount
    +str reference_id
    +int reporting_period_id
    -__str__() str
}
```
## Event
```mermaid
class Event {
    +str table
    +int id
    +int created_date
    +int modified_date
    +str modified_by
    +str event_code
    +str even_name
    +str description
    +int modifier
    -__str__() str
}
```
## Medication
```mermaid
class Medication {
    +str table
    +int id
    +int created_date
    +int modified_date
    +str modified_by
    +str medication_code
    +str medication_name
    +float fill_amount
    +float medication_amount
    +str preferred_unit
    +float concentration
    +str status
    -__str__() str
}
```

## ReportingPeriod
```mermaid
class ReportingPeriod {
    +str table
    +int id
    +int created_date
    +int modified_date
    +str modified_by
    +int start_date
    +int end_date
    +str status
    -__str__() str
}
```

## Status
```mermaid
class Status {
    +str table
    +int id
    +int created_date
    +int modified_date
    +str modified_by
    +str status_code
    +str status_name
    +str description
    -__str__() str
}
```

## Unit
```mermaid
class Unit {
    +str table
    +int id
    +int created_date
    +int modified_date
    +str modified_by
    +str unit_code
    +str unit_name
    +int decimals
    -__str__() str
}
```
