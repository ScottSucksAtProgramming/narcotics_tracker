# Refactoring Part 1

As of version 0.2.0 the Narcotics Tracker has become complicated and poorly
organized. A refactoring pass is being made to improve the code.

## Areas of Concern

> Clean code is separate into a hierarchy of concerns.

### List of All Concerns

-   Defining interfaces for all builders.
-   Constructing objects.
-   Scripts which setup the Narcotics Tracker.
-   A library of pre-build objects.
-   Conversion of between units.
-   Objects which store container data.
-   Objects which store event data.
-   Objects which store adjustment data.
-   Objects which store medication data.
-   Objects which store reporting period data.
-   Objects which store status data.
-   Objects which store unit data.
-   Connecting to a database.
-   Creation of Tables.
-

## Medication Class

What is the Single Responsibility?

-   This class should do nothing except store data for a medication.

What things fall outside of the responsibility?

-   saving medication to the database.
-   reading medication data from the database.
-   updating the medication in the database.
-   deleting the medication from the database.

1. Step 1: Create a DatabaseObject Abstract Base Class which contains
   attributes for id, created_date, modified_date, and modified_by, table_name,

2. Step 2:
