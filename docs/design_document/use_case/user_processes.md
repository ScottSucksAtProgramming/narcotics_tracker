# User Processes

**Purpose:** This document will list all the processes that are performed for
narcotics tracking so the database and UI design can be focused on the user.

### Table of Contents

-   Processes
    -   [Orders](#orders) - [Data Points](#orders-dp)
    -   [Lot Tracking](#lots) - [Data Points](#lots-dp)
    -   [Destroy Medications](#destruction) - [Data Points](#destruction-dp)
    -   [Move Medications](#move) - [Data Points](#move-dp)
    -   [Waste Medications](#waste)
    -   [Administer Medications](#administer)
    -   [Lose Medications](#lose)
    -   [Weekly Inventory Count](#weekly-inventory)
    -   [Bi-Annual Inventory Audit](#biannual-inventory)

# Processes

<a name="orders"></a>

## Orders

Medications are primarily ordered from BoundTree Medical, though can be ordered
from multiple suppliers. This may be another configuration process where users
set up the suppliers they order from.

1. Order is placed through the supplier. 
2. 3. Agency Generates an order number
   (PO Number). 
4. Controlled Substance Orders spread sheet filled out: 
    5. Order Number 
    6. 222 Form Number (If Used) 7. Date Ordered 8. Medications and amount ordered. 
    7. Any paperwork is signed, scanned, filed.
2. Medication is received
    3. Medications are verified. 
    4. Order Packing Slip is signed, scanned, filed.
5. Controlled Substance Orders spreadsheet updated:
    6. Date Medications Received 
    7. Number of Packages (Boxes) 
8. Stock Inventory Sheet (DOH-3850) Created per Lot Number 
    9. Medication Name 
    10. Agency Name 
    11. Agency Code 
    12. CS Lisence Number 
    13. Supplier Name 
    14. Manufacturer 
    15. Lot Number 
    16. Total Amount Received in mg 
17. Stock Safe Entry Log is filled out.
3. Medications are entered into the

### Notes

-   Multiple medications can be ordered in a single order.
-   Medications from the same order can be received at different times
    depending on supplier availability.
-   Multiple boxes of the same medication will likely have the same Lot
    Number - but not always.
-   Different Medications will never have the same lot number.

<a name="orders-dp"></a>

### Data Points

Orders are their own object. Once the order is received and verified it's
technically closed

-   Order Number | `int`
-   222 Form Number | `str`
-   Date Ordered | `Date Obj. / str`
-   Medication's Ordered
    -   Amount ordered per medication in vials | `int`
    -   Date Received | `Date Obj. / str`
    -   Number of Packages | `int`
-   Agent | `Agent Obj. / str`
-   Date Updated | `Date obj. / str`
-   Order Status | `str`

<a name="lots"></a>

## Lot Tracking

**Lots do not contribute to the overall inventory**

Medications are tracked in Lots with a shared Lot Number. Dispersements of
those medications are subtracted from the total balance. Dispersements may be
moved to a sub-stock or for destruction at a reverse distributor. When the
balance is depleted the Lot is closed.

1. Medication is physically moved.
2. Stock Inventory Sheet (DOH-3850) for that Lot Number is updated. 3. Date 4.
   Quantity (in mg) 5. Location 6. Agent
3. Stock Safe Entry Form and Sub-Stock Safe Entry Form filled out. (These will
   **not** be part of this application.)

<a name="lots-dp"></a>

### Data Points

-   Entry Date | `Date Obj. / str`
-   Entry Event | `str`
-   Quantity in mg | `float`
-   Location | `Sub-Stock Obj. / str`
-   Lot Status | `str`
-   Agent | `Agent Obj. / str`
-   Date Created | `Date Obj. / str`
-   Date Modified | `Date Obj. / str`

<a name="destruction"></a>

## Destroy Medications

Medications that are expired are sent to a reverse distributor for destruction.

1. A destruction request is made to the reverse distributor.
2. Medications for destructions are inventoried and submitted to reverse
   distributor by NDC number. 3. NDC Number 4. Medication 5. Manufacturer 6.
   Concentration 7. Package Size (in ml) 8. The NDC number generates the
   package size which may be calcucated per vial, or per box. 8. Amount to be
   sent (in ml) 9. Amount of Full Packages (meeting the size) 10. Amount of
   Partial Packages (Less than package size) 11. The Reverse Distributor only
   cares about the total ml's not vials or anything else.
3. Once the order is submitted and paid for a 222 form and shipping container
   is sent.
4. Medications are shipped out and a receipt of destruction is provided.
5. Recipt of desctruction is signed, scanned, filed.

<a name="destruction-dp"></a>

### Data Points

<a name="move"></a>

## Move Medications

Medicationas have to be moved between different locations frequently.

Sub stocks: It would be useful to have users specify the different sub stock
locations as that will be different for each organization. Likely to need a
substock object or similar concept in fentanyl.

-   Locations
    -   Stock Safe
        -   Full / Partials / Expired
    -   Sub-Stocks
        -   291 A
        -   291 B
        -   292 A
        -   292 B
        -   293 A
        -   293 B
        -   2999 A
        -   2999 B

<a name="move-dp"></a>

### Data Points

<a name="waste"></a>

## Waste Medications

<a name="administer"></a>

## Administer Medications

<a name="lose"></a>

## Lose Medications

<a name="weekly-inventory"></a>

## Weekly Inventory

<a name="biannual-inventory"></a>

## Bi-Annual Inventory Audit

# Interface

# Ordering Medications

1. Order is Placed.
2. Order information is added to Orders Table by user.
    3. `order_number`, `222_form_number`, `date_ordered`, (`medications_ordered`, `amount`), `Agent`, `date_modified`, `supplier`
    4. `order_status` set to `OPEN`
4. Medications are received.
    5. Order information updated in Order Table by user.
        6. (`medications_received`, `amount`, `lot_number`, ),`date_received`,
        7. If all medications are received `order_status` set to `CLOSED`.
        8. `comments` added as necessary.
8. Medications Added to Inventory Automatically by program.
    9. `medication`, `amount_in_mg`, `date_received` `order_number`
10. New Lot Table Created by Program.
    11. Table Name: `medication` + `lot_number`
    12. `medication`, `supplier`, `supplier_DEA_number`, `manufacturer`, `lot_number`, `amount_in_mg`
    13. Additional Information added by user.
