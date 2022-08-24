"""Contains Test_Order class used for testing the order module.

Classes:

    Test_OrderModule: Contains all unit tests for the order module.

    Test_Order: Contains all unit tests for the Order class.
"""

from narcotics_tracker import order


class Test_OrderModule:
    """Contains all unit tests for the Order module.

    Behaviors Tested:
        - Order module can be accessed.
    """

    def test_can_access_order_module(self):
        """Tests that the order module can be accessed.

        Asserts that order.__doc__ does not return 'None'.
        """
        assert order.__doc__ != None


class Test_Order:
    """Contains all unit tests for the Order class.

    Behaviors Tested:
        - Order class can be accessed.
    """

    def test_can_access_Order_class(self):
        """Tests the the Order class can be accessed.

        Asserts that order.Order.__doc__ does not return 'None'.
        """
        assert order.Order.__doc__ != None
