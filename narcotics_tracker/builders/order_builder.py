"""Contains the concrete builder for the order class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    OrderBuilder: Builds and returns order objects.
"""

from narcotics_tracker.builders import order_builder_template
from narcotics_tracker import order


class OrderBuilder(order_builder_template.Order):
    """Builds and returns order objects.

    Initializer:

        def __init__(self) -> None:

            Initializes the order builder. Sets all attributes to None.

    Instance Methods:

        set_order_id: Sets the order's id number.

        set_name: Sets the order's name.

        set_code: Sets the unique code for the order.

        set_container: Sets the order's container type.

        set_fill_amount: Sets the order's fill amount.

        set_dose_and_unit: Sets the order's dose and unit.

        set_concentration: Sets the order's concentration.

        set_status: Sets the order's status.

        set_created_date: Sets the order's created date.

        set_modified_date: Sets the order's modified date.

        set_modified_by: Sets the order's modified by property.

        calculate_concentration: Calculates order's concentration.

    Exceptions:

        TypeError: Raised when an enum type is not valid.
    """

    def __init__(self) -> None:
        """Initializes the order builder. Sets all attributes to None."""
        self.order_id = None
        self.po_number = None
        self.date_ordered = None
        self.medication_code = None
        self.containers_amount = None
        self.supplier = None
        self.supplier_order_number = None
        self.dea_form_number = None
        self.date_received = None
        self.packages_received = None
        self.comment = None
        self.status = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def set_order_id(self, order_id: int = None) -> None:
        """Sets the order's id number. Should not be called by the user.

        This method will set the order's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the order is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            order_id (int): The order's unique id. Defaults to None.
        """
        self.order_id = order_id

    def set_po_number(self, po_number: str) -> None:
        """Sets the order's po_number.

        Args:
            po_number (str): The Purchase Order Number. Defaults to None.
        """
        self.po_number = po_number

    def set_date_ordered(self, date_ordered: str) -> None:
        """Sets the date the order was placed.

        Args:
            date_ordered (str): Date order was placed. Defaults to None.
        """
        self.date_ordered = date_ordered

    def set_medication_code(self, medication_code: str) -> None:
        """Sets the medication_code for the medications ordered.
        Args:
            medication_code (str): Unique identifier for a specific
                medication.
        """
        self.medication_code = medication_code

    def set_containers_amount(self, containers_amount: int) -> None:
        """Sets the amount of medication containers ordered.

        Args:
            containers_amount (int): The amount of containers ordered.
                Defaults to None.
        """
        self.containers_amount = containers_amount

    def set_supplier(self, supplier: str) -> None:
        """Sets the supplier name for the order

        Args:
            supplier (str): The name of the supplier for the order. Defaults
                to None.
        """
        self.supplier = supplier

    def set_supplier_order_number(self, supplier_order_number: str) -> None:
        """Sets the order number assigned by the supplier.

        Args:
            supplier_order_number (str): The order number assigned by the
                supplier. Defaults to None.
        """
        self.supplier_order_number = supplier_order_number

    def set_dea_form_number(self, dea_form_number: str) -> None:
        """Sets the dea (or 222) for number used to place the order.

        Args:
            dea_form_number (str): The order of the dea (222) form used to
                place the order. Defaults to None.
        """
        self.dea_form_number = dea_form_number

    def set_date_received(self, date_received: str) -> None:
        """Sets the date when the order was received.

        Args:
            date_received (str): The date which the order was received.
                Defaults to None.
        """
        self.date_received = date_received

    def set_packages_received(self, packages_received: int) -> None:
        """Sets the number of packaged received as part of the order.

        Args:
            packages_received (str): The number of packages received. Defaults
                to None.
        """
        self.packages_received = packages_received

    def set_comment(self, comment: str) -> None:
        """Sets the order's comments.

        Args:
            comments (str): Additional information about the order.
                Defaults to None.
        """
        self.comment = comment

    def set_status(self, status: str) -> None:
        """Sets the order's status via the enum MedicationStatus class.

        Args:
            status (str): The status of the
                order.
        """
        self.status = status

    def set_created_date(self, created_date: str) -> None:
        """Sets the order's created date. Should not be called users.

        This method will set the order's created date. The created date
        is set automatically when the order is saved in the database.
        This method is useful in setting the created date when loading a
        order from the database. It will override any created date set in
        the database table. Users should not call this method.

        Args:
            created_date (str): The date the order was created.
        """
        self.created_date = created_date

    def set_modified_date(self, modified_date: str) -> None:
        """Sets the order's modified date. Should not be called the user.

        This method will set the order's modified by date. The modified
        by date is set automatically when the order is updated in the
        database. This method is useful in setting the modified_by date when
        loading a order from the database. It will override any modified
        by date set in the database table. Users should not call this method.

        Args:
            modified_date (str): The date the order was last modified.
        """
        self.modified_date = modified_date

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who last modified the order.

        Args:
            modified_by (str): The identifier of the user who last modified
                the order."""
        self.modified_by = modified_by

    def set_all_properties(self, properties: dict) -> None:
        """Sets all properties of the medication.

        Args:
            properties (dict): The properties of the order. Dictionary
                keys are formatted as the order's property names.
        """
        self.set_order_id(properties["order_id"])
        self.set_po_number(properties["po_number"])
        self.set_date_ordered(properties["date_ordered"])
        self.set_medication_code(properties["medication_code"])
        self.set_containers_amount(properties["containers_amount"])
        self.set_supplier(properties["supplier"])
        self.set_supplier_order_number(properties["suppler_order_number"])
        self.set_dea_form_number(properties["dea_form_number"])
        self.set_date_received(properties["date_received"])
        self.set_packages_received(properties["packages_received"])
        self.set_comment(properties["comment"])
        self.set_status(properties["status"])
        self.set_created_date(properties["created_date"])
        self.set_modified_date(properties["modified_date"])
        self.set_modified_by(properties["modified_by"])

    def build(self) -> "order.Order":
        """Returns the order object. Assigns the order's properties.

        This is the last method to be called as part of the building process.
        It will return the order object with all of its properties set.
        The concentration is calculated using the calculate_concentration
        method.

        Returns:
            order.order: The order object.
        """

        return order.Order(self)
