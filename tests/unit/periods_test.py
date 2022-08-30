"""Contains the classes and test which test the periods module.

Classes:
    Test_PeriodsModule: Contains all unit tests for the periods module.
    
    Test_PeriodAttributes: Contains all unit tests for Period's attributes.
    
    Test_PeriodMethods: Contains all unit tests for the Period Class' methods.
"""

from narcotics_tracker import database, periods


class Test_PeriodsModule:
    """Contains all unit tests for the periods module.

    Behaviors Tested:
        - Periods module can be accessed.
        - Method return_table_creation_query returns correct string.
        - Method return_periods returns all reporting_periods.
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
            STARTING_DATE INTEGER,                
            ENDING_DATE INTEGER,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""

        assert periods.return_table_creation_query() == expected_query

    def test_return_periods_returns_expected_reporting_periods(
        self, test_period, reset_database
    ) -> None:
        """Tests that the show method returns the expected reporting periods.

        Loads and saves test_period. Calls periods.show().

        Asserts that periods.show returns expected data.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(periods.return_table_creation_query())

        test_period = test_period
        test_period.save(db)
        periods_list, _ = periods.return_periods(db)
        assert (
            "Reporting Period 9001. Started on: 2000-12-31 19:00:00. Ends on: 2100-06-29 20:00:00"
            in periods_list
        )


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

        Asserts that test_period.starting_date is '978307200'.
        """
        test_period = test_period

        assert test_period.starting_date == 978307200

    def test_ending_date_returns_correct_value(self, test_period) -> None:
        """Tests that the ending_date attributes returns the correct value.

        Loads test_period.

        Asserts that test_period.ending_date is '4117996800'
        """
        test_period = test_period

        assert test_period.ending_date == 4117996800

    def test_created_date_returns_correct_value(self, test_period) -> None:
        """Tests that the created_date attributes returns the correct value.

        Loads test_period.

        Asserts that test_period.created_date is '1659312000'
        """
        test_period = test_period

        assert test_period.created_date == 1659312000

    def test_modified_date_returns_correct_value(self, test_period) -> None:
        """Tests that the modified_date attributes returns the correct value.

        Loads test_period.

        Asserts that test_period.modified_date is '1659312000'
        """
        test_period = test_period

        assert test_period.modified_date == 1659312000

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
        - __repr__ returns correct string.
        - Can save ReportingPeriod to database.
        - Can update ReportingPeriod starting date.
        - Can update ReportingPeriod ending date.
        - return_attributes returns the correct values.
        - Can delete reporting period from database.
    """

    def test___init___sets_attributes_correctly(self, test_period) -> None:
        """Tests the initializer sets the objects attributes correctly.

        Loads test_period.

        Asserts that period_id, starting_date, and ending_date attributes are
        set to the expected values.
        """
        test_period = test_period

        assert (
            test_period.period_id == 9001
            and test_period.starting_date == 978307200
            and test_period.ending_date == 4117996800
        )

    def test___repr___returns_expected_string(self, test_period) -> None:
        """Tests that __repr__ returns correct string.

        Loads test_period. Calls str(test_period).

        Asserts that str(test_med) returns:
            "
        """
        test_period = test_period

        assert str(test_period) == (
            "Reporting Period 9001. Started on: 2000-12-31 19:00:00. Ends on: 2100-06-29 20:00:00."
        )

    def test_can_save_reporting_period_to_database(
        self, test_period, reset_database
    ) -> None:
        """Tests that reporting periods can be saved to the database.

        Loads test_period. Calls test_period.save. Calls db.return_data()
        using the period_id of '9001'.

        Asserts that returned data has starting_date value of '02-29-0001'.
        """
        test_period = test_period

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(periods.return_table_creation_query())

        test_period.save(db)

        data = db.return_data(
            """SELECT starting_date FROM reporting_periods WHERE period_id = '9001'"""
        )

        assert data[0][0] == 978307200

    def test_return_attributes(self, test_period):
        """Tests that the reporting period data is correctly returned.

        Loads test_period. Calls test_period.return_attributes().

        Asserts values returned are expected values.
        """
        test_period = test_period
        assert test_period.return_attributes() == (
            9001,
            978307200,
            4117996800,
            1659312000,
            1659312000,
            "Cinder",
        )

    def test_can_update_starting_date(self, test_period, reset_database) -> None:
        """Tests that the reporting period's starting date can be updated.

        Loads test_period. Updates starting date to '2022-12-25 00:00:00'. Queries the
        starting date for the period_id of 9001.

        Asserts that test_period.starting_date is '2022-12-25 00:00:00'.
        """
        test_period = test_period

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(periods.return_table_creation_query())
        test_period.save(db)

        test_period.update_starting_date("2022-12-25 00:00:00", db)

        data = db.return_data(
            """SELECT starting_date FROM reporting_periods WHERE period_id = 9001"""
        )
        assert data[0][0] == 1671926400

    def test_can_update_ending_date(self, test_period, reset_database) -> None:
        """Tests that the reporting period's ending date can be updated.

        Loads test_period. Updates ending date to '2011-09-11'. Queries the
        ending date for the period_id of 9001.

        Asserts that test_period.ending_date is '2011-09-11'.
        """
        test_period = test_period

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(periods.return_table_creation_query())
        test_period.save(db)

        test_period.update_ending_date("2011-09-11", db)

        data = db.return_data(
            """SELECT ending_date FROM reporting_periods WHERE period_id = 9001"""
        )
        assert data[0][0] == 1315699200

    def test_can_delete_reporting_period_from_database(
        self, test_period, reset_database
    ):
        """Tests that reporting periods can be deleted from the database.

        Loads test_period. Saves it to database. Then deletes it. Gets data from
        reporting_periods table.

        Asserts data is empty.
        """
        test_period = test_period

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(periods.return_table_creation_query())

        test_period.save(db)
        test_period.delete(db)

        data = db.return_data("""SELECT * FROM reporting_periods""")
        assert data == []
