# User Processes

**Purpose:** This document will list all the processes that are performed for narcotics tracking so the database and UI design can be focused on the user.

### Table of Contents
- Processes
	- [Order New Medications](#orders)
	- [Destroy Medications](#destruction)
	- [Move Medications](#move)
	- [Waste Medications](#waste)
	- [Administer Medications](#administer)
	- [Lose Medications](#lose)
	- [Weekly Inventory Count](#weekly-inventory)
	- [Bi-Annual Inventory Audit](#biannual-inventory)

# Processes

<a name="orders"></a>
## Order New Medications
Medications are primarily ordered from BoundTree Medical, though can be ordered from multiple suppliers. This may be another configuration process where users set up the suppliers they order from.

1. Order is placed through the supplier.
    2. Mulitple medications can be ordered in a single order.
    3. Agency Generates an order number (PO Number).
    4. Controlled Substance Orders spread sheet filled out:
        5. Order Number
        6. 222 Form Number (If Used)
        7. Date Ordered
        8. Medications and amount ordered.
    9. Any paperwork received for the order is scaned / saved as PDF and placed in Controlled Substance Purchase Folder on Google Drive.
2. Medication is received
    4. Medications are verified.
    5. Order Packing Slip is signed by Agent, scanned into Google Drive and physcial copy filed in cabinet.
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

#### Lot Information
It makes sense to think of this in 

<a name="destruction"></a>
## Destroy Medications

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


