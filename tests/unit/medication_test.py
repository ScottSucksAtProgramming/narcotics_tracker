"""Contains all the unit tests for the medication module."""

import pytest

from narcotics_tracker import database, medication
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.utils import date


class Test_MedicationClassProperties:
    """Unit Tests for the properties of the Medication Class."""

    def test_can_instantiate_Medication_object(self, test_med):
        """Check to see if Medication object can be instantiated."""

        test_med = test_med

        assert isinstance(test_med, medication.Medication)

    def test_medication_id(self, test_med):
        """Check to see if the medication's id can be retrieved."""

        test_med = test_med
        test_med.medication_id = None

        assert test_med.medication_id == None

    def test_code(self, test_med):
        """Check to see if medication's unique code can be retrieved."""

        test_med = test_med

        assert test_med.code == "Un-69420-9001"

    def test_name(self, test_med):
        """Check to see if the medication's name can be retrieved."""

        test_med = test_med

        assert test_med.name == "Unobtanium"

    def test_container_type(self, test_med):
        """Check to see if the medications container_type can be retrieved."""

        test_med = test_med

        assert test_med.container_type == containers.Container.VIAL

    def test_fill_amount(self, test_med):
        """Check to see if the medication's fill_amount can be retrieved."""

        test_med = test_med

        assert test_med.fill_amount == 9_001

    def test_dose(self, test_med):
        """Check to see if the medication's dose can be retrieved."""

        test_med = test_med

        assert test_med.dose == 69_420

    def test_preferred_unit(self, test_med):
        """Check to see if the medication's unit can be retrieved."""

        test_med = test_med

        assert test_med.preferred_unit == units.Unit.MCG

    def test_unit_restriction(self):
        """Checks that a medication with an incorrect unit type raises an
        exception."""

        with pytest.raises(AttributeError):
            fentanyl = medication.Medication(
                name="Fentanyl",
                code="Fe-100-2",
                container_type=containers.Container.VIAL,
                fill_amount=2,
                dose=100,
                unit=units.Unit.KG,
                concentration=50,
                status=medication_statuses.MedicationStatus.ACTIVE,
                created_date="08-01-2022",
                modified_date="08-01-2022",
                modified_by="test",
            )

    def test_concentration(self, test_med):
        """Check to see if the medication's concentration can be retrieved."""

        test_med = test_med

        assert test_med.concentration == 7.712476391512054

    def test_container_type_restriction(self):
        """Checks that a medication with an incorrect container types raises
        an exception."""

        with pytest.raises(AttributeError):
            fentanyl = medication.Medication(
                name="Fentanyl",
                code="Fe-100-2",
                container_type=containers.Container.BOTTLE,
                fill_amount=2,
                dose=100,
                unit=units.Unit.MCG,
                concentration=50,
                status=medication_statuses.MedicationStatus.ACTIVE,
                created_date="08-01-2022",
                modified_date="08-01-2022",
                modified_by="test",
            )

    def test_created_date(self, test_med):
        """Checks to see if the medication's created_date can be retrieved."""

        test_med = test_med
        test_med.created_date = "08-01-2022"

        assert test_med.created_date == "08-01-2022"

    def test_modified_date(self, test_med):
        """Checks to see if the medication's modified_date can be retrieved."""

        test_med = test_med
        test_med.modified_date = "08-09-2022"

        assert test_med.modified_date == "08-09-2022"

    def test_modified_by(self, test_med):
        """Checks to see if the medication's modified_by property can be retrieved."""

        test_med = test_med
        test_med.modified_by = "SRK"

        assert test_med.modified_by == "SRK"

    def test_mediation_can_be_edited(self, test_med):
        """Checks to see if a medication's properties return the new value
        after being edited."""

        test_med = test_med

        test_med.preferred_unit = units.Unit.G

        assert str(test_med) == (
            f"Medication Object 1 for Unobtanium with code Un-69420-9001. "
            f"Container type: Vial. Fill amount: 9001 ml. Dose: 69420 G. "
            f"Concentration: 7.712476391512054. Status: Discontinued. "
            f"Created on 01-02-1986. Last modified on 08-09-2022 by Kvothe."
        )


class Test_MedicationClassMethods:
    """Unit Tests for the methods of the Medication class."""

    def test_printing_a_Medication_object_returns_correct_string(self, test_med):
        """Check to see if printing a Medication object returns a string."""

        test_med = test_med
        assert str(test_med) == (
            f"Medication Object 1 for Unobtanium with code Un-69420-9001. "
            f"Container type: Vial. Fill amount: 9001 ml. Dose: 69420 mcg. "
            f"Concentration: 7.712476391512054. Status: Discontinued. Created "
            f"on 01-02-1986. Last modified on 08-09-2022 by Kvothe."
        )

    def test_medication_table_query_returns_correct_string(self):
        """Check to see if medication table query returns correct string."""

        assert medication.return_table_creation_query() == (
            """CREATE TABLE IF NOT EXISTS medication (
            MEDICATION_ID INTEGER PRIMARY KEY,
            CODE TEXT UNIQUE,                
            NAME TEXT,
            CONTAINER_TYPE TEXT,
            FILL_AMOUNT REAL,
            DOSE REAL,
            UNIT TEXT,
            CONCENTRATION REAL,
            STATUS TEXT,
            CREATED_DATE TEXT,
            MODIFIED_DATE TEXT,
            MODIFIED_BY TEXT
            )"""
        )

    def test_return_attributes(self, test_med):
        """Checks to see if the medication data is correctly returned."""

        test_med = test_med
        assert test_med.return_attributes() == (
            1,
            "Un-69420-9001",
            "Unobtanium",
            "Vial",
            9001,
            69420,
            "mcg",
            7.712476391512054,
            "Discontinued",
            "01-02-1986",
            "08-09-2022",
            "Kvothe",
        )

    def test_save_to_database(self, test_med):
        """Checks to see if the medication data is correctly written to
        database."""

        test_med = test_med
        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS medication")
        db.create_table(medication.return_table_creation_query())

        test_med.save(db)
        data = db.return_data(
            """SELECT * FROM medication WHERE CODE='Un-69420-9001'"""
        )[0][2]

        assert data == "Unobtanium"

    def test_delete_medication(self, test_med, database_test_set_up):
        """Checks to see if the medication can be deleted from the database."""

        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS medication")
        db.create_table(medication.return_table_creation_query())

        test_med = test_med
        test_med.save(db)
        test_med.delete(db)

        data = db.return_data("""SELECT * FROM medication""")
        assert data == []

    def test_update(self, test_med, database_test_set_up):
        """Tests to see if a medication's attributes can be updated in the
        database."""

        test_med = test_med

        db = database.Database()
        db.connect("test_database.db")
        db.create_table(medication.return_table_creation_query())
        test_med.modified_by = "SRK"
        test_med.save(db)

        med_code = "Un-69420-9001"
        loaded_med = db.load_medication(med_code)
        loaded_med.status = medication_statuses.MedicationStatus.ACTIVE
        loaded_med.update(db, med_code)

        data = db.return_data(
            """SELECT status FROM medication WHERE CODE=(?)""", [med_code]
        )

        assert data[0][0] == medication_statuses.MedicationStatus.ACTIVE.value
