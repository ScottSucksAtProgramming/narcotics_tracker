"""Unit tests the Medications Module.

Classes:

    Test_Medications: Unit tests the Medication Class.
"""

from narcotics_tracker.items.medications import Medication


class Test_Medications:
    """Unit tests the Medication Class.

    Behaviors Tested:
        - Medications class can be accessed.
        - Medications return expected id.
        - Medications return expected medication_code.
        - Medications return expected medication_name.
        - Medications return expected fill_amount.
        - Medications return expected medication_amount.
        - Medications return expected preferred_unit.
        - Medications return expected concentration.
        - Medications return expected status.
        - Medications return expected string.
        - Medications return expected dictionary.
    """

    test_medication = Medication(
        table="medications",
        id=-1,
        medication_code="apap",
        medication_name="Acetaminophen",
        fill_amount=10,
        medication_amount=100000,
        preferred_unit="mg",
        concentration=0.1,
        status="unknown",
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="SRK",
    )

    def test_medication_class_can_be_accessed(self) -> None:
        assert Medication.__doc__ != None

    def test_medications_return_expected_id(self) -> None:
        assert self.test_medication.id == -1

    def test_medications_return_expected_medication_code(self) -> None:
        assert self.test_medication.medication_code == "apap"

    def test_medications_return_expected_name(self) -> None:
        assert self.test_medication.medication_name == "Acetaminophen"

    def test_medications_return_expected_fill_amount(self):
        assert self.test_medication.fill_amount == 10

    def test_medications_return_expected_medication_amount(self):
        assert self.test_medication.medication_amount == 100000

    def test_medications_return_expected_preferred_unit(self):
        assert self.test_medication.preferred_unit == "mg"

    def test_medications_return_expected_concentration(self):
        assert self.test_medication.concentration == 0.1

    def test_medications_return_expected_status(self):
        assert self.test_medication.status == "unknown"

    def test_medications_return_expected_string(self) -> None:
        assert (
            str(self.test_medication)
            == "Medication #-1: Acetaminophen (apap) 1.0 mg in 10 ml."
        )

    def test_medications_return_expected_dictionary(self) -> None:
        assert vars(self.test_medication) == {
            "table": "medications",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "SRK",
            "medication_code": "apap",
            "medication_name": "Acetaminophen",
            "fill_amount": 10,
            "medication_amount": 100000,
            "preferred_unit": "mg",
            "concentration": 0.1,
            "status": "unknown",
        }
