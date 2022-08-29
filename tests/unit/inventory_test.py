"""Contains the classes that unit test the inventory module.

Classes:

    Test_InventoryModule: Contains the unit tests for the inventory module.

    Test_AdjustmentAttributes: Contains unit tests for the class' attributes.
"""

from narcotics_tracker import inventory


class Test_InventoryModule:
    """Contains the unit tests for the inventory module.

    Behaviors Tested:
        - Inventory module can be accessed.
        - Method return_table_creation_query returns expected string.

    """

    def test_can_access_inventory_module(self) -> None:
        """Tests the the inventory module exists and can be accessed.

        Asserts that inventory.__doc__ does not return nothing.
        """
        assert inventory.__doc__ != None

    def test_return_table_creation_query_returns_expected_string(self) -> None:
        """Tests that the return_table_creation_query returns as expected.

        Asserts that method returns: 'CREATE TABLE IF NOT EXISTS inventory (
            INVENTORY_ID INTEGER PRIMARY KEY,
            EVENT_DATE TEXT,
            EVENT_CODE TEXT FOREIGN KEY,
            MEDICATION_CODE TEXT,
            QUANTITY_IN_MCG REAL,
            REPORTING_PERIOD_ID INTEGER,
            REFERENCE_ID TEXT,
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT,
            FOREIGN KEY (EVENT_CODE) REFERENCES event_types (EVENT_CODE)
            ON UPDATE CASCADE ON DELETE RESTRICT,
            FOREIGN KEY (MEDICATION_CODE) REFERENCES medication (MEDICATION_CODE)
            ON UPDATE CASCADE ON DELETE RESTRICT,
            FOREIGN KEY (REPORTING_PERIOD_ID) REFERENCES reporting_periods (PERIOD_ID)
            ON UPDATE CASCADE ON DELETE RESTRICT,
            )'
        """
        assert (
            inventory.return_table_creation_query()
            == """CREATE TABLE IF NOT EXISTS inventory (
            INVENTORY_ID INTEGER PRIMARY KEY,
            EVENT_DATE TEXT,                
            EVENT_CODE TEXT FOREIGN KEY,
            MEDICATION_CODE TEXT,
            QUANTITY_IN_MCG REAL,
            REPORTING_PERIOD_ID INTEGER,
            REFERENCE_ID TEXT,
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT,
            FOREIGN KEY (EVENT_CODE) REFERENCES event_types (EVENT_CODE) 
            ON UPDATE CASCADE ON DELETE RESTRICT,
            FOREIGN KEY (MEDICATION_CODE) REFERENCES medication (MEDICATION_CODE)
            ON UPDATE CASCADE ON DELETE RESTRICT,
            FOREIGN KEY (REPORTING_PERIOD_ID) REFERENCES reporting_periods (PERIOD_ID)
            ON UPDATE CASCADE ON DELETE RESTRICT,
            )"""
        )


class Test_AdjustmentAttributes:
    """Contains unit tests for the Adjustment Class' attributes.

    Behaviors Tested:
        - Adjustments class can be accessed.
    """

    def test_can_access_adjustment_class(self) -> None:
        """Tests that the Adjustment class exists and can be accessed.

        Asserts that inventory.Adjustment.__doc__ does not return nothing.
        """
        assert inventory.Adjustment.__doc__ != None
