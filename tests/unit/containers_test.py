"""Contains the classes and tests which test the containers module.

Classes:

    Test_ContainersModule: Contains all unit tests for the containers module.

    Test_ContainerAttributes: Contains unit tests for Unit's attributes.

    Test_ContainerMethods: Contains unit tests for the Unit's methods.
"""

from narcotics_tracker import containers
from persistence import database


class Test_ContainersModule:
    """Contains all unit tests for the Containers module.

    Behaviors Tested:
        - Containers module can be accessed.
        - Method return_table_creation_query returns correct string.
        #! - Method return_containers returns all containers.
        #! - Method parse_unit_data returns correct dictionary and values.
    """

    def test_containers_module_can_be_accessed(self) -> None:
        """Tests that the containers module exists and can be accessed.

        Asserts that calling containers.__doc__ does not return 'None'.
        """
        assert containers.__doc__ != None

    def test_return_table_creation_query_returns_expected_string(self) -> None:
        """Tests that the table_creation_query returns the correct string.

        Calls containers.return_table_creation_query().

        Asserts that expected_query is returned.
        """
        expected_query = """CREATE TABLE IF NOT EXISTS containers (
            CONTAINER_ID INTEGER PRIMARY KEY,
            CONTAINER_CODE TEXT UNIQUE,                
            CONTAINER_NAME TEXT,
            CREATED_DATE INTEGER,
            MODIFIED_DATE INTEGER,
            MODIFIED_BY TEXT
            )"""

        assert containers.return_table_creation_query() == expected_query

    def test_return_containers_returns_expected_containers(
        self, test_container, reset_database
    ) -> None:
        """Tests that the return_containers method returns the expected containers.

        Loads and saves test_container. Creates and save. 2nd_unit
        Calls containers.return_containers().

        Asserts that containers.return_containers() returns expected data.
        """
        with database.Database("test_database.db") as db:
            db.create_table(containers.return_table_creation_query())

            test_container = test_container

            test_container.save(db)

            containers_list = containers.return_containers(db)

        assert "Container -7: Suppository. Code: 'supp'." in containers_list[0]

    def test_parse_container_data_returns_correct_values(
        self, reset_database, test_container
    ) -> None:
        """Tests if parse_container_data returns dictionary with correct data.

        Resets the database. Creates containers table. Builds and saves
        test_container to database. Queries database for unit data and
        calls the parser.

        Asserts that dictionary returned assigns the correct data to correct
        keys.
        """
        with database.Database("test_database.db") as db:
            db.create_table(containers.return_table_creation_query())

            test_container = test_container
            test_container.save(db)
            data = test_container.read(db)
            dictionary = containers.parse_container_data(data)

        assert (
            dictionary["container_id"] == -7
            and dictionary["container_code"] == "supp"
            and dictionary["container_name"] == "Suppository"
        )


class Test_ContainerAttributes:
    """Contains all unit tests for the Container Class' attributes.

    Behaviors Tested:
        - Container class can be accessed.
        - Container objects can be created.
        - container_id attribute returns correct value.
        - container_code attribute returns correct value.
        - container_name attribute returns correct value.
        - created_date attribute returns correct value.
        - modified_date attribute returns correct value.
        - modified_by attribute returns correct value.
    """

    def test_container_class_can_be_accessed(self) -> None:
        """Tests that the Container Class exists and can be accessed.

        Asserts that calling Container.__doc__ does not return 'None'.
        """
        assert containers.Container.__doc__ != None

    def test_can_create_container_objects(self, test_container) -> None:
        """Tests that objects can be created from the Container Class.

        Loads test_container.

        Asserts that test_container is an instance of the Container Class.
        """
        test_container = test_container

        assert isinstance(test_container, containers.Container)

    def test_container_id_returns_correct_value(self, test_container) -> None:
        """Tests that the container_id attribute returns the correct value.

        Loads test_container.

        Asserts test_container.container_id is '-7'.
        """
        test_container = test_container

        assert test_container.container_id == -7

    def test_container_code_returns_correct_value(self, test_container) -> None:
        """Tests that the container_code attribute returns the correct value.

        Loads test_container.

        Asserts that test_container.container_code is 'supp'.
        """
        test_container = test_container

        assert test_container.container_code == "supp"

    def test_container_name_returns_correct_value(self, test_container) -> None:
        """Tests that the container_name attributes returns the correct value.

        Loads test_container.

        Asserts that test_container.container_name is 'Suppository'
        """
        test_container = test_container

        assert test_container.container_name == "Suppository"

    def test_created_date_returns_correct_value(self, test_container) -> None:
        """Tests that the created_date attributes returns the correct value.

        Loads test_container.

        Asserts that test_container.created_date is '08-26-2022'
        """
        test_container = test_container

        assert test_container.created_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_date_returns_correct_value(self, test_container) -> None:
        """Tests that the modified_date attributes returns the correct value.

        Loads test_container.

        Asserts that test_container.modified_date is '08-01-2022'
        """
        test_container = test_container

        assert test_container.modified_date == database.return_datetime(
            "2022-08-01 00:00:00"
        )

    def test_modified_by_returns_correct_value(self, test_container) -> None:
        """Tests that the modified_by attributes returns the correct value.

        Loads test_container.

        Asserts that test_container.modified_by is 'Elodin'
        """
        test_container = test_container

        assert test_container.modified_by == "Elodin"


