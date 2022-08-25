"""Contains the classes and test which test the periods module."""

from narcotics_tracker import periods


class Test_PeriodsModule:
    """Contains all unit tests for the periods module.

    Behaviors Tested:
        - Periods module can be accessed.
        - return_table_creation_query returns correct string.
    """

    def test_periods_module_can_be_accessed(self) -> None:
        """Tests that the periods module exists and can be accessed.

        Asserts that calling periods.__doc__ does not return 'None'.
        """
        assert periods.__doc__ != None

    def test_return_table_creation_query_returns_expected_string(self) -> None:
        """Tests that the table_creation_query returns the correct string.

        Calls periods.return_table_creation_query().

        Asserts that expected_query is returned.
        """
        expected_query = """CREATE TABLE IF NOT EXISTS reporting_periods (
            PERIOD_ID INTEGER PRIMARY KEY,
            STARTING_DATE TEXT,                
            ENDING_DATE TEXT,
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT
            )"""

        assert periods.return_table_creation_query() == expected_query


class Test_PeriodAttributes:
    """Contains all unit tests for the Period Class' attributes.

    Behaviors Tested:
        - Period class can be accessed.
        - Period objects can be created.
        - period_id attribute returns correct value.
        - starting_date attribute returns correct value.
        - ending_date attribute returns correct value.
        - created_date attribute returns correct value.
        - modified_date attribute returns correct value.
        - modified_by attribute returns correct value.
    """

    def test_period_class_can_be_accessed(self) -> None:
        """Tests that the Period Class exists and can be accessed.

        Asserts that calling Period.__doc__ does not return 'None'.
        """
        assert periods.ReportingPeriod.__doc__ != None

    def test_can_create_period_objects(self, test_period) -> None:
        """Tests that objects can be created from the Period Class.

        Loads test_period.

        Asserts that test_period is an instance of the Period Class.
        """
        test_period = test_period

        assert isinstance(test_period, periods.ReportingPeriod)

    def test_period_id_returns_correct_value(self, test_period) -> None:
        """Tests that the period_id attribute returns the correct value.

        Loads test_period. Sets the period_id to '9001'.

        Asserts test_period.period_id is '9001'.
        """
        test_period = test_period
        test_period.period_id = 9001

        assert test_period.period_id == 9001

    def test_starting_date_returns_correct_value(self, test_period) -> None:
        """Tests that the starting_date attribute returns the correct value.

        Loads test_period.

        Asserts that test_period.starting_date is '02-29-0001'.
        """
        test_period = test_period

        assert test_period.starting_date == "02-29-0001"

    def test_ending_date_returns_correct_value(self, test_period) -> None:
        """Tests that the ending_date attributes returns the correct value.

        Loads test_period.

        Asserts that test_period.ending_date is '01-35-0000'
        """
        test_period = test_period

        assert test_period.ending_date == "01-35-0000"

    def test_created_date_returns_correct_value(self, test_period) -> None:
        """Tests that the created_date attributes returns the correct value.

        Loads test_period.

        Asserts that test_period.created_date is '08-26-2022'
        """
        test_period = test_period

        assert test_period.created_date == "08-26-2022"

    def test_modified_date_returns_correct_value(self, test_period) -> None:
        """Tests that the modified_date attributes returns the correct value.

        Loads test_period.

        Asserts that test_period.modified_date is '08-01-2022'
        """
        test_period = test_period

        assert test_period.modified_date == "08-01-2022"

    def test_modified_by_returns_correct_value(self, test_period) -> None:
        """Tests that the modified_by attributes returns the correct value.

        Loads test_period.

        Asserts that test_period.modified_by is 'Cinder'
        """
        test_period = test_period

        assert test_period.modified_by == "Cinder"


class Test_PeriodMethods:
    """Contains all unit tests for the Period Class' methods.

    Behaviors Tested:
        - __init__ sets attributes correctly.
    """

    def test___init___sets_attributes_correctly(self, test_period) -> None:
        """Tests the initializer sets the objects attributes correctly.

        Loads test_period.

        Asserts that period_id, starting_date, and ending_date attributes are
        set to the expected values.
        """
        test_period = test_period

        assert (
            test_period.period_id == None
            and test_period.starting_date == "02-29-0001"
            and test_period.ending_date == "01-35-0000"
        )
