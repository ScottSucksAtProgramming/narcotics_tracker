# Narcotics Tracker Design Document

| Version | Created    | Updated    |
| :------ | :--------- | :--------- |
| 0.1.0   | 08/01/2022 | 08/24/2022 |

{{TOC}}

## Summary

Welcome to the **Narcotics Tracker**! This software is designed to assist controlled substance agents working at EMS agencies with inventory tracking and periodic reporting of controlled substance activities to their governing agencies.

#### Motivation
I am a controlled substance agent working in New York State. The tracking of controlled substances is complicated and requires multiple forms and processes. I have wished for a single place where all of that information can be stored and easily accessed. This software is intended to fill that need.

### Goals

The **Narcotics Tracker** will provide a single place to enter all changes to an agencies controlled substance inventory. Each change in the inventory can be entered peridoically where the data can be queried to return information requried for reporting and compliance with tracking specifications.

##### Project Specifications
    1. Inventory tracking of all controlled substances used by an EMS agency.
    2. Ability to create agency specific medications.
    3. Tracking of medication lots as they as disbursed to sub-stocks.
    4. Tracking of medication orders.
    5. Tracking of medication destruction.
    6. Tracking of medication administration.
    7. Tracking of medication waste.
    8. Built in reports which can be generated at the users request which fulfill the New York State and DEA requirements.
    9. A simple but powerful console user interface.
    10. A graphical user interface.

I am a self-taught programmer looking to improve my knowledge and experience in soft-ware design by building projects which have practical applications.

##### Personal Learning Goals 
    1. Increase my knowledge and experience with Python.
    2. Learn about Object Oriented Programming.
    3. Practice and gain experience with Test Driven Development
    4. Gain knowledge on the storage, and manipulation, of data and the use of databases.
    5. Potentially branch out into GUI development with Python or different languages as necessary.
    6. To put out a product which I may be able to use to help generate extra income though licensing and service contracts.

## Design Discussion and Alternatives

---

### Development Roadmap / Progress

I'm not entirely sure where the best place to begin is. I do not have a enough
experience to know how to design this kind of software. I'll be using a lot of
trial and error. Here is my imagined development Path.

-   [x] Medication Creation and Management
  -   [x] Builder Pattern
-   [x] Communication with a Database.
-   [ ] Order Management.
-   [ ] Lot Management.
-   [ ] Destruction Management.
-   [ ] Medication Use and Waste Management.
-   [ ] Inventory Management
-   [ ] Controlled Substance Agent Account Management.
-   [ ] Report Generation
-   [ ] Console User Interface
-   [ ] Graphical User Interface

### Medication Creation and Management
In order to track the inventory of controlled substance medications a model of the medications has to be built within the program. I decided to start the probject by building a module to handle the creation and implementation of medications. 

Medications will be similar across EMS agencies but the specific dosages, concentrations and other attributes of the meds will vary. There are many specifics for controlled substance medications but I narrowed it down to 7 medication specific attributes and 5 which will be important to working with the medication as part of the database.
    
###### Medication Facing Attributes
    
    - name (str): The name of the medication.

    - container_type (containers.Container): The type of container the medication comes in.

    - fill_amount (float): The amount of the solvent in the container. Measured in milliliters (ml).

    - dose (float): The amount of medication in the container.

    - preferred_unit (units.Unit): The unit of measurement the medication is commonly measured in.

    - concentration (float): The concentration of the medication to its solvent.
    
    - status (medication_status.MedicationStatus): The status of the medication.
    
    
###### Database Facing Attributes
    
    - medication_id (int): The numeric identifier of the medication in the database.

    - code (str): The unique identifier for the specific medication. 

    - created_date (str): The date the medication was first entered into the database.

    - modified_date (str): The date the medication was last modified in the database

    - modified_by (str): The user who last modified the medication in the database.
 
 
A list of five main requirements for controlled substance medications were identified.
###### Medication Behaviors
     1. Creation of new medications by users.
     2. Saving of medications within the database.
     3. Loading of saved medications.
     4. Updating of saved medications.
     5. Deletion of medications from the database.
 