class Test_containerMethods:
    """Contains all unit tests for the Container Class' methods.

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

    def test___init___sets_attributes_correctly(self, test_container) -> None:
        """Tests the initializer sets the objects attributes correctly.

        Loads test_container.

        Asserts that container_id, container_code, and container_name attributes are set to
        the expected values.
        """
        test_container = test_container

        assert (
            test_container.container_id == -7
            and test_container.container_code == "supp"
            and test_container.container_name == "Suppository"
        )

    def test___repr___returns_expected_string(self, test_container) -> None:
        """Tests that __repr__ returns correct string.

        Loads test_container. Calls str(test_container).

        Asserts that str(test_container) returns:
            'Unit Test. Code: TEST. Used for testing the EventType Class.'
        """
        test_container = test_container

        assert str(test_container) == (f"Unit Number -7: Suppository. Code: 'supp'.")

    def test_can_save_container_to_database(
        self, test_container, reset_database
    ) -> None:
        """Tests that containers can be saved to the database.

        Loads test_container. Calls test_container.save. Calls db.return_data()
        using the container_id of '821'.

        Asserts that returned data has container_code value of 'tn'.
        """
        test_container = test_container

        with database.Database("test_database.db") as db:
            db.create_table(containers.return_table_creation_query())

            test_container.save(db)

            data = db.return_data(
                """SELECT container_code FROM containers WHERE container_id = '-7'"""
            )

        assert data[0][0] == "supp"

    def test_can_read_container_from_database(
        self, reset_database, test_container
    ) -> None:
        """Tests to see if the containers's data can be returned from database.

        Resets the database. Creates containers table. Builds and saves
        test_container. Calls test_container.read().

        Asserts that data returned matches expected values.
        """
        with database.Database("test_database.db") as db:
            db.create_table(containers.return_table_creation_query())

            test_container = test_container
            test_container.save(db)

            data = test_container.read(db)[0]
            expected = [-7, "supp", "Suppository"]

        assert (
            data[0] == expected[0] and data[1] == expected[1] and data[2] == expected[2]
        )

    def test_can_load_container_from_database(
        self, reset_database, test_container
    ) -> None:
        """Tests to see if an Unit Object can be loaded from data.
        Loads and saves test_container. Creates loaded_unit from data.

        Asserts that test_container and loaded_unit return identical
        attributes.
        """
        with database.Database("test_database.db") as db:
            db.create_table(containers.return_table_creation_query())

            test_container = test_container
            test_container.save(db)

            loaded_unit = db.load_container("supp")

        assert (
            loaded_unit.return_attributes()[0] == test_container.return_attributes()[0]
            and loaded_unit.return_attributes()[1]
            == test_container.return_attributes()[1]
            and loaded_unit.return_attributes()[2]
            == test_container.return_attributes()[2]
        )

    def test_can_update_container_in_database(
        self, reset_database, test_container
    ) -> None:
        """Tests to see if Unit data can be updated.

        Resets database. Creates Unit Table. Builds and saves test_container to
        database. Loads test_container as loaded_unit. Changes Name and updates
        database. Queries the data.

        Asserts that the returned data has the new name.
        """
        with database.Database("test_database.db") as db:
            db.create_table(containers.return_table_creation_query())

            test_container = test_container
            test_container.save(db)

            test_container.container_name = "Not Tina"

            test_container.update(db)

            data = db.return_data(
                """SELECT container_name FROM containers WHERE container_code = 'supp'"""
            )[0][0]

        assert data == "Not Tina"

    def test_can_delete_container_from_database(self, test_container, reset_database):
        """Tests that containers can be deleted from the database.

        Loads test_container. Saves it to database. Then deletes it. Gets data from
        containers table.

        Asserts data is empty.
        """
        test_container = test_container

        with database.Database("test_database.db") as db:
            db.create_table(containers.return_table_creation_query())

            test_container.save(db)
            test_container.delete(db)

            data = db.return_data("""SELECT * FROM containers""")
        assert data == []

    def test_return_attributes(self, test_container):
        """Tests that the containers data is correctly returned.

        Loads test_container. Calls test_container.return_attributes().

        Asserts values returned are expected values.
        """
        test_container = test_container
        assert test_container.return_attributes() == (
            -7,
            "supp",
            "Suppository",
            database.return_datetime("2022-08-01 00:00:00"),
            database.return_datetime("2022-08-01 00:00:00"),
            "Elodin",
        )
