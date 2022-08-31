"""Contains the classes that unit test the inventory module.

Classes:

    Test_InventoryModule: Contains the unit tests for the inventory module.

    Test_AdjustmentAttributes: Contains unit tests for the class' attributes.
"""

from narcotics_tracker import database, inventory


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

        Asserts that method returns the expected string.
        """
        assert (
            inventory.return_table_creation_query()
            == """CREATE TABLE IF NOT EXISTS inventory (
            INVENTORY_ID INTEGER PRIMARY KEY,
            EVENT_DATE TEXT,
            EVENT_CODE TEXT,
            MEDICATION_CODE TEXT,
            QUANTITY_IN_MCG REAL,
            REPORTING_PERIOD_ID INTEGER,
            REFERENCE_ID TEXT,
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT,
            FOREIGN KEY (EVENT_CODE) REFERENCES event_types (EVENT_CODE) ON UPDATE CASCADE ON DELETE RESTRICT,
            FOREIGN KEY (MEDICATION_CODE) REFERENCES medications (MEDICATION_CODE) ON UPDATE CASCADE ON DELETE RESTRICT,
            FOREIGN KEY (REPORTING_PERIOD_ID) REFERENCES reporting_periods (PERIOD_ID) ON UPDATE CASCADE ON DELETE RESTRICT
            )"""
        )


class Test_AdjustmentAttributes:
    """Contains unit tests for the Adjustment Class' attributes.

    Behaviors Tested:
        - Adjustments class can be accessed.
        - Adjustments return expected database_connection.
        - Adjustments return expected Adjustment_ID.
        - Adjustments return expected adjustment_date.
        #! - Adjustments return expected name.
        #! - Adjustments return expected container_type.
        #! - Adjustments return expected fill_amount.
        #! - Adjustments return expected dose.
        #! - Adjustments return expected preferred_unit.
        #! - Adjustments return expected concentration.
        #! - Adjustments return expected created_date.
        #! - Adjustments return expected modified_date.
        #! - Adjustments return expected modified_by.
        #! - Adjustments can be edited.
    """

    def test_can_access_adjustment_class(self) -> None:
        """Tests that the Adjustment class exists and can be accessed.

        Asserts that inventory.Adjustment.__doc__ does not return nothing.
        """
        assert inventory.Adjustment.__doc__ != None

    def test_adjustments_return_expected_database_connection(
        self, test_adjustment
    ) -> None:
        """Tests that the correct database_connection is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.database_connection is not None."""
        test_adjustment = test_adjustment

        assert test_adjustment.database_connection != None

    def test_adjustments_return_expected_adjustment_id(self, test_adjustment) -> None:
        """Tests that the correct adjustment_id is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.adjustment_id is -300."""
        test_adjustment = test_adjustment

        assert test_adjustment.adjustment_id == -300

    def test_adjustments_return_expected_adjustment_date(self, test_adjustment) -> None:
        """Tests that the correct adjustment_date is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.adjustment_date is 1659348000."""
        test_adjustment = test_adjustment

        assert test_adjustment.adjustment_date == database.return_datetime(
            "2022-08-01 10:00:00"
        )