#### Discussion
##### Attributes

**The NDC Number was removed from the list of attributes.** The NDC number is only important for medication destruction. NDC Numbers change between manufacturers and concentrations for the same medication. NDC Numbers may not be tracked at all within the Narcotics Tracker, if they are going to be tracked they will be part of a different module.

- - -

**The Box Quantity was removed from the list of attributes.** Box Quantity (how many containers come in the box) will be important for Orders and Lot Management but not as part of the medication module.

##### Medication Data Structures
There were tons of ways to represent medications within the **Narcotics Tracker**. Ordered lists and dictionaries are simple and would fulfill most of the requirements. As of version 0.1.0 dictionaries are used to load medications as objects from data stored in the database and lists are used in a script to quickly create the medications I personally use at my agency. **I decided that using classes and objects would be the best way for me to achieve the results I wanted with this project and help me improve my object oriented programming skills.** 

##### The Builder Pattern
Since I decided to go with objects as the data structure for medications I needed a way to simplify the creation of medications for myself as the developer and for the users. With twelve total attributes it would be easy to assign values to the wrong attributes, forget attributes and potentiall build medications which would be unusable. 

**I employed the builder pattern to separate to separate the creation of medications into smaller, easier to understand steps. Using the builder pattern does add complexity to the code it also adds the flexibility to use the same approach to different objects used later within the Narcotics Tracker.**

##### Enums vs. Vocabulary Control Tables
There are limited options for the types of containers a controlled substance medication might come in. The status of each medication and it’s preferred dosage unit also have limited options. 

As of the version 0.1.0 release Enums were created for each of those three attributes and are handled through Python and it’s objects. It was brought to my attention that this will limit the flexibility for users who may need to create custom options for these attributes. 

**In a future release these Enums will be converted in vocabulary control tables within the datbase. This will allow for users to create new statuses, containers, and units as needed for their agency.**

##### Medication Deletion
It’s likely that deleting medications will cause issues in long term record keeping. Attributes for medications which are no longer in use are important when pulling records from previous periods when they were in use. Deletion of medication is likely not going to be a feature that the users will have access to. **Deleting Medications is important enough for this option to be available during development of the Narcotics Tracker that I have chosen to build it.** It can be removed later if deemed unnecessary.

### Communication with a Database
Databases are used everywhere in software and I’ve never worked with one. The **Narcotics Tracker** is an ideal project for me to dip my toes in and build my understanding of databases. Other method for storing data were considered such as writing to JSON Files, CSV Files and Pickle Files but the strengths of using a database made it an obvious choice.

The only attribute required for the database is the connection to the database file. A 

###### Database Attributes
    - database_connection (sqlite3.Connection): The connection to the database file.
    
###### Database Behaviors
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

#### Discussion
##### Attributes
There were not many other attributes I thought would be important to store within the database objects. **One attribute which may be added later is the path to the data directory.** Currently the path is hard coded into the methods, but it might make sense to give users an option on where they want their database files to be stored.

##### Database Choice
**I decided to use SQLite3 for this project.** SQLite3 is built into Python. It requires no configuration or external services, and I already watched a course on using it, so there!

##### Database Tables
Multiple tables will be required for the inventory tracking portion of this project:

**Inventory Tables**

    1. Medication Table
    2. Order Table
    3. Lot Table
    4. Administration Table
    5. Inventory Table
    6. User / Agent Table

In addition vocabulary control tables will be required to help set the specific types of data and events in the project:

**Vocabulary Control Tables**

    1. Medication Containers
    2. Medication Statuses
    3. Medication Units
    4. Order Statuses
    5. Order Suppliers
    6. Inventory Events



    1. Containers Table
    2. Medication Statuses Table
    3. Dosage Units Table
    4. Events Table

Additional tables may be identified as the project progresses.

### Tracking of Controlled Substance Orders
Ordering controlled substance medications are one of the only ways new stock gets added into the inventory. They are integral to this project and are next up on my list of features to add.


