"""Contains the classes and tests which test the units module.

Classes:

    Test_UnitsModule: Contains all unit tests for the units module.

    Test_UnitAttributes: Contains unit tests for Unit's attributes.

    Test_UnitsMethods: Contains unit tests for the Unit's methods.
"""

from persistence import database

from narcotics_tracker import units


class Test_UnitsModule:
    """Contains all unit tests for the Units module.

    Behaviors Tested:
        - Units module can be accessed.
        - Method return_table_creation_query returns correct string.
        - Method return_units returns all units.
        - Method parse_unit_data returns correct dictionary and values.
    """

    def test_units_module_can_be_accessed(self) -> None:
        """Tests that the units module exists and can be accessed.

        Asserts that calling units.__doc__ does not return 'None'.
        """
        assert units.__doc__ != None

    def test_return_table_creation_query_returns_expected_string(self) -> None:
        """Tests that the table_creation_query returns the correct string.

        Calls units.return_table_creation_query().

        Asserts that expected_query is returned.
        """
        expected_query = """CREATE TABLE IF NOT EXISTS units (
            UNIT_ID INTEGER PRIMARY KEY,
            UNIT_CODE TEXT UNIQUE,                
            UNIT_NAME TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""

        assert units.return_table_creation_query() == expected_query

    def test_return_units_returns_expected_units(
        self, test_unit, reset_database
    ) -> None:
        """Tests that the return_units method returns the expected units.

        Loads and saves test_unit. Creates and save. 2nd_unit
        Calls units.return_units().

        Asserts that units.return_units() returns expected data.
        """
        with database.Database("test_database.db") as db:
            db.create_table(units.return_table_creation_query())

            test_unit = test_unit

            test_unit.save(db)

            units_list = units.return_units(db)

        assert "Unit Number 821: Tina. Code: 'tn'." in units_list[0]

    def test_parse_unit_data_returns_correct_values(
        self, reset_database, test_unit
    ) -> None:
        """Tests if parse_unit_data returns dictionary with correct data.

        Resets the database. Creates units table. Builds and saves
        test_unit to database. Queries database for unit data and
        calls the parser.

        Asserts that dictionary returned assigns the correct data to correct
        keys.
        """
        with database.Database("test_database.db") as db:
            db.create_table(units.return_table_creation_query())

            test_unit = test_unit
            test_unit.save(db)
            data = test_unit.read(db)
            dictionary = units.parse_unit_data(data)

        assert (
            dictionary["unit_id"] == 821
            and dictionary["unit_code"] == "tn"
            and dictionary["unit_name"] == "Tina"
        )


class Test_UnitAttributes:
    """Contains all unit tests for the Unit Class' attributes.

    Behaviors Tested:
        - Unit class can be accessed.
        - Unit objects can be created.
        - unit_id attribute returns correct value.
        - unit_code attribute returns correct value.
        - unit_name attribute returns correct value.
        - created_date attribute returns correct value.
        - modified_date attribute returns correct value.
        - modified_by attribute returns correct value.
    """

    def test_unit_class_can_be_accessed(self) -> None:
        """Tests that the Unit Class exists and can be accessed.

        Asserts that calling Unit.__doc__ does not return 'None'.
        """
        assert units.Unit.__doc__ != None

    def test_can_create_unit_objects(self, test_unit) -> None:
        """Tests that objects can be created from the Unit Class.

        Loads test_unit.

        Asserts that test_unit is an instance of the Unit Class.
        """
        test_unit = test_unit

        assert isinstance(test_unit, units.Unit)

    def test_unit_id_returns_correct_value(self, test_unit) -> None:
        """Tests that the unit_id attribute returns the correct value.

        Loads test_unit.

        Asserts test_unit.unit_id is '821'.
        """
        test_unit = test_unit

        assert test_unit.unit_id == 821

    def test_unit_code_returns_correct_value(self, test_unit) -> None:
        """Tests that the unit_code attribute returns the correct value.

        Loads test_unit.

        Asserts that test_unit.unit_code is 'tn'.
        """
        test_unit = test_unit

        assert test_unit.unit_code == "tn"

    def test_unit_name_returns_correct_value(self, test_unit) -> None:
        """Tests that the unit_name attributes returns the correct value.

        Loads test_unit.

        Asserts that test_unit.unit_name is 'Tina'
        """
        test_unit = test_unit

        assert test_unit.unit_name == "Tina"

    def test_created_date_returns_correct_value(self, test_unit) -> None:
        """Tests that the created_date attributes returns the correct value.

        Loads test_unit.

        Asserts that test_unit.created_date is '08-26-2022'
        """
        test_unit = test_unit

        assert test_unit.created_date == database.return_datetime("2022-08-01 00:00:00")

    def test_modified_date_returns_correct_value(self, test_unit) -> None:
        """Tests that the modified_date attributes returns the correct value.

        Loads test_unit.

        Asserts that test_unit.modified_date is '08-01-2022'
        """
        test_unit = test_unit

        assert test_unit.modified_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_by_returns_correct_value(self, test_unit) -> None:
        """Tests that the modified_by attributes returns the correct value.

        Loads test_unit.

        Asserts that test_unit.modified_by is 'Denna'
        """
        test_unit = test_unit

        assert test_unit.modified_by == "Denna"


class Test_UnitMethods:
    """Contains all unit tests for the Unit Class' methods.

    Behaviors Tested:
        - __init__ sets attributes correctly.
        - __repr__ returns correct string.
        - Can save Unit to database.
        - Can read Unit data from database.
        - Can load Unit from database.
        - Can update Unit in database.
        - Can delete Unit from database.
        - return_attributes returns the correct values.
    """

    def test___init___sets_attributes_correctly(self, test_unit) -> None:
        """Tests that  the initializer sets the objects attributes correctly.

        Loads test_unit.

        Asserts that unit_id, unit_code, and unit_name attributes are set to
        the expected values.
        """
        test_unit = test_unit

        assert (
            test_unit.unit_id == 821
            and test_unit.unit_code == "tn"
            and test_unit.unit_name == "Tina"
        )

    def test___repr___returns_expected_string(self, test_unit) -> None:
        """Tests that __repr__ returns correct string.

        Loads test_unit. Calls str(test_unit).

        Asserts that str(test_unit) returns:
            'Unit Test. Code: TEST. Used for testing the EventType Class.'
        """
        test_unit = test_unit
        expected = f"Unit Number 821: Tina. Code: 'tn'."

        assert str(test_unit) == expected

    def test_can_save_unit_to_database(self, test_unit, reset_database) -> None:
        """Tests that Units can be saved to the database.

        Loads test_unit. Calls test_unit.save. Calls db.return_data()
        using the unit_id of '821'.

        Asserts that returned data has unit_code value of 'tn'.
        """
        test_unit = test_unit

        with database.Database("test_database.db") as db:
            db.create_table(units.return_table_creation_query())

            test_unit.save(db)

            data = db.return_data(
                """SELECT unit_code FROM units WHERE unit_id = '821'"""
            )

            assert data[0][0] == "tn"

    def test_can_read_unit_from_database(self, reset_database, test_unit) -> None:
        """Tests to see if the units's data can be returned from database.

        Resets the database. Creates units table. Builds and saves
        test_unit. Calls test_unit.read().

        Asserts that data returned matches expected values.
        """
        with database.Database("test_database.db") as db:
            db.create_table(units.return_table_creation_query())

            test_unit = test_unit
            test_unit.save(db)

            data = test_unit.read(db)[0]
            expected = [821, "tn", "Tina"]

        assert (
            data[0] == expected[0] and data[1] == expected[1] and data[2] == expected[2]
        )

    def test_can_load_unit_from_database(self, reset_database, test_unit) -> None:
        """Tests to see if a Unit Object can be loaded from data.

        Loads and saves test_unit. Creates loaded_unit from data.

        Asserts that test_unit and loaded_unit return identical
        attributes.
        """
        with database.Database("test_database.db") as db:
            db.create_table(units.return_table_creation_query())

            test_unit = test_unit
            test_unit.save(db)

            loaded_unit = db.load_unit("tn")

        assert (
            loaded_unit.return_attributes()[0] == test_unit.return_attributes()[0]
            and loaded_unit.return_attributes()[1] == test_unit.return_attributes()[1]
            and loaded_unit.return_attributes()[2] == test_unit.return_attributes()[2]
        )

    def test_can_update_unit_in_database(self, reset_database, test_unit) -> None:
        """Tests to see if Unit data can be updated.

        Resets database. Creates Unit Table. Builds and saves test_unit to
        database. Loads test_unit as loaded_unit. Changes Name and updates
        database. Queries the data.

        Asserts that the returned data has the new name.
        """
        with database.Database("test_database.db") as db:
            db.create_table(units.return_table_creation_query())

            test_unit = test_unit
            test_unit.save(db)

            test_unit.unit_name = "Not Tina"

            test_unit.update(db)

            data = db.return_data(
                """SELECT unit_name FROM units WHERE unit_code = 'tn'"""
            )[0][0]

        assert data == "Not Tina"

    def test_can_delete_unit_from_database(self, test_unit, reset_database) -> None:
        """Tests that Units can be deleted from the database.

        Loads test_unit. Saves it to database. Then deletes it. Gets data from
        units table.

        Asserts data is empty.
        """
        test_unit = test_unit

        with database.Database("test_database.db") as db:
            db.create_table(units.return_table_creation_query())

            test_unit.save(db)
            test_unit.delete(db)

            data = db.return_data("""SELECT * FROM units""")
        assert data == []

    def test_return_attributes(self, test_unit) -> None:
        """Tests that the Units data is correctly returned.

        Loads test_unit. Calls test_unit.return_attributes().

        Asserts values returned are expected values.
        """
        test_unit = test_unit
        expected = (
            821,
            "tn",
            "Tina",
            database.return_datetime("2022-08-01 00:00:00"),
            database.return_datetime("2022-08-01 00:00:00"),
            "Denna",
        )

        assert test_unit.return_attributes() == expected
