# 1.0 - Project Design Architecture

| Section | Version | Created    | Updated    |
| :------ | :------ | :--------- | :--------- |
| 1.0     | 0.2.5   | 10/25/2022 | 10/25/2022 |

{{TOC}}

## Code Structure

### Persistence Layer

Handles the storage of data within the SQLite3 Database.

### Use Case Layer
Contains the buisness logic which enables inventory management.

#### DataItems
The objects which enable inventory management of controlled substances.

###### Adjustments
###### Events
###### [Medications](01_medications.md)
###### Reporting Periods
###### Statuses
###### Units

#### Commands
Objects which handle the higher-level concerns of inventory management.

###### Inventory Management
###### Order Management
Not Yet Implemented
###### Lot Disbursement Management
Not Yet Implemented
###### Provider Managemement
Not Yet Implemented
###### Agent Management
Not Yet Implemented


#### Reports

Not Yet Implemented


### User Facing Layer


#### Command Line User Interface
Not Yet Implemented
#### Console User Interface
Not Yet Implemented
#### Graphical User Interface
Not Yet Implemented

[Design Document Table of Contents](01_table_of_contents.md)
