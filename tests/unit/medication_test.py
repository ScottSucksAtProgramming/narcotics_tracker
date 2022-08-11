"""Contains all the unit tests for the medication module."""

import pytest

from narcotics_tracker import database, date, medication
from narcotics_tracker.enums import containers, medication_statuses, units


class Test_MedicationClassProperties:
    """Unit Tests for the properties of the Medication Class."""

    def test_can_instantiate_Medication_object(self, test_med):
        """Check to see if Medication object can be instantiated."""

        test_med = test_med

        assert isinstance(test_med, medication.Medication)

    def test_medication_id(self, test_med):
        """Check to see if the medication's id can be retrieved."""

        test_med = test_med

        assert medication.Medication.medication_id == None

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

    def test__unit(self, test_med):
        """Check to see if the medication's unit can be retrieved."""

        test_med = test_med

        assert test_med.unit == units.Unit.MCG

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

        test_med.unit = units.Unit.G

        assert str(test_med) == (
            f"Medication Object 1 for Unobtanium with code Un-69420-9001. "
            f"Container type: Vial. Fill amount: 9001 ml. Dose: 69420 G. "
            f"Concentration: 7.712476391512054. Status: Discontinued. "
            f"Created on 08-01-2022. Last modified on 08-09-2022 by SRK."
        )


class Test_MedicationClassMethods:
    """Unit Tests for the methods of the Medication class."""

    def test_printing_a_Medication_object_returns_correct_string(self, test_med):
        """Check to see if printing a Medication object returns a string."""

        test_med = test_med
        assert str(test_med) == (
            f"Medication Object 1 for Unobtanium with code Un-69420-9001. "
            f"Container type: Vial. "
            f"Fill amount: 9001 ml. "
            f"Dose: 69420 mcg. "
            f"Concentration: 7.712476391512054. "
            f"Status: Discontinued. Created on 08-01-2022. "
            f"Last modified on 08-09-2022 by SRK."
        )

    def test_medication_table_query_returns_correct_string(self):
        """Check to see if medication table query returns correct string."""

        assert medication.Medication.return_table_creation_query() == (
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

    def test_return_properties(self, test_med):
        """Checks to see if the medication data is correctly returned."""

        test_med = test_med
        assert test_med.return_properties() == (
            1,
            "Unobtanium",
            "Un-69420-9001",
            "Vial",
            9001,
            69420,
            "mcg",
            7.712476391512054,
            "Discontinued",
            "08-01-2022",
            "08-09-2022",
            "SRK",
        )

    def test_save_to_database(self, test_med):
        """Checks to see if the medication data is correctly written to
        database."""

        test_med = test_med
        db = database.Database()
        db.connect("test_database.db")
        db.delete_table("DROP TABLE IF EXISTS test_table")

        test_med.save(db)
        data = db.read_table(
            """SELECT * FROM sqlite_master WHERE type='table' AND name=(?)""",
            ["medication"],
        )[0][4]

        assert (
            data
            == """CREATE TABLE medication (
                MEDICATION_ID INTEGER PRIMARY KEY,
                NAME TEXT,
                CODE TEXT UNIQUE,
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

    def test_created_date_is_none(self, test_med):
        """Checks to see if the created date is None."""

        test_med = test_med

        test_med.created_date = None

        assert test_med.created_date_is_none() == True

    def test_created_date_has_value(self, test_med):
        """Checks to see if the created date is None."""

        test_med = test_med

        assert test_med.created_date_is_none() == False

    def test_created_date_set_if_none(self, test_med):
        """Checks to see if the created date is initially set to none it is replaced with current date."""

        test_med = test_med
        db = database.Database()
        db.connect("test_database.db")

        test_med.created_date = None

        test_med.save(db)

        assert test_med.created_date == date.get_date_as_string()