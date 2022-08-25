# Inventory Part 1- Designing the Inventory Feature

{{TOC}}

In the previous series I designed and implemented the [representation of medications](LINK) that will be used within the **Narcotics Tracker**. With medications defined we can move on to what this project is all about: **Inventory Tracking**.

My overall goal for this project was to created a simple interface where all controlled substance inventory changes can be locked and tracked. Lets take a look at what that looks like in this project.

## Events
Each row in the Inventory Table is going to represent an event which changes the stock (or amount) of a medication.

### Inventory Event Attributes
There are a handfull of data points which are important for inventory tracking.

**`event_id`**
: Unique identifier for a specific event.

**`event_date`** 
: The date the event occured on.

**`event_code`**
: The type of event which occured.

**`medication_code`**
: The code of the specific medication which was effected by the event.

: Pulled from the **Medication Table**.

**`quanitity_in_mcg`**
: The amount of the medication which was changed.

: Always handled in micrograms within the **Narcotics Tracker**.

**`reporting_period_id`**
: The reporting period in which the event occured during.

: Pulled from the **Reporting Periods Table**.

**`reference_id`**
: A unique identifier pointing to a entry in a different table which provides more information about this event.

: Example: A medication which was used during patient care would use the ePCR Number as its `reference_id`.

: Example: A medication which was received from an order would use the Purchase Order Number as its `reference_id`.

Additionally **`created_date`**, **`modified_date`**, and **`modified_by`** data points will be used.

### Adding Stock to the Inventory
Using the [Medication Feature](LINK) we can define the different medications that are used at our agency. The three medications I used are Fentanyl, Morphine and Midazolam. 

Controlled substance medications cannot be exchanged, or traded between agencies or healthcare facilities. The transfer of these medications require trackable orders and certain medications require the use of 222 Forms.

**222 Form**
: A form issued to approved medical providers which are used to purchase and transfer controlled substances.

The primary way agencies will obtain new controlled substances is by *ordering* them. Agencies which may use this software likely have a stock of controlled substances from previous orders. To accomodate this medications will also be able to be *imported* into the inventory.

### Removing Stock from the Inventory
There are multiple ways in which an amount of a medication can be removed from the inventory.

The most frequent is *patient use*; the medication is given to a patient. Medications are also removed from the inventory when partial vials are *wasted*. Expired vials which are unopened have to be sent out for *destruction*. 

Medications can all be *lost*, though this is a rare occurence and must be investigated. 

### Intended Use Case
I imagine that users of the **Narcotics Tracker** will sit down periodically (I do it about once per week,) to update the inventory and log all changes.

Logging of events in the inventory table is something users may do manually, though I have the ability to print up a report from my electronic patient care reporting software. I may wish to be able to have those reports added directly using the comma separated values format.

## Requirements
There are a bunch of requirements outlined above which can be broken down a few peces.

### Event Types
    1. The creation of an Events Type Table.
    2. The ability to create, update, read and delete event types from the table.
    
### Reporting Periods
    1. The creation of a reporting period table.
    2. The creation of a Reporting Period class to handle reporting periods.
    3. The ability for reporting periods to be created, read, updated, and deleted from the table.

### Event Class
    1. The creation of an Event Class to handle the actual events as objects.
    2. The ability for users to create new events, specify their details, and save them into the Inventory Table.
    3. The ability for users to read and update events already saved in the table.
    4. The ability for users to delete events from the Inventory Table (this may be removed in the future).
    5. A mechanism where new events are assigned the appropriate `reporting_period_id` and `created_date`.
    6. A mechanism to assign a `modified_date` when events are updated.

### Inventory Table
    1. Creation of the Inventory Table.


## Conclusion
It looks like I’ve got my work cut out for me. In the next part of this series I’ll start implementing those requirements.

LINK