##### Order Attributes
    - order_id (int): The numeric identifier of the order in the database.
    
    - po_number (str): The unique identifier for the specific order.
    
    - date_ordered (str): Date the order was placed.
    
    - medication_code (str): `medication.Medication.code` of medications ordered.
    
    - containers_amount (int): The number of containers for the medication ordered.
    
    - supplier (Enum): The name of the supplier.
    
    - supplier_order_number (str): The suppliers order number for reference.
    
    - dea_form_number (str): The number of the 222 form used to order Class II medications. (Optional)
    
    - date_received (str): Date a package is received.
    
    - packages_received (int): Number of packages of a specific medication received.
    
    - comments (str): Any comments or additional details for the order.
    
    - status (Enum): The status of the order.
    
    - created_date (str): The date the order was first entered into the narcotics tracker.
    
    - modified_date (str): The date the order was last modified.
    
    - modified_by (str): The user who last modified the order.

##### Order Behaviors
    - Creation of new orders.
    - Saving of orders to the database.
    - Loading of orders from data.
    - Updating orders.
    - Deleting orders.




#### Discussion
##### Attributes
Currently my controlled substance orders are tracked in a spread sheet. The following attributes are tracked.

Row Number, Purchase Order Number, Date Ordered, Medications and Amount Ordered, Supplier, Supplier Order Number, 222 Form Number, Dates Received, Packaged Received, Comments / Notes.

The Purchase Order Number will be the user-facing unique identifier for the order. 

Because medications can be received in different shipments a compound or composite primary key (Purchase Order Number AND Medication) need to be used to ensure that this can be acommodated.

##### Behaviors
The process for ordering medications is located in `docs/design/user_processes.md`

**New Orders**
* Orders have to be created.
* PO Number is assigned.
* Spreadsheet is filled out with initial info: 
  * Purchase Order Number, 
  * 222 Form Number, 
  * Date Ordered, 
  * Medications and Amounts Ordered
* Order Status is set to ‘Open’.

**Shipment is Received**
* Spreadsheet is updated:
    * Date Shipment Received
    * Medications and Amounts in shipment
        * Lot number of Medications.
* Stock Inventory Sheet (DOH-3850) created for each Lot.
* Medications are added to the inventory.
* Repeated for any additional shipments.
* When all medications are received the Status is set to ‘Closed’.

What would This look Like?
1. USER: Places and order with the supplier. Forms are filled out and all paperwork is filed.
2. USER: Creates a New Order.
3. USER: Fills in attributes.
  4. PO Number
  5. Date Ordered
  6. Medication Ordered
    7. Amount Ordered
  8. 222 Form Number (if applicable)
  9. Status set to ‘Open’.
10. USER: Receives medications. Forms a filled out and filed. Medications are placed in safe.
11. USER: Loads Order via PO Number.
12. USER: Updates Order:
    13. Date Received
    14. Medication Received
        15. Amount Received
16. NARCOTICS TRACKER: Creates an Add event in the Inventory Table sending the Medication info, date received, amount in mcg, and the PO Number.
17. NARCOTICS TRACKER: Creates a new Lot Table passing the Lot Number, Amount of Medication, Date, and PO Number for reference.
18. USER: Sets Medication Order to ‘Closed’

##### Tables Needed
* Order Table
* Order Status Table (Vocabulary Control Table)
  * Open; Closed; Delayed; Cancelled
* Supplier Table (Vocabluary Control Table)
  * BoundTree Medical;
* * Lot Table (To be implemented in a future update)
* Inventory Table (To be implemented in a future update)
* Events Table (To be implemented in a future update)


### Lot Management
To Be Written.
### Destruction Management
To Be Written.
### Medication Use and Waste Management
To Be Written.
### Inventory Management
##### Events
- Import (Add)
- Add (Add)
- Administer (Subtract)
- Waste (Subtract)
- Destroy (Subtract)
### Controlled Substance Agent Account Management
To Be Written.
### Report Generation
To Be Written.
### Console User Interface
To Be Written.
### Graphical User Interface
To Be Written.