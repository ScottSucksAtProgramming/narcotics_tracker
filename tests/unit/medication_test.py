"""Contains Test_MedicationAttributes and Test_MedicationMethods classes.

Classes:

    Test_Medication Module: Contains all unit tests for the Medication Module.
    
    Test_MedicationAttributes: Contains all unit tests for the attributes of the Medication Class.
    
    Test_MedicationMethods: Contains all unit tests for the methods of the Medication Class.
    
"""

import pytest

from narcotics_tracker import database, medication, units
from narcotics_tracker.enums import containers, medication_statuses


class Test_MedicationModule:
    """Contains all unit tests for the Medication Module.

    Behaviors Tested:
        - Medication module can be accessed.
        - Method return_table_creation_query returns correct string.
        - Method parse_medication_data creates dictionary with correct vales.
        - Method return_medications returns all medications.
        - Method return_preferred_unit returns the correct unit.
    """

    def test_medication_module_can_be_accessed(self) -> None:
        """Tests that the medication module exists and can be accessed.

        Asserts that calling medication.__doc__ does not return 'None'.
        """
        assert medication.__doc__ != None

    def test_medication_table_query_returns_correct_string(self):
        """Tests that return_table_creation_query returns correct string.

        Calls medication.return_table_creation_query

        Asserts that return_table_create_query is
        'CREATE TABLE IF NOT EXISTS medications (
            MEDICATION_ID INTEGER PRIMARY KEY,
            MEDICATION_CODE TEXT UNIQUE,
            NAME TEXT,
            CONTAINER_TYPE TEXT,
            FILL_AMOUNT REAL,
            DOSE_IN_MCG REAL,
            PREFERRED_UNIT TEXT,
            CONCENTRATION REAL,
            STATUS TEXT,
            CREATED_DATE INT,
            MODIFIED_DATE INT,
            MODIFIED_BY TEXT,
            FOREIGN KEY (PREFERRED_UNIT) REFERENCES units (unit_code)  ON UPDATE CASCADE
            )'
        """
        assert medication.return_table_creation_query() == (
            """CREATE TABLE IF NOT EXISTS medications (
            MEDICATION_ID INTEGER PRIMARY KEY,
            MEDICATION_CODE TEXT UNIQUE,
            NAME TEXT,
            CONTAINER_TYPE TEXT,
            FILL_AMOUNT REAL,
            DOSE_IN_MCG REAL,
            PREFERRED_UNIT TEXT,
            CONCENTRATION REAL,
            STATUS TEXT,
            CREATED_DATE INT,
            MODIFIED_DATE INT,
            MODIFIED_BY TEXT,
            FOREIGN KEY (PREFERRED_UNIT) REFERENCES units (unit_code)  ON UPDATE CASCADE
            )"""
        )

    def test_parse_medication_data_creates_dictionary_with_correct_values(
        self, test_med
    ):
        """Tests that parse_medication_data returns correct dictionary data.

        Loads test_med and saves to database. Retrieves medication data from
        database and parses it.

        Asserts that the data returned matches ALL expected values.
        """
        test_med = test_med
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(medication.return_table_creation_query())
        test_med.save(db)

        code = ["Un-69420-9001"]
        raw_data = db.return_data(
            """SELECT * FROM medications WHERE medication_code=(?)""", code
        )

        med_data = medication.parse_medication_data(raw_data)

        assert (
            med_data["medication_id"] == 1
            and med_data["name"] == "Unobtanium"
            and med_data["medication_code"] == "Un-69420-9001"
            and med_data["container_type"] == containers.Container.VIAL
            and med_data["fill_amount"] == 9_001.0
            and med_data["dose"] == 69_420.0
            and med_data["unit"] == "mg"
            and med_data["concentration"] == 7.712476391512054
            and med_data["status"] == medication_statuses.MedicationStatus.DISCONTINUED
        )

    def test_return_medication_returns_expected_medication(
        self, test_med, reset_database
    ) -> None:
        """Tests that the return_medication method returns the expected medication.

        Loads and saves test_med. Creates and save. 2nd_med
        Calls medication.return_medication().

        Asserts that medication.return_medication() returns expected data.
        """
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(medication.return_table_creation_query())

        test_med = test_med
        second_med = test_med
        second_med.code = "SECOND MED"
        test_med.save(db)
        second_med.save(db)

        medication_list = medication.return_medication(db)

        assert (
            "Unobtanium 69420.0 mg in 9001.0 ml. Code: Un-69420-9001."
            in medication_list
        )

    def test_return_preferred_unit_returns_correct_unit_as_string(
        self, reset_database, test_med
    ) -> None:
        """Tests that the correct unit is returned for the specified med.

        Loads and saves test_med to database. Calls
        medication.return_preferred_unit(test_med, db).

        Asserts that 'mg' is returned."""
        db = database.Database()
        db.connect("test_database_2.db")

        test_med = test_med
        test_med.medication_code = "morphine"

        assert medication.return_preferred_unit(test_med.medication_code, db)


