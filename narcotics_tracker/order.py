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

    Each order has attributes that assisted in tracking the order
    inventory including the orders and amounts ordered and the purchase
    order number. This class defines the attributes and behaviors of
    controlled substance orders and handles the storing, updating and deletion
    of order data within the database. Any aspects related to controlled
    substance orders should be handled by this class.

    Initializer:

    Attributes:

        order_id (int): The numeric identifier of the order in the database.

        po_number (str): The unique identifier for the specific order.

        date_ordered (str): Date the order was placed.

        order_code (str): `order.order.code` of orders
            ordered.

        containers_amount (int): The number of containers for the order
            ordered.

        supplier (str): The name of the supplier.

        supplier_order_number (str): The suppliers order number for reference.

        dea_form_number (str): The number of the 222 form used to order Class
            II orders. (Optional)

        date_received (str): Date a package is received.

        packages_received (int): Number of packages of a specific order
            received.

        comments (str): Any comments or additional details for the order.

        status (str): The status of the order.

        created_date (str): The date the order was first entered into the
            narcotics tracker.

        modified_date (str): The date the order was last modified.

        modified_by (str): The user who last modified the order.

    Instance Methods:

    Static Methods:
    """

    def __init__(self, builder=None) -> None:
        """Initializes the order object using the orderBuilder.

        orders are complex objects with many attributes. The Builder
        Pattern was used to separate the creation of orders to the
        Builder Package. Refer to the documentation for the orderBuilder
        for more information.

        Args:
            builder (builder.orderBuilder): The builder used to
            construct the order object.
        """
        self.order_id = builder.order_id
        self.po_number = builder.po_number
        self.date_ordered = builder.date_ordered
        self.medication_code = builder.medication_code
        self.containers_amount = builder.containers_amount
        self.supplier = builder.supplier
        self.supplier_order_number = builder.supplier_order_number
        self.dea_form_number = builder.dea_form_number
        self.date_received = builder.date_received
        self.packages_received = builder.packages_received
        self.comment = builder.comment
        self.status = builder.status
        self.created_date = builder.created_date
        self.modified_date = builder.modified_date
        self.modified_by = builder.modified_by

    def __repr__(self) -> str:
        """Returns a string expression of the order object.

        Returns:
            str: The string describing the order object
        """

        return (
            f"Controlled Substance Order: {self.po_number}, placed on: "
            f"{self.date_ordered} from {self.supplier}. Order State: "
            f"{self.status}."
        )
