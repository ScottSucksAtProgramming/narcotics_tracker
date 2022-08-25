# Design Doc Part 3- Inventory

|Section | Version | Created    | Updated    |
|:-------| :------ | :--------- | :--------- |
|   3    | 0.1.0   | 08/26/2022 | 08/26/2022 |

{{TOC}}

Inventory tracking is what we’re all about in the **Narcotics Tracker**. 

The goal is to have a single place where all controlled substance medication inventory changes can be entered this will be The Inventory Table. This table can be queried to pull all sorts of information which will be important for [Report Generation](11_reports.md)

## Intended Use
Each time a user wants to update the inventory they will add an event to the Inventory Table. The user must specify which medication (using a `medication_code`) is being adjusted and the amount changed (using that medication’s `preferred_unit`) and the event’s type (using an `event_code`).

Additional functionality will be added for [Report Generation](11_reports.md) allowing users to pull up the records they need for the mandatory Department Of Health paperwork.

## Attributes    
    - Inventory Table creation query
    - Events Table creation query
    - Reporting Periods Table creation query.

## Behaviors
    1. Create the Inventory Table.
    2. Add events to table.
    3. Modify events on the table.
    4. Delete events from the table.
    5. Assign the correct `reporting_period_id` to new events.
    6. Assign the `created_date` and `modified_date` for new events.
    7. Update the `modified_date` when modifying the event.

## Discussion

### Events
There are multiple events which perform one of two operations, **adding** and **subtracting** inventory. Subtraction can be represented using the `-` sign preceeding its value. 

#### Event Types
Events type are handled by the  Event Table which specifies the available events.

| Event Name | Operator | Description | Code |
| :-|:-|:-|
|Imported|`+`|Used when adding pre-existing stock to the table.|IMPORT|
|Ordered|`+`|Used when adding new stock from a purchase order.|ORDER|
|Used|`-`|Used when subtracting medication that was administered to a patient.|USE|
|Wasted|`-`|Used when subtracting medication which was wasted.|WASTE|
|Destruction|`-`|Used when subtracting medication which was destroyed through a reverse distributor.|DESTROY|
|Loss|`-`|Used for medications which are lost or stolen.|LOSS|


[Return To TOC](00_design_overview.md)