# Design Doc Part 2- Database

|Section | Version | Created    | Updated    |
|:-------| :------ | :--------- | :--------- |
|   2    | 0.1.0   | 08/25/2022 | 08/24/2022 |

{{TOC}}

Databases are used everywhere in software and I’ve never worked with one. The **Narcotics Tracker** is an ideal project for me to dip my toes in and build my understanding of databases. Other method for storing data were considered such as writing to JSON Files, CSV Files and Pickle Files but the strengths of using a database made it an obvious choice.

The only attribute required for the database is the connection to the database file. A 

## Attributes
    - database_connection (sqlite3.Connection): The connection to the database file.
    
## Behaviors
    1. Creation and connection with a database file.
    2. Creation of tables within the database.
    3. Querying of table names from the database file.
    4. Querying of columns names from database tables.
    5. Updating tables within the database.
    6. Deleting tables from the database.
    7. Writing data to the database.
    8. Reading data from the database.
    9. Loading objects from data saved in the database.
    10. Setting of the dates when saving objects to the database.

## Discussion
### Attributes
There were not many other attributes I thought would be important to store within the database objects. **One attribute which may be added later is the path to the data directory.** Currently the path is hard coded into the methods, but it might make sense to give users an option on where they want their database files to be stored.

### Database Choice
**I decided to use SQLite3 for this project.** SQLite3 is built into Python. It requires no configuration or external services, and I already watched a course on using it, so there!

### Table Design
Multiple tables will be required for the inventory tracking portion of this project:

#### Medication Table
The medication table will hold all the information relating to the medications themselves. 

medication_table_design 2.png

The `code` is the unique identifier which will be used to select the medication when querying the database. It will be used as a foreign key which gets imported into multiple other tables.

For more information look at [Design Doc Part 3- Medications](01_medications.md).

#### Inventory Table
The Inventory Table is the main table used for this project. It will handle all inventory changes which happen and will be interacted with frequently.

inventory_table_design.png

The `inventory_id` is the primary key for this table and will be used to select a specific inventory change.

The `event_code` will be pulled from a list of acceptable event types from the [Events Table]. The `medication_code` will be the unique identified of the medication pulled from the [Medication Table]. The `reporting_period_id` will identify which reporting period this even happened in and is pulled from the [Reporting Period Table]

For more information look at [Design Doc Part 3- Inventory](03_inventory.md).

#### Reporting Period Table
The Reporting Periods Table will specify which reporting period an event on the [Inventory Table] happens in. There are Two reporting periods each year: *January 1st to June 30th*, and *July 1st to December 31st.*

reporting_period_table.png

For more information look at [Design Doc Part 3- Inventory](03_inventory.md).

### Vocabulary Control Table Design
Vocabulary Control Tables specify acceptable options for columns of other tables within the database.

#### Containers, Units, Medication Statuses Tables
As of version 0.1.0 the acceptable values for the `container_type`, `preferred_unit` and `medication_status` columns of the medication table are limited though the use of enumerations that were built in python. These will be switched over to Vocabulary Control Tables in a future update.

For more information look at [Design Doc Part 1- Medications](01_medications.md).

#### Events Types Table
The Events Table will specify which event types can be used within the Narcotics Tracker.

events_table_design.png

For more information look at [Design Doc Part 3- Inventory](03_inventory.md).

[Return To TOC](00_design_overview.md)