class Test_MedicationAttributes:
    """Contains all unit tests for the attributes of the Medication Class.

    Behaviors Tested:
        - Medications can be created.
        - Medications return expected medication_ID.
        - Medications return expected code.
        - Medications return expected name.
        - Medications return expected container_type.
        - Medications return expected fill_amount.
        - Medications return expected dose.
        - Medications return expected preferred_unit.
        - Medications return expected concentration.
        - Medications return expected created_date.
        - Medications return expected modified_date.
        - Medications return expected modified_by.
        - Medications can be edited.
    """

    def test_medications_can_be_created(self, test_med):
        """Tests that Medication object can be created.

        Loads test_med.

        Asserts that test_med is an instance of the medication.Medication
        Class.
        """
        test_med = test_med

        assert isinstance(test_med, medication.Medication)

    def test_medications_return_expected_medication_id(self, test_med):
        """Tests that the medication_id is returned as expected.

        Loads test_med.

        Asserts that test_med.medication_id equals '1'.
        """
        test_med = test_med

        assert test_med.medication_id == 1

    def test_medications_return_expected_code(self, test_med):
        """Tests that the medication's code is returned as expected.

        Loads test_med.

        Asserts that test_med.code equals 'Un-69420-9001'.
        """
        test_med = test_med

        assert test_med.medication_code == "Un-69420-9001"

    def test_medications_return_expected_name(self, test_med):
        """Tests that the medication's code is returned as expected.

        Loads test_med.

        Asserts that test_med.name equals 'Unobtanium'.
        """
        test_med = test_med

        assert test_med.name == "Unobtanium"

    def test_medications_return_expected_container_type(self, test_med):
        """Tests that the medication's code is returned as expected.

        Loads test_med.

        Asserts that test_med.container_type equals
        'containers.Container.VIAL'.
        """
        test_med = test_med

        assert test_med.container_type == containers.Container.VIAL

    def test_medications_return_expected_fill_amount(self, test_med):
        """Tests that the medication's fill amount is returned correctly.

        Loads test_med.

        Asserts that test_med.fill_amount equals '9001'.
        """
        test_med = test_med

        assert test_med.fill_amount == 9_001

    def test_medications_return_expected_dose(self, test_med):
        """Tests that the medication's dose is returned correctly.

        Loads test_med.

        Asserts that test_med.dose equals '69420'.
        """
        test_med = test_med

        assert test_med.dose == 69_420

    def test_medications_return_expected_preferred_unit(self, test_med):
        """Tests that the medication's preferred unit is returned correctly.

        Loads test_med.

        Asserts that test_med.preferred_unit equals 'units.Unit.MCG'.
        """
        test_med = test_med

        assert test_med.preferred_unit == "mg"

    def test_medications_return_expected_concentration(self, test_med):
        """Tests that the medication's concentration is returned correctly.

        Loads test_med.

        Asserts that test_med.concentration equals '7.712476391512054'.
        """
        test_med = test_med

        assert test_med.concentration == 7.712476391512054

    def test_medications_return_expected_created_date(self, test_med):
        """Tests that the medication's created_date is returned correctly.

        Loads test_med.

        Asserts that test_med.created_date equals '01-02-1986'.
        """
        test_med = test_med

        assert test_med.created_date == "01-02-1986"

    def test_medications_return_expected_modified_date(self, test_med):
        """Tests that the medication's modified_date is returned correctly.

        Loads test_med.

        Asserts that test_med.modified_date equals '08-09-2022'.
        """
        test_med = test_med

        assert test_med.modified_date == "08-09-2022"

    def test_medications_return_expected_modified_by(self, test_med):
        """Tests that the medication's modified_by is returned correctly.

        Loads test_med.

        Asserts that test_med.modified_by equals 'Kvothe'.
        """
        test_med = test_med

        assert test_med.modified_by == "Kvothe"

    def test_medications_can_be_edited(self, test_med):
        """Tests that the medication's attributes and be changed.

        Loads test_med. Changes preferred_unit to 'G'.

        Asserts that test_med.preferred unit is 'G'.
        """
        test_med = test_med

        test_med.preferred_unit = "G"

        assert test_med.preferred_unit == "G"


