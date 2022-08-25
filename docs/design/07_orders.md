# Design Doc Part 7- Orders

|Section | Version | Created    | Updated    |
|:-------| :------ | :--------- | :--------- |
|   7    | 0.1.0   | 08/24/2022 | 08/24/2022 |

{{TOC}}

Ordering controlled substance medications are one of the only ways new stock gets added into the inventory. They are integral to this project and are next up on my list of features to add.


## Order Attributes
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
    
    - comment (str): Any comments or additional details for the order.
    
    - status (Enum): The status of the order.
    
    - created_date (str): The date the order was first entered into the narcotics tracker.
    
    - modified_date (str): The date the order was last modified.
    
    - modified_by (str): The user who last modified the order.

## Order Behaviors
    - Creation of new orders.
    - Saving of orders to the database.
    - Loading of orders from data.
    - Updating orders.
    - Deleting orders.




## Discussion
### Attributes
Currently my controlled substance orders are tracked in a spread sheet. The following attributes are tracked.

Row Number, Purchase Order Number, Date Ordered, Medications and Amount Ordered, Supplier, Supplier Order Number, 222 Form Number, Dates Received, Packaged Received, Comments / Notes.

The Purchase Order Number will be the user-facing unique identifier for the order. 

Because medications can be received in different shipments a compound or composite primary key (Purchase Order Number AND Medication) need to be used to ensure that this can be acommodated.

### Behaviors
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

### Tables Needed
* Order Table
* Order Status Table (Vocabulary Control Table)
  * Open; Closed; Delayed; Cancelled
* Supplier Table (Vocabluary Control Table)
  * BoundTree Medical;
* * Lot Table (To be implemented in a future update)
* Inventory Table (To be implemented in a future update)
* Events Table (To be implemented in a future update)

[Return To TOC](00_design_overview.md)