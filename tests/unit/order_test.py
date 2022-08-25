"""Contains Test_Order class used for testing the order module.

Classes:

    Test_OrderModule: Tests the order module.

    Test_OrderAttributes: Tests the attributes of the Order class.

    Test_OrderMethods: Tests the methods of the Order class.
"""

from narcotics_tracker import order


class Test_OrderModule:
    """Contains all unit tests for the Order module.

    Behaviors Tested:
        - Order module can be accessed.
    """

    def test_can_access_order_module(self) -> None:
        """Tests that the order module can be accessed.

        Asserts that order.__doc__ does not return 'None'.
        """
        assert order.__doc__ != None


class Test_OrderAttributes:
    """Contains all unit tests for the attributes of the Order class.

    Behaviors Tested:
        - Order class can be accessed.
        - Order objects can be created.
        - Orders return expected order_id.
        - Orders return expected purchase_order_number.
        - Orders return expected date_ordered.
        - Orders return expected medication_code.
        - Orders return expected containers_ordered.
        - Orders return expected supplier.
        - Orders return expected suppler_order_number.
        - Orders return expected 222_form_number.
        - Orders return expected date_received.
        - Orders return expected packaged_received.
        - Orders return expected comments.
        - Orders return expected status.
        - Orders return expected created_date.
        - Orders return expected modified_date.
        - Orders return expected modified_by.
        - Orders can be edited.
    """

    def test_can_access_Order_class(self) -> None:
        """Tests the the Order class can be accessed.

        Asserts that order.Order.__doc__ does not return 'None'.
        """
        assert order.Order.__doc__ != None

    def test_order_objects_can_be_created(self, test_order) -> None:
        """Tests that order objects can be created from the Order class.

        Loads test_order from conftest.

        Asserts that test_order is an instance of 'order.Order'.
        """
        test_order = test_order

        assert isinstance(test_order, order.Order)

    def test_orders_return_expected_order_id(self, test_order) -> None:
        """Tests that the order_id is returned as expected.

        Loads test_order.

        Asserts that test_order.order_id equals '69_420'.
        """
        test_order = test_order

        assert test_order.order_id == 69_420

    def test_orders_return_expected_purchase_order_number(self, test_order) -> None:
        """Tests that the po_number is returned as expected.

        Loads test_order.

        Asserts that test_order.po_number equals '2022-ThisOne'.
        """
        test_order = test_order

        assert test_order.po_number == "2022-ThisOne"

    def test_orders_return_expected_date_ordered(self, test_order) -> None:
        """Tests that the date_ordered is returned as expected.

        Loads test_order.

        Asserts that test_order.date_ordered equals '01-02-1986'.
        """
        test_order = test_order

        assert test_order.date_ordered == "01-02-1986"

    def test_orders_return_expected_medication_code(self, test_order) -> None:
        """Tests that the medication_code is returned as expected.

        Loads test_order.

        Asserts that test_order.medication_code equals 'Un-69420-9001'.
        """
        test_order = test_order

        assert test_order.medication_code == "Un-69420-9001"

    def test_orders_return_expected_containers_amount(self, test_order) -> None:
        """Tests that the containers_amount is returned as expected.

        Loads test_order.

        Asserts that test_order.containers_amount equals '3_000_001'.
        """
        test_order = test_order

        assert test_order.containers_amount == 3_000_001

    def test_orders_return_expected_supplier(self, test_order) -> None:
        """Tests that the supplier is returned as expected.

        Loads test_order.

        Asserts that test_order.supplier equals 'Mystical Medicine'.
        """
        test_order = test_order

        assert test_order.supplier == "Mystical Medicine"

    def test_orders_return_expected_supplier_order_number(self, test_order) -> None:
        """Tests that the supplier_order_number is returned as expected.

        Loads test_order.

        Asserts that test_order.supplier_order_number equals 'BoundTree-999999'.
        """
        test_order = test_order

        assert test_order.supplier_order_number == "BoundTree-999999"

    def test_orders_return_expected_dea_form_number(self, test_order) -> None:
        """Tests that the dea_form_number is returned as expected.

        Loads test_order.

        Asserts that test_order.dea_form_number equals '11223344556677889900'.
        """
        test_order = test_order

        assert test_order.dea_form_number == "11223344556677889900"

    def test_orders_return_expected_date_received(self, test_order) -> None:
        """Tests that the date_received is returned as expected.

        Loads test_order.

        Asserts that test_order.date_received equals '13-44-2022'.
        """
        test_order = test_order

        assert test_order.date_received == "13-44-2022"

    def test_orders_return_expected_packages_received(self, test_order) -> None:
        """Tests that the packages_received is returned as expected.

        Loads test_order.

        Asserts that test_order.packages_received equals '300'.
        """
        test_order = test_order

        assert test_order.packages_received == 300

    def test_orders_return_expected_comments(self, test_order) -> None:
        """Tests that the comments is returned as expected.

        Loads test_order.

        Asserts that test_order.comments equals 'Best Order ever''.
        """
        test_order = test_order

        assert test_order.comment == "Best Order Ever."

    def test_orders_return_expected_status(self, test_order) -> None:
        """Tests that the status is returned as expected.

        Loads test_order.

        Asserts that test_order.status equals 'Forgotten'.
        """
        test_order = test_order

        assert test_order.status == "Forgotten"

    def test_orders_return_expected_created_date(self, test_order) -> None:
        """Tests that the created_date is returned as expected.

        Loads test_order.

        Asserts that test_order.created_date equals '13-44-2022'.
        """
        test_order = test_order

        assert test_order.created_date == "13-44-2022"

    def test_orders_return_expected_modified_date(self, test_order) -> None:
        """Tests that the modified_date is returned as expected.

        Loads test_order.

        Asserts that test_order.modified_date equals '13-44-2022'.
        """
        test_order = test_order

        assert test_order.modified_date == "34-44-2022"

    def test_orders_return_expected_modified_by(self, test_order) -> None:
        """Tests that the modified_by is returned as expected.

        Loads test_order.

        Asserts that test_order.modified_by equals 'Navi'.
        """
        test_order = test_order

        assert test_order.modified_by == "Navi"

    def test_orders_can_be_edited(self, test_order):
        """Tests that the orders's properties and be changed.

        Loads test_order. Changes modified_by to 'Willem'.

        Asserts that test_order.modified_by is 'Willem'.
        """
        test_order = test_order

        test_order.modified_by = "Willem"

        assert test_order.modified_by == "Willem"


class Test_OrderMethods:
    """Contains all unit tests for the methods of the Order class.

    Behaviors Tested:
        - __repr__ returns the correct string.
    """

    def test__repr___returns_correct_string(self, test_order):
        """Tests that __repr__ returns correct string.

        Loads test_order. Calls str(test_order).

        Asserts that str(test_order) returns:
            Controlled Substance Order: 2022-ThisOne, placed on: 01-02-1986 "
            "from Mystical Medicine. Order State: Forgotten.
        """
        test_order = test_order
        assert str(test_order) == (
            f"Controlled Substance Order: 2022-ThisOne, placed on: "
            f"01-02-1986 from Mystical Medicine. Order State: Forgotten."
        )
