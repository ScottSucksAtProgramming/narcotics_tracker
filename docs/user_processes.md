# User Processes

**Purpose:** This document will list all the processes that are performed for narcotics tracking so the database and UI design can be focused on the user.

### Table of Contents
- Processes
	- [Orders](#orders)
	- [Lot Tracking](#lots)
	- [Destroy Medications](#destruction)
	- [Move Medications](#move)
	- [Waste Medications](#waste)
	- [Administer Medications](#administer)
	- [Lose Medications](#lose)
	- [Weekly Inventory Count](#weekly-inventory)
	- [Bi-Annual Inventory Audit](#biannual-inventory)

# Processes

<a name="orders"></a>
## Orders
Medications are primarily ordered from BoundTree Medical, though can be ordered from multiple suppliers. This may be another configuration process where users set up the suppliers they order from.

1. Order is placed through the supplier.
    3. Agency Generates an order number (PO Number).
    4. Controlled Substance Orders spread sheet filled out:
        5. Order Number
        6. 222 Form Number (If Used)
        7. Date Ordered
        8. Medications and amount ordered.
    9. Any paperwork is signed, scanned, filed
2. Medication is received
    4. Medications are verified.
    5. Order Packing Slip is signed, scaned, filed
    5. Controlled Substance Orders spreadsheet updated:
        6. Date Medications Received
        7. Number of Packages (Boxes)
    8. Stock Inventory Sheet (DOH-3850) Created per Lot Number
        9. Medication Name
        10. Agency Name
        11. Agency Code
        12. CS Lisence Number
        11. Supplier Name
        12. Manufacturer
        13. Lot Number
        14. Total Amount Received in mg
    15. Stock Safe Entry Log is filled out.
4. Medications are entered into the 

### Notes
* Mulitple medications can be ordered in a single order.
* Medications from the same order can be received at different times depending on supplier availability.
* Multiple boxes of the same medication will likely have the same Lot Number - but not always.
* Different Medications will never have the same lot number.

### Data Points
#### Order Information
Orders are their own object. Once the order is received and verified it's technically close
* Order Number `int`
* 222 Form Number `str`
* Date Ordered `Date Obj. / str`
* Medication's Ordered
    * Amount ordered per medication in vials `int`
    * Date Received `Date Obj. / str`
    * Number of Packages `int`
* Agent `Agent Obj. / str`
* Date Updated `Date obj. / str`
* Order Status `str`

<a name="lots"></a>
## Lot Tracking
Medications are tracked in Lots with a shared Lot Number. Dispersements of those medications are subtracted from the total balance. Dispersements may be moved to a sub-stock or for destruction at a reverse distributor. When the balance is depleted the Lot is closed. 

1. Medication is physically moved.
2. Stock Inventory Sheet (DOH-3850) for that Lot Number is updated.
    3. Date `Date Obj. / str`
    4. Quantity in mg `float`
    5. Location `Sub-Stock Obj / str`
    6. Agent `Agent Obj. / str`
7. Stock Safe Entry Form and Sub-Stock Safe Entry Form filled out. (These will **not** be part of this application.)



<a name="destruction"></a>
## Destroy Medications
Medications that are expired are sent to a reverse distributor for destruction. 

1. A destruction request is made to the reverse distributor.
2. Medications for destructions are inventoried and submitted to reverse distributor by NDC number.
    3. NDC Number
    4. Medication
    5. Manufacturer
    6. Concentration
    7. Package Size (in ml)
        8. The NDC number generates the package size which may be calcucated per vial, or per box.
    8. Amount to be sent (in ml)
        9. Amount of Full Packages (meeting the size)
        10. Amount of Partial Packages (Less than package size)
        11. The Reverse Distributor only cares about the total ml's not vials or anything else.
12. Once the order is submitted and paid for a 222 form and shipping container is sent.
13. Medications are shipped out and a receipt of destruction  is provided.
14. Recipt of desctruction is signed, scanned, filed.

<a name="move"></a>
## Move Medications
Medicationas have to be moved between different locations frequently. 

Sub stocks: It would be useful to have users specify the different sub stock locations as that will be different for each organization. Likely to need a substock object or similar concept in fentanyl.

- Locations
	- Stock Safe
		- Full / Partials / Expired
	- Sub-Stocks
		- 291 A
		- 291 B
		- 292 A
		- 292 B
		- 293 A
		- 293 B
		- 2999 A
		- 2999 B


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


