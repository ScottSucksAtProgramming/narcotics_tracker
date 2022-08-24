"""Defines the representation of controlled substance orders.

New controlled substances are added to the inventory by ordering them from 
approved suppliers. This module defines the Order class which stores the 
information needed to manage controlled substance orders.

See the database module for information on interacting with the database.
Tests are located in the tests/unit/order_tests.py file.

Classes:

    Order: Represents controlled substance orders.

Functions:

    return_table_creation_query: Returns query to create order table.

    parse_order_data: Returns order data from database as dictionary.
"""


class Order:
    """Represents controlled substance orders in the Narcotics Tracker.

    Each order has attributes that assisted in tracking the medication
    inventory including the medications and amounts ordered and the purchase
    order number. This class defines the attributes and behaviors of
    controlled substance orders and handles the storing, updating and deletion
    of order data within the database. Any aspects related to controlled
    substance orders should be handled by this class.

    Initializer:

    Attributes:

    Instance Methods:

    Static Methods:

    """
