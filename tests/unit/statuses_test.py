"""Contains the classes and tests which test the statuses module.

Classes:

    Test_StatusModule: Contains all unit tests for the statuses module.

    Test_StatusAttributes: Contains unit tests for Status' attributes.

    Test_StatusMethods: Contains unit tests for the Status' methods.
"""

from narcotics_tracker import statuses
from persistence import database


class Test_StatusModule:
    """Contains all unit tests for the Statuses module.

    Behaviors Tested:
        - Statuses module can be accessed.
        - Method return_table_creation_query returns correct string.
        - Method return_statuses returns all statuses.
        - Method parse_unit_data returns correct dictionary and values.
    """

    def test_statuses_module_can_be_accessed(self) -> None:
        """Tests that the statuses module exists and can be accessed.

        Asserts that calling statuses.__doc__ does not return 'None'.
        """
        assert statuses.__doc__ != None

    def test_return_table_creation_query_returns_expected_string(self) -> None:
        """Tests that the table_creation_query returns the correct string.

        Calls statuses.return_table_creation_query().

        Asserts that expected_query is returned.
        """
        expected_query = """CREATE TABLE IF NOT EXISTS statuses (
            STATUS_ID INTEGER PRIMARY KEY,
            STATUS_CODE TEXT UNIQUE,                
            STATUS_NAME TEXT,
            DESCRIPTION TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""

        assert statuses.return_table_creation_query() == expected_query

    def test_return_statuses_returns_expected_statuses(
        self, test_status, reset_database
    ) -> None:
        """Tests that the return_statuses method returns the expected statuses.

        Loads and saves test_status. Creates and save. 2nd_unit
        Calls statuses.return_statuses().

        Asserts that statuses.return_statuses() returns expected data.
        """
        with database.Database("test_database.db") as db:
            db.create_table(statuses.return_table_creation_query())

            test_status = test_status

            test_status.save(db)

            statuses_list = statuses.return_statuses(db)

        assert (
            "Status -19: Active. Code: 'ACTIVE'. Used for items which are currently in use."
            in statuses_list[0]
        )

    def test_parse_status_data_returns_correct_values(
        self, reset_database, test_status
    ) -> None:
        """Tests if parse_status_data returns dictionary with correct data.

        Resets the database. Creates statuses table. Builds and saves
        test_status to database. Queries database for unit data and
        calls the parser.

        Asserts that dictionary returned assigns the correct data to correct
        keys.
        """
        with database.Database("test_database.db") as db:
            db.create_table(statuses.return_table_creation_query())

            test_status = test_status
            test_status.save(db)
            data = test_status.read(db)
            dictionary = statuses.parse_status_data(data)

        assert (
            dictionary["status_id"] == -19
            and dictionary["status_code"] == "ACTIVE"
            and dictionary["status_name"] == "Active"
        )


class Test_StatusAttributes:
    """Contains all unit tests for the Status Class' attributes.

    Behaviors Tested:
        - Status class can be accessed.
        - Status objects can be created.
        - status_id attribute returns correct value.
        - status_code attribute returns correct value.
        - status_name attribute returns correct value.
        - created_date attribute returns correct value.
        - modified_date attribute returns correct value.
        - modified_by attribute returns correct value.
    """

    def test_status_class_can_be_accessed(self) -> None:
        """Tests that the Status Class exists and can be accessed.

        Asserts that calling Status.__doc__ does not return 'None'.
        """
        assert statuses.Status.__doc__ != None

    def test_can_create_status_objects(self, test_status) -> None:
        """Tests that objects can be created from the Status Class.

        Loads test_status.

        Asserts that test_status is an instance of the Status Class.
        """
        test_status = test_status

        assert isinstance(test_status, statuses.Status)

    def test_status_id_returns_correct_value(self, test_status) -> None:
        """Tests that the status_id attribute returns the correct value.

        Loads test_status.

        Asserts test_status.status_id is '-19'.
        """
        test_status = test_status

        assert test_status.status_id == -19

    def test_status_code_returns_correct_value(self, test_status) -> None:
        """Tests that the status_code attribute returns the correct value.

        Loads test_status.

        Asserts that test_status.status_code is 'ACTIVE'.
        """
        test_status = test_status

        assert test_status.status_code == "ACTIVE"

    def test_status_name_returns_correct_value(self, test_status) -> None:
        """Tests that the status_name attributes returns the correct value.

        Loads test_status.

        Asserts that test_status.status_name is 'Active'
        """
        test_status = test_status

        assert test_status.status_name == "Active"

    def test_status_description_returns_correct_value(self, test_status) -> None:
        """Tests that the status_description attributes returns the correct value.

        Loads test_status.

        Asserts that test_status.status_description is 'Used for items which are currently in use.'
        """
        test_status = test_status

        assert test_status.description == "Used for items which are currently in use."

    def test_created_date_returns_correct_value(self, test_status) -> None:
        """Tests that the created_date attributes returns the correct value.

        Loads test_status.

        Asserts that test_status.created_date is '08-26-2022'
        """
        test_status = test_status

        assert test_status.created_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_date_returns_correct_value(self, test_status) -> None:
        """Tests that the modified_date attributes returns the correct value.

        Loads test_status.

        Asserts that test_status.modified_date is '08-01-2022'
        """
        test_status = test_status

        assert test_status.modified_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_by_returns_correct_value(self, test_status) -> None:
        """Tests that the modified_by attributes returns the correct value.

        Loads test_status.

        Asserts that test_status.modified_by is 'Abenthy'
        """
        test_status = test_status

        assert test_status.modified_by == "Abenthy"


class Test_StatusMethods:
    """Contains all unit tests for the Status Class' methods.

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

    def test___init___sets_attributes_correctly(self, test_status) -> None:
        """Tests the initializer sets the objects attributes correctly.

        Loads test_status.

        Asserts that status_id, status_code, and status_name attributes are set to
        the expected values.
        """
        test_status = test_status

        assert (
            test_status.status_id == -19
            and test_status.status_code == "ACTIVE"
            and test_status.status_name == "Active"
            and test_status.description == "Used for items which are currently in use."
        )

    def test___repr___returns_expected_string(self, test_status) -> None:
        """Tests that __repr__ returns correct string.

        Loads test_status. Calls str(test_status).

        Asserts that str(test_status) returns:
            Status -19: Active. Code: 'ACTIVE'. Used for items which are currently in use.'
        """
        test_status = test_status

        assert str(test_status) == (
            f"Status -19: Active. Code: 'ACTIVE'. Used for items which are currently in use."
        )

    def test_can_save_status_to_database(self, test_status, reset_database) -> None:
        """Tests that statuses can be saved to the database.

        Loads test_status. Calls test_status.save. Calls db.return_data()
        using the status_id of '821'.

        Asserts that returned data has status_code value of 'tn'.
        """
        test_status = test_status

        with database.Database("test_database.db") as db:
            db.create_table(statuses.return_table_creation_query())

            test_status.save(db)

            data = db.return_data(
                """SELECT status_code FROM statuses WHERE status_id = -19"""
            )

        assert data[0][0] == "ACTIVE"

    def test_can_read_status_from_database(self, reset_database, test_status) -> None:
        """Tests to see if the statuses's data can be returned from database.

        Resets the database. Creates statuses table. Builds and saves
        test_status. Calls test_status.read().

        Asserts that data returned matches expected values.
        """
        with database.Database("test_database.db") as db:
            db.create_table(statuses.return_table_creation_query())

            test_status = test_status
            test_status.save(db)

            data = test_status.read(db)[0]
            expected = [-19, "ACTIVE", "Active"]

        assert (
            data[0] == expected[0] and data[1] == expected[1] and data[2] == expected[2]
        )

    def test_can_load_status_from_database(self, reset_database, test_status) -> None:
        """Tests to see if an Unit Object can be loaded from data.
        Loads and saves test_status. Creates loaded_unit from data.

        Asserts that test_status and loaded_unit return identical
        attributes.
        """
        with database.Database("test_database.db") as db:
            db.create_table(statuses.return_table_creation_query())

            test_status = test_status
            test_status.save(db)

            loaded_unit = db.load_status("ACTIVE")

        assert (
            loaded_unit.return_attributes()[0] == test_status.return_attributes()[0]
            and loaded_unit.return_attributes()[1] == test_status.return_attributes()[1]
            and loaded_unit.return_attributes()[2] == test_status.return_attributes()[2]
        )

    def test_can_update_status_in_database(self, reset_database, test_status) -> None:
        """Tests to see if Unit data can be updated.

        Resets database. Creates Unit Table. Builds and saves test_status to
        database. Loads test_status as loaded_unit. Changes Name and updates
        database. Queries the data.

        Asserts that the returned data has the new name.
        """
        with database.Database("test_database.db") as db:
            db.create_table(statuses.return_table_creation_query())

            test_status = test_status
            test_status.save(db)

            test_status.status_name = "Not Tina"

            test_status.update(db)

            data = db.return_data(
                """SELECT status_name FROM statuses WHERE status_code = 'ACTIVE'"""
            )[0][0]

        assert data == "Not Tina"

    def test_can_delete_status_from_database(self, test_status, reset_database):
        """Tests that statuses can be deleted from the database.

        Loads test_status. Saves it to database. Then deletes it. Gets data from
        statuses table.

        Asserts data is empty.
        """
        test_status = test_status

        with database.Database("test_database.db") as db:
            db.create_table(statuses.return_table_creation_query())

            test_status.save(db)
            test_status.delete(db)

            data = db.return_data("""SELECT * FROM statuses""")
            assert data == []

    def test_return_attributes(self, test_status):
        """Tests that the statuses data is correctly returned.

        Loads test_status. Calls test_status.return_attributes().

        Asserts values returned are expected values.
        """
        test_status = test_status
        assert test_status.return_attributes() == (
            -19,
            "ACTIVE",
            "Active",
            "Used for items which are currently in use.",
            database.return_datetime("2022-08-01 00:00:00"),
            database.return_datetime("2022-08-01 00:00:00"),
            "Abenthy",
        )