class Test_MedicationMethods:
    """Contains all unit tests for the methods of the Medication Class.

    Behaviors Tested:

        - __repr__ returns the correct string.
        - Medication data can be saved to the database.
        - Medication data can be updated in the database.
        - Medication data can be deleted from the database.
        - return_attributes returns the correct information.
    """

    def test__repr___returns_correct_string(self, test_med):
        """Tests that __repr__ returns correct string.

        Loads test_med. Calls str(test_med).

        return f"{self.name} {self.dose}{self.preferred_unit} in {self.fill_amount}ml. Code: {self.medication_code}"

        Asserts that str(test_med) returns:
            "Unobtainium 69420.0mg in 9001ml. Code: Un-69420-9001."
        """
        test_med = test_med
        assert str(test_med) == ("Unobtanium 69420.0mg in 9001ml. Code: Un-69420-9001.")

    def test_return_attributes(self, test_med):
        """Tests that the medication data is correctly returned.

        Loads test_med. Calls test_med.return_attributes().

        Asserts values returned are expected values.
        """
        test_med = test_med
        assert test_med.return_attributes() == (
            1,
            "Un-69420-9001",
            "Unobtanium",
            "Vial",
            9001,
            69420.0,
            "mg",
            7.712476391512054,
            "Discontinued",
            "01-02-1986",
            "08-09-2022",
            "Kvothe",
        )

        """Tests that the medication data is correctly written to
        database.

        Loads test_med. Saves to database. Calls db.return_data() on
        medication.

        Asserts data return has name 'Unobtanium'.
        """
        test_med = test_med
        db = database.Database()
        db.connect("test_database.db")
        db.create_table(medication.return_table_creation_query())
        test_med.save(db)

        data = db.return_data(
            """SELECT * FROM medications WHERE MEDICATION_CODE='Un-69420-9001'"""
        )[0][2]

        assert data == "Unobtanium"

    def test_delete_medication(self, test_med, reset_database):
        """Tests that the medication can be deleted from the database.

        Loads test_med. Saves it to database. Then deletes it. Gets data from
        medication table.

        Asserts data is empty.
        """
        test_med = test_med

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(medication.return_table_creation_query())

        test_med.save(db)
        test_med.delete(db)

        data = db.return_data("""SELECT * FROM medications""")
        assert data == []

    def test_update(self, test_med, reset_database):
        """Tests that a medication's attributes can be updated in the
        database.

        Loads test_med and saves to database. Loads medication info from
        database to loaded_med. Changes loaded_med status to
        'medication_statuses.MedicationStatus.ACTIVE'. Updates medication in
        database.

        Asserts medication status is
        'Active'.
        """
        test_med = test_med

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(medication.return_table_creation_query())
        test_med.save(db)

        med_code = "Un-69420-9001"
        loaded_med = db.load_medication(med_code)
        loaded_med.status = medication_statuses.MedicationStatus.ACTIVE
        loaded_med.update(db, med_code)

        data = db.return_data(
            """SELECT status FROM medications WHERE MEDICATION_CODE=(?)""", [med_code]
        )

        assert data[0][0] == "Active"
