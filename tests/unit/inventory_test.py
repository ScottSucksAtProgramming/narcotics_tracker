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
        - Adjustments return expected adjustment_ID.
        - Adjustments return expected adjustment_date.
        - Adjustments return expected event_code.
        - Adjustments return expected medication_code.
        - Adjustments return expected amount_in_preferred_unit
        - Adjustments return expected amount_in_mcg.
        - Adjustments return expected reporting_period_id.
        - Adjustments return expected reference_id.
        - Adjustments return expected created_date.
        - Adjustments return expected modified_date.
        - Adjustments return expected modified_by.
        - Adjustments can be edited.
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

    def test_adjustments_return_expected_event_code(self, test_adjustment) -> None:
        """Tests that the correct event_code is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.event_code is WASTE."""
        test_adjustment = test_adjustment

        assert test_adjustment.event_code == "WASTE"

    def test_adjustments_return_expected_medication_code(self, test_adjustment) -> None:
        """Tests that the correct medication_code is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.medication_code is morphine."""
        test_adjustment = test_adjustment

        assert test_adjustment.medication_code == "morphine"

    def test_adjustments_return_expected_amount_in_preferred_unit(
        self, test_adjustment
    ) -> None:
        """Tests that the correct amount_in_preferred_unit is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.amount_in_preferred_unit is 1."""
        test_adjustment = test_adjustment

        assert test_adjustment.amount_in_preferred_unit == 1

    def test_adjustments_return_expected_amount_in_mcg(self, test_adjustment) -> None:
        """Tests that the correct amount_in_mcg is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.amount_in_mcg is -1000."""
        test_adjustment = test_adjustment

        assert test_adjustment.amount_in_mcg == -1000

    def test_adjustments_return_expected_reporting_period_id(
        self, test_adjustment
    ) -> None:
        """Tests that the correct reporting_period_id is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.reporting_period_id is 2."""
        test_adjustment = test_adjustment

        assert test_adjustment.reporting_period_id == 2

    def test_adjustments_return_expected_reference_id(self, test_adjustment) -> None:
        """Tests that the correct reference_id is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.reference_id is TEST ID."""
        test_adjustment = test_adjustment

        assert test_adjustment.reference_id == "TEST ID"

    def test_adjustments_return_expected_created_date(self, test_adjustment) -> None:
        """Tests that the correct created_date is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.created_date is Yesterday."""
        test_adjustment = test_adjustment

        assert test_adjustment.created_date == "Yesterday"

    def test_adjustments_return_expected_modified_date(self, test_adjustment) -> None:
        """Tests that the correct modified_date is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.modified_date is Tomorrow."""
        test_adjustment = test_adjustment

        assert test_adjustment.modified_date == "Tomorrow"

    def test_adjustments_return_expected_modified_by(self, test_adjustment) -> None:
        """Tests that the correct modified_by is returned.

        Loads test_adjustment.

        Asserts that test_adjustment.modified_by is Ambrose."""
        test_adjustment = test_adjustment

        assert test_adjustment.modified_by == "Ambrose"

    def test_adjustment_attributes_can_be_edited(self, test_adjustment) -> None:
        """Tests that an Adjustment's attributes can be edited.

        Loads test_adjustment. Changes test_adjustment.modified_by.

        Asserts that test_adjustment.modified_by equals new value.
        """
        test_adjustment = test_adjustment

        test_adjustment.modified_by = "Me, Duh!"

        assert test_adjustment.modified_by == "Me, Duh!"


class Test_AdjustmentMethods:
    """Contains all unit tests for the methods of the Adjustment class.

    Behaviors Tested:
        - __repr__ returns correct string.
        - Adjustments can be saved to inventory table.
        - Adjustment data can be updated.
        - Adjustments can be deleted from database.
        - Method return_attributes returns the correct information.
    """

    def test__repr___returns_correct_string(self, test_adjustment):
        """Tests that __repr__ returns correct string.

        Loads test_adjustment. Calls str(test_adjustment).


        Asserts that str(test_adjustment) returns:
            "Adjustment Number -300 occurred at 2022-08-01 10:00:00. 1 mg of Morphine was with
        """
        test_adjustment = test_adjustment
        assert str(test_adjustment) == (
            f"Medication Object 1 for Unobtanium with code Un-69420-9001. "
            f"Container type: Vial. Fill amount: 9001 ml. Dose: 69420.0 mg. "
            f"Concentration: 7.712476391512054. Status: Discontinued. Created "
            f"on 01-02-1986. Last modified on 08-09-2022 by Kvothe."
        )